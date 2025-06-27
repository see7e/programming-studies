---
title: Understanding Django Permissions
tags:
  - studies
  - programming
  - permissions
  - auth
use: Documentation
languages: Python
dependences: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [New Note](#new-note)

</details>

---
- [i] #to_review : Reescrever, explicar examplos, conectar, tags, toc
# Understanding Django Permissions
## In Class-Based Views
### Permission Format: `app_label.action_modelname`

```python
# Django automatically creates these permissions for each model:
'articles.add_article'     # Can create articles
'articles.change_article'  # Can edit articles  
'articles.delete_article'  # Can delete articles
'articles.view_article'    # Can view articles (Django 2.1+)

# Built-in User model permissions:
'auth.add_user'
'auth.change_user' 
'auth.delete_user'
'auth.view_user'
```

### Custom Permissions:

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    
    class Meta:
        permissions = [
            ('publish_article', 'Can publish articles'),
            ('feature_article', 'Can feature articles on homepage'),
            ('moderate_comments', 'Can moderate article comments'),
        ]

# Usage:
class PublishArticleView(PermissionRequiredMixin, UpdateView):
    model = Article
    permission_required = 'articles.publish_article'
    fields = ['is_published']
```

### Why Permission Mixins are Beneficial:

#### Role-Based Access Control

```python
# Different views for different roles
class AuthorDashboard(PermissionRequiredMixin, TemplateView):
    permission_required = 'articles.add_article'
    template_name = 'author_dashboard.html'

class EditorDashboard(PermissionRequiredMixin, TemplateView):
    permission_required = 'articles.publish_article'
    template_name = 'editor_dashboard.html'

class AdminDashboard(PermissionRequiredMixin, TemplateView):
    permission_required = 'auth.change_user'
    template_name = 'admin_dashboard.html'
```

#### Fine-Grained Security

```python
class ArticleEditView(PermissionRequiredMixin, UpdateView):
    model = Article
    permission_required = 'articles.change_article'
    fields = ['title', 'content']

class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Article
    permission_required = 'articles.delete_article'
    success_url = '/articles/'
```

#### API Security

```python
class ArticleAPIView(PermissionRequiredMixin, DetailView):
    model = Article
    permission_required = 'articles.view_article'
    
    def render_to_response(self, context):
        return JsonResponse({
            'id': self.object.id,
            'title': self.object.title,
            'content': self.object.content
        })
```

### Enhanced Permission Mixin:

```python
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseForbidden, JsonResponse
from django.core.exceptions import PermissionDenied

class PermissionRequiredMixin:
    permission_required = None
    permission_denied_message = "You don't have permission to access this page."
    raise_exception = False  # If True, raise PermissionDenied instead of returning 403
    
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
    def has_permission(self):
        """Check if user has required permission"""
        if self.permission_required is None:
            return True
        
        if not self.request.user.is_authenticated:
            return False
            
        # Handle multiple permissions
        perms = self.get_permission_required()
        return self.request.user.has_perms(perms)
    
    def get_permission_required(self):
        """Return list of permissions required"""
        if self.permission_required is None:
            return []
        
        if isinstance(self.permission_required, str):
            return [self.permission_required]
        return self.permission_required
    
    def handle_no_permission(self):
        """Handle when user lacks permission"""
        if self.raise_exception:
            raise PermissionDenied(self.permission_denied_message)
        
        # Handle AJAX requests
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'error': 'Permission denied',
                'message': self.permission_denied_message
            }, status=403)
        
        # Add error message
        if self.permission_denied_message:
            messages.error(self.request, self.permission_denied_message)
        
        return HttpResponseForbidden(self.permission_denied_message)
```

### Advanced Usage Patterns:

#### Multiple Permissions:

```python
class SuperAdminView(PermissionRequiredMixin, TemplateView):
    permission_required = [
        'auth.change_user',
        'articles.delete_article',
        'orders.view_financial_data'
    ]  # User must have ALL these permissions
    template_name = 'super_admin.html'
```

#### Combining with Authentication:

```python
class SecureArticleView(RequireLoginMixin, PermissionRequiredMixin, UpdateView):
    model = Article
    permission_required = 'articles.change_article'
    fields = ['title', 'content']
    
    def get_queryset(self):
        # Additional security: users can only edit their own articles
        return Article.objects.filter(author=self.request.user)
```

#### Dynamic Permissions:

```python
class DynamicPermissionMixin:
    def get_permission_required(self):
        """Override to calculate permission dynamically"""
        if self.request.user.is_staff:
            return ['articles.change_article']
        else:
            return ['articles.view_article']

class ArticleView(DynamicPermissionMixin, DetailView):
    model = Article
```

#### Object-Level Permissions:

```python
class ObjectPermissionMixin:
    def has_permission(self):
        """Check both model-level and object-level permissions"""
        # Check basic permission first
        if not super().has_permission():
            return False
        
        # Check object-level permission
        obj = self.get_object()
        return self.request.user.has_perm(self.permission_required, obj)

class ArticleEditView(ObjectPermissionMixin, UpdateView):
    model = Article
    permission_required = 'articles.change_article'
    
    # With django-guardian or similar package:
    # User needs 'change_article' permission on this specific article
```

### Real-World Scenarios:

#### Content Management System:

```python
class CreatePostView(RequireLoginMixin, PermissionRequiredMixin, CreateView):
    model = Post
    permission_required = 'blog.add_post'
    fields = ['title', 'content', 'category']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PublishPostView(PermissionRequiredMixin, UpdateView):
    model = Post
    permission_required = 'blog.publish_post'  # Custom permission
    fields = ['is_published']
```

#### E-commerce Admin:

```python
class OrderManagementView(PermissionRequiredMixin, ListView):
    model = Order
    permission_required = 'orders.view_order'
    template_name = 'admin/orders.html'

class RefundOrderView(PermissionRequiredMixin, UpdateView):
    model = Order
    permission_required = 'orders.refund_order'  # Custom permission
    fields = ['refund_amount', 'refund_reason']
```

#### API Endpoints:

```python
class APIPermissionMixin(PermissionRequiredMixin):
    def handle_no_permission(self):
        return JsonResponse({
            'error': 'Permission denied',
            'required_permission': self.permission_required
        }, status=403)

class UserAPIView(APIPermissionMixin, DetailView):
    model = User
    permission_required = 'auth.view_user'
    
    def render_to_response(self, context):
        return JsonResponse({
            'id': self.object.id,
            'username': self.object.username,
            'email': self.object.email
        })
```
