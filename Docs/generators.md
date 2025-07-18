---
title: Generators
tags:
  - studies
  - programming
use: Documentation, Coding
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [Generators](#generators)
    - [What Differs a Generator from an Iterator?](#what-differs-a-generator-from-an-iterator)
    - [Generators Across Programming Languages](#generators-across-programming-languages)
    - [Best Practices for Using Generators](#best-practices-for-using-generators)
  - [External References and Further Reading](#external-references-and-further-reading)

</details>

---

# Generators
Generators are a powerful programming construct that enable efficient, memory-friendly iteration by yielding values one at a time, rather than computing and storing entire sequences in memory. They are particularly *useful for handling large datasets, implementing lazy evaluation, and simplifying asynchronous programming*.

These routines that can be paused and resumed, allowing them to produce a sequence of values over time. In languages like Python, a generator function uses the `yield` keyword to return values one at a time, suspending its state between each call. This contrasts with regular functions that return a single value and terminate.

**Python Example:**
```python
def count_up_to(n: int) -> Generator[int, None, None]:
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)
```
> This will print numbers from 1 to 5, yielding them one at a time.

### What Differs a Generator from an Iterator?
While both generators and iterators are used to iterate over a sequence of values, they differ in how they are implemented and used:

- **Iterator**:
    - An object in Python that implements both `__iter__()` and `__next__()` methods.
    - You need to explicitly define a class and manage iteration state manually.
- **Generator**:
    - A special type of iterator that is automatically created by a function using `yield`.
    - Automatically implements the iterator protocol.
    - More concise and easier to write.

**Iterator Example:**
```python
class CountUpTo:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        current = self.current
        self.current += 1
        return current

for num in CountUpTo(5):
    print(num)
```

**Generator Equivalent:**
```python
def count_up_to(n: int) -> Generator[int, None, None]:
    for i in range(1, n+1):
        yield i

for num in count_up_to(5):
    print(num)
```

Generators are a convenient way to write iterators without the boilerplate code.

---

### Generators Across Programming Languages

**Python**: Introduced generators in version 2.2. Widely used for large or infinite sequences. **Generators in Python can and should have [type annotations](../Languages/Python/typing-annotations-python.md), especially in modern codebases that use static type checkers like `mypy` or editors like VS Code and PyCharm that rely on them.

**JavaScript**: ECMAScript 6 (ES6) introduced generator functions using the `function*` syntax.
```js
function* countUpTo(n) {
    for (let i = 1; i <= n; i++) {
        yield i;
    }
}

for (let value of countUpTo(5)) {
    console.log(value);
}
```

**C#**: Supports generators through the `yield return` statement.
```cpp
IEnumerable<int> CountUpTo(int n) {
    for (int i = 1; i <= n; i++) {
        yield return i;
    }
}
```

**PHP**: Since version 5.5, PHP introduced generators using the `yield` keyword.
```php
function countUpTo($n) {
    for ($i = 1; $i <= $n; $i++) {
        yield $i;
    }
}

foreach (countUpTo(5) as $value) {
    echo $value . "\n";
}
```

**Ruby**: Uses the `Enumerator` class.
```ruby
enum = Enumerator.new do |yielder|
  1.upto(5) { |i| yielder << i }
end

enum.each { |val| puts val }
```

---

### Best Practices for Using Generators

1. **Use Generators for Large or Infinite Sequences**: Ideal for when data sets are too large to fit into memory.
2. **Prefer Generator Expressions for Simple Transformations**: In Python:
```
squares = (x * x for x in range(10))
```

3. **Be Cautious of Multiple Iterations**: Convert to a list if needed multiple times:
```
gen = (x for x in range(3))
list(gen)  # [0, 1, 2]
list(gen)  # []
```

4. **Understand One-Time Nature**: Generators are consumed once unless explicitly re-instantiated.

---

Generators play a significant role in modern software development by:

- **Enhancing Performance**: Yielding one item at a time minimizes memory usage.
- **Simplifying Code**: Cleaner syntax and logic abstraction.

**Async JavaScript Generator Example:**

```js
async function* asyncGenerator() {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts');
  const data = await response.json();
  for (let post of data) {
    yield post;
  }
}
```

By leveraging generators appropriately, developers can write more efficient, readable, and maintainable code, especially when dealing with large or complex data processing tasks.

---

## External References and Further Reading

- Codecademy: Python Generators
- Wikipedia: Generator (computer programming)
- Programiz: Python Generators
- Labex.io: Generator Best Practices
- Datanovia: Common Pitfalls
