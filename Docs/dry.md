---
title: DRY – Don’t Repeat Yourself
tags:
  - studies
  - programming
  - design
  - principle
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [The DRY Principle](#the-dry-principle)
  - [Core Concept and Philosophy](#core-concept-and-philosophy)
  - [Benefits of Following DRY](#benefits-of-following-dry)
    - [Enhanced Maintainability and Consistency](#enhanced-maintainability-and-consistency)
    - [Reduced Error Rates and Improved Reliability](#reduced-error-rates-and-improved-reliability)
    - [Simplified Development Process](#simplified-development-process)
  - [Practical Implementation Strategies](#practical-implementation-strategies)
    - [Code Organization and Structure](#code-organization-and-structure)
    - [Creating Reusable Components](#creating-reusable-components)
  - [The WET Alternative and Its Drawbacks](#the-wet-alternative-and-its-drawbacks)
  - [When **Not** to Apply DRY](#when-not-to-apply-dry)
    - [Avoiding Premature Abstraction](#avoiding-premature-abstraction)
    - [The Rule of Three](#the-rule-of-three)
    - [Balancing Readability and Abstraction](#balancing-readability-and-abstraction)
  - [Tools and Best Practices](#tools-and-best-practices)
    - [Relationship to Other Design Principles](#relationship-to-other-design-principles)
    - [Implementation Support](#implementation-support)
    - [Documentation and Team Collaboration](#documentation-and-team-collaboration)
  - [External References](#external-references)

</details>

---
 
# The DRY Principle
The DRY principle, which ==**stands for "Don't Repeat Yourself"**==, is a fundamental software development principle *aimed at reducing repetition of information and code that is likely to change*. This principle was originally formulated by Andy Hunt and Dave Thomas in their influential book *The Pragmatic Programmer*, where they defined it as: "**Every piece of knowledge must have a single, unambiguous, authoritative representation within a system**".

## Core Concept and Philosophy
The DRY principle *emphasizes the elimination of unnecessary code duplication* in software development projects [SOLID](solid.md). Rather than copying and pasting similar code throughout a codebase, developers should create modular and referenceable code that can be reused wherever needed. This approach promotes the creation of abstractions that are less likely to change, replacing repetitive patterns with centralized, maintainable solutions.

The principle applies broadly across all aspects of software development, including database schemas, test plans, build systems, and even [documentation](project_documentation.md). *When successfully implemented, modifications to any single element of a system do not require changes in other logically unrelated elements*.

## Benefits of Following DRY

### Enhanced Maintainability and Consistency
Following the DRY principle provides several significant advantages for software development teams. By consolidating duplicate logic into single locations, developers *save considerable time and cognitive energy* that would otherwise be spent writing repetitive code. This approach creates more consistent definitions throughout the system, *ensuring that business logic and metrics have standardized implementations*.

### Reduced Error Rates and Improved Reliability
DRY code significantly reduces the likelihood of bugs and inconsistencies. When the same logic exists in multiple places and requires modification, there's a high risk that necessary changes won't be correctly applied to every location. *This can lead to systems where multiple locations fall out of sync*, creating maintenance nightmares and introducing numerous bugs.

### Simplified Development Process
The principle *enables developers to focus their cognitive resources on solving bigger, more complex problems rather than wasting time on repetitive syntax*. While there may be an initial investment in creating good abstractions, the long-term benefits include substantial time savings and reduced development headaches.

## Practical Implementation Strategies

### Code Organization and Structure
Effective implementation involves several key strategies. Developers should identify common patterns and recurring themes in their codebase that indicate opportunities for abstraction and reuse. *Common functionality such as input validation, error handling, and data manipulation are prime candidates for abstraction*.

### Creating Reusable Components
*Once common patterns are identified, they should be extracted into reusable components, functions, or modules*. These components should encapsulate well-defined functionality and be designed with clear interfaces that promote reusability. *Parameterization and generalization* make these components more flexible and adaptable by avoiding hardcoded values or assumptions that limit their applicability.

> [!TIP]
> ### Temperature Conversion Example
> A simple illustration of DRY implementation can be seen in temperature conversion logic. Before applying DRY, developers might write duplicate conversion formulas in multiple places throughout their code. After refactoring, the conversion logic is consolidated into a single reusable function like `fahrenheitToCelsius()` that can be called wherever needed.
> 
> ### E-commerce Platform Case Study
> In a practical scenario involving an e-commerce platform, teams often write similar code for product filtering across multiple pages: search results, recommendations, and related products. Initially, these repetitive code snippets become maintenance headaches as the application grows. By refactoring to create a single reusable function for product filtering, teams achieve immediate benefits including efficiency boosts, reduced bugs, and improved collaborative ease.

## The WET Alternative and Its Drawbacks
*The opposing approach to DRY is called WET*, which stands for various backronyms including "Write Everything Twice," "Write Every Time," "We Enjoy Typing," or "Waste Everyone's Time". WET solutions are *common in multi-tiered architectures* where developers might repeat the same text strings, functions, or logic across multiple locations.

While WET code might seem faster to implement initially, DRY code provides superior long-term benefits by making codebases easier to manage and less prone to bugs. WET approaches **lead to bloated, harder-to-maintain codebases that require multiple updates whenever changes are needed**.

## When **Not** to Apply DRY

### Avoiding Premature Abstraction
Despite its benefits, the DRY principle shouldn't be applied blindly in all situations. One of the most common misapplications occurs when developers create abstractions too early in the development process.
*Before understanding how code will actually be used in multiple contexts, forcing DRY can create overly complex abstractions that are hard to understand and introduce unnecessary coupling between components*.

### The Rule of Three
A practical guideline for avoiding premature DRY implementation is the **"Three Strikes and You Refactor"** rule: 
1. The first time you implement something, you simply do it. 
2. The second time you encounter something similar, you acknowledge the duplication but proceed with the duplicate implementation.
3. The third time you encounter the pattern, you refactor to create a DRY solution.

This approach helps developers distinguish between **essential duplication** (which should be eliminated) and **accidental duplication** (which may be coincidental).

### Balancing Readability and Abstraction
Sometimes removing duplication can make code harder to understand. *If extracting shared functionality requires jumping through multiple files to follow logic, introduces obscure naming to cover multiple use cases, or creates overly clever but confusing solutions*, then the DRY principle might be causing more harm than good. In such cases, readable code may be more valuable than perfectly DRY code.

## Tools and Best Practices

### Relationship to Other Design Principles
The DRY principle works in conjunction with other software design principles, particularly the SOLID principles.
While DRY focuses on eliminating duplication, principles like Single Responsibility Principle (SRP) ensure that classes have focused purposes, and the Open-Closed Principle (OCP) allows for extension without modification. Together, these principles create a framework for writing modular, flexible, and robust code.

### Implementation Support
Various tools and practices support DRY implementation, including version control systems, modular coding approaches, and continuous integration processes that enforce consistency. Code generators, automatic build systems, and scripting languages help developers observe the DRY principle across different layers of their applications.

### Documentation and Team Collaboration
One often overlooked benefit of DRY implementation is its *positive impact on developer onboarding*. In DRY-compliant codebases, new developers can understand core functionalities by studying well-documented reusable functions and modules rather than sifting through repetitive code blocks. This *reduces onboarding time and allows new team members to contribute more quickly to projects*.

---

The DRY principle represents a cornerstone of effective software development, promoting maintainability, consistency, and efficiency through the elimination of code duplication.
While it *requires careful consideration to avoid premature abstraction and over-engineering*, when properly applied, DRY creates more robust systems that are easier to maintain and extend. By understanding both the benefits and limitations of this principle, developers can make informed decisions about when and how to implement DRY practices in their projects, ultimately *leading to more sustainable and maintainable software systems*.

## External References
1. Hunt, A., & Thomas, D. (1999). _The Pragmatic Programmer: From Journeyman to Master_. Addison-Wesley Professional.
2. Meyer, B. (1988). _Object-Oriented Software Construction_. Prentice Hall.
3. Martin, R. C. (2008). _Clean Code: A Handbook of Agile Software Craftsmanship_. Prentice Hall.
4. Fowler, M. (1999). _Refactoring: Improving the Design of Existing Code_. Addison-Wesley Professional.
5. Beck, K. (2000). _Extreme Programming Explained: Embrace Change_. Addison-Wesley Professional.
6. [Don't repeat yourself](https://en.wikipedia.org/wiki/Don't_repeat_yourself)
7. [Dry principles](https://www.getdbt.com/blog/dry-principles)
8. [understanding-the-dry-dont-repeat-yourself-principle](https://www.plutora.com/blog/understanding-the-dry-dont-repeat-yourself-principle)
9. [solid-dry-kiss](https://scalastic.io/en/solid-dry-kiss/)
10. [dry-software-design-principle](https://www.baeldung.com/cs/dry-software-design-principle)
11. [the-dry-principle-in-software-development](https://dev.to/officialozioma/the-dry-principle-in-software-development-10fn)
12. [embracing-the-dry-principle-in-programming](https://gazar.dev/clean-code/embracing-the-dry-principle-in-programming)
13. [dry-principle-in-software-development](https://www.zetaton.com/blog/dry-principle-in-software-development)
14. [dry-vs-wet-code-understanding-the-cost-of-repetition-in-software-development](https://blog.stackademic.com/dry-vs-wet-code-understanding-the-cost-of-repetition-in-software-development-a6600289a3e8)
15. [dry](https://codeconservatory.com/blog/post/dry/)
16. [when-not-to-use-the-dry-principle-exceptions-to-the-rule](https://dev.to/maximlogunov/when-not-to-use-the-dry-principle-exceptions-to-the-rule-4eda)
17. [i-dry-ed-up-my-code-and-now-its-hard-to-work-with-what-happened](https://www.justinweiss.com/articles/i-dry-ed-up-my-code-and-now-its-hard-to-work-with-what-happened/)
18. [practical-insights-on-solid-dry-kiss-explained-in-noob-vs-pro-analogy](https://dev.to/yatendra2001/practical-insights-on-solid-dry-kiss-explained-in-noob-vs-pro-analogy-2a92)
19. [dry-dont-repeat-yourself](https://www.secoda.co/glossary/dry-dont-repeat-yourself)
20. [what-is-dry-development](https://www.digitalocean.com/community/tutorials/what-is-dry-development)
21. [best-practices-for-writing-dry-dont-repeat-yourself-code/](https://blog.pixelfreestudio.com/best-practices-for-writing-dry-dont-repeat-yourself-code/)
22. [is-violation-of-dry-principle-always-bad](https://stackoverflow.com/questions/17788738/is-violation-of-dry-principle-always-bad)
23. [subtle-naming-and-declaration-violations-of-dry/](https://daedtech.com/subtle-naming-and-declaration-violations-of-dry/)
24. [why_dry_is_the_most_overrated_programming](https://www.reddit.com/r/programming/comments/xn14lx/why_dry_is_the_most_overrated_programming/)
25. [dry-principle-object-oriented/](https://nkamphoa.com/dry-principle-object-oriented/)
26. [clean-codedry-principle](https://dev.to/moh_moh701/c-clean-codedry-principle-4e5c)
27. [Code-refactoring-patterns-with-examples](https://www.theserverside.com/tip/Code-refactoring-patterns-with-examples)
28. [dry-principle-cost-benefit-example/](https://thevaluable.dev/dry-principle-cost-benefit-example/)
29. [code-comments-are-mostly-a-violation-of-dry.html](https://danielrotter.at/2021/01/16/code-comments-are-mostly-a-violation-of-dry.html)
