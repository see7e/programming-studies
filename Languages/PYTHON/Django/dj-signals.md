---
title: Django Signals
tags: studies, programming, python, django
use: Documentation
languages: Python
dependences: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [Django Signals: Complete Guide to Event-Driven Architecture](#django-signals-complete-guide-to-event-driven-architecture)
  - [Understanding Django Signals](#understanding-django-signals)
    - [How Django Signals Work](#how-django-signals-work)
    - [Built-in Signals](#built-in-signals)
  - [Implementing Django Signals](#implementing-django-signals)
    - [Basic Signal Usage](#basic-signal-usage)
    - [Signal Registration](#signal-registration)
    - [Creating Custom Signals](#creating-custom-signals)
  - [Advanced Signal Patterns](#advanced-signal-patterns)
    - [Signal Arguments and Parameters](#signal-arguments-and-parameters)
    - [Conditional Signal Handling](#conditional-signal-handling)
    - [Audit Trail Implementation](#audit-trail-implementation)
  - [Signal Performance and Considerations](#signal-performance-and-considerations)
    - [Synchronous Nature](#synchronous-nature)
    - [Performance Impact](#performance-impact)
    - [Limitations and Pitfalls](#limitations-and-pitfalls)
  - [Testing Django Signals](#testing-django-signals)
    - [Approach 1: Mock the Receiver](#approach-1-mock-the-receiver)
    - [Approach 2: Test Signal Effects](#approach-2-test-signal-effects)
    - [Approach 3: Manual Signal Testing](#approach-3-manual-signal-testing)
  - [Related Technologies and Patterns](#related-technologies-and-patterns)
    - [Django Signals vs Middleware](#django-signals-vs-middleware)
    - [Custom Middleware Integration](#custom-middleware-integration)
    - [Asynchronous Signal Handling](#asynchronous-signal-handling)
    - [Database Transactions and Signals](#database-transactions-and-signals)
  - [Best Practices](#best-practices)
    - [Organization and Structure](#organization-and-structure)
    - [Performance Optimization](#performance-optimization)
    - [Error Handling](#error-handling)
    - [When to Use Signals](#when-to-use-signals)
    - [When NOT to Use Signals](#when-not-to-use-signals)
  - [Alternative Approaches](#alternative-approaches)
    - [Override Model Methods](#override-model-methods)
    - [Django Lifecycle Hooks](#django-lifecycle-hooks)
- [References](#references)

</details>

---

# Django Signals: Complete Guide to Event-Driven Architecture
Django signals provide a powerful mechanism for implementing **event-driven architecture** in Django applications. They ==**enable decoupled communication between different components, allowing certain senders to notify a set of receivers when specific actions occur**==[^1][^2]. This comprehensive guide explores Django signals, their implementation, best practices, and related concepts.

## Understanding Django Signals
Django signals are based on the **Observer Design Pattern**, facilitating a high degree of decoupling between *event producers* (senders) and *consumers* (receivers)[^1][^3]. The signal dispatcher helps decoupled applications get notified when actions occur elsewhere in the framework[^2].

### How Django Signals Work
At its core, the signal dispatching system **enables certain senders** (usually Django models) **to notify a set of receivers** (functions or methods) when certain events occur[^4]. The process involves three main components:
1. *Signal Definition*: Creating or using built-in signals;
2. *Receiver Registration*: Connecting functions to respond to signals;
3. *Signal Dispatching*: Sending signals when events occur.

### Built-in Signals
Django provides several built-in signals for common use cases[^5][^6]:

| Signal             | When It Triggers                  |
| :----------------- | :-------------------------------- |
| `pre_save`         | Right before a model is saved     |
| `post_save`        | Right after a model is saved      |
| `pre_delete`       | Right before a model is deleted   |
| `post_delete`      | Right after a model is deleted    |
| `m2m_changed`      | When a many-to-many field changes |
| `request_finished` | When an HTTP request ends         |
| `user_logged_in`   | When a user logs in               |
| `user_logged_out`  | When a user logs out              |

## Implementing Django Signals

### Basic Signal Usage
Here's a simple example of using the `post_save` signal to create a user profile automatically when a new user signs up[^5]:

```python
# accounts/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

### Signal Registration
Is important to ensure that signals are loaded when Django starts, **you need to import them in your app's `apps.py`**[^5][^7]:

```python
# accounts/apps.py
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = 'accounts'
    
    def ready(self):
        import accounts.signals
```

### Creating Custom Signals
You can define custom signals for application-specific events[^5][^8]:

```python
# signals.py
from django.dispatch import Signal

# Define a custom signal
order_placed = Signal()

# In your views or logic
order_placed.send(sender=None, order_id=123, customer_email="user@example.com")
```

## Advanced Signal Patterns

### Signal Arguments and Parameters
Signal receivers must accept specific arguments[^1][^2]:
- `sender`: The *model class* that sent the signal;
- `instance`: The actual *instance* being  modified (saved/deleted);
- `created`: Boolean indicating *if a new record was created* (for `post_save`);
- `**kwargs`: Additional keyword arguments.

### Conditional Signal Handling
You can implement conditional logic within signal handlers[^9]:

```python
@receiver(pre_save, sender=MyModel)
def set_dynamic_field(sender, instance, **kwargs):
    if instance.some_condition:
        instance.dynamic_field = 'Value based on condition'
```

### Audit Trail Implementation
Signals are excellent for implementing **audit trails**[^9]:

```python
@receiver(post_save, sender=MyModel)
def log_audit(sender, instance, created, **kwargs):
    action = 'Created' if created else 'Updated'
    with transaction.atomic():
        AuditLog.objects.create(
            action=action,
            instance_id=instance.id,
            instance_data=str(instance)
        )
```

## Signal Performance and Considerations

### Synchronous Nature
**Django signals are synchronous by default**[^10][^11]. When a signal is triggered, all receivers are executed synchronously before the sending function continues. This has important implications:
- **Signal handlers block the main execution flow**;
- Heavy operations in signal handlers **can impact performance**[^12];
- *Database operations in signals are part of the same transaction*[^13].

### Performance Impact
The performance of signals depends on[^12]:
- Number of connected handlers;
- Complexity of receiver code;
- Database operations within handlers.

For heavy operations, consider using background task queues like [Celery](dj-celery.md)[^5][^12].

### Limitations and Pitfalls
Signals have several important limitations[^14]:
1. **Can be circumvented**: Bulk operations (`bulk_create`, `bulk_update`) don't trigger signals;
2. **Request unaware**: Signals don't have access to request objects;
3. **Debugging challenges**: Signal execution can be hard to trace[^10];
4. **Silent failures**: Errors in signal handlers may fail silently[^15].

> [!QUESTION]
> ### Should the `receiver` return something (like a callback function)?
> All four methods return a list of tuple pairs `[(receiver, response), ...]`, representing the list of called receiver functions and their response values [^2].
> But the problem here is to catch the retuned values of multiple results from multiple receivers.

## Testing Django Signals
Testing signals requires specific approaches[^16][^17][^18], note that is possible to be tested separately or altogether.

### Approach 1: Mock the Receiver

```python
from unittest.mock import patch
import pytest

@pytest.mark.django_db
@patch('myapp.signals.send_email')
def test_user_creation_signal(mock_send_email):
    User.objects.create(username='testuser', email='test@example.com')
    mock_send_email.assert_called_once()
```

### Approach 2: Test Signal Effects

```python
@pytest.mark.django_db
def test_profile_creation():
    user = User.objects.create(username='testuser')
    assert Profile.objects.filter(user=user).exists()
```

### Approach 3: Manual Signal Testing

```python
def test_signal_handler():
    user = User(username='testuser', email='test@example.com')
    create_user_profile(User, user, created=True)
    # Assert expected behavior
```

## Related Technologies and Patterns

### Django Signals vs Middleware
While both signals and middleware can intercept and process requests/responses, they serve different purposes[^19]:
- **Signals**: Event-driven *communication between decoupled components*;
- **Middleware**: *Global request/response* processing pipeline.

### Custom Middleware Integration
You can combine signals with custom middleware for comprehensive event handling[^20][^21]:

```python
class AuditTrailMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Pre-processing
        response = self.get_response(request)
        # Post-processing with signals
        audit_signal.send(sender=None, request=request, response=response)
        return response
```

### Asynchronous Signal Handling
For asynchronous operations, consider these alternatives[^22][^23][^24]:
1. **Celery Integration**: Use Celery tasks within signal handlers;
2. **Async Signal Libraries**: Third-party packages like `async-signals`;
3. **Django's `transaction.on_commit()`**: Defer execution until transaction ;commits[^25].

### Database Transactions and Signals
As mentioned, Signals execute within the same database transaction as the triggering operation[^13][^25]. To defer signal execution until after transaction commit:

```python
from django.db import transaction

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    transaction.on_commit(lambda: perform_defered_task(instance.id))
```

## Best Practices

### Organization and Structure
1. **Dedicated signals module**: Create `signals.py` files for each app[^7];
2. **Proper registration**: Import signals in `apps.py` `ready()` method;
3. **Clear naming**: Use descriptive names for signal handlers;
4. **Documentation**: Document signal purposes and triggers[^26].

### Performance Optimization
1. **Minimize signal usage**: Use signals prudently[^10][^14];
2. **Lightweight handlers**: Keep signal handlers simple and fast;
3. **Async operations**: Use background (async) tasks for heavy operations;
4. **Conditional execution**: Add guards to prevent unnecessary execution.

### Error Handling
1. **Exception handling**: Wrap signal code in try-catch blocks[^15];
2. **Logging**: Implement comprehensive logging for debugging;
3. **Testing**: Write rigorous tests for signal behavior;
4. **Monitoring**: Use tools like Sentry (can fix this 🐱) for production error tracking[^27].

### When to Use Signals
Signals are appropriate for[^28]:
- Cross-app communication
- Audit logging and tracking
- Cache invalidation
- Notification systems
- Event-driven workflows

### When NOT to Use Signals
Avoid signals when[^10][^14]:
- Logic is tightly coupled to a specific model
- Simple operations that can be done in model methods (don't overengineer)
- Operations requiring specific execution order
- Performance-critical code paths

## Alternative Approaches

### Override Model Methods
For simple cases, overriding model methods might be more appropriate[^31][^10], but keep in mind to not break LSP.

```python
class MyModel(models.Model):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Custom logic here
        send_notification(self)
```
### Django Lifecycle Hooks
Consider `django-lifecycle` as an alternative that provides more organized event handling[^29][^30].  This way you avoid overloading the parent (`models.Model`)  `save()` method.

```python
from django_lifecycle import LifecycleModel, hook, AFTER_SAVE

class MyModel(LifecycleModel):
    @hook(AFTER_SAVE)
    def after_save_change(self):
        pass # Handle status change
```

I won't enter in much detail here to avoid escaping the scope, but here's the `@hook` signature and the [default moment flags](https://rsinger86.github.io/django-lifecycle/hooks_and_conditions/#lifecycle-moments):

```python
@hook(
    moment: str,
    condition: Optional[types.Condition] = None,
    priority: int = DEFAULT_PRIORITY,
    on_commit: Optional[bool] = None,
	
    # Legacy parameters
    when: str = None,
    when_any: List[str] = None,
    has_changed: bool = None,
    is_now: Any = '*',
    is_not: Any = None,
    was: Any = '*',
    was_not: Any = None,
    changes_to: Any = None,
)
```

---

Django signals provide a powerful mechanism for implementing event-driven architecture and decoupling application components. While they offer significant benefits for code organization and modularity, they should be used with careful consideration of their **synchronous nature**, **performance implications**, and **debugging challenges**.

When implemented properly with appropriate testing, error handling, and performance considerations, Django signals can significantly enhance application architecture and maintainability. The key is understanding when to use them and when simpler alternatives might be more appropriate.

# References
[^1] [Mastering Django Signals: A Comprehensive Guide - GUVI Blogs](https://www.guvi.in/blog/guide-for-django-signals-and-their-uses/)
[^2] [Signals - Django documentation](https://docs.djangoproject.com/en/5.2/topics/signals/)
[^3] [Understanding Signals in Django - SitePoint](https://www.sitepoint.com/understanding-signals-in-django/)
[^4] [Django Signals mastery - DEV Community](https://dev.to/yokwejuste/django-signals-mastery-144d)
[^5] [How to Use Django Signals in Your Projects - freeCodeCamp](https://www.freecodecamp.org/news/how-to-use-django-signals-in-your-projects/)
[^6] [Signals - Django documentation](https://docs.djangoproject.com/en/5.2/ref/signals/)
[^7] [Where Should Signal Handlers Live in a Django Project](https://www.geeksforgeeks.org/where-should-signal-handlers-live-in-a-django-project/)
[^8] [A Comprehensive Guide to Custom Signals in Django - hashnode.dev](https://musaaib.hashnode.dev/mastering-decoupled-communication-a-comprehensive-guide-to-custom-signals-in-django)
[^9] [Advanced Django Signals: 4 Powerful Use Cases Explained](https://www.technaureus.com/blog-detail/advanced-django-signals-4-powerful-use-cases-expla)
[^10] [Django Anti-Patterns: Signals - Lincoln Loop](https://lincolnloop.com/blog/django-anti-patterns-signals/)
[^11] [Sync or Async? Unpacking the Mysteries of Django Signals](https://www.mattlayman.com/blog/2023/django-signals-async/)
[^12] [Performance of signals in Django - Stack Overflow](https://stackoverflow.com/questions/10839834/performance-of-signals-in-django)
[^13] [Sending and receiving custom signals and ensuring it is atomic](https://forum.djangoproject.com/t/sending-and-receiving-custom-signals-and-ensuring-it-is-atomic/27964)
[^14] [Signals - Django antipatterns](https://www.django-antipatterns.com/antipattern/signals.html)
[^15] [How do I make Django signal handlers not fail silently](https://stackoverflow.com/questions/14481225/how-do-i-make-django-signal-handlers-not-fail-silently-when-an-exception-is-enco)
[^16] [Five Ways to Test Django Signals - Python in Plain English](https://python.plainenglish.io/five-ways-to-test-django-signals-9f3643664d2d)
[^17] [Django Signals - Automated Tests - tech.serhatteker.com](https://tech.serhatteker.com/post/2024-09/django-signals-automated-tests/)
[^18] [How to test Django Signals like a pro - freeCodeCamp](https://www.freecodecamp.org/news/how-to-testing-django-signals-like-a-pro-c7ed74279311/)
[^19] [What is the difference between signal and middleware in Django?](https://stackoverflow.com/questions/73620854/what-is-the-difference-between-signal-and-middleware-in-django)
[^20] [Mastering Django's Hidden Powers: Signals & Custom Middleware!](https://www.linkedin.com/pulse/mastering-djangos-hidden-powers-signals-custom-muhammad-nasser-ji9cf)
[^21] [django custom middleware - build an audit trail - Kipchirchir Langat](https://blog.kipchirchirlangat.com/implementing-an-audit-trail-middleware-in-django-for-tracking-user-actions-in-django)
[^22] [nyergler/async-signals: Asynchronous signal handling for Django](https://github.com/nyergler/async-signals)
[^23] [async-signals - PyPI](https://pypi.org/project/async-signals/)
[^24] [Django Signals: Sync/Async? - Python in Plain English](https://python.plainenglish.io/django-signals-sync-async-c2bd3294e403)
[^25] [Trigering post\_save signal only after transaction has completed](https://stackoverflow.com/questions/33180727/trigering-post-save-signal-only-after-transaction-has-completed)
[^26] [The Power of Django Signals: Boosting App Performance](https://nuventureconnect.com/blog/2024/01/12/the-power-of-django-signals-boosting-app-performance-full-guide/)
[^27] [Mastering Django debugging: a complete guide - Aubergine Solutions](https://www.aubergine.co/insights/mastering-django-debugging-a-complete-guide)
[^28] [Use case for signals : r/django - Reddit](https://www.reddit.com/r/django/comments/150o42r/use_case_for_signals/)
[^29] [Django Lifecycle Hooks: A better alternative to signals - KubeBlogs](https://www.kubeblogs.com/django-lifecycle-hooks/)
[^30] [rsinger86/django-lifecycle - GitHub](https://github.com/rsinger86/django-lifecycle)
[^31] [Django Signals vs. Overriding Save Method - GeeksforGeeks](https://www.geeksforgeeks.org/python/django-signals-vs-overriding-save-method/)
[^32] [What Are Django Signals & How Do Django Signals Work in 2024](https://www.horilla.com/blogs/what-are-django-signals-and-how-do-django-signals-work/)
[^33] [Django Signals: Structure, Use Cases, and Best Practices - Reddit](https://www.reddit.com/r/django/comments/1ize1cz/django_signals_structure_use_cases_and_best/)
[^34] [How to setup django signals in django project - Stack Overflow](https://stackoverflow.com/questions/76594563/how-to-setup-django-signals-in-django-project-which-has-multiple-apps-in-it)
[^35] [Signals good practice to use User built in model - Django Forum](https://forum.djangoproject.com/t/signals-good-practice-to-use-user-built-in-model/29008)
[^36] [Best Practice Using Django Signal - Stack Overflow](https://stackoverflow.com/questions/62392576/best-practice-using-django-signal-for-user-authentication)
[^37] [Django Signals - Introduction! - YouTube](https://www.youtube.com/watch?v=8p4M-7VXhAU)
[^38] [How to Create and Use Signals in Django ? - GeeksforGeeks](https://www.geeksforgeeks.org/python/how-to-create-and-use-signals-in-django/)
[^39] [debugging django signals' problems - Stack Overflow](https://stackoverflow.com/questions/6011512/debugging-django-signals-problems)
[^40] [Testing and Debugging in Django: Advanced Techniques and Tools](https://www.scoutapm.com/testing-and-debugging-in-django-advanced-techniques-and-tools/)
[^41] [Django signals vs API](https://forum.djangoproject.com/t/django-signals-vs-api/16388)
[^42] [Alternate to Django Signals in FastAPI!!!!!! - Reddit](https://www.reddit.com/r/FastAPI/comments/odh0sj/alternate_to_django_signals_in_fastapi/)
[^43] [Why Signals are bad? : r/django - Reddit](https://www.reddit.com/r/django/comments/1evvaeu/why_signals_are_bad/)
[^44] [Alternatives to Django post\_save - Stack Overflow](https://stackoverflow.com/questions/61357135/alternatives-to-django-post-save)
[^45] [Django Signals: Handling Events and Notifications | Seldom India](https://seldomindia.com/django-signals-handling-events-and-notifications/)
[^46] [Mastering Django Signals: A Comprehensive Guide - Stackademic](https://blog.stackademic.com/mastering-django-signals-a-comprehensive-guide-153d11c856e3)
[^47] [How to test my code inside the Django built-in signals - Reddit](https://www.reddit.com/r/django/comments/igz357/how_to_test_my_code_inside_the_django_builtin/)
[^48] [Signals - Advanced Django Training](https://django-advanced-training.readthedocs.io/en/latest/features/signals/)
[^49] [How to catch Exception raised in pre\_save Signal](https://www.reddit.com/r/django/comments/k1em32/how_to_catch_exception_raised_in_pre_save_signal/)
[^50] [Proper way to test Django signals - Stack Overflow](https://stackoverflow.com/questions/3817213/proper-way-to-test-django-signals)
[^51] [Registering Multiple Signals in Django - Stack Overflow](https://stackoverflow.com/questions/5923012/registering-multiple-signals-in-django)
[^52] [Testing in Django Tutorial #13 - Testing Signals - YouTube](https://www.youtube.com/watch?v=DWMM0IJ2uNw)
[^53] [How to add a Django custom signal to worked out request](https://stackoverflow.com/questions/74912330/how-to-add-a-django-custom-signal-to-worked-out-request)
[^54] [Middleware - Django documentation](https://docs.djangoproject.com/en/5.2/topics/http/middleware/)
[^55] [How to Set Up Custom Middleware in Django? | GeeksforGeeks](https://www.geeksforgeeks.org/how-to-set-up-custom-middleware-in-django/)
[^56] [Django - signals. Simple examples to start - Stack Overflow](https://stackoverflow.com/questions/27803633/django-signals-simple-examples-to-start)
[^57] [django-realworld-example-app/conduit/apps/authentication/signals](https://github.com/gothinkster/django-realworld-example-app/blob/master/conduit/apps/authentication/signals.py)
[^58] [Using Django's Built in Signals and Writing Custom Signals](https://micropyramid.com/blog/using-djangos-built-in-signals-and-writing-custom-signals/)
[^59] [How To Build Secure Django Apps By Using Custom Middleware](https://www.nilebits.com/blog/2024/10/how-to-build-secure-django-apps/)
[^60] [mansha99/django-custom-and-model-signals - GitHub](https://github.com/mansha99/django-custom-and-model-signals)
[^61] [Unlocking the Power of Django Signals: Revolutionize Your Web](https://mathison.ch/en-ch/blog/unlocking-the-power-of-django-signals-revolutioniz/)
[^62] [Introducing Django Signals and the Observer Pattern - YouTube](https://www.youtube.com/watch?v=SYT_Me2uZXs)
[^63] [Signals - Django's bug tracker](https://code.djangoproject.com/wiki/Signals)
[^64] [Design Patterns in Django - Reddit](https://www.reddit.com/r/django/comments/1j6emk/design_patterns_in_django/)
[^65] [Signals - Django v1.2 documentation - Pythonhosted.org](https://pythonhosted.org/django_simple_feedback/topics/signals.html)
[^66] [Understanding Django Signals - Earthly Blog](https://earthly.dev/blog/django-signals/)
[^67] [Django Signals 2025 - A Hands-On Guide to Event-Driven Apps](https://blog.devgenius.io/django-signals-2025-a-hands-on-guide-to-event-driven-apps-3af7d6464928)
[^68] [Signals - django-simple-history 3.10.1 documentation](https://django-simple-history.readthedocs.io/en/stable/signals.html)
[^69] [Sinais (Signals) - Django 1.0 documentation](https://django-portuguese.readthedocs.io/en/1.0/topics/signals.html)
[^70] [aaugustin/django-transaction-signals - GitHub](https://github.com/aaugustin/django-transaction-signals)
[^71] [Authentication and Authorization Using Middleware in Django](https://www.scoutapm.com/blog/authentication-and-authorization-using-middleware-in-django)
[^72] [Database transactions - Django documentation](https://docs.djangoproject.com/en/5.2/topics/db/transactions/)
[^73] [Django Signals vs Database Triggers. Which one to go for? - Reddit](https://www.reddit.com/r/django/comments/it93qb/django_signals_vs_database_triggers_which_one_to/)
[^74] [How to achieve Async Signals without celery : r/django - Reddit](https://www.reddit.com/r/django/comments/15k02yw/how_to_achieve_async_signals_without_celery/)
[^75] [Is Django post\_save signal asynchronous? - Stack Overflow](https://stackoverflow.com/questions/11899088/is-django-post-save-signal-asynchronous)
[^76] [Asynchronous support - Django documentation](https://docs.djangoproject.com/en/5.2/topics/async/)
