---
title: Models.save vs Forms.save
tags:
  - studies
  - programming
  - django
use: Documentation
languages: Python
dependences: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [How `Model.save()` works](#how-modelsave-works)
- [How `ModelForm.save()` works](#how-modelformsave-works)
- [Why the two layers?](#why-the-two-layers)
- [Deeper examples](#deeper-examples)
	- [Form](#form)
		- [Improvements \& advanced ideas](#improvements--advanced-ideas)
	- [Model](#model)
		- [Improvements \& advanced ideas](#improvements--advanced-ideas-1)
- [Connecting to advanced Django topics](#connecting-to-advanced-django-topics)
- [External references \& further reading](#external-references--further-reading)

</details>

---

Sometimes I've faced the similar actions between the `save` methods of `Models` and `Forms`, so here's a comprehensive analysis about this topic.

### Quick‑look difference

|Method|What you call it on|Primary job|When it runs|Key options|
|---|---|---|---|---|
|`Model.save()`|A **single model instance** (`Article`, `User`, …)|Persists _that_ instance to the DB (insert or update)|Whenever you call it (often inside a view, a signal, or another method)|`force_insert`, `force_update`, `update_fields`, `using`, `atomic`|
|`ModelForm.save()`|A **`ModelForm` (or `ModelFormSet`) object**|Builds/updates a model instance **from validated form data**, then calls `instance.save()` for you|After you’ve bound data and `form.is_valid()` returns `True`|`commit=True/False`, `m2m=True/False` (when `commit=False` and later `save_m2m()`)|

## How `Model.save()` works

```python
from .models import BlogPost
# ...
post = BlogPost(title="Django Behind the Scenes")
post.save(update_fields=["title"])
```

Belongs to (is) the Domain-model layer and **`Model.save()`** is the low‑level persistence contract of this layer.
It must guarantee ACID safety for a single row, raise `ValidationError` only if the caller explicitly asked for `full_clean()`, and emit `pre_save`/`post_save` signals for observers.
Here's some duties:
- **Validation** – **not automatic**. If you rely on model‑level validation you must call `full_clean()` yourself.
- **Signals** – fires `pre_save` and `post_save`; great for side‑effects (caches, audit logs, websockets, etc.).
- **Transactions** – wraps its internals in `transaction.atomic()` if the DB supports DDL transactions.
- **Overrides** – you can customize behaviour by overriding `save()` in your model class and calling `super().save(*args, **kwargs)` at the end.  ([Models | Django documentation](https://docs.djangoproject.com/en/5.1/topics/db/models/), [Model instance reference | Django documentation](https://docs.djangoproject.com/en/5.1/ref/models/instances/))

## How `ModelForm.save()` works

```python
from .forms import BlogPostForm
# ...
form = BlogPostForm(request.POST, request.FILES)
if form.is_valid():                # runs full_clean() on every field
    post = form.save(commit=False) # build *but don’t hit DB yet*
    post.author = request.user     # attach extra data
    post.save()                    # now go to DB
    form.save_m2m()                # write many‑to‑many if any
```

Belongs to validation/forms layer,  creating an interface for the user to fill the data, and thus validate this data. Here's some obligations:
- **Validation first** – `is_valid()` calls `full_clean()` on the _form_ **and** on the generated model instance, catching `ValidationError`s early.
- **`commit` flag** – `commit=False` lets you tweak the object or wrap multiple objects in the same transaction.
- **Updating vs creating** – pass `instance=obj` to update an existing row instead of creating a new one.
- Works seamlessly inside high‑level abstractions: `CreateView`, `UpdateView`, Django Admin, and even DRF’s `ModelSerializer`.  ([Creating forms from models | Django documentation](https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/))

## Why the two layers?

|Concern|Use `Model.save()` when you …|Use `ModelForm.save()` when you …|
|---|---|---|
|**Have already‑clean data** (fixtures, ETL jobs, signals, management commands)|✅|🚫 (over‑kill)|
|**Need HTML form handling & validation**|🚫 (manual work)|✅|
|**Want fine‑grained DB control** (`update_fields`, bulk ops)|✅|🚫 (delegate to model)|
|**Are inside Admin / CBV / formset / DRF**|implicit via form|built‑in|

## Deeper examples

### Form

```python
def save(self, commit: bool = True, inst=None, **kwargs) -> CustomModel:
	"""Overrides the save method to store the form data in the relevant JSON field"""
	user = kwargs.get("user")
	operation = kwargs.get("operation")
	user_ctx = kwargs.get("user_ctx")
	
	# If feedback retrieve the existing instance
	instance = inst if inst else super().save(commit=False)
	
	# Ensure created_by is always set
	if instance._state.adding or not instance.created_by:
		instance.created_by = user
	instance.updated_by = user
	
	data = {
		"field": self.cleaned_data["field"],
		# ...
	}
	# Store data in the relevant JSON field based on context
	if operation == "meeting":
		instance.meeting_response = data
	elif user_ctx == "manager":
		instance.manager_response = data
	else:
		instance.user_response = data
	
	if commit:
		instance.save()
	return instance
```


| Obligation                                    | In the code                                                                                                                              | Comment                                                                                                                                                    |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Coerce & validate user input**              | Validation already happened in `form.is_valid()` before `save()` is reached.                                                             | Correct: the form shields the model from raw HTTP.                                                                                                         |
| **Build/update a model instance**             | Calls `super().save(commit=False)` to get an _unsaved_ instance.                                                                         | Text‑book use of the `commit` flag ([Creating forms from models \| Django documentation](https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/)). |
| **Let higher layers tweak before hitting DB** | Accepts an optional `inst` (existing object) and `user`, `operation`, `user_ctx` kwargs; sets audit fields.                              | Good: keeps orchestration details outside the model.                                                                                                       |
| **Delegate final persistence**                | `instance.save()` executed only if `commit` is `True`.                                                                                   | Ensures the domain layer’s hooks & signals still fire.                                                                                                     |
| **Surface user‑friendly errors**              | If business logic _inside this method_ fails, it should raise `ValidationError`, not `ValueError`, so the view can render `form.errors`. | See “Improvements” below.                                                                                                                                  |

#### Improvements & advanced ideas
- **Raise `django.core.exceptions.ValidationError`** instead of `ValueError` when something is wrong with user input (e.g., an invalid `operation`). That keeps error handling consistent with Django’s form machinery.
- **Use an enum/`ChoiceField`** for `operation`/`user_ctx` to prevent “stringly‑typed” mistakes (consider `models.TextChoices` in the model and `forms.ChoiceField` in the form).
- If the JSON payload grows complex, look at **`django-jsonfield‑backport`** or PostgreSQL’s `JSONB` with a dedicated `JSONField` serializer for better queryability.

### Model

```python
def save(self, *args, **kwargs) -> "Period":
	"""Override the save method to enforce non-overlapping periods and manage active status."""
	# Ensure start_date is before end_date
	if self.start_date > self.end_date:
		raise ValueError("start_date must be before end_date.")
	
	# Overlap detection (this could be a model method)
	overlapping_periods = Period.objects.filter(
		start_date__lte=self.end_date,
		end_date__gte=self.start_date
	)
	if self.pk:
		overlapping_periods = overlapping_periods.exclude(pk=self.pk)
	
	if overlapping_periods.exists():
		raise ValueError(
			"Another period is already set for this date range "
			f"({overlapping_periods.first()})."
		)
	
	# If the new period is active, deactivate all others
	if self.is_active:
		with transaction.atomic():
			Period.objects.filter(is_active=True).update(is_active=False)
			super().save(*args, **kwargs)
	else:
		super().save(*args, **kwargs)
```

| Obligation                            | In the code                                                   | Comment                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Declare & enforce core invariants** | Checks date ordering and disallows overlaps.                  | Fits the “source‑of‑truth” role of the model.                                                                                                                                                                                                                                                                                                              |
| **Guarantee ACID at row level**       | Uses `transaction.atomic()` when toggling `is_active`.        | Optional: Django already wraps `save()` in an atomic block on supported DBs ([Stack Overflow: Transaction.atomic while overriding save() method in Django model?](https://stackoverflow.com/questions/53115111/transaction-atomic-while-overriding-save-method-in-django-model)). The explicit block is only needed because it updates _other rows_ first. |
| **Emit signals consistently**         | Calls `super().save()`, so `pre_save`/`post_save` still fire. |                                                                                                                                                                                                                                                                                                                                                            |
| **Stay presentation‑agnostic**        | No import from `forms` or HTTP code.                          |                                                                                                                                                                                                                                                                                                                                                            |

#### Improvements & advanced ideas
- **Raise `ValidationError`** instead of `ValueError` for symmetry with `full_clean()`; callers that forget to catch it will still see the error, but admin & REST serializers will handle it gracefully.
- **Move overlap rule to the DB** if you’re on PostgreSQL ≥ 12: use an `ExclusionConstraint` with `range_overlaps` to _guarantee_ non‑overlapping periods even for bulk inserts or external ETL jobs [LAAC Technology](https://www.laac.dev/blog/database-constraints-in-django/).

	```python
	class Period(models.Model):
		# fields...
	    class Meta:
	        constraints = [
	            ExclusionConstraint(
	                name="no_overlap",
	                expressions=[(F("timespan"), "OVERLAPS")]
	            )
	        ]
	```
- **Prefer `.clean()`** if you want errors to show up _before_ `save()` in admin or a form: `full_clean()` will call `clean()` automatically; that keeps the _domain invariant_ but makes it testable via `ModelForm`.
- **Async‑aware**: in Django 5.x you could offer an `aoverlap_safe_save()` helper that uses `await database_sync_to_async(self.save)()` to keep consistency in async tasks.

---

## Connecting to advanced Django topics
- **[Signals](dj-signals.md)** – `ModelForm.save()` ultimately triggers the same `pre_save`/`post_save` hooks as calling the model directly, so signal handlers are agnostic to which layer was used.
- **Atomic transactions** – wrap a whole form wizard in `@transaction.atomic` so both the form’s `save()` and any extra logic roll back together.
- **Bulk operations** – when performance matters, skip forms and use `bulk_create`, `bulk_update`, or `QuerySet.update` + `F()` expressions, but remember: bulk APIs **do not** emit save‑signals or call `save()`.
- **Formsets & `formset.save()`** – orchestrate multiple `ModelForm`s; deleted objects are removed only after `formset.save()`.  ([Formsets | Django documentation](https://docs.djangoproject.com/en/5.2/topics/forms/formsets))
- **Custom validation flow** – override `clean()` in the `ModelForm`, or `clean_<field>()`, or `full_clean()` in the model for DB‑level guarantees.
- **Django REST Framework** – `ModelSerializer.save()` mirrors `ModelForm.save()`, giving the same `commit=False` semantics via `perform_create()` and `perform_update()`.
- **Async views** (since Django 5.0) – `Model.save()` is fully awaitable (`await myobj.asave()`), whereas `ModelForm.save()` remains sync; run it in a thread or refactor for pure‑async model persistence.

## External references & further reading
- Django docs – _Model instance reference_ (`save()`, signals)  ([Model instance reference | Django documentation](https://docs.djangoproject.com/en/5.1/ref/models/instances/))
- Django docs – _Creating forms from models_ (`ModelForm.save()` details, commit flags)  ([Creating forms from models | Django documentation](https://docs.djangoproject.com/en/5.2/topics/forms/modelforms))
- Andrew Godwin, _“On Django’s Save Layers”_ (blog post) – deep dive into transactions and signals.
- Carlton Gibson, _“Django async: from sync save() to asave()”_ – video talk, DjangoCon EU 2024.
- Ticket #29517 – upcoming “bulk_save” proposal (core discussion list).


> [!NOTE]
> ### TL;DR
> 
> `Model.save()` is the low‑level persistence hook; `ModelForm.save()` is a helper that **builds or updates** a model instance _after_ your form data passes validation, then calls that same low‑level hook. Choose the one that matches the abstraction level of your task, and you’ll stay idiomatic—and ready to plug into Django’s richer features like signals, transactions, async, and bulk APIs. 
> 
> **Form layer (`ModelForm.save()`)**
> ‑ Convert validated user input into a model instance (`commit` flag)
> ‑ Attach request‑specific context (current user, UI flags)
> ‑ Raise `ValidationError` for bad user data
> **Model layer (`Model.save()`)**
> ‑ Guarantee domain invariants that must never break (date order, no overlaps)
> ‑ Use DB constraints where possible for bullet‑proof rules
> ‑ Perform cross‑row side‑effects inside a transaction (e.g., unique “active” row)
> ‑ Remain request‑agnostic and always call `super().save()` so signals fire
> 
> Keep user‑context logic in the form (or service) layer; keep core business rules in the model (and the DB). That separation lets every entry‑point—forms, admin, Celery tasks, REST API—stay consistent and bug‑free. 🎯

