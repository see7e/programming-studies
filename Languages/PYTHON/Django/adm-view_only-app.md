---
title: Keeping a Django App Admin-Only
tags:
  - studies
  - programming
  - deprecation
use: Documentation
languages: Python
dependences: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [Keeping a Django App Admin-Only (View-Only App)](#keeping-a-django-app-admin-only-view-only-app)
  - [1. Leave It in `INSTALLED_APPS`](#1-leave-it-in-installed_apps)
  - [2. Disable URLs and Views](#2-disable-urls-and-views)
  - [3. Limit Access in Admin](#3-limit-access-in-admin)
  - [4. Flag Models Internally](#4-flag-models-internally)
  - [5. Hide in Admin with a Feature Flag (optional)](#5-hide-in-admin-with-a-feature-flag-optional)
  - [Related Concepts and Tools](#related-concepts-and-tools)

</details>

---

# Keeping a Django App Admin-Only (View-Only App)
If you want to keep a deprecated app's models *accessible in the Django Admin*, but prevent them from being interacted with via views, APIs, or external forms, here's a clean strategy:

## 1. Leave It in `INSTALLED_APPS`
Do *not* remove it from `INSTALLED_APPS`, so migrations and admin will still work.

## 2. Disable URLs and Views
Ensure you don’t include any views or URL routes from the app:

```python
# <my_project>/urls.py
# Do NOT include:
# path('app_*/', include('app_*.urls')),
```

## 3. Limit Access in Admin
If you're concerned about editing/deleting data, make the models *read-only in Django Admin*:

```python
# app_worktime/admin.py
from django.contrib import admin
from app_*.models import WorkLog

@admin.register(WorkLog)
class WorkLogAdmin(admin.ModelAdmin):
    readonly_fields = [f.name for f in WorkLog._meta.fields]
    def has_add_permission(self, request): return False
    def has_delete_permission(self, request, obj=None): return False
    def has_change_permission(self, request, obj=None): return False
```

## 4. Flag Models Internally
Mark models as deprecated or legacy:

```python
# app_*/models.py
class WorkLog(models.Model):
    """[DEPRECATED] Only available for read-only admin access."""
    ...
```

## 5. Hide in Admin with a Feature Flag (optional)

```python
if settings.SHOW_LEGACY_MODELS:
    admin.site.register(WorkLog, WorkLogAdmin)
```

---
## Related Concepts and Tools

* *Test filtering* with [`pytest-django`](https://pytest-django.readthedocs.io/en/latest/)
* *Admin customization* in [Django Admin Docs](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
* Using [badges with shields.io](https://shields.io/) dynamically based on test thresholds
* Excluding apps in coverage reports via `.coveragerc`:

```ini
[run]
omit =
    */migrations/*
    app_*/*
```
