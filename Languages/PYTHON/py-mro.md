---
title: Method Resolution Order (MRO) in Python
tags:
  - studies
  - programming
  - oop
  - object-oriented
  - programming
  - inheritance
  - multiple
  - inheritance
  - mro
  - c3
  - design
use: Documentation
languages: Python
dependences: C3
---

<details> <summary>Table of Contents 🔖</summary>

- [Method Resolution Order (MRO) in Python](#method-resolution-order-mro-in-python)
  - [What Is MRO?](#what-is-mro)
  - [C3 Linearization](#c3-linearization)
  - [Related Concepts](#related-concepts)
  - [Insights](#insights)
  - [References](#references)

</details>

---

# Method Resolution Order (MRO) in Python
In object-oriented programming, especially in languages like Python that support **multiple inheritance**, the *[Method Resolution Order (MRO)](../../Docs/mro.md)* determines the sequence in which base classes are looked up when searching for a method. This mechanism is *crucial to ensure predictable and consistent behavior* when multiple classes define the same method.

## What Is MRO?
Is **==the order in which Python looks for a method or attribute in a hierarchy of classes==**. This becomes particularly important when a class inherits from multiple classes. Python uses a specific algorithm to compute this order: **C3 linearization**.

Consider this simple multiple inheritance scenario:

```python
class A:
    def speak(self):
        print("A")

class B(A):
    def speak(self):
        print("B")

class C(A):
    def speak(self):
        print("C")

class D(B, C):
    pass

d = D()
d.speak()
```

You might expect either `B` or `C` to be printed, but which one? Python uses MRO to decide, and in this case, the order is `D → B → C → A`. So **the output is `B`**. *If any of the `speak` methods calls `super()` than the behavior will be different*, as explained below.

## C3 Linearization
The **C3 Linearization** algorithm ensures:
1. A class always appears before its parents.
2. The order of base classes is preserved.
3. No duplicate classes are included in the final order.

This ensures a consistent and predictable lookup chain, avoiding ambiguity and conflicts in complex inheritance trees.

You can inspect the MRO of a class using the [dunder method](py-dunder_methods.md):

```python
print(D.__mro__)
```

Or with the built-in function:

```python
print(D.mro())
```

## Related Concepts
- **`super()` Function**: Python’s `super()` uses the MRO to determine the next class’s method to call. **It doesn't always mean the parent class — ==it means "next in line" according to MRO==**.
- **Cooperative Multiple Inheritance**: Using `super()` correctly in all classes helps to chain method calls across all classes in the MRO. This enables multiple classes to contribute to the behavior of a method without explicitly calling their parents.
    ```python
    class A:
        def speak(self):
            print("A")
    
    class B(A):
        def speak(self):
            print("B")
            super().speak()
    
    class C(A):
        def speak(self):
            print("C")
            super().speak()
    
    class D(B, C):
        def speak(self):
            print("D")
            super().speak()
    
    D().speak()
    
    # Output:
    # D
    # B
    # C
    # A
    ```

## Insights
- MRO prevents the *diamond problem* — a classic issue in multiple inheritance where the same base class can be called multiple times.
- Understanding MRO helps debug inheritance-related issues, especially when behavior isn't what you expect.
- **Using `super()`  — except at the root class — universally (even when it seems unnecessary) is a best practice when designing class hierarchies for reuse and extensibility**.

## References
1. [Python 3.12 documentation - DAta Model Standad type hierarchy](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)
2. [Raymond Hettinger’s talk: “Super considered super!”](https://www.youtube.com/watch?v=EiOglTERPEo)
3. [Python C3 Linearization Explanation](https://www.python.org/download/releases/2.3/mro/)
4. [Real Python – Python’s super()](https://realpython.com/python-super/)
5. [PEP 333 – MRO changes in Python 2.3](https://peps.python.org/pep-0333/)
6. [Python MRO Visualizer (external tool)](https://mrovisualizer.com/)
