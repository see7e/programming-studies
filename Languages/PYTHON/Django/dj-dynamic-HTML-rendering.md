---
title: Dynamic HTML Rendering in Django
tags:
  - studies
  - programming
  - django
use: Documentation
languages: Python, HTML, CSS
dependences: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [Dynamic HTML Rendering in Django: From Nested Dictionaries to Structured HTML](#dynamic-html-rendering-in-django-from-nested-dictionaries-to-structured-html)
  - [The Basic Challenge](#the-basic-challenge)
  - [Django Template-Based Rendering](#django-template-based-rendering)
    - [Why?](#why)
    - [Basic Template](#basic-template)
    - [View Function](#view-function)
  - [Advanced Table Rendering in Templates](#advanced-table-rendering-in-templates)
  - [Safe Rendering with Filters](#safe-rendering-with-filters)
  - [Django Custom Template Tag: Recursive Renderer](#django-custom-template-tag-recursive-renderer)
  - [Responsive Styling with Django](#responsive-styling-with-django)
  - [Performance Optimizations](#performance-optimizations)
  - [Testing HTML Output](#testing-html-output)
  - [Related Topics](#related-topics)
- [References](#references)

</details>

---

# Dynamic HTML Rendering in Django: From Nested Dictionaries to Structured HTML
Rendering nested dictionaries as structured, safe, styled HTML is a **core scenario in Django**, especially in:
- **admin dashboards**
- **custom reports**
- **dynamic templates for API data**
- **CMS content rendering**

## The Basic Challenge
**Example nested dictionary**:

```python
data = {
    "user_details": {
        "name": "John Doe",
        "email": "john@example.com",
        "role": "Developer",
    },
    "performance_metrics": {
        "score": 85,
        "projects_completed": 12,
        "rating": "Excellent",
    },
    "metadata": {
        "last_updated": "2024-01-15",
        "department": "Engineering",
    },
}
```

We want to turn this into **clean, semantic, safe HTML**.

## Django Template-Based Rendering
### Why?
- Django templates have **automatic escaping** (protection against XSS).
- Clean separation of **logic (views) and presentation (templates)**.

### Basic Template
Create a Django template, e.g., `templates/data_display.html`:

```django
<div class="data-container">
  {% for key, value in data.items %}
    <section class="data-section">
      <h2>{{ key|capfirst }}</h2>
      {% if value.items %}
        <dl>
          {% for nested_key, nested_value in value.items %}
            <div class="data-field">
              <dt>{{ nested_key|capfirst }}</dt>
              <dd>{{ nested_value }}</dd>
            </div>
          {% endfor %}
        </dl>
      {% else %}
        <p>{{ value }}</p>
      {% endif %}
    </section>
  {% endfor %}
</div>
```

This template:  
- Iterates safely over nested dictionaries  
- Uses semantic HTML ([`<dl>`](https://www.w3schools.com/tags/tag_dl.asp))  
- Auto-escapes output
- (optional) Sets some keys and values as capitalized ([`capfirst`](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#capfirst)) words

### View Function
At **views.py**:

```python
from django.shortcuts import render

def show_data(request):
    data = {
        "user_details": {
            "name": "John Doe",
            "email": "john@example.com",
            "role": "Developer",
        },
        # ...
    }
    return render(request, "data_display.html", {"data": data})
```

## Advanced Table Rendering in Templates
If you want **table output**, create `templates/data_table.html`:

```django
<table class="data-table">
  <tbody>
    {% for key, value in data.items %}
      <tr>
        <th>{{ key|capfirst }}</th>
        <td>
          {% if value.items %}
            <table class="nested-table">
              {% for nested_key, nested_value in value.items %}
                <tr>
                  <th>{{ nested_key }}</th>
                  <td>{{ nested_value }}</td>
                </tr>
              {% endfor %}
            </table>
          {% else %}
            {{ value }}
          {% endif %}
        </td>
      </tr>
    {% endfor %}
  </tbody>
</table>
```

## Safe Rendering with Filters
When you absolutely must output raw HTML, use the `safe` filter cautiously (**But avoid this** unless you **fully control** `some_html`):

```django
<div>{{ some_html|safe }}</div>
```

Instead, prefer **escaping** with `{{ value }}` or `{{ value|escape }}`.

## Django Custom Template Tag: Recursive Renderer
If you want a more elegant approach, try *recursive rendering* with arbitrary nesting, use a **custom template tag**.

At **templatetags/render_dict.py**:

```python
from django import template

register = template.Library()

@register.inclusion_tag('render_dict_recursive.html')
def render_dict(data):
    return {'data': data}
```

At **templates/render_dict_recursive.html**:

```django
<ul>
  {% for key, value in data.items %}
    <li>
      <strong>{{ key|capfirst }}:</strong>
      {% if value.items %}
        {% include "render_dict_recursive.html" with data=value %}
      {% else %}
        {{ value }}
      {% endif %}
    </li>
  {% endfor %}
</ul>
```

**Usage in your main template:**

```django
{% load render_dict %}
<div class="nested-dict">
  {% render_dict data %}
</div>
```

## Responsive Styling with Django
Add CSS:

```css
.nested-dict ul {
  list-style: none;
  padding-left: 1rem;
}
.nested-dict li {
  margin-bottom: 0.5rem;
}
@media (max-width: 768px) {
  .nested-dict ul {
    padding-left: 0.5rem;
  }
}
```

## Performance Optimizations
- If your dictionary is **very large**, pre-process it in the view to avoid rendering thousands of items in templates.
- Use **pagination** if appropriate.
- Cache the rendered HTML using Django’s *template fragment caching*:

```django
{% load cache %}
{% cache 600 large_dict data %}
  {% render_dict data %}
{% endcache %}
```

## Testing HTML Output
Django’s `TestCase` makes it easy to test rendered HTML:

```python
def test_render_contains_key(self):
	response = self.client.get('/your-url/')
	self.assertContains(response, 'User Details')
```

Is also possible to test the rendered templates.

```python
def test_templates_rendered_correctly(self, mock_success, mock_error):
	"""Test that all views render the correct templates."""
	for url in self.urls:
		with self.subTest(msg=f"Testing route: {url}"):
			view_name = resolve(str(url)).view_name
			response = self.client.get(url)
			
			for expected_templates in URL_INFO[view_name]["templates"]:
				self.assertTemplateUsed(response, expected_templates)
```

## Related Topics
- **Django Serializer + `JSONField`**: if you need to store nested dictionaries in the database.   [Docs](https://docs.djangoproject.com/en/stable/ref/contrib/postgres/fields/#jsonfield)
- **Django Template Filters**: custom filters for formatting nested data.   [Custom filters](https://docs.djangoproject.com/en/stable/howto/custom-template-tags/#writing-custom-template-filters)
- **Django Debug Toolbar**: helps you see rendered templates and performance.   [Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)

---

In Django, **dynamic dictionary rendering** is best done via:
- Template-based rendering  
- Custom template tags for recursion  
- Automatic escaping  
- Semantic HTML  
- Optional caching for performance

# References
- [Django Template Language: for](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#for)
- [Django Autoescape](https://docs.djangoproject.com/en/stable/topics/templates/#automatic-html-escaping)
- [Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Django Template Inheritance](https://docs.djangoproject.com/en/stable/topics/templates/#template-inheritance)
- [Safe HTML in Django](https://docs.djangoproject.com/en/stable/topics/security/#cross-site-scripting-xss-protection)
- [Reusable Template Tags](https://docs.djangoproject.com/en/stable/howto/custom-template-tags/)
