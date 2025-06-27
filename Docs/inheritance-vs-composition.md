---
title: Inheritance vs Composition
tags:
  - studies
  - programming
  - design
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [New Note](#new-note)

</details>

---

- [i] #to_review : Escrever, conectar, toc, tags
# Inheritance vs Composition

## Foundations
Inheritance and composition are complementary mechanisms for re-using behavior in object-oriented design.
- **Inheritance** establishes an **is-a** subtype link: a subclass automatically acquires all public members of its parent.
- **Composition** establishes a **has-a** link: an object delegates work to the collaborating objects it holds.

Both mechanisms pre-date any specific language and appear in the classic “Gang of Four” (GoF) patterns, whose very first guideline reads: _“Favor object composition over class inheritance.”_

In essence:
- Inheritance promotes a **hierarchical**, top-down structure.
- Composition enables **modular**, bottom-up behavior aggregation.

##  Strengths and Liabilities

| Aspect                | Inheritance                                  | Composition                                  |
| --------------------- | -------------------------------------------- | -------------------------------------------- |
| Code reuse style      | Compile-time sharing of implementation       | Run-time assembly of behavior                |
| Coupling              | Tight: subclasses depend on parent internals | Loose: collaborators can be swapped          |
| Substitutability risk | Can violate Liskov Substitution Principle    | Naturally preserved (no subtype relation)    |
| Flexibility           | Rigid hierarchy; limited variants            | Combinatorial; avoids subclass explosion     |
| Evolution cost        | Changes propagate across hierarchy           | Components evolve independently              |
| Discoverability       | Clear taxonomy via class hierarchy           | More indirection through delegation          |
| Runtime behavior      | Static                                       | Dynamic (components can be replaced/swapped) |
| Expressiveness        | Semantic clarity for taxonomies              | Greater behavioral variation                 |

## Typical Misuses
1. **Implementation inheritance**: Extending a class only to reuse code rather than model a true is-a relationship often leads to brittle designs and breaks the Liskov Substitution Principle.
2. **Deep hierarchies**: Modeling every axis of variation as a new subclass level leads to an exponential number of subclasses—a situation known as the “subclass explosion.”

## When to Prefer Each
Use **inheritance** when:
- There is a true is-a relationship.
- All subclasses uphold the behavioral contract of the superclass (per the LSP).
- You want polymorphic substitution (e.g., GUI components with a shared rendering base).

Use **composition** when:
- Behavior varies independently along multiple axes (e.g., payment processors, logging).
- Runtime configurability is important (strategy pattern).
- Domain logic changes often (typical in business and domain-driven applications).

**Pragmatic Rule**: Start with composition by default. Use inheritance _only_ when substitutability is provable, domain-relevant, and semantically clear.

## Design-Pattern Bridges
Design patterns bridge theory and practical implementation. Here are key patterns that leverage composition:
- **Strategy**: Encapsulates algorithms in interchangeable objects. The context class delegates to a strategy object.
- **Decorator**: Dynamically adds behavior to an object by wrapping it with another object—useful for layered functionality.
- **Bridge**: Separates abstraction from implementation, enabling both to vary independently through composition.

These patterns make the _“composition over inheritance”_ principle actionable.

## Beyond Classical OO

### 6.1 Mixins & Traits
Languages like **Scala**, **Rust**, and **Swift** allow code reuse through **traits** or **mixins**. These offer composition-like granularity within an inheritance-based model, often resolving the diamond problem via linearization.

### 6.2 Entity-Component Systems (ECS)
Game engines such as Unity use **ECS**, where entities are just IDs and all behavior is implemented via systems acting on data-only components. This is **extreme composition**, optimized for modularity and performance.

### 6.3 Functional & ADT Paradigms
In purely functional languages, behavior is organized through **algebraic data types** (ADTs), **pattern matching**, and **higher-order functions**. These mechanisms replace class hierarchies entirely, preserving substitutability via the type system.

## SOLID Connections
Inheritance and composition have deep ties to the SOLID principles:

| Principle | Inheritance Impact                                                      | Composition Advantage                                                  |
| --------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **SRP**   | Inheritance can lead to bloated base classes with multiple duties.      | Composition encourages small, cohesive, single-purpose components.     |
| **OCP**   | Extending behavior via subclassing may require altering parent classes. | New composed objects extend behavior without changing existing code.   |
| **LSP**   | Easy to violate if subclass alters expected behavior.                   | Composition sidesteps substitutability issues entirely.                |
| **ISP**   | Inheritance can lock classes into large base interfaces.                | Composition promotes use of small, targeted interfaces.                |
| **DIP**   | Inheritance ties modules to specific class hierarchies.                 | Composition encourages depending on interfaces and injecting behavior. |

## Guidelines for Daily Practice
1. Use inheritance only when a genuine subtype relationship exists.
2. Encapsulate change-prone logic with interfaces and inject via composition.
3. Prefer shallow hierarchies and delegation over override-heavy subclassing.
4. Blend composition with abstraction: define interfaces, compose implementations.
5. Validate subtypes with **contract-based tests** to catch LSP violations early.

---

Inheritance and composition are not rivals but tools—each with strengths, trade-offs, and risks. Modern architecture favors **composition** for its flexibility, testability, and adaptability. Inheritance remains valuable when used judiciously and semantically.

Understanding when and why to use each—guided by design patterns, SOLID principles, and the real-world nature of your domain—leads to software that’s robust, understandable, and built to last.

# References
1. [DigitalOcean – Composition vs Inheritance](https://www.digitalocean.com/community/tutorials/composition-vs-inheritance)
2. [Wikipedia – Composition over Inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance)
3. [LinkedIn – Why Composition Is Favored Over Inheritance](https://www.linkedin.com/pulse/why-composition-favored-over-inheritance-shehan-chanuka)
4. [Python Patterns Guide – Composition Over Inheritance](https://python-patterns.guide/gang-of-four/composition-over-inheritance/)
5. [JustAcademy – Advantages and Disadvantages of Inheritance](https://www.justacademy.co/blog-detail/advantages-and-disadvantages-of-inheritance-in-java)
6. [Adservio – Composition vs Inheritance](https://www.adservio.fr/post/composition-vs-inheritance)
7. [Cekrem Blog – Liskov Substitution](https://cekrem.github.io/posts/liskov-substitution-the-real-meaning-of-inheritance/)
8. [Wikipedia – Liskov Substitution Principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle)
9. [João Júnior – Composition, Inheritance, and LSP](https://joaojunior.org/posts/composition-inheritance-and-liskov-substitution-principle/)
10. [Veerpal Brar – Inheritance vs Composition](https://veerpalbrar.github.io/blog/2021/06/30/Inheritance-vs-Composition)
11. [StackOverflow – Strategy Pattern vs Inheritance](https://stackoverflow.com/questions/25710295/differences-between-strategy-pattern-and-inheritance)
12. [StackOverflow – Composition in the Bridge Pattern](https://stackoverflow.com/questions/70971858/what-does-composition-mean-in-the-composition-vs-inheritance-debate)
13. [Reddit – Scala Traits vs Abstract Classes](https://www.reddit.com/r/scala/comments/ejvqc8/how_exactly_are_traits_different_from_abstract/)
14. [Smithy 2.0 Spec – Mixins](https://smithy.io/2.0/spec/mixins.html)
15. [Unity Docs – ECS Concepts](https://docs.unity3d.com/Packages/com.unity.entities@0.51/manual/ecs_core.html)
16. [SoftwareEngineering.SE – LSP Without Inheritance](https://softwareengineering.stackexchange.com/questions/432838/what-would-be-an-example-of-the-liskov-substitution-principle-if-you-dont-use)
17. [Adesso – The SOLID Design Principles](https://www.adesso.de/en/news/blog/the-solid-design-principles.jsp)
18. [Reddit – When Is Inheritance Better?](https://www.reddit.com/r/softwarearchitecture/comments/8xmp8z/when_is_inheritance_better_than_composition/)
19. [Reddit – AskProgramming on Composition](https://www.reddit.com/r/AskProgramming/comments/lv7m7a/i_still_dont_understand_the_prefer_composition/)
20. [Dev.to – Design Patterns: Composition vs Inheritance](https://dev.to/elayachiabdelmajid/design-pattern-difference-between-composition-and-inheritance-and-decorator-mji)
21. [LinkedIn – Implementing Composition with Design Patterns](https://www.linkedin.com/advice/3/how-can-you-use-design-patterns-implement-composition-21ywf)
22. [Develpreneur – Flexibility in OOP](https://develpreneur.com/flexibility-in-oop-build-in-hooks-for-change/)
23. [Feldman Law Group – Common Inheritance Mistakes](https://www.feldmanlawgroup.com/blog/2024/september/7-common-inheritance-mistakes-to-avoid/)
24. [ThoughtWorks – Composition vs Inheritance](https://www.thoughtworks.com/en-es/insights/blog/composition-vs-inheritance-how-choose)
25. [Oregon State Blog – Problems with Inheritance](https://blogs.oregonstate.edu/posts/2024/01/24/6-common-problems-with-inheritance-and-what-to-do/)
26. [Onewheel Studio – Strategy Pattern and Composition](https://onewheelstudio.com/blog/2020/8/16/strategy-pattern-composition-over-inheritance)
27. [Hacker News – Inheritance vs Composition](https://news.ycombinator.com/item?id=43767011)
28. [Hillel Wayne – When to Prefer Inheritance](https://buttondown.com/hillelwayne/archive/when-to-prefer-inheritance-to-composition/)
