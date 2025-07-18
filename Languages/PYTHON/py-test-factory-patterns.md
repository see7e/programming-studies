---
title: Python - Test Factory Patterns
tags:
  - studies
  - programming
  - deep-dive
  - patterns
  - testing
  - factory-pattern
  - class-methods
  - instance-methods
  - architecture
  - design-patterns
  - design-principles
  - best-practices
  - common-pitfalls
use: Documentation
languages: Python
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [Test Factory Patterns](#test-factory-patterns)
  - [Understanding the Core Problem](#understanding-the-core-problem)
  - [The Factory Pattern in Python Testing](#the-factory-pattern-in-python-testing)
    - [What is a Factory Pattern?](#what-is-a-factory-pattern)
    - [Factory Pattern Benefits in Testing](#factory-pattern-benefits-in-testing)
  - [Class Methods vs Instance Methods in Testing](#class-methods-vs-instance-methods-in-testing)
    - [Understanding the Distinction](#understanding-the-distinction)
    - [When to Use Class Methods in Testing](#when-to-use-class-methods-in-testing)
  - [Solution Analysis: Two Approaches](#solution-analysis-two-approaches)
    - [Solution 1: Parameter-Based Approach](#solution-1-parameter-based-approach)
    - [Solution 2: Class-Level Storage](#solution-2-class-level-storage)
  - [Best Practices for Python Test Factories](#best-practices-for-python-test-factories)
    - [1. Choose the Right Method Type](#1-choose-the-right-method-type)
    - [2. Factory Method Design Principles](#2-factory-method-design-principles)
  - [Advanced Factory Pattern Implementations](#advanced-factory-pattern-implementations)
    - [Class-Based Factory with Registry](#class-based-factory-with-registry)
    - [Enum-Based Factory Selection](#enum-based-factory-selection)
  - [Testing Framework Integration](#testing-framework-integration)
    - [`unittest` Integration](#unittest-integration)
    - [`pytest` Integration](#pytest-integration)
  - [Performance Considerations](#performance-considerations)
    - [Memory vs. Database Objects](#memory-vs-database-objects)
    - [Caching Strategies](#caching-strategies)
  - [Common Pitfalls and Solutions](#common-pitfalls-and-solutions)
    - [1. Shared State Issues](#1-shared-state-issues)
    - [2. Factory-Model Synchronization](#2-factory-model-synchronization)
    - [3. Over-Engineering](#3-over-engineering)
  - [Testing the Factory Pattern](#testing-the-factory-pattern)
    - [Unit Testing Factory Methods](#unit-testing-factory-methods)
    - [Integration Testing](#integration-testing)
- [References](#references)

</details>

---

# Test Factory Patterns
> A Comprehensive Guide to Class-Level Setup and Object Creation

One of the fundamental challenges in Python testing: **how to effectively manage object creation and initialization in test environments**. This article explores the deeper concepts around Python *test factory patterns*, class methods, and the critical *distinction between class-level and instance-level operations* in testing frameworks.

## Understanding the Core Problem
A common architectural challenge in Python testing e.g.: `TestObjectFactory` class *attempts to use an instance attribute* (`app_name`) *within a class method* (`set_up`). This mismatch highlights the fundamental difference between class methods and instance methods[^1][^2].

```python
class TestObjectFactory:
    app_name: str  # Ensures app_name is a defined attribute
	
    def __init__(self, app_name: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.app_name = app_name
	
    def _get_app_name(self) -> str: ...
	
    @classmethod
    def set_up(cls) -> None:
        cls.default_user, cls.manager_user = cls._create_users(cls.app_name) # <-- main issue is here
        (
            cls.unlogged_client,
            cls.default_client,
            cls.manager_client,
        ) = Client(), Client(), Client()
        cls._log_user_in(cls.default_client, cls.default_user)
        cls._log_user_in(cls.manager_client, cls.manager_user)
	
    @classmethod
    def _create_users(cls, app_name: str) -> Tuple[object, object]: ...
    @classmethod
    def _log_user_in(cls, client: object, user: object) -> None: ...
    @classmethod
    def get_clients_and_contexts(cls) -> List[Tuple[object, str]]: ...
```

The issue is created by accessing instance data (`self.app_name`) from a class method (`@classmethod`), which only has access to the class itself (`cls`) rather than any specific instance. This is a crucial distinction that affects how we design factory patterns in Python testing frameworks.

## The Factory Pattern in Python Testing

### What is a Factory Pattern?
In short, is a creational design pattern that provides an interface for creating objects without specifying their concrete classes[^3][^4]. In testing contexts, factory patterns are particularly valuable because they:
- **Centralize object creation logic**[^4]
- **Reduce code duplication** across test cases
- **Provide consistent test data** generation
- **Enable dynamic object creation** based on parameters

### Factory Pattern Benefits in Testing
Factory patterns in testing offer several advantages:
1. **Separation of Concerns**: The factory handles object creation while tests focus on behavior verification[^4]
2. **Maintainability**: Changes to object creation logic are centralized[^5]
3. **Consistency**: All tests use the same object creation mechanism[^6]
4. **Flexibility**: Easy to modify object creation without affecting individual tests[^7]

## Class Methods vs Instance Methods in Testing

### Understanding the Distinction
The fundamental difference between class methods and instance methods is crucial for understanding the original problem[^1][^2]:
- **Instance methods** operate on specific instances and have access to `self`
- **Class methods** operate on the class itself and have access to `cls`
- **Static methods** operate independently of both class and instance data

### When to Use Class Methods in Testing

Class methods are particularly useful in testing for:
1. **Setup operations that apply to all test instances**[^8]
2. **Factory methods that create test objects**[^2]
3. **Shared initialization logic**[^9]

The `setUpClass` method in `unittest` (also used in [Django test suite](Django/dj-tests.md)) is a perfect example of when class methods are appropriate - it **runs once before all tests** in a class, *making it ideal for expensive setup operations*[^8].

## Solution Analysis: Two Approaches

### Solution 1: Parameter-Based Approach
The first solution passes `app_name` as a parameter to the `set_up` method, by implementing a [dependency injection](../../Docs/to_review/dependency-injection.md) approach:

```python
@classmethod
def set_up(cls, app_name: str) -> None:
    """Set up test data common to all test cases."""
    cls.default_user, cls.manager_user = cls._create_users(app_name)
    # ... rest of setup
```

**Advantages:**
- **Explicit parameter passing** makes dependencies clear
- **Flexible** - different `app_name` values can be used for different setups
- **No side effects** on class state
- **Follows functional programming principles**

**Disadvantages:**
- **Requires caller to provide** `app_name` each time
- **Less convenient** for repeated use
- **Breaks encapsulation** if `app_name` is conceptually tied to the class

### Solution 2: Class-Level Storage
The second solution stores `app_name` at the class level:

```python
def __init__(self, app_name: str, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    self.app_name = app_name
    self.__class__.app_name = app_name  # Set at class level
```

**Advantages:**
- **Maintains the original interface** of `set_up`
- **Convenient access** from class methods
- **Preserves encapsulation** of `app_name` within the class

**Disadvantages:**
- **Potential race conditions** if multiple instances modify class attributes
- **Shared state** between instances
- **Less predictable** behavior in multi-threaded environments

## Best Practices for Python Test Factories

### 1. Choose the Right Method Type
Select method types based on their intended use[^10]:
- **Instance methods**: For operations that depend on specific object state
- **Class methods**: For alternative constructors and shared operations
- **Static methods**: For utility functions that don't require class or instance data

### 2. Factory Method Design Principles
When designing factory methods, consider these principles[^6]:
- **Keep factories minimal**: Only include required data
- **Use traits for optional data**: Avoid defaults that might change
- **Prefer `build()` over `create()`**: Use memory objects when possible
- **Maintain factory-model sync**: Keep factories updated with model changes[^5]

Choose between different setup strategies based on your needs[^8][^9]:
- **`setUp()`**: For per-test initialization
- **`setUpClass()`**: For expensive, shared initialization
- **Factory methods**: For dynamic object creation
- **Fixtures**: For reusable test data

> [!TIP]
> ### (Optional) Avoid by Mocking
> In some cases, you might not need a full factory pattern. Instead, consider using mocking interfaces, that allows you to simplify your tests by mimicking the behavior of complex objects without needing to instantiate them. This can be particularly useful for external dependencies or services.
> 
> ```python
> from unittest.mock import Mock
> class TestObjectFactory:
>     @classmethod
>     def create_mock_user(cls, user_type: str):
>         """Create a mocked user object."""
>         mock_user = Mock()
>         mock_user.type = user_type
>         return mock_user
> ```

## Advanced Factory Pattern Implementations

### Class-Based Factory with Registry
A more sophisticated approach uses a registry pattern:

```python
class TestObjectFactory:
    _factories = {}
    
    @classmethod
    def register(cls, app_name: str):
        """Register a factory for a specific app."""
        def decorator(factory_class):
            cls._factories[app_name] = factory_class
            return factory_class
        return decorator
    
    @classmethod
    def create(cls, app_name: str):
        """Create a factory instance for the given app."""
        if app_name not in cls._factories:
            raise ValueError(f"No factory registered for {app_name}")
        return cls._factories[app_name]()
```

This approach provides:
- **Dynamic registration** of factories
- **Type safety** through class-based implementation
- **Extensibility** for new application types

### Enum-Based Factory Selection
Using enums for factory selection provides type safety and clarity[^11]:

```python
from enum import Enum

class AppType(Enum):
    WEB = "web"
    MOBILE = "mobile"
    API = "api"

class TestObjectFactory:
    @classmethod
    def create_for_app(cls, app_type: AppType):
        factory_map = {
            AppType.WEB: cls._create_web_factory,
            AppType.MOBILE: cls._create_mobile_factory,
            AppType.API: cls._create_api_factory,
        }
        return factory_map[app_type]()
```

## Testing Framework Integration

### `unittest` Integration
When integrating with `unittest`, consider the lifecycle methods[^8] (some used above at the initial example):
- **`setUpClass()`**: Called once before all tests
- **`setUp()`**: Called before each test method
- **`tearDown()`**: Called after each test method
- **`tearDownClass()`**: Called once after all tests

> [!INFO]
> Remember that Django's `TestCase` (`SimpleTestCase`) inherits from `unittest.TestCase` so these methods are present in the framework test suite.

### `pytest` Integration
For `pytest` users, fixtures provide a more flexible approach[^12]:

```python
@pytest.fixture(scope="class")
def app_factory():
    return TestObjectFactory("test_app")

@pytest.fixture
def test_users(app_factory):
    return app_factory.create_users()
```

## Performance Considerations

### Memory vs. Database Objects
Choose between memory and database objects based on performance needs[^6]:
- **Memory objects**: Faster, suitable for unit tests
- **Database objects**: Slower, necessary for integration tests

### Caching Strategies
Implement caching for expensive operations[^13]:

```python
class TestObjectFactory:
    _cache = {}
    
    @classmethod
    def get_cached_user(cls, user_type: str):
        if user_type not in cls._cache:
            cls._cache[user_type] = cls._create_user(user_type)
        return cls._cache[user_type]
```

## Common Pitfalls and Solutions

### 1. Shared State Issues
**Problem**: Multiple tests modifying the same class-level attributes.
**Solution**: Use instance-level storage or implement proper cleanup mechanisms.

### 2. Factory-Model Synchronization
**Problem**: Factories becoming outdated when models change[^5].
**Solutions**:
- Implement automated checks for factory-model consistency
- Use type hints to catch mismatches early
- Regular factory maintenance as part of the development (refactor) process

### 3. Over-Engineering
**Problem**: Creating overly complex factory hierarchies.
**Solution**: Start simple and add complexity only when needed. Follow the [YAGNI](../../Docs/yagni.md) principle and don't overengineer at the begening.

## Testing the Factory Pattern

### Unit Testing Factory Methods
Test factory methods themselves to ensure they create correct objects, this will also help when refactoring the Factory, at a possible model update.

```python
def test_factory_creates_correct_user_type(self):
    factory = TestObjectFactory("test_app")
    user = factory.create_user("admin")
    self.assertEqual(user.role, "admin")
    self.assertEqual(user.app_name, "test_app")
```

### Integration Testing
Test the factory within the broader test framework:

```python
class TestWithFactory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = TestObjectFactory("integration_test")
        
    def test_factory_integration(self):
        user = self.factory.create_user("default")
        # Test user behavior...
```


---
The interaction between class methods and instance methods in Python testing reveals deeper *architectural considerations* about object creation and state management. The two solutions presented each have their merits:
- **Parameter-based approach** offers flexibility and explicit dependencies
- **Class-level storage** provides convenience and maintains encapsulation

The choice **depends on your specific use case**, team preferences, and the broader architecture of your testing framework. By understanding these patterns and their trade-offs, you can build more **maintainable** and **effective** test suites that scale with your application's complexity (and not the opposite).

Remember that the *factory pattern* is not just about object creation—it's about **creating a sustainable, maintainable approach to test data management that supports your long-term development goals**. Whether you choose class methods, instance methods, or a hybrid approach, the key is consistency and clarity in your implementation.

# References
[^1]: https://www.designgurus.io/answers/detail/what-is-the-difference-between-class-and-instance-methods
[^2]: https://pynative.com/python-class-method-vs-static-method-vs-instance-method/
[^3]: https://refactoring.guru/design-patterns/factory-method/python/example
[^4]: https://realpython.com/factory-method-python/
[^5]: https://www.skovy.dev/blog/techniques-for-effectively-using-object-factories-for-testing
[^6]: https://github.com/camilamaia/factory-boy-best-practices
[^7]: https://dagster.io/blog/python-factory-patterns
[^8]: https://stackoverflow.com/questions/23667610/what-is-the-difference-between-setup-and-setupclass-in-python-unittest
[^9]: https://www.freecodecamp.org/news/how-to-write-unit-tests-for-instance-methods-in-python/
[^10]: https://realpython.com/instance-class-and-static-methods-demystified/
[^11]: https://andrewfavia.dev/posts/enums-and-factory-pattern-python/
[^12]: https://stackoverflow.com/questions/8607767/how-to-run-initialization-code-before-tests-when-using-pythons-unittest-module
[^13]: https://insightfultscript.com/collections/programming/python/python-class-method-decorator/
[^14]: https://dev.to/alfredo-pasquel/python-decorators-simplifying-code-with-examples-34ne
[^15]: https://www.datacamp.com/tutorial/decorators-python
[^16]: https://www.linkedin.com/pulse/static-method-vs-class-instance-python-3-ryan-parsa-kvgdc
[^17]: https://www.geeksforgeeks.org/python/class-method-vs-static-method-vs-instance-method-in-python/
[^18]: https://stackoverflow.com/questions/10294014/python-decorator-best-practice-using-a-class-vs-a-function
[^19]: https://dev.to/khushboo/factory-design-pattern-in-python-3p74
[^20]: https://www.reddit.com/r/learnpython/comments/1e7n84t/benefits_of_classmethods_using_a_decorator/
[^21]: https://stackabuse.com/the-factory-method-design-pattern-in-python/
[^22]: https://stackoverflow.com/questions/17134653/difference-between-class-and-instance-methods
[^23]: https://www.stratascratch.com/blog/mastering-python-class-methods-a-practical-guide/
[^24]: https://www.geeksforgeeks.org/python/factory-method-python-design-patterns/
[^25]: https://www.reddit.com/r/learnpython/comments/17oblv2/class_method_vs_instance_method/
[^26]: https://betterprogramming.pub/how-to-use-the-magical-staticmethod-classmethod-and-property-decorators-in-python-e42dd74e51e7
[^27]: https://refactoring.guru/design-patterns/python
[^28]: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/UnitTesting.html
[^29]: https://stackoverflow.com/questions/32643907/how-to-test-an-abstract-factory
[^30]: https://stackoverflow.com/questions/14768135/how-to-fail-a-python-unittest-in-setupclass/14768333
[^31]: https://www.coursera.org/articles/design-patterns-in-python
[^32]: https://gist.github.com/twolfson/13f5f5784f67fd49b245
[^33]: https://python-patterns.guide
[^34]: https://dzone.com/articles/python-unit-testing-one-time-initialization
[^35]: https://kobiton.com/blog/test-automation-design-patterns-you-should-know/
[^36]: https://refactoring.guru/design-patterns/abstract-factory/python/example
[^37]: https://docs.python.org/3/library/unittest.html
[^38]: https://www.reddit.com/r/learnpython/comments/1c2n6lf/best_resource_to_learn_about_design_patterns_in/
[^39]: https://www.youtube.com/watch?v=jVlZ59E_wvg
[^40]: https://www.dataquest.io/blog/unit-tests-python/
[^41]: https://realpython.com/python-class-constructor/
[^42]: https://www.frugaltesting.com/blog/page-object-model-and-page-factory-in-selenium-with-python
[^43]: https://www.reddit.com/r/learnpython/comments/16j3jy5/how_should_i_be_testing_the_init_of_my_class/
[^44]: https://blog.thea.codes/my-python-testing-style-guide/
[^45]: https://www.youtube.com/watch?v=ST0wu-YvYHU
[^46]: https://softwareengineering.stackexchange.com/questions/166699/python-factory-function-best-practices
[^47]: https://docs.python.org/3/tutorial/classes.html
[^48]: https://www.repeato.app/how-to-stop-all-tests-from-inside-a-test-or-setup-using-unittest-in-python/
[^49]: https://stackoverflow.com/questions/14992474/factory-method-for-objects-best-practice
[^50]: https://realpython.com/python-testing/

