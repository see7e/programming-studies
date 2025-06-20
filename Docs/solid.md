---
title: SOLID Design Principles
tags:
  - studies
  - programming
  - solid
  - design
  - principle
use: Documentation, Design, Principles
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [SOLID Design Principles](#solid-design-principles)
  - [S – Single Responsibility Principle (SRP)](#s--single-responsibility-principle-srp)
    - [Common Signs a Class Has More Than One Reason to Change](#common-signs-a-class-has-more-than-one-reason-to-change)
      - [Broader Implications](#broader-implications)
  - [O – Open/Closed Principle (OCP)](#o--openclosed-principle-ocp)
  - [L – Liskov Substitution Principle (LSP)](#l--liskov-substitution-principle-lsp)
  - [I – Interface Segregation Principle (ISP)](#i--interface-segregation-principle-isp)
  - [D – Dependency Inversion Principle (DIP)](#d--dependency-inversion-principle-dip)
- [References](#references)

</details>

---

# SOLID Design Principles
The **SOLID principles** are a set of five core guidelines for object-oriented design, introduced by Robert C. Martin (Uncle Bob) around 2000 [1](#references). The name is an acronym formed from the first letters of each principle. SOLID is widely taught as a cornerstone of good OOP design because following these principles tends to produce code that is easier to understand, extend, and maintain. The principles are:

## S – Single Responsibility Principle (SRP)
A class should have one, and only one, reason to change [2](#references). In other words, ==each class should only fulfill a single responsibility or functionality== [3](#references). If a class does too many things, it becomes complex and difficult to maintain. *By keeping classes focused, you achieve higher cohesion*.

> [!TIP]
> The point about "only one reason to change" is related with the [coupling](to_review/coupling.md) of the logic ("responsibility") that is expected for that class/method to perform. If more than one performed tasks changes (Robert also refers to *stakeholders*) and this triggers a change in the class, than this principle is broken.

> For example, a class `ReportGenerator` might have the sole job of generating reports – it shouldn’t also be handling database connections or logging, because those are separate concerns. Following SRP makes classes "smaller" and more maintainable.

As Uncle Bob humorously avises, **“classes should be small! … We count responsibilities to measure class size”**. ==If you can’t describe what a class does in a concise sentence, it likely has multiple responsibilities and should be refactored== [4](#references). Adhering to SRP yields benefits in **maintainability (easier to understand and change one focused class) and testability (simpler to write unit tests for a class that does one thing).**

Other correlation that could be made with the example is that is if another class needs to make another connection with the database, probably the logic will be repeated, and this breaks the [DRY](dry.md) principle.

### Common Signs a Class Has More Than One Reason to Change
Several "*code smells*" and structural symptoms indicate that a class is violating the Single Responsibility Principle (SRP) by having more than one reason to change:

**1. Multiple Areas of Functionality**
- The class contains *methods or logic that serve distinct, unrelated purposes*. For example, a class that both handles business logic and manages database transactions is taking on too many roles [6](#references) [7](#references).

**2. Method Grouping by Unrelated Tasks**
- Methods in the class naturally *group into separate clusters based on different concerns* (e.g., "these are report methods," "these are calculation methods") [6](#references).

**3. Difficult or Compound Naming**
- If you *struggle to name the class succinctly*, or the name contains "and" (e.g., `ReportAndCalculationManager`), it's a sign the class does too much [6](#references).

**4. Multiple Stakeholders or Change Drivers**
- The class must be modified for different reasons by different people (e.g., a change in business rules vs. a change in reporting format) [8](#references).

**5. Too Many Dependencies**
- The class *depends on many unrelated services or libraries*, making it complex and tightly coupled [5](#references).

**6. Low Cohesion**
- The class's methods *do not operate on the same data* or do not logically belong together, reducing cohesion [6](#references).

**7. Frequent Changes for Unrelated Reasons**
- The class is often modified for reasons that are *not directly related* (e.g., updating how data is stored vs. changing how data is displayed) [7](#references) [8](#references).

**8. Implementing Many Interfaces**
- The class *implements interfaces for different concerns*, suggesting it handles multiple responsibilities [6](#references).

**9. "Big Ball of Mud"**
- The class *grows large and unwieldy*, with logic for many different tasks, making it fragile and hard to maintain [6](#references).

> If you have an `Employee` class that both calculates pay and prints history reports, you would need to change it if the pay calculation changes or if the report format changes. This means the class has more than one reason to change and should be split into separate classes for each responsibility [8].

#### Broader Implications
- **Coupling:** Multiple responsibilities in one class cause coupling between unrelated features, making the code fragile and harder to test [9](#references).
- **Maintainability:** Classes with a single responsibility are easier to maintain, extend, debug and test [5](#references).
If you notice any of these signs, it's a good indication that your class may need to be refactored to better adhere to the Single Responsibility Principle.

---
## O – Open/Closed Principle (OCP)
 _“Software entities (classes, modules, functions) should be open for extension, but closed for modification.”_[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=The%20open%E2%80%93closed%20principle%20,8) This means you should design classes in a way that new functionality can be added by writing new code (e.g., new subclasses, new methods) rather than changing the existing class code. If you find yourself frequently editing the internals of a class to accommodate new needs, that class might violate OCP. A classic example is using inheritance or interfaces: Suppose you have a class that calculates area for shapes – rather than writing a big `if` or switch that checks shape type (circle, square, etc.), you make it open for extension by having a base class `Shape` with a method `area()`. Each new shape subclass implements `area()` accordingly. The code that uses `Shape.area()` doesn’t need to change when a new shape is added – you just add a new subclass. This principle ties closely to polymorphism and to using abstraction to insulate high-level code from changes in low-level concrete implementations[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=In%20software%20programming%20%2C%20SOLID,1)[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=The%20open%E2%80%93closed%20principle%20,8). **The benefit is reduced risk when adding features** – you add new code without breaking existing code (which presumably already works and is tested). This leads to more stable systems as they evolve[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=,to%20changing%20requirements%20more%20easily).
 > Software entities (classes, modules, functions) should be **open for extension** but **closed for modification**. You achieve this by writing code that allows new functionality via extension (e.g., subclassing or composition) without altering existing code, thus avoiding bugs in tested code.

## L – Liskov Substitution Principle (LSP)
Introduced by Barbara Liskov, LSP states that _subtypes must be substitutable for their base types_[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=). More formally: if `S` is a subtype of `T`, then objects of type `T` in a program may be replaced with objects of type `S` without altering any desirable properties of the program (correctness, task performed, etc.). In practice, this means derived classes should extend the base class’s behavior without contradicting its expected behavior. For example, if you have a class `Bird` with a method `fly()`, and a subclass `Penguin` that cannot actually fly, making `Penguin.fly()` throw an exception would violate LSP because wherever a `Bird` is expected to fly, a `Penguin` would break the behavior assumptions. Violating LSP often indicates a design problem in your inheritance hierarchy. Adhering to LSP ensures **polymorphism works correctly** – any code using the base class should not need special case handling for subclasses[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=)[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=,9). It also implies you should not strengthen preconditions or weaken postconditions when overriding methods. The result is **reliable interchangeability**, which is the whole point of polymorphism. LSP encourages careful hierarchy design and often pushes designs toward using composition or interfaces when inheritance doesn’t truly model an “is-a” relationship.
>  Subtypes must be substitutable for their base types. Any class inheriting from a base class should be usable wherever the base class is expected, without breaking the program. This encourages proper inheritance hierarchies (no surprising side-effects when using a subclass in place of a parent class).

## I – Interface Segregation Principle (ISP)
_“Clients should not be forced to depend on interfaces they do not use.”_[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=) This principle is about the granularity of interfaces. It’s better to have many small, specific interfaces than a single large interface with many methods that different clients only partly use. If an interface is too broad, any class implementing it might have to stub out unused methods, and any client using it will be aware of more than it needs. For example, instead of one giant `IMonster` interface that has methods `stalkPrey()`, `fly()`, `spitFire()`, etc. (many monsters may not do all those things), it’s better to have smaller interfaces like `IPredator`, `IFlyer`, `IFireBreather` and have classes implement the ones that are applicable. ISP leads to more **decoupled and modular code**[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=). It also makes the impact of changes smaller – if you need to change one method of an interface, ideally only a few classes implementing that small interface are affected, rather than a huge number of classes implementing a bloated interface. Following ISP often means using **multiple interfaces to model different aspects of an object’s capabilities**, which is common in OOP design (especially in languages like Java and C# that support multiple interfaces). The end result is that **clients (code that uses an interface) are simpler** because they know only about the methods they actually need, and **implementers are not overly burdened** by requirements that don’t make sense for them.
> No client should be forced to depend on methods it does not use. It’s better to have many small, specific interfaces than one large “god” interface. This way, implementing classes only need to worry about the methods that are relevant to them.

## D – Dependency Inversion Principle (DIP)
_“Depend upon abstractions, [not] concretions.”_[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=) In essence, high-level modules (overall policy/logic) should not depend on low-level modules (details); both should depend on abstractions (e.g., interfaces). Additionally, abstractions should not depend on details; details should depend on abstractions. This principle helps decouple software layers. For example, if you have a class `DatabaseSaver` that saves data to a database, a high-level class `UserService` might need to save user info. Without DIP, `UserService` might directly instantiate a `DatabaseSaver` and call its method. This creates a concrete dependency – if you later want to save data to a file instead, you’d have to change `UserService`. With DIP, you would define an interface `IDataStore` with a method `save(data)`, and `DatabaseSaver` would implement this interface. `UserService` would depend only on `IDataStore` abstraction, and at runtime you can provide it with any concrete implementation (database, file, in-memory, etc.). This is often implemented via **dependency injection frameworks or factory patterns** to supply the desired implementation. DIP leads to **looser coupling**, making code more flexible and testable (you can provide a mock implementation of `IDataStore` to test `UserService` easily, for instance)[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=Dependency%20inversion%20principle). It’s a key principle behind many architectural patterns (like hexagonal architecture, clean architecture, etc.), ensuring that high-level logic remains agnostic of low-level implementation details. By inverting dependencies, changes in low-level modules (like switching database library, or changing how logging works) have minimal impact on higher-level logic.
> High-level modules should not depend on low-level modules; both should depend on abstractions. Also, abstractions (interfaces) should not depend on details; details (implementations) should depend on abstractions. This principle inverts the typical dependency direction to reduce coupling. For example, instead of a class directly instantiating a database object, it would depend on an interface; a concrete database implementation then fulfills that interface. This makes swapping out components (like using a different database) much easier.


Each SOLID principle addresses a specific aspect of software design, but they complement each other. Together they guide us to write **code that has high cohesion (related functionality in one place) and low coupling (minimal dependencies between modules)**[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=)[en.wikipedia.org](https://en.wikipedia.org/wiki/SOLID#:~:text=,on%20methods%20they%20don%27t%20use). Adhering to SOLID tends to produce systems that are easier to maintain and extend – which directly ties to why OOP is valued. For instance, a class following SRP and DIP is likely easier to modify without side effects, and you can substitute implementations thanks to LSP and ISP, enabling flexible architectures and even **plug-in-like designs**.

It’s worth noting that SOLID principles are guidelines, not iron-clad laws. Sometimes overzealous application can lead to too many layers of abstraction (e.g., making an interface for every single class even when not needed, or splitting responsibilities too finely). The key is balance – use SOLID to eliminate blatant design smells (like classes that do too much, or brittle interdependencies) but keep the code as simple as possible. As a rule of thumb, if following a principle makes the design _more_ complex with no clear benefit, reconsider the approach. Properly applied, SOLID helps manage complexity in large codebases and is almost a checklist for good OO design. In fact, many modern **agile and clean coding practices** build on these principles – for example, many of Clean Code’s class design recommendations echo SRP and ISP (keep classes small, focused, and interfaces narrowly tailored to clients)



---

# References

1. [`en.wikipedia.org`](https://en.wikipedia.org/wiki/SOLID#:~:text=Software%20engineer%20and%20instructor%20Robert,5)
2. ["Single Responsibility Principle"](https://web.archive.org/web/20150202200348/http://www.objectmentor.com/resources/articles/srp.pdf) (PDF). `objectmentor.com`. Archived from the original on 2 February 2015.
3. [Martin, Robert C.](https://en.wikipedia.org/wiki/Robert_Cecil_Martin) (2003). [_Agile Software Development, Principles, Patterns, and Practices_](https://books.google.com/books?id=0HYhAQAAIAAJ). Prentice Hall. p. 95. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0135974445](https://en.wikipedia.org/wiki/Special:BookSources/978-0135974445 "Special:BookSources/978-0135974445").
4. [medium.com](https://medium.com/javarevisited/clean-code-classes-dae3cb44eb90#:~:text=The%20name%20of%20a%20class,then%20it%27s%20likely%20too%20large)
5. [LogRocket: SRP in practice](https://blog.logrocket.com/single-responsibility-principle-srp/)
6. [Stack Overflow: Signs of violating SRP](https://stackoverflow.com/questions/246068/how-do-you-define-a-single-responsibility)
7. [TutorialsTeacher: Real-world SRP examples](https://www.tutorialsteacher.com/csharp/single-responsibility-principle)
8. [Reddit: Practical implications of SRP](https://www.reddit.com/r/learnprogramming/comments/wla9pg/there_should_never_be_more_than_one_reason_for_a/)
9. [Duke University: SRP and coupling](https://courses.cs.duke.edu/fall22/compsci307d/readings/srp.pdf)
10. 