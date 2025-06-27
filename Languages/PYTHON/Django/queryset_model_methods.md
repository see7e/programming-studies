---
title: QuerySet Model Methods
tags: studies, programming, python, django, querysets, models, views
use: Organizing Code
languages: Python
dependences: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [Reflection about **separation of concerns**, **testability**, and **maintainability**](#reflection-about-separation-of-concerns-testability-and-maintainability)
    - [✅ TL;DR (short summary)](#-tldr-short-summary)
    - [📦 Options \& Best Practices](#-options--best-practices)
      - [1. **Model Methods**](#1-model-methods)
      - [2. **Custom Managers**](#2-custom-managers)
      - [3. **Services or Repositories (an extra layer)**](#3-services-or-repositories-an-extra-layer)
    - [Testing 🧪](#testing-)
    - [Practical Recommendations](#practical-recommendations)
- [Integrating Service Layer with Django Models Managers](#integrating-service-layer-with-django-models-managers)
  - [What Changes vs What Stays the Same](#what-changes-vs-what-stays-the-same)
    - [Stays the Same](#stays-the-same)
    - [What Changes](#what-changes)
  - [Example to Illustrate](#example-to-illustrate)
  - [If You Want Default Optimizations](#if-you-want-default-optimizations)

</details>

---

# Reflection about **separation of concerns**, **testability**, and **maintainability**
> all solid design principles in Django (and software development in general).


> Let’s say in my views (in several of them), I call multiple QuerySets from models with different filters. Would it be better to keep these queries in the `views.py` file or create model methods inside `models.py`? I think about this because of test creation—it makes more sense to me to test the querysets inside the models. However, there are many of them. Which file should I “pollute” less?

---

### ✅ TL;DR (short summary)

- **Extract complex QuerySet logic into model methods (or managers) when:**
  - The logic is reused across multiple views;
  - The queryset is complex or needs to be tested in isolation;
  - You want a cleaner abstraction layer for testing and maintenance.

- **Keep it in `views.py` when:**
  - The logic is very simple and used only in that view.

---

### 📦 Options & Best Practices

#### 1. **Model Methods**
```python
# models.py
class Order(models.Model):
    status = models.CharField(...)
    customer = models.ForeignKey(...)

    @classmethod
    def pending_orders(cls):
        return cls.objects.filter(status='pending')
```

- ✅ Great for shared logic across multiple views.
- ✅ Easily testable in `tests/test_models.py`.
- ❌ Can clutter `models.py` if there are **too many methods**.

#### 2. **Custom Managers**
```python
class OrderQuerySet(models.QuerySet):
    def pending(self):
        return self.filter(status='pending')

class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    def pending(self):
        return self.get_queryset().pending()

class Order(models.Model):
    status = models.CharField(...)
    objects = OrderManager()
```

Usage:
```python
orders = Order.objects.pending()
```

- ✅ Very useful when you have multiple reusable filters.
- ✅ Helps keep things better organized than cramming everything into the model.
- ✅ Great for chaining (`.filter().pending().recent()` etc.)
- ✅ Excellent for testing.

#### 3. **Services or Repositories (an extra layer)**

If queries are highly contextual (e.g., business logic specific to one view), you can isolate that logic in a module:

```python
# services/orders.py
def get_orders_for_dashboard():
    return Order.objects.filter(status='pending', date__gte=timezone.now() - timedelta(days=7))
```

- ✅ Isolates view-specific logic that doesn’t quite belong on the model.
- ✅ Testable separately.
- ✅ Avoids polluting `views.py`.

---

### Testing 🧪
Separating `QuerySets` makes testing easier. Example:

```python
def test_pending_orders_returns_only_pending():
    Order.objects.create(status='pending')
    Order.objects.create(status='completed')

    result = Order.pending_orders()
    assert result.count() == 1
```

---

### Practical Recommendations

| Case                         | Where to put it                 |
| ---------------------------- | ------------------------------- |
| Simple filter used once      | `views.py`                      |
| Medium complexity & reusable | model class method or `Manager` |
| Complex & chainable filters  | Custom `QuerySet` / `Manager`   |
| View-specific query          | Separate `services.py` file     |

# Impact over the default Model.Manager()
In Django, the lines are often blurred because:
- `Managers` are convenient and "feel" Pythonic
- `QuerySets` are lazy and composable
- The [Active Record Pattern](../../../Docs/django-active_record-pattern.md) encourages putting logic on models

**My recommendation**: Start with managers for simple cases, but don't hesitate to introduce services when complexity grows. The hybrid approach often works well in Django projects.

But what about the default methods of the past `models.Manager()`? Are they lost when a custom Manager is implemented?

## What Changes vs What Stays the Same

### Stays the Same
- `Model.objects.all()` - works normally
- `Model.objects.filter(...)` - works normally
- `Model.objects.exclude(...)` - works normally
- `Model.objects.get(...)` - works normally
- All other standard `QuerySet` methods work normally

### What Changes
- **New custom methods**: `Ticket.objects.assigned_to_user(user)` becomes available
- **Query optimization**: If your custom `QuerySet` overrides `get_queryset()` to add default `select_related()` or `prefetch_related()`, those optimizations apply to ALL queries
- **Default filtering**: If you add default filters in `get_queryset()`, they apply to all queries

## Example to Illustrate

```python
class TicketQuerySet(models.QuerySet["Ticket"]):
    def assigned_to_user(self, user: AbstractBaseUser) -> QuerySet:
        return self.filter(stage_tracking__assigned_to=user)

class TicketManager(models.Manager["Ticket"]):
    def get_queryset(self) -> TicketQuerySet:
        return TicketQuerySet(self.model, using=self._db)
    
    def assigned_to_user(self, user: AbstractBaseUser) -> QuerySet:
        return self.get_queryset().assigned_to_user(user)

class Ticket(models.Model):
    objects = TicketManager()
	# model fields ...
```

**These all work exactly the same as before:**

```python
Ticket.objects.all()                    # Works
Ticket.objects.filter(title="Test")     # Works  
Ticket.objects.exclude(status="DONE")   # Works
Ticket.objects.get(id=1)                # Works
```

**This is new:**

```python
Ticket.objects.assigned_to_user(some_user)  # New custom method
```

## If You Want Default Optimizations

If you want **ALL** queries to have certain optimizations by default, you can override `get_queryset()`:

```python
class TicketManager(models.Manager["Ticket"]):
    def get_queryset(self) -> TicketQuerySet:
        return TicketQuerySet(
	        self.model, using=self._db
		).select_related(
			'user', 'category'
		)
```

Then even `Ticket.objects.all()` would include those `select_related()` optimizations automatically.
