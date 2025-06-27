---
title: Advanced Python Features for Better Code
tags: studies, programming, python
use: Coding
languages: Python
dependences: NULL
---
- [i] #to_review : Conectar com outros artigos de python e de design, adicionar ToC e tags

# Advanced Python Features for Better Code

> [![Py-Core Python Programming](https://miro.medium.com/v2/resize:fill:88:88/1*rLxk1HNyO_Pq_EFVFAzNbw.png)](https://medium.com/@ccpythonprogramming "Python programmer focused on data transfer between systems. Major strength: Python interaction with legacy programming/management interfaces (console windows).")
> [Py-Core Python Programming](https://medium.com/@ccpythonprogramming "Python programmer focused on data transfer between systems. Major strength: Python interaction with legacy programming/management interfaces (console windows).") [Follow](https://medium.com/@ccpythonprogramming "Python programmer focused on data transfer between systems. Major strength: Python interaction with legacy programming/management interfaces (console windows).")
> androidstudio · February 13, 2025 (Updated: February 13, 2025)

Python has many features that make development easier. Some are well known, others not so well known. In this article, I'll touch base on a few advanced tools that help coders write cleaner, more efficient code.

The features include **decorators**, **context managers**, **metaclasses**, **descriptors**, and **slot optimization**. Each serves a different purpose but improves code structure and performance.

### Using Decorators to Modify Function Behavior

Decorators wrap functions, adding functionality without changing the original code. A basic decorator takes a function as input, does something before or after execution, and returns a modified function.

```python
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b
add(3, 5)
```

The `@log_function` decorator adds logging without modifying the `add` function. When `add(3, 5)` runs, it prints the function call and result.

Decorators help with logging, caching, and authentication. They keep functions simple while handling extra logic separately.

### Managing Resources with Context Managers

Certain resources require proper handling. Files, network connections, and database connections need cleanup to prevent memory leaks or unexpected behavior.

Python's context managers simplify resource management. They ensure cleanup happens, even if an error occurs. The `with` statement handles this process.

```python
with open("example.txt", "w") as file:
	file.write("Hello, world!")
```

Once the block ends, Python automatically closes the file. No need to call `file.close()`. This reduces errors and keeps code cleaner.

Custom context managers can be created using classes.

```python
class ManagedResource:
	def __enter__(self):
		print("Resource acquired")
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		print("Resource released")

with ManagedResource():
	print("Using resource")
```

When the block starts, `__enter__` runs. When it ends, `__exit__` ensures cleanup happens.

The `contextlib` module provides an easier way to define context managers.

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
	print("Resource acquired")
	yield
	print("Resource released")

with managed_resource():
	print("Using resource")
```

Using `@contextmanager` reduces boilerplate code. Both approaches ensure resources get released, improving program stability.

### Understanding Metaclasses for Custom Class Behavior

Metaclasses define how classes behave. They control class creation before an object exists. Python allows modifying classes dynamically using metaclasses.

A basic metaclass looks like this:

```python
class Meta(type):
	def __new__(cls, name, bases, class_dict):
		print(f"Creating class {name}")
		return super().__new__(cls, name, bases, class_dict)

class MyClass(metaclass=Meta):
pass
```

When `MyClass` is defined, `Meta.__new__` runs before the class gets created. This prints `"Creating class MyClass"`.

Metaclasses modify attributes, enforce naming conventions, or add methods automatically.

For example, forcing class attributes to be uppercase:

```python
class UpperCaseMeta(type):
	def __new__(cls, name, bases, class_dict):
		uppercase_attrs = {key.upper(): value for key, value in class_dict.items()}
		return super().__new__(cls, name, bases, uppercase_attrs)
		
class CustomClass(metaclass=UpperCaseMeta):
	var = "hello"

print(CustomClass.VAR) # Prints "hello"
```

This ensures all attributes in `CustomClass` are uppercase. If `var` was accessed as `CustomClass.var`, it would fail.

Metaclasses provide deep control over class behavior. They are useful for frameworks that create many dynamic classes.

### Combining for Cleaner Code

Each feature improves code structure in different ways.

-   Decorators allow modifying function behavior without rewriting existing code.
-   Context managers ensure resources get cleaned up, making programs more reliable.
-   Metaclasses customize how classes work, enabling powerful abstractions.

Together, they make Python a flexible language. Using them effectively leads to better-designed applications.

### Descriptors Control Attribute Access

Descriptors manage how attributes in a class are accessed, modified, and deleted. They allow fine-grained control over object attributes.

A descriptor defines at least one of these methods:

-   `__get__` for retrieving values
-   `__set__` for assigning values
-   `__delete__` for removing values

```python
class Descriptor:
	def __get__(self, instance, owner):
		print("Getting value")
		return instance._value
	def __set__(self, instance, value):
		print("Setting value")
		instance._value = value

class MyClass:
	attr = Descriptor()
	def __init__(self, value):
		self._value = value

obj = MyClass(10)
print(obj.attr) # Calls __get__
obj.attr = 20 # Calls __set__
```

Descriptors are used in frameworks like Django for model fields.

### Slot Optimization Reduces Memory Usage

Python stores instance attributes in a dictionary by default. This makes attribute lookup flexible but increases memory use. The `__slots__` attribute limits attributes to a predefined set, reducing memory overhead.

```python
class Optimized:
	__slots__ = ['x', 'y']
	def __init__(self, x, y):
		self.x = x
		self.y = y

obj = Optimized(10, 20)
# This would raise an error because 'z' is not in __slots__
# obj.z = 30
```

Using `__slots__` avoids storing attributes in a dictionary, improving memory efficiency.
