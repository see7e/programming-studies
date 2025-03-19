---
---

# Securing User Inputs in Django

Django provides built-in functionality for input sanitization and validation, and generally, Django's methods are more comprehensive and safer than creating custom solutions on simple functions.

### Django's Built-In Functionality

The validation and cleaning are seamlessly integrated into forms and models, which makes it easier to manage as part of the overall application structure.

1. **Form Validation**: automatically validate and clean user input based on the field types. For example, `CharField`, `IntegerField`, `BooleanField`, etc., each have their own validation and cleaning mechanisms. You can also define  custom `clean_<fieldname>()` methods within a form class to provide additional validation and cleaning.

2. **Model Validation**: provides validation mechanisms similar to forms. When you save a model, Django will run the `full_clean()` method, which validates and cleans the data according to the field definitions.

3. **Template Escaping**: the templates automatically escape HTML special characters by default, preventing XSS attacks. If you want to render raw HTML, you must explicitly mark the content as safe using the `|safe` filter.

4. **Security**: Overall the security features built into Django have been thoroughly tested and are maintained by the community. They are generally safer because they handle edge cases that might be overlooked in custom implementations.
   - **Security Middleware**: Django includes middleware that helps protect against various attacks, including XSS, CSRF, and SQL injection.

5. **Django's `bleach` Library**: for more aggressive sanitization, Django can be integrated with the `bleach` library, which allows you to clean and sanitize HTML, CSS, and JavaScript content.

6. **Flexibility**: allows you to extend or override the cleaning process through custom methods.

7. **Performance**: Since Django’s validation is tightly coupled with its ORM and template system, it's optimized for performance within that context.

If you’re working within a Django project, it’s better to rely on Django’s form and model validation, along with its template escaping and middleware, rather than implementing a custom solution. The custom function might be useful in non-Django environments or very specific cases, but within Django, it's almost always better to use the built-in tools.

## Implementing

1. **Form Validation and Cleaning**: We'll create a Django form that validates and cleans input.
2. **Model Validation and Cleaning**: We'll create a model with fields that include validation and custom cleaning.
3. **Template Escaping**: We'll show how Django templates automatically escape content to prevent XSS attacks.
4. **View to Handle Form Submission**: We'll add a view to handle the form submission and model saving.
5. **URL Configuration**: We'll add the view to the URL configuration.
6. **Other Aproaches**

### 1. Form Validation and Cleaning

First, let's create a Django form that includes validation and cleaning:

```python
# forms.py
from django import forms
from django.core.exceptions import ValidationError
import re

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=0, max_value=120)
    email = forms.EmailField()
    website = forms.URLField(required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    # Custom validation method for the name field
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[a-zA-Z\s]+$', name):
            raise ValidationError('Name can only contain letters and spaces.')
        return name

    # Custom validation method for the website field
    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website and not website.startswith('https'):
            raise ValidationError('Website must start with https.')
        return website

    # General clean method for the entire form
    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        comments = cleaned_data.get('comments')

        # Custom validation for comments based on age
        if age and age < 18 and comments:
            raise ValidationError('Comments are not allowed for users under 18.')
        return cleaned_data
```

### 2. Model Validation and Cleaning

Next, let's create a Django model with validation and custom cleaning:

```python
# models.py
from django.db import models
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(f'{value} is not an even number.')

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[validate_even])
    email = models.EmailField()
    bio = models.TextField()

    # Custom clean method for the model
    def clean(self):
        super().clean()
        if self.age < 0:
            raise ValidationError('Age cannot be negative.')

        if 'forbidden' in self.bio.lower():
            raise ValidationError('Bio contains forbidden content.')

    def __str__(self):
        return self.name
```

### 3. Template Escaping

Django templates automatically escape HTML content to prevent XSS attacks. Here's how you might render data in a template:

```html
<!-- template.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Form</title>
</head>
<body>
    <h1>Submit Your Details</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>

    {% if form.errors %}
        <ul>
            {% for field in form %}
                {% for error in field.errors %}
                    <li>{{ error }}</li>
                {% endfor %}
            {% endfor %}
        </ul>
    {% endif %}

    <h2>Your Bio</h2>
    <p>{{ mymodel.bio }}</p>
</body>
</html>
```

### 4. View to Handle Form Submission

Let's add a view to handle the form submission and model saving. Notice that in here you can add some extra layers on the view function using decorators like `@login_required`, `@require_http_methods`, and `@permission_required` to secure the view function.

```python
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from .forms import MyForm
from .models import MyModel

@login_required
@require_http_methods(['GET', 'POST'])
@permission_required('auth.access_myapp')
def submit_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Normally save the form data or create a model instance
            my_model = MyModel(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
                bio=form.cleaned_data['comments']
            )
            try:
                my_model.full_clean()  # Validates the model
                my_model.save()  # Saves to the database
                return redirect('success_page')
            except ValidationError as e:
                form.add_error(None, e.message_dict)
    else:
        form = MyForm()

    return render(request, 'template.html', {'form': form})
```

### 5. URL Configuration

Finally, make sure to add the view to your URL configuration:

```python
# urls.py
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('submit/', views.submit_form, name='submit_form'),
    path('success/', views.success_page, name='success_page'),
]
```

### 6. Other Approaches

If you used only the frontend to send the data, using AJAX or HTMX these are some other approaches to secure the data:

- **CORS Policy**: If you're sending data from a different domain, you need to set up the CORS policy to allow the request.
- **CSRF Token**: If you're using AJAX, you need to include the CSRF token in the request headers.
- **Content Security Policy (CSP)**: You can set up a CSP to restrict the sources of content that can be loaded on your site.
- **HTTP Headers**: You can set up various HTTP headers to improve security, such as HSTS, X-Frame-Options, etc.
- **Rate Limiting**: You can implement rate limiting to prevent abuse of your API endpoints.

#### Ajax Example

```javascript
// script.js
const element = document.querySelector('#elementId');
element.addEventListener('click', async () => {
    $.ajax('{% url "submit_form" %}', { // leveraging Django's URL template tag
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}', // leveraging Django's CSRF token template tag
        },
        body: JSON.stringify({
            name: 'John Doe',
            age: 30,
            email: 'mail@mail.com',
        })
    });
    if (response.ok) {
        const data = await response.json();
        console.log(data);
    } else {
        console.error('Failed to submit form');
    }
});
```

#### HTMX Example

```html
<!-- template.html -->
<script src="https://unpkg.com/htmx.org"></script>
<button id="send_form"
    hx-post="{% url 'submit_form' %}"
    hx-headers="{'X-CSRFToken': '{{ csrf_token }}'}"
    hx-trigger="click"
    <!-- other hx-attributes -->
>
```
