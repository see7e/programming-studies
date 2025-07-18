---
title: Python - Django Testings
tags: studies, programming, testing, pyhton, django
uses: Documentation
languages: Python
dependencies: Django
---

<details> <summary>Table of Contents 🔖</summary>

- [Organize Your Tests](#organize-your-tests)
- [Write Different Types of Tests](#write-different-types-of-tests)
- [Use Django’s `TestCase`](#use-djangos-testcase)
- [Fixture Management](#fixture-management)
- [Use Mocks and Patches](#use-mocks-and-patches)
  - [Understanding Mocks and Patches](#understanding-mocks-and-patches)
    - [Mocks](#mocks)
    - [Patches](#patches)
  - [When to Use Mocks and Patches](#when-to-use-mocks-and-patches)
  - [How to Use Mocks and Patches](#how-to-use-mocks-and-patches)
    - [Basic Example of Mocking](#basic-example-of-mocking)
    - [Patching Objects](#patching-objects)
    - [Context Manager with Patch](#context-manager-with-patch)
  - [Using Mock Side Effects](#using-mock-side-effects)
  - [Testing Django Models with Mock](#testing-django-models-with-mock)
- [Run Tests Frequently](#run-tests-frequently)
- [Test Coverage](#test-coverage)
- [Use Django’s Testing Utilities](#use-djangos-testing-utilities)
- [Test Isolated Units](#test-isolated-units)
- [Use Assertions Effectively](#use-assertions-effectively)
- [Testing Asynchronous Code](#testing-asynchronous-code)
- [External References and Further Reading](#external-references-and-further-reading)

</details>

---

Developing tests in Django is crucial for ensuring that your application works correctly and remains maintainable over time. Here are some best practices for developing tests in Django:

> [!WARNING]
> Be very cautious, some views when not very structured can lead to a fragile test case. Find here some [common pitfalls](dj-testing-common-pitfalls.md).

## Organize Your Tests
   - **Separate Test Modules:** Organize tests in a directory called `tests` within each app. This makes it easy to locate and manage tests.
   - **Use Descriptive Names:** Name your test functions and methods clearly to describe what they test.

## Write Different Types of Tests
   - **Unit Tests:** Test individual pieces of code (e.g., models, forms, utilities).
   - **Integration Tests:** Test how different pieces of code work together (e.g., views interacting with models).
   - **End-to-End Tests:** Or also called *Functional Tests*, test the full workflow of the application (e.g., using tools like Selenium for browser-based testing).

## Use Django’s `TestCase`
   - **Django’s `TestCase` Class:** This is a subclass of Python’s `unittest.TestCase` that comes with built-in database support, allowing you to test database interactions.
   ```python
   from django.test import TestCase

   class MyModelTest(TestCase):
       def test_something(self):
           self.assertEqual(1 + 1, 2)
   ```

## Fixture Management
   - **Use Factories Over Fixtures:** Use libraries like `Factory Boy` to create test data dynamically. Fixtures are static and can become outdated or cumbersome.
   ```python
   import factory
   from myapp.models import MyModel

   class MyModelFactory(factory.django.DjangoModelFactory):
       class Meta:
           model = MyModel
	
       field1 = 'test'
       field2 = 123
   ```

## Use Mocks and Patches

### Understanding Mocks and Patches

#### Mocks
Mocks are objects that simulate the behavior of real objects in controlled ways. They are used to replace parts of your system under test and make assertions about how they have been used.

#### Patches
Patches are used to temporarily replace an object in the module with another object during a test. This is useful for replacing external dependencies with mocks.

> [!QUESTION] If the object is replaced, should I patch in the module definition or where it (the symbol) is imported?
> *`patch()` **does not** replace the _definition_ in the original module that defined it. It ==only replaces **the binding in the namespace you patch**==.* See [more in here](dj-testing-common-pitfalls.md#wich-path-to-patch).

### When to Use Mocks and Patches
- **Mock External Services:** Use `unittest.mock` to mock external service calls to ensure your tests do not depend on external systems.
- **External Services:** When your code interacts with external APIs, databases, or services.
- **Dependencies:** When you want to isolate a function or method from its dependencies.
- **Performance:** When certain operations are slow or resource-intensive.
- **State Management:** When the function under test modifies shared state.
   ```python
   from unittest.mock import patch

   @patch('myapp.services.external_service')
   def test_external_service(self, mock_service):
       mock_service.return_value = 'mocked result'
       # Test the function that calls the external service
   ```

### How to Use Mocks and Patches

#### Basic Example of Mocking
In order to isolate the code and ensuring that the tests do not depend on external systems or other parts of your codebase. Here is a basic example of mocking an external API call in a Django view.

```python
# views.py
import requests
from django.shortcuts import render

def fetch_data(request):
    response = requests.get('https://api.example.com/data')
    data = response.json()
    return render(request, 'data.html', {'data': data})
```

```python
# test_views.py
from django.test import TestCase
from unittest.mock import patch

class FetchDataTest(TestCase):
    @patch('myapp.views.requests.get')
    def test_fetch_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'key': 'value'}
		
        response = self.client.get('/fetch-data/')
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'value')
```

#### Patching Objects
Use `patch()` to replace an object with a mock within a particular scope.

```python
# services.py
import requests

def get_user_data(user_id):
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

# test_services.py
from unittest import TestCase
from unittest.mock import patch
from myapp.services import get_user_data

class GetUserDataTest(TestCase):
    @patch('myapp.services.requests.get')
    def test_get_user_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'id': 1, 'name': 'John Doe'}

        data = get_user_data(1)
        
        self.assertEqual(data, {'id': 1, 'name': 'John Doe'})
```

#### Context Manager with Patch
Use `patch()` as a context manager for a temporary replacement.

```python
from unittest import TestCase
from unittest.mock import patch
from myapp.services import get_user_data

class GetUserDataTest(TestCase):
    def test_get_user_data(self):
        with patch('myapp.services.requests.get') as mock_get:
            mock_response = mock_get.return_value
            mock_response.json.return_value = {'id': 1, 'name': 'John Doe'}
            
            data = get_user_data(1)
            
            self.assertEqual(data, {'id': 1, 'name': 'John Doe'})
```

### Using Mock Side Effects
Side effects can be used to raise exceptions or return different values on subsequent calls.

```python
# services.py
import requests

def get_user_data(user_id):
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

# test_services.py
from unittest import TestCase
from unittest.mock import patch, Mock
from myapp.services import get_user_data

class GetUserDataTest(TestCase):
    @patch('myapp.services.requests.get')
    def test_get_user_data_with_side_effect(self, mock_get):
        mock_get.side_effect = [
            Mock(status_code=200, json=lambda: {'id': 1, 'name': 'John Doe'}),
            Mock(status_code=404, json=lambda: {'error': 'Not Found'})
        ]
		
        data = get_user_data(1)
        self.assertEqual(data, {'id': 1, 'name': 'John Doe'})
		
        data = get_user_data(2)
        self.assertEqual(data, {'error': 'Not Found'})
```

### Testing Django Models with Mock
Sometimes you need to mock model methods or properties.

```python
# models.py
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

# test_models.py
from django.test import TestCase
from unittest.mock import patch
from myapp.models import UserProfile

class UserProfileTest(TestCase):
    @patch('myapp.models.UserProfile.get_full_name')
    def test_get_full_name(self, mock_get_full_name):
        mock_get_full_name.return_value = 'Mocked Name'
        profile = UserProfile.objects.create(user=User.objects.create(username='testuser'))
        
        self.assertEqual(profile.get_full_name(), 'Mocked Name')
```

## Run Tests Frequently
   - **Continuous Integration (CI):** Integrate your test suite with a CI tool (e.g., GitHub Actions, Travis CI) to run tests automatically on every push.
   - **Local Testing:** Run tests frequently during development to catch issues early.

## Test Coverage
   - **Measure Test Coverage:** Use tools like `coverage.py` to measure test coverage and identify untested parts of your code.
   ```bash
   coverage run --source='.' manage.py test
   coverage report -m
   ```

## Use Django’s Testing Utilities
   - **Client:** Use Django’s test client to simulate requests and test views.
   ```python
   from django.test import TestCase, Client

   class MyViewTest(TestCase):
       def setUp(self):
           self.client = Client()
	
       def test_my_view(self):
           response = self.client.get('/my-url/')
           self.assertEqual(response.status_code, 200)
   ```
   - **LiveServerTestCase:** For integration tests that require a live server (e.g., Selenium tests).
   ```python
   from django.contrib.staticfiles.testing import LiveServerTestCase
   from selenium import webdriver

   class MySeleniumTest(LiveServerTestCase):
       def setUp(self):
           self.browser = webdriver.Chrome()
		
       def tearDown(self):
           self.browser.quit()
	
       def test_login(self):
           self.browser.get(self.live_server_url + '/login/')
           # Continue testing...
   ```

## Test Isolated Units
   - **Isolate Tests:** Ensure tests are isolated and do not depend on each other or external state.
   - **Database Isolation:** Each test should run in its own transaction and should not affect other tests.

## Use Assertions Effectively
   - **Specific Assertions:** Use specific assertions provided by `unittest` and `Django` to check different conditions.
   ```python
   self.assertTrue(condition)
   self.assertEqual(obj1, obj2)
   self.assertContains(response, text)
   ```

## Testing Asynchronous Code
   - **Django Channels:** If you are using Django Channels, use the `ChannelsLiveServerTestCase` for testing WebSocket consumers.
   ```python
   from channels.testing import ChannelsLiveServerTestCase
   from channels.layers import get_channel_layer
   from asgiref.testing import ApplicationCommunicator

   class MyConsumerTest(ChannelsLiveServerTestCase):
       async def test_my_consumer(self):
           channel_layer = get_channel_layer()
           communicator = ApplicationCommunicator(MyConsumer, {"type": "websocket.connect"})
           await communicator.send_input({"type": "websocket.connect"})
           response = await communicator.receive_output()
           self.assertEqual(response["type"], "websocket.accept")
   ```

## External References and Further Reading
- [Django Testing Documentation](https://docs.djangoproject.com/en/stable/topics/testing/): Refer to the official Django testing documentation for detailed guidance and best practices.
- **Third-Party Libraries:** Utilize third-party libraries that enhance Django testing, such as `pytest-django`.
- [unittest.mock — Mocking and Patching](https://docs.python.org/3/library/unittest.mock.html)
- [Testing in Django](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/)
- [Effective Django Testing](https://testdriven.io/blog/django-testing/)
- [Mocking in Python: A Guide to Better Unit Tests](https://realpython.com/python-mock-library/)