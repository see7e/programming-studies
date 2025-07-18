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

- [Inheritance vs Composition](#inheritance-vs-composition)
  - [Foundations](#foundations)
  - [Strengths and Liabilities](#strengths-and-liabilities)
  - [Typical Misuses](#typical-misuses)
    - [Implementation inheritance](#implementation-inheritance)
    - [Deep hierarchies](#deep-hierarchies)
  - [When to Prefer Each](#when-to-prefer-each)
  - [Design-Pattern Bridges](#design-pattern-bridges)
  - [Beyond Classical OO](#beyond-classical-oo)
    - [6.1 Mixins \& Traits](#61-mixins--traits)
    - [6.2 Entity-Component Systems (ECS)](#62-entity-component-systems-ecs)
    - [6.3 Functional \& ADT Paradigms](#63-functional--adt-paradigms)
  - [SOLID Connections](#solid-connections)
  - [Guidelines for Daily Practice](#guidelines-for-daily-practice)
- [References](#references)

</details>

---

# Inheritance vs Composition

## Foundations
Inheritance and composition are complementary mechanisms for re-using behavior in [OOP](OOP.md).
- **Inheritance** establishes an **is-a** subtype link: a subclass automatically acquires all public members of its parent.
- **Composition** establishes a **has-a** link: an object delegates work to the collaborating objects it holds.

Both mechanisms pre-date any specific language and appear in the classic [“Gang of Four” (GoF) patterns](books/Design-Patterns-Erich-Gamma-Richard-Helm-Ralph-Johnson-John-Vlissides.md), whose very first guideline reads: _“Favor object composition over class inheritance.”_

In essence:
- Inheritance promotes a **hierarchical**, top-down structure.
- Composition enables **modular**, bottom-up behavior aggregation.

##  Strengths and Liabilities

| Aspect                | Inheritance                                  | Composition                                      |
| --------------------- | -------------------------------------------- | ------------------------------------------------ |
| **Code reuse** style  | Compile-time sharing of implementation       | Run-time assembly of behavior                    |
| **Coupling**          | Tight: subclasses depend on parent internals | **Loose**: collaborators can be swapped          |
| Substitutability risk | Can violate Liskov Substitution Principle    | **Naturally preserved** (no subtype relation)    |
| Flexibility           | Rigid hierarchy; limited variants            | Combinatorial; **avoids subclass explosion**     |
| Evolution cost        | **Changes propagate across hierarchy**       | Components evolve independently                  |
| Discoverability       | **Clear taxonomy via class hierarchy**       | More indirection through delegation              |
| Runtime behavior      | Static                                       | Dynamic (**components can be replaced/swapped**) |
| Expressiveness        | *Semantic clarity for taxonomies*            | *Greater behavioral variation*                   |

> [!NOTE]
> **Taxonomy**, mentioned above, refers to the structured classification or categorization of entities—typically within an object-oriented design. When it says "clear taxonomy via class hierarchy," it means that the class hierarchy in inheritance provides a well-defined and organized structure. This structure allows you to categorize different types of objects and their relationships in a clear, hierarchical way.

## Typical Misuses
### Implementation inheritance
Extending a class only to reuse code rather than model a true is-a relationship often leads to brittle designs and breaks the Liskov Substitution Principle.

```python
class Vehicle:
    def start_engine(self):
        print("Engine starting...")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine starting...")

class Airplane(Vehicle):
    def start_engine(self):
        print("Airplane engine starting...")

# Wrong usage: Treating Airplane as a Vehicle
def start_vehicle_engine(vehicle: Vehicle):
    vehicle.start_engine()

start_vehicle_engine(Car())  # Correct behavior
start_vehicle_engine(Airplane())
```

> [!WARNING] 
> **Problem**: The `Vehicle` class was extended for code reuse, but the **`start_engine()` method’s behavior might not be the same for all types of vehicles**. If the `Airplane` subclass had different behavior for engines that isn't compatible with the `Vehicle` class interface, it would violate the Liskov Substitution Principle, which expects derived classes to behave in a way that makes them substitutable for the parent class.
> A possible solution is to compose the `Vehicle` class with an `Engine` interface, allowing different types of engines to be used without breaking the substitutability contract.
> ```python
> class Engine:
>     def start(self):
>         pass
> 
> class CarEngine(Engine):
>     def start(self):
>         print("Car engine starting...")
> 
> class AirplaneEngine(Engine):
>     def start(self):
>         print("Airplane engine starting...")
> 
> class Vehicle:
>     def __init__(self, engine: Engine):
>         self.engine = engine
> 
>     def start_engine(self):
>         self.engine.start()
> ```

### Deep hierarchies
Modeling every axis of variation as a new subclass level leads to an exponential number of subclasses—a situation known as the “subclass explosion.”

```python
class Shape:
    def area(self): pass

class Circle(Shape):
    def area(self):
        return "π * radius^2"

class Square(Shape):
    def area(self):
        return "side^2"

# Adding more and more specific subclasses for different shapes
class SmallCircle(Circle):
    def area(self):
        return "π * (small radius)^2"

class LargeCircle(Circle):
    def area(self):
        return "π * (large radius)^2"

class SmallSquare(Square):
    def area(self):
        return "small side^2"

class LargeSquare(Square):
    def area(self):
        return "large side^2"

# This quickly grows and leads to a subclass explosion.
```

> [!WARNING]
> **Problem**: Here, each variation in shape size results in a new subclass, which **leads to deep, unwieldy hierarchies**. With many such axes of variation (e.g., sizes, colors, types), this model could grow exponentially and become very difficult to maintain or modify. A better approach might be to use composition or other design patterns like the Strategy pattern to avoid this explosion of subclasses.
> ```python
> class Circle(Shape):
>     def __init__(self, radius):
>         self.radius = radius
> 
>     def area(self):
>         return 3.14 * (self.radius ** 2)
> 
> class Square(Shape):
>     def __init__(self, side):
>         self.side = side
> 
>     def area(self):
>         return self.side ** 2
> 
> # Separate the "size" variation using a Size class rather than subclassing
> class Size:
>     def __init__(self, size_type):
>         self.size_type = size_type
> 
>     def get_factor(self):
>         if self.size_type == "small":
>             return 0.5
>         elif self.size_type == "large":
>             return 2
>         return 1
> ```

## When to Prefer Each
Use **inheritance** when:
- There is a **true is-a relationship**.
- All subclasses uphold the **behavioral contract of the superclass** (per the LSP).
- You want **polymorphic substitution** (e.g., GUI components with a shared rendering base).

Use **composition** when:
- **Behavior varies independently** along multiple axes (e.g., payment processors, logging).
- **Runtime configurability is important** (*strategy pattern*).
- **Domain logic** changes often (typical in business and domain-driven applications).

> [!TIP]
> **Pragmatic Rule**: Start with composition by default. Use inheritance _only_ when substitutability is provable, domain-relevant, and semantically clear.

## Design-Pattern Bridges
Design patterns bridge theory and practical implementation. Here are key patterns that leverage composition:
- **Strategy**: Encapsulates algorithms in interchangeable objects. The context class delegates to a strategy object (an interface).
- **Decorator**: Dynamically adds behavior to an object by wrapping it with another object—useful for layered functionality.
- **Bridge**: Separates abstraction from implementation, enabling both to vary independently through composition.

These patterns make the _“composition over inheritance”_ principle actionable.

## Beyond Classical OO

### 6.1 Mixins & Traits
Languages like **Scala**, **Rust**, and **Swift** or even frameworks like [Django](../Languages/Python/Django/dj-mixins.md) allow code reuse through **traits** or **mixins**. These offer composition-like granularity within an inheritance-based model, often resolving the diamond problem via linearization.

### 6.2 Entity-Component Systems (ECS)
Game engines such as Unity use **ECS**, where entities are just IDs and *all behavior is implemented via systems acting on data-only components*. This is **extreme composition**, optimized for modularity and performance.

### 6.3 Functional & ADT Paradigms
In purely functional languages, behavior is organized through **algebraic data types** (ADTs), **pattern matching**, and **higher-order functions**. These mechanisms replace class hierarchies entirely, preserving substitutability via the type system.

## [SOLID](solid.md) Connections
Inheritance and composition have deep ties to the SOLID principles:

| Principle | Inheritance Impact                                                      | Composition Advantage                                                    |
| --------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **SRP**   | Can lead to bloated base classes with multiple duties.                  | **Encourages small, cohesive, single-purpose components**.               |
| **OCP**   | Extending behavior via subclassing may require altering parent classes. | **New composed objects extend behavior without changing existing code**. |
| **LSP**   | Easy to violate if subclass alters expected behavior.                   | **Sidesteps substitutability issues entirely**.                          |
| **ISP**   | Can lock classes into large base interfaces.                            | **Promotes use of small, targeted interfaces**.                          |
| **DIP**   | Ties modules to specific class hierarchies.                             | **Encourages depending on interfaces and injecting behavior**.           |

## Guidelines for Daily Practice
1. Use **inheritance only when a genuine subtype relationship exists**.
2. **Encapsulate change-prone logic with interfaces** and inject via composition.
3. Prefer **shallow hierarchies and delegation** over override-heavy subclassing.
4. Blend composition with abstraction: define interfaces, **compose implementations**.
5. Validate subtypes with **contract-based tests** to catch LSP violations early.

---

Inheritance and composition are not rivals but tools—each with strengths, trade-offs, and risks. *Modern architecture favors **composition** for its flexibility, testability, and adaptability*. Inheritance remains valuable when used judiciously and semantically.

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
