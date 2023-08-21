---
title: Recursion
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents 🔖</summary>

- [Intro](#intro)
  - [What Is Recursion?](#what-is-recursion)
  - [Why Use Recursion?](#why-use-recursion)
    - [Properties of Recursion](#properties-of-recursion)
  - [Implementing](#implementing)
  - [Recursion in Python](#recursion-in-python)
- [References](#references)

</details>

---

# Intro

The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a recursive function. Using a recursive algorithm, certain problems can be solved quite easily.

-   What it means for a function to call itself **recursively**
-   How the **design** of Python functions supports recursion
-   What **factors** to consider when choosing whether or not to solve a problem recursively
-   How to **implement** a recursive function in Python

## What Is Recursion?

The word **recursion** comes from the Latin word _recurrere_, meaning to run or hasten back, return, revert, or recur. Here are some online definitions of recursion:

-   [**Dictionary.com**:](https://www.dictionary.com/browse/recursion) The act or process of returning or running back
-   [**Wiktionary**:](https://en.wiktionary.org/wiki/recursion) The act of defining an object (usually a function) in terms of that object itself
-   [**The Free Dictionary**:](https://www.thefreedictionary.com/recursion) A method of defining a sequence of objects, such as an expression, function, or set, where some number of initial objects are given and each successive object is defined in terms of the preceding objects

A **recursive** definition is one in which the defined term appears in the definition itself. Self-referential situations often crop up in real life, even if they aren’t immediately recognizable as such. For example, suppose you wanted to describe the set of people that make up your ancestors. You could describe them this way:

[![Recursive definition of ancestors](https://files.realpython.com/media/jsturtz-ancestors.9f0adeb014ef.png)](https://files.realpython.com/media/jsturtz-ancestors.9f0adeb014ef.png)

Notice how the concept that is being defined, **ancestors**, shows up in its own definition. This is a recursive definition.

## Why Use Recursion?

Most programming problems are solvable without recursion. So, strictly speaking, recursion usually isn’t necessary.

However, some situations particularly lend themselves to a **self-referential** definition—for example, the definition of ancestors shown above. If you were devising an algorithm to handle such a case programmatically, a recursive solution would likely be cleaner and more concise.

Traversal of [tree-like data structures](ds_tree.md) [#](https://en.wikipedia.org/wiki/Tree_(data_structure)) is another good example. Because these are nested structures, they readily fit a recursive definition. A non-recursive algorithm to walk through a nested structure is likely to be somewhat clunky, while a recursive solution will be relatively elegant, but certainly easier to understand.

On the other hand, recursion isn’t for every situation. Here are some other factors to consider:

-  Recursive implementations often consume more memory than non-recursive ones.
-  In some cases, using recursion may result in slower execution time.

### Properties of Recursion

-   Performing the same operations multiple times with different inputs.
-   In every step, we try smaller inputs to make the problem smaller.
-   Base condition is needed to stop the recursion otherwise infinite loop will occur.

## Implementing

The algorithmic steps for implementing recursion in a function are as follows:

1. Define a base case: **Identify the simplest case for which the solution is known or trivial. This is the stopping condition for the recursion**, as it prevents the function from infinitely calling itself.

2. Define a recursive case: Define the problem in terms of smaller subproblems. **Break the problem down into smaller versions of itself, and call the function** recursively to solve each subproblem.

3. Ensure the recursion terminates: Make sure that the recursive function eventually reaches the base case, and does not enter an infinite loop.

4. Combine the solutions: Combine the solutions of the subproblems to solve the original problem.


## Recursion in Python

When you call a function in Python, the interpreter creates a new [local namespace](https://realpython.com/python-namespaces-scope/) so that names defined within that function don’t [collide](https://en.wikipedia.org/wiki/Name_collision) with identical names defined elsewhere. One function can call another, and even if they both define objects with the same name, it all works out fine because those objects exist in separate **namespaces**.

The same holds true if multiple instances of the same function are running concurrently. For example, consider the following definition:

```python
def function():
    x = 10
    function()
```

When `function()` executes the first time, Python creates a namespace and assigns `x` the value `10` in that namespace. Then `function()` calls itself recursively. The second time `function()` runs, the interpreter creates a second namespace and assigns `10` to `x` there as well. These two instances of the name `x` are distinct from each another and can coexist without clashing because they are in separate namespaces.

Unfortunately, running `function()` as it stands produces a result that is less than inspiring, as the following [traceback](https://realpython.com/python-traceback/) shows:

```python
>>> function()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in function
  File "<stdin>", line 3, in function
  File "<stdin>", line 3, in function
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
```

As written, `function()` would in theory go on forever, calling itself over and over without any of the calls ever returning. In practice, of course, nothing is truly forever. Your computer only has so much memory, and it would run out eventually.

Python doesn’t allow that to happen. The interpreter limits the maximum number of times a function can call itself recursively, and when it reaches that limit, it raises a `RecursionError` [exception](https://realpython.com/python-exceptions/), as you see above.

**Technical note:** You can find out what Python’s recursion limit is with a function from the `sys` module called `getrecursionlimit()`:

```python
>>> from sys import getrecursionlimit
>>> getrecursionlimit()
### 1000
```

You can change it, too, with `setrecursionlimit()`:

```python
>>> from sys import setrecursionlimit
>>> setrecursionlimit(2000)
>>> getrecursionlimit()
### 2000
```

You can set it to be pretty large, but you can’t make it infinite.

There isn’t much use for a function to indiscriminately call itself recursively without end. It’s reminiscent of the instructions that you sometimes find on shampoo bottles: “Lather, rinse, repeat.” If you were to follow these instructions literally, you’d shampoo your hair forever!

This logical flaw has evidently occurred to some shampoo manufacturers, because some shampoo bottles instead say “Lather, rinse, repeat _as necessary_.” That provides a termination condition to the instructions. Presumably, you’ll eventually feel your hair is sufficiently clean to consider additional repetitions unnecessary. Shampooing can then stop.

Similarly, a function that calls itself recursively must have a plan to eventually stop. Recursive functions typically follow this pattern:

-   There are one or more base cases that are directly solvable without the need for further recursion.
-   Each recursive call moves the solution progressively closer to a base case.


---
# References

- https://www.geeksforgeeks.org/introduction-to-recursion-data-structure-and-algorithm-tutorials/
- https://realpython.com/python-recursion/