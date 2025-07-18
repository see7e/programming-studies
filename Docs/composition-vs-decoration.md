---
title: Composition vs Decoration
tags:
  - studies
  - programming
  - design
  - design-patterns
  - patterns
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [Composition vs Decoration](#composition-vs-decoration)
  - [Composition](#composition)
  - [Decoration (Decorator Pattern)](#decoration-decorator-pattern)
  - [Connecting the Ideas](#connecting-the-ideas)
  - [Related Topics](#related-topics)
    - [Dependency Injection](#dependency-injection)
    - [Functional Composition](#functional-composition)
    - [Aspect-Oriented Programming (AOP)](#aspect-oriented-programming-aop)
    - [Adapter vs. Decorator](#adapter-vs-decorator)
  - [Insights and Recommendations](#insights-and-recommendations)
  - [References and Further Reading](#references-and-further-reading)

</details>

---
# Composition vs Decoration
**Composition** and **Decoration** are two powerful paradigms for constructing complex behaviors by **combining simpler building blocks** rather than relying on inheritance or monolithic structures.

## Composition
Means **assembling functionality by combining objects or functions that each have a single, well-defined responsibility**. Instead of subclassing, you inject or attach collaborators.
_Example_: Instead of subclassing `Bird` into `FlyingBird`, you compose a `Bird` with a `FlightBehavior`.
**Benefit**: Promotes **loose coupling** and **reusability**.

## Decoration (Decorator Pattern)
Refers to **dynamically adding responsibilities or capabilities to an object without altering its structure**.
_Example_: Wrapping a data reader with a compression decorator to transparently compress data.
**Benefit**: Allows behavior extension at runtime.

## Connecting the Ideas
These concepts are often interrelated:
- **Decorators rely on composition** under the hood: you compose the original object and the decorator.
- Both approaches follow the **Open/Closed Principle** ([SOLID](solid.md)).
- Composition is usually **static** (fixed during setup), while decoration can be **dynamic** (wrapped on demand).

In other words:
- **Composition**: _Build with parts._
- **Decoration**: _Wrap to enhance._

This distinction is subtle but crucial—composition gives you a clear structure of capabilities, while decoration allows ad hoc enrichment.

## Related Topics

### [Dependency Injection](to_review/dependency-injection.md)
Composition frequently relies on **dependency injection**: providing objects their dependencies from outside. This keeps the system decoupled and testable.

### Functional Composition
In functional programming, **composition** refers to chaining pure functions:

```text
f ∘ g ∘ h
```

Each function transforms input into output, resulting in predictable flows.

### Aspect-Oriented Programming (AOP)
Decoration overlaps with **cross-cutting concerns**:
- Logging
- Caching
- Security  
    These can be implemented as decorators (in OO) or aspects (in AOP frameworks).

### Adapter vs. Decorator
- **Adapter** converts interfaces.
- **Decorator** adds behavior transparently.  
    It’s easy to confuse them, but their purposes differ.

## Insights and Recommendations
- Prefer **[composition over inheritance](inheritance-vs-composition.md)** to avoid rigid class hierarchies.
- Use **decoration** when you need dynamic, combinable behavior.
- Compose behaviors as **orthogonal capabilities**—e.g., Logging, Caching, Validation.
- In functional languages, leverage **pure function composition** for clarity and testability.
- Be mindful of **decorator stacking**, which can make your code look like an onion of wrappers and make debugging more complex.

---

## References and Further Reading
1. _Design Patterns: Elements of Reusable Object-Oriented Software_ – Erich Gamma et al.
2. _Effective Java_ – Joshua Bloch (Chapters on composition)
3. _Functional Programming in Scala_ – Paul Chiusano and Rúnar Bjarnason
4. _Clean Architecture_ – Robert C. Martin
5. _Refactoring: Improving the Design of Existing Code_ – Martin Fowler
6. Wikipedia: [Decorator Pattern](https://en.wikipedia.org/wiki/Decorator_pattern)
7. Wikipedia: [Composition over Inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance)
8. Martin Fowler’s article on [Dependency Injection](https://martinfowler.com/articles/injection.html)
9. _You Don’t Know JS_ – Kyle Simpson (Functional composition in JavaScript)
10. _Programming Rust_ – Jim Blandy and Jason Orendorff (Composition with traits)
