---
title: Python Functions
tags:
  - studies
  - programming
use: Documentation, Coding
languages: Python
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [Elements of a function](#elements-of-a-function)
	- [Argument x Parameter](#argument-x-parameter)
	- [Return](#return)
	- [Yield](#yield)

</details>

---

## Elements of a function
### Argument x Parameter
> "*A parameter is the variable listed inside the parentheses in the function definition. An argument is the value that is sent to the function when it is called.*" [_font_](https://stackoverflow.com/questions/156767/whats-the-difference-between-an-argument-and-a-parameter#:~:text=A%20parameter%20is%20the%20variable,function%20when%20it%20is%20called.)

![arg vs param](https://i.stack.imgur.com/9lg1H.png)

These elements are used when you're making a [dependency injection](../../Docs/to_review/dependency-injection.md). It's a really useful software design pattern, often used to reduce [coupling](../../Docs/to_review/coupling.md), improve test-ability, maintainability and flexibility.
### Return
The use of a function can be only for processing algorithms or just to print an information:
```python
>>> def my_function():
...		print("Hello friend, from a function")

>>> my_function()
```

Or to `return` a value, like a math operation:
```python
>>> def sum(a, b)
...		return (a + b)

>>> print(sum(3, 4))
```

So in other words, the `return` value of the function is what it will deliver to the `Caller`. This optionally can be explicit declared with [typing annotations](typing-annotations-python.md) at the function signature:

```python
def log_message(msg: str) -> None: ...

def add(a: int, b: int) -> int: ...

def calculate_pi() -> float: ...

def is_even(n: int) -> bool: ...

def greet(name: str) -> str: ...

def get_primes_under(n: int) -> list[int]: ...

def user_info() -> dict[str, int | str]: ...

def get_min_max(nums: list[int]) -> tuple[int, int]: ...

def unique_tags(items: list[str]) -> set[str]: ...

class Result:
    def __init__(self, status: bool, data: list[int]) -> None: ...

def compute() -> Result: ...

def multiplier(factor: int) -> callable: ...

def count_up_to(n: int) -> Iterator[int]: ...

def find_user(id: int) -> Optional[dict[str, str]]: ...

def square(n: int) -> int: ...

def get_config() -> dict[str, str]: ...
```

In some cases there'll be the need to return part of the data (sometimes called *chunks*) before the ending of the function.

### Yield
Is a keyword used in **[generators](../../Docs/generators.md)**. It allows a function to temporarily suspend its execution and **return a value to the caller**, but unlike `return`, it **preserves the function’s state**, allowing it to resume where it left off.

```python
def count_up_to(n: int) -> Generator[int, None, None]:
	count = 1
	while count <= n:
		yield count
		count += 1
```
This function returns a generator that **produces values lazily**, one at a time, only when requested.

- Much like human focus, `yield` mimics **selective attention**—deferring work until necessary. It’s **event-driven** and resource-efficient.
- In frameworks like **`asyncio`** or **Node.js**, `yield` relates to **non-blocking I/O**, improving **scalability** by avoiding thread starvation.
- In Django, `yield` can be used in **middleware** or **streamed HTTP responses** (e.g., file downloads).
- In **Flask**, generators allow **incremental data rendering** in templates or streaming APIs.


---
Visit the following resources to learn more:
-	[Python Functions - W3Schools](https://www.w3schools.com/python/python_functions.asp)
-	[Python Functions – How to Define and Call a Function](https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/)
-	[Python Functions](https://www.geeksforgeeks.org/python-functions/)
-	[Built-in Functions in Python](https://docs.python.org/3/library/functions.html)