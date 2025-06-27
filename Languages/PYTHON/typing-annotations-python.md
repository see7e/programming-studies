---
title: Typing Annotations
tags:
  - studies
  - programming
  - typing_annotations
  - runtime
  - validations
  - linting
use: Documentation, Coding, Conventions
languages: Python
dependences: typing, mypy, pyright, pylint
---

<details> <summary>Table of Contents 🔖</summary>

- [Understanding Typing Annotations in Python](#understanding-typing-annotations-in-python)
  - [What Are Typing Annotations?](#what-are-typing-annotations)
    - [Basic Syntax](#basic-syntax)
  - [Why Use Type Annotations?](#why-use-type-annotations)
  - [Typing Basics: Parameters and Returns](#typing-basics-parameters-and-returns)
  - [Collections and the `typing` Module](#collections-and-the-typing-module)
  - [Optional and Union Types](#optional-and-union-types)
  - [Callable, Any, and Literal](#callable-any-and-literal)
  - [Type Aliases and `NewType`](#type-aliases-and-newtype)
    - [Type Aliases](#type-aliases)
    - [`NewType`](#newtype)
  - [Advanced Elements](#advanced-elements)
    - [`TypedDict`](#typeddict)
      - [Is `TypedDict` Heavier Than `dict`?](#is-typeddict-heavier-than-dict)
      - [When to Use `TypedDict`](#when-to-use-typeddict)
      - [When Not to Use `TypedDict`](#when-not-to-use-typeddict)
    - [Protocol (Structural Subtyping)](#protocol-structural-subtyping)
    - [Generics](#generics)
    - [Generators](#generators)
  - [✅ Typing Generators in Python](#-typing-generators-in-python)
    - [Syntax (using `typing.Generator`):](#syntax-using-typinggenerator)
    - [Breakdown of `Generator[yield_type, send_type, return_type]`:](#breakdown-of-generatoryield_type-send_type-return_type)
  - [📌 Examples](#-examples)
    - [1. Basic Generator (Only Yields)](#1-basic-generator-only-yields)
    - [2. Generator That Receives Sent Values](#2-generator-that-receives-sent-values)
    - [3. Using `Iterator` or `Iterable` Instead](#3-using-iterator-or-iterable-instead)
  - [Best Practices](#best-practices)
  - [Correlations with Other Topics](#correlations-with-other-topics)

</details>

---

# Understanding Typing Annotations in Python
Python is a **dynamically typed language**, which means you don't have to declare the type of variables. However, with the growth of large codebases, it's often hard to reason about types, leading to runtime bugs and poor code maintainability.

**Typing annotations** were introduced to bring **clarity, safety, and better tooling** to Python without sacrificing its dynamic nature.

It's also worth mentioning about Linters and type-checkers, that automate this process and helps ensure the code conventions standards.

## What Are Typing Annotations?
Typing annotations allow you to **explicitly specify the types** of variables, function arguments, and return values. They are **hints**—they don’t affect runtime behavior but can be used by tools like `mypy`, `pyright`, and editors like VS Code for **type checking, autocompletion, and refactoring**.

> from [Does Python type hint (annotations) cause some run-time effects? - Stack Overflow](https://stackoverflow.com/questions/41692473/does-python-type-hint-annotations-cause-some-run-time-effects)
> Type hints and annotations do provide attributes (see [`typing.get_type_hints`](https://docs.python.org/3/library/typing.html)) that can be passed by 3rd party tools but **native CPython will not type check these at runtime**, so this should not affect the code performance significantly in the same way that comments don't. I ran some tests with `timeit` and removing type hints had a negligible effect (not distinguishable from the background _noise_) on the run time, so any concerns about performance would certainly be a severe case of premature optimization.
> From [PEP 484](https://www.python.org/dev/peps/pep-0484/#non-goals):
> *While the proposed typing module will contain some building blocks for runtime type checking -- in particular the get_type_hints() function -- third party packages would have to be developed to implement specific runtime type checking functionality, for example using decorators or metaclasses. Using type hints for performance optimizations is left as an exercise for the reader.*

### Basic Syntax

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```
- `name: str` hints that `name` should be a string.
- `-> str` hints that the function returns a string.

## Why Use Type Annotations?

| Benefit                 | Description                             |
| ----------------------- | --------------------------------------- |
| **Clarity**             | Code is self-documenting                |
| **Early Bug Detection** | Tools can catch errors before runtime   |
| **Editor Support**      | Better IntelliSense/autocomplete        |
| **Refactoring Safety**  | Refactor tools use type info            |
| **Collaboration**       | Others understand your API expectations |

## Typing Basics: Parameters and Returns

```python
def add(a: int, b: int) -> int:
    return a + b
```

You can annotate:
- **Function parameters**
- **Return types**
- **Local variables (Python 3.6+)**

```python
message: str = "Hello"
```

## Collections and the `typing` Module
Use the `typing` module to specify **generic types** like lists, dictionaries, and tuples.

```python
from typing import List, Dict, Tuple, Set

def process_names(names: List[str]) -> Dict[str, int]:
    return {name: len(name) for name in names}

def split_coords() -> Tuple[float, float]:
    return (12.3, 45.6)
```

In Python 3.9+, you can use built-in generics:

```python
def process_names(names: list[str]) -> dict[str, int]: ...
```

## Optional and Union Types
Use `Optional[T]` or `T | None` to indicate a value can be `None`. *`T` stands for a generic type, refer to Generics topic below.*

```python
from typing import Optional

def find_user(id: int) -> Optional[dict[str, str]]: ...
```

Use `Union` when multiple types are allowed.

```python
from typing import Union

def load_config(src: str | dict[str, str]) -> dict[str, str]: ...
```

## Callable, Any, and Literal
- **`Callable`**: Type hint for functions.

```python
from typing import Callable

def apply_func(x: int, func: Callable[[int], int]) -> int:
    return func(x)
```

- **`Any`**: Use when type is unknown or dynamic.

```python
from typing import Any

def log_event(data: Any) -> None:
    print(data)
```

- **`Literal`** (Python 3.8+): For fixed choices.

```python
from typing import Literal

def get_status(code: int) -> Literal["success", "error", "unknown"]: ...
```

## Type Aliases and `NewType`

### Type Aliases
Simplify repeated complex types.

```python
User = dict[str, str]

def get_user() -> User: ...
```

### `NewType`
Create distinct semantic types (safe for refactors). Acts the same way as `typedef` in C.

```python
from typing import NewType

UserId = NewType('UserId', int)

def get_user(id: UserId) -> dict: ...
```

---
## Advanced Elements

### `TypedDict`
For dictionaries with fixed keys and value types. Acts like a C/Go `struct`.
Was introduced in **PEP 589** to bring **static type safety** to standard dictionaries. In other words:
> It lets you define the _shape_ of a dictionary **at the type level**, **without enforcing it at runtime**.

```python
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str

def greet_user(user: User) -> None:
    print(f"Hello {user['name']} (id={user['id']})")
```
With a regular `dict[str, str | int]`, you have no guarantee which keys exist or what their value types are. With `TypedDict`, tools like **`mypy`** or **`pyright`** can catch:
- Missing keys
- Extra keys
- Wrong value types

#### Is `TypedDict` Heavier Than `dict`?
 **No, not really at runtime.** A `TypedDict` **is still just a regular `dict` at runtime**.

- No overhead at instantiation time:   The statement `User(id=1, name="Alice")` is just syntactic sugar for `{"id": 1, "name": "Alice"}`.
- No memory overhead: `TypedDict` adds **no attributes, methods, or structure** to the instance. It’s **not a class with `__init__`**—it's a **type-checking aid only**.
 - Not enforced at runtime: There's **no validation** or performance penalty unless you manually do runtime checks (e.g. with `pydantic` or `attrs`).

```python
user: User = {"id": 1, "name": "Alice"}  # totally valid
user: User = {"id": 1}  # mypy will catch: missing 'name'
```

#### When to Use `TypedDict`
- You want to **define data contracts** with fixed keys (e.g. from APIs, configs).
- You want **type safety** without introducing full classes (`@dataclass`, etc).
- You're working with **JSON-like structures**, but want to restrict shape.
This is better than just `dict[str, Any]`, especially for teams or large codebases.

#### When Not to Use `TypedDict`
- You need **runtime guarantees or validation**:  use [`pydantic`](https://docs.pydantic.dev/) or `dataclasses`.
- You want **methods, behavior, or inheritance**: use a regular class.
- You care about **runtime type enforcement**: `TypedDict` won’t help.

| Feature       | `dict`       | `TypedDict`      | `dataclass`        |
| ------------- | ------------ | ---------------- | ------------------ |
| Runtime check | ❌ No         | ❌ No             | ✅ Yes              |
| IDE support   | ❌ Weak       | ✅ Strong         | ✅ Strong           |
| Type hints    | ❌ Manual     | ✅ Structured     | ✅ Structured       |
| Mutability    | ✅ Yes        | ✅ Yes            | ✅ Yes (mutable)    |
| Use case      | Dynamic data | Structured dicts | Structured objects |

### Protocol (Structural Subtyping)
Supports Duck Typing in type hints.

```python
from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None: ...

def cleanup(resource: SupportsClose) -> None:
    resource.close()
```

> [!NOTE]
> [Duck typing](https://devopedia.org/duck-typing) is a programming style, often found in dynamically typed languages, where an object's suitability for a specific task is determined by its ability to perform the required actions (methods or attributes) rather than by its formal type or class. The name comes from the "duck test": "If it walks like a duck and it quacks like a duck, then it must be a duck". 
> ### How it works:
> Instead of checking if an object is of a specific type, duck typing focuses on whether the object possesses the necessary methods and attributes to be used in a particular context. If an object has the methods and attributes needed to fulfill a function's requirements, it's considered compatible, regardless of its actual type. 
> #### Example:
> Consider a function designed to process objects that can be "walked" and "quacked". With duck typing, this function wouldn't check if the object is an instance of a "Duck" class. Instead, it would call `walk()` and `quack()` on the object and expect those methods to be defined. If an object has those methods, it's treated as a duck-like object, even if it's actually a different type.
### Generics
For reusable type-safe components.

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
```

### Generators
**Can and should have type annotations**, especially in modern codebases that use static type checkers like `mypy` or editors like VS Code and PyCharm that rely on them.

Python provides a standard way to annotate generator functions using the `Generator` or `Iterator` type from the `typing` module (or `collections.abc` in Python 3.9+).

#### Breakdown of `Generator[yield_type, send_type, return_type]`:
- `yield_type`: The type of values yielded by the generator.
- `send_type`: The type accepted by `generator.send(value)`. Often `None` if not used.
- `return_type`: The return value of the generator (after `StopIteration`). Also often `None`.
#### Examples
1. Basic Generator (Only Yields)
```python
from typing import Generator

def gen_nums() -> Generator[int, None, None]:
    yield 1
    yield 2
```

2. Generator That Receives Sent Values
```python
from typing import Generator

def echo() -> Generator[str, str, None]:
    while True:
        received = yield
        print(f"Received: {received}")
```

3. Using `Iterator` or `Iterable` Instead
If you're only yielding and not sending or returning specific values:
```python
from typing import Iterator, Iterable

def get_lines() -> Iterator[str]:
    yield "line1"
    yield "line2"
```

> [!TIP]
> From Python 3.9+ you can use `collections.abc.Generator`, `Iterator`, etc., without importing from `typing`:
> 
> ```python
> from collections.abc import Generator
> 
> def stream_data() -> Generator[int, None, None]:
>     for i in range(100):
>         yield i
> ```

---
## Best Practices

| Practice                                     | Reason                            |
| -------------------------------------------- | --------------------------------- |
| Use type hints in public APIs                | Helps documentation and consumers |
| Use `Optional` for values that can be `None` | Clear nullability                 |
| Prefer concrete over `Any` where possible    | Ensures type safety               |
| Use `mypy` or `pyright` to validate          | Enforces correctness              |
| Avoid over-annotating local trivial vars     | Keeps code clean                  |

## Correlations with Other Topics
- **`Dataclasses`**: Combine nicely with annotations.

    ```python
    from dataclasses import dataclass
    
    @dataclass
    class Product:
        name: str
        price: float
    ```

- **Static Analysis**: Works with `mypy`, `pyright`, `pylint`.
- **Testing**: Type-safe code makes writing tests easier.
- **Docs Generation**: Tools like `sphinx-autodoc-typehints` use annotations.
- **IDE Support**: Editors give richer autocomplete with types.

Typing in Python is **optional but powerful**. It bridges the gap between dynamic scripting and robust software engineering. Adopt it **gradually**, and you'll find:
- **Cleaner code**
- **Fewer bugs**
- **Better collaboration**
- **More maintainable architecture**
