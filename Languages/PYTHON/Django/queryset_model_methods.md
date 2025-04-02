---
title: QuerySet Model Methods
tags: studies, programming, python, django, querysets, models, views
use: Organizing Code
languages: Python
dependences: Django
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

### 🧪 Testing

Separating QuerySets makes testing easier. Example:

```python
def test_pending_orders_returns_only_pending():
    Order.objects.create(status='pending')
    Order.objects.create(status='completed')

    result = Order.pending_orders()
    assert result.count() == 1
```

---

### 📌 Practical Recommendations

| Case | Where to put it |
|------|------------------|
| Simple filter used once | `views.py` |
| Medium complexity & reusable | model class method or `Manager` |
| Complex & chainable filters | Custom `QuerySet` / `Manager` |
| View-specific query | Separate `services.py` file |

---

### 💡 Final Tip

If you’re ending up with **too many methods** in `models.py`, it might be time to:

1. Use `managers` or custom `querysets`;
2. Start modularizing your app (`apps`, `services`, etc).
