---
title: Understanding Django Permissions
tags:
  - studies
  - programming
  - permissions
  - auth
  - security
  - django
use: Management, Security
languages: Python
dependences: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [Understanding Django Permissions in Practice](#understanding-django-permissions-in-practice)
  - [The Basics: Permission Names and Formats](#the-basics-permission-names-and-formats)
  - [Custom Permissions](#custom-permissions)
  - [Enforcing Permissions in Class-Based Views](#enforcing-permissions-in-class-based-views)
    - [Why Use Permission Mixins?](#why-use-permission-mixins)
  - [Advanced Permission Techniques](#advanced-permission-techniques)
    - [Multiple Permissions](#multiple-permissions)
    - [Dynamic Permissions](#dynamic-permissions)
    - [Object-Level Permissions](#object-level-permissions)
  - [Real-World Examples](#real-world-examples)
  - [Tips and Insights](#tips-and-insights)
- [References](#references)

</details>

---

# Understanding Django Permissions in Practice
Django comes with a **robust permissions system** that lets you control access to your application’s models and views. This is a key part of implementing **Role-Based Access Control (RBAC)** and enforcing **fine-grained security** in both traditional web applications and APIs.

Let’s explore how this system works, using real-world examples.

## The Basics: Permission Names and Formats
By default, **Django automatically creates four permissions** for each model:

```
'app_label.action_modelname'
```

For example, if you have an `Document` model in an `articles` app, you get:
- `articles.add_document`: can create documents.
- `articles.change_document`: can edit documents.
- `articles.delete_document`: can delete documents.
- `articles.view_document`: can view documents (since Django 2.1).

These permissions are accessible via the Django admin, APIs, or in your views.

Example:

```python
'auth.add_user'
'auth.change_user'
'auth.delete_user'
'auth.view_user'
```
> Related Topic:
> - [Django Model Permissions Docs](https://docs.djangoproject.com/en/stable/topics/auth/default/#permissions-and-authorization)

## Custom Permissions
Sometimes you need _more than_ the defaults. For example, you might want to grant certain users the ability to **publish** or **feature** an article.

Example model:

```python
class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    
    class Meta:
        permissions = [
            ("publish_document", "Can publish documents"),
            ("feature_document", "Can feature documents on homepage"),
            ("moderate_comments", "Can moderate document comments"),
        ]
```

This pattern is often used in **CMS** and **newsrooms**.
> Related Topic:
> - [Custom Model Permissions](https://docs.djangoproject.com/en/stable/topics/auth/customizing/#custom-permissions)

## Enforcing Permissions in Class-Based Views
The most maintainable way to protect views is using `PermissionRequiredMixin`, this [mixin](dj-mixins.md) makes sure that only users with the right permissions can access a view.

Example for publishing:

```python
class PublishDocumentView(PermissionRequiredMixin, UpdateView):
    model = Document
    permission_required = 'articles.publish_document'
    fields = ['is_published']
```

### Why Use Permission Mixins?
- **Role-based dashboards:**
    ```python
    class AuthorDashboard(PermissionRequiredMixin, TemplateView):
        permission_required = 'articles.add_document'
    
    class EditorDashboard(PermissionRequiredMixin, TemplateView):
        permission_required = 'articles.publish_document'
    
    class AdminDashboard(PermissionRequiredMixin, TemplateView):
        permission_required = 'auth.change_user'
    ```

- **Fine-grained edit and delete:**
    ```python
    class DocumentEditView(PermissionRequiredMixin, UpdateView):
        permission_required = 'articles.change_document'
    
    class DocumentDeleteView(PermissionRequiredMixin, DeleteView):
        permission_required = 'articles.delete_document'
    ```

- **API security:**
    ```python
    class DocumentAPIView(PermissionRequiredMixin, DetailView):
        permission_required = 'articles.view_document'
        
        def render_to_response(self, context):
            return JsonResponse({
                'id': self.object.id,
                'title': self.object.title,
                'content': self.object.content
            })
    ```

These examples demonstrate how Django permissions seamlessly integrate with **class-based views**, **APIs**, and **custom workflows**.

## Advanced Permission Techniques
Django permissions can go beyond simple model-level checks:

### Multiple Permissions
Require all permissions simultaneously:

```python
class SuperAdminView(PermissionRequiredMixin, TemplateView):
    permission_required = [
        'auth.change_user',
        'articles.delete_document',
        'orders.view_financial_data'
    ]
```

### Dynamic Permissions
Decide which permissions are needed at runtime:

```python
class DynamicPermissionMixin:
    def get_permission_required(self):
        if self.request.user.is_staff:
            return ['articles.change_document']
        return ['articles.view_document']
```

### Object-Level Permissions
Check permissions for a _specific object_ (e.g., using `django-guardian`):

```python
class ObjectPermissionMixin:
    def has_permission(self):
        if not super().has_permission():
            return False
        obj = self.get_object()
        return self.request.user.has_perm(self.permission_required, obj)
```
> Related Topic:
> - [django-guardian: Object-Level Permissions](https://django-guardian.readthedocs.io/)

## Real-World Examples
Here are a few scenarios you might build:

- **Content Management System:**
    ```python
    class CreatePostView(PermissionRequiredMixin, CreateView):
        permission_required = 'blog.add_post'
    
    class PublishPostView(PermissionRequiredMixin, UpdateView):
        permission_required = 'blog.publish_post'
    ```

- **E-commerce Admin:**
    ```python
    class RefundOrderView(PermissionRequiredMixin, UpdateView):
        permission_required = 'orders.refund_order'
    ```

- **API Endpoint:**
    ```python
    class UserAPIView(PermissionRequiredMixin, DetailView):
        permission_required = 'auth.view_user'
    
        def render_to_response(self, context):
            return JsonResponse({
                'id': self.object.id,
                'username': self.object.username
            })
    ```


## Tips and Insights
- **Combine authentication and permissions** to secure both access and actions.
- **Custom messages and handling:** override `handle_no_permission()` for JSON error responses or redirects.
- **Dynamic and object-level permissions** are essential in apps where ownership matters.
- **Use packages** like `django-guardian` for advanced per-object permission control.
- **Audit permissions regularly** to ensure your *RBAC* remains consistent.

---

# References
1. [Django Permissions and Authorization](https://docs.djangoproject.com/en/stable/topics/auth/default/#permissions-and-authorization)
2. [Customizing Permissions](https://docs.djangoproject.com/en/stable/topics/auth/customizing/#custom-permissions)
3. [PermissionRequiredMixin](https://docs.djangoproject.com/en/stable/topics/class-based-views/mixins/#django.contrib.auth.mixins.PermissionRequiredMixin)
4. [django-guardian: Object-Level Permissions](https://django-guardian.readthedocs.io/)
5. [Django REST Framework Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
6. [Role-Based Access Control (RBAC)](https://en.wikipedia.org/wiki/Role-based_access_control)
