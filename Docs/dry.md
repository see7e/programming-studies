---
title: DRY
tags:
  - studies
  - programming
  - principle
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [New Note](#new-note)

</details>

---
 
# The DRY Principle #to_review
The DRY principle, which ==**stands for "Don't Repeat Yourself"**==, is a fundamental software development principle aimed at reducing repetition of information and code that is likely to change [1](https://en.wikipedia.org/wiki/Don't_repeat_yourself). This principle was originally formulated by Andy Hunt and Dave Thomas in their influential book _The Pragmatic Programmer_, where they defined it as: "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system" [2](https://www.getdbt.com/blog/dry-principles) [1](https://en.wikipedia.org/wiki/Don't_repeat_yourself) [3](https://www.plutora.com/blog/understanding-the-dry-dont-repeat-yourself-principle).

## Core Concept and Philosophy
The DRY principle emphasizes the elimination of unnecessary code duplication in software development projects[4](https://scalastic.io/en/solid-dry-kiss/). Rather than copying and pasting similar code throughout a codebase, developers should create modular and referenceable code that can be reused wherever needed[2](https://www.getdbt.com/blog/dry-principles). This approach promotes the creation of abstractions that are less likely to change, replacing repetitive patterns with centralized, maintainable solutions[1](https://en.wikipedia.org/wiki/Don't_repeat_yourself).

The principle applies broadly across all aspects of software development, including database schemas, test plans, build systems, and even documentation[1](https://en.wikipedia.org/wiki/Don't_repeat_yourself). When successfully implemented, modifications to any single element of a system do not require changes in other logically unrelated elements[1](https://en.wikipedia.org/wiki/Don't_repeat_yourself).

## Benefits of Following DRY

## Enhanced Maintainability and Consistency
Following the DRY principle provides several significant advantages for software development teams[5](https://www.baeldung.com/cs/dry-software-design-principle)[4](https://scalastic.io/en/solid-dry-kiss/). By consolidating duplicate logic into single locations, developers save considerable time and cognitive energy that would otherwise be spent writing repetitive code[2](https://www.getdbt.com/blog/dry-principles). This approach creates more consistent definitions throughout the system, ensuring that business logic and metrics have standardized implementations[2](https://www.getdbt.com/blog/dry-principles).

## Reduced Error Rates and Improved Reliability
DRY code significantly reduces the likelihood of bugs and inconsistencies[6](https://dev.to/officialozioma/the-dry-principle-in-software-development-10fn)[3](https://www.plutora.com/blog/understanding-the-dry-dont-repeat-yourself-principle). When the same logic exists in multiple places and requires modification, there's a high risk that necessary changes won't be correctly applied to every location[6](https://dev.to/officialozioma/the-dry-principle-in-software-development-10fn). This can lead to systems where multiple locations fall out of sync, creating maintenance nightmares and introducing numerous bugs[6](https://dev.to/officialozioma/the-dry-principle-in-software-development-10fn).

## Simplified Development Process
The principle enables developers to focus their cognitive resources on solving bigger, more complex problems rather than wasting time on repetitive syntax[2](https://www.getdbt.com/blog/dry-principles). While there may be an initial investment in creating good abstractions, the long-term benefits include substantial time savings and reduced development headaches[2](https://www.getdbt.com/blog/dry-principles).

## Practical Implementation Strategies

## Code Organization and Structure
Effective DRY implementation involves several key strategies[7](https://gazar.dev/clean-code/embracing-the-dry-principle-in-programming). Developers should identify common patterns and recurring themes in their codebase that indicate opportunities for abstraction and reuse[7](https://gazar.dev/clean-code/embracing-the-dry-principle-in-programming). Common functionality such as input validation, error handling, and data manipulation are prime candidates for abstraction[7](https://gazar.dev/clean-code/embracing-the-dry-principle-in-programming).

## Creating Reusable Components
Once common patterns are identified, they should be extracted into reusable components, functions, or modules[7](https://gazar.dev/clean-code/embracing-the-dry-principle-in-programming). These components should encapsulate well-defined functionality and be designed with clear interfaces that promote reusability[7](https://gazar.dev/clean-code/embracing-the-dry-principle-in-programming). Parameterization and generalization make these components more flexible and adaptable by avoiding hardcoded values or assumptions that limit their applicability[7](https://gazar.dev/clean-code/embracing-the-dry-principle-in-programming).

## Real-World Examples

### Temperature Conversion Example
A simple illustration of DRY implementation can be seen in temperature conversion logic[5](https://www.baeldung.com/cs/dry-software-design-principle). Before applying DRY, developers might write duplicate conversion formulas in multiple places throughout their code[5](https://www.baeldung.com/cs/dry-software-design-principle). After refactoring, the conversion logic is consolidated into a single reusable function like `fahrenheitToCelsius()` that can be called wherever needed[5](https://www.baeldung.com/cs/dry-software-design-principle).

### E-commerce Platform Case Study
In a practical scenario involving an e-commerce platform, teams often write similar code for product filtering across multiple pages: search results, recommendations, and related products[8](https://www.zetaton.com/blog/dry-principle-in-software-development). Initially, these repetitive code snippets become maintenance headaches as the application grows[8](https://www.zetaton.com/blog/dry-principle-in-software-development). By refactoring to create a single reusable function for product filtering, teams achieve immediate benefits including efficiency boosts, reduced bugs, and improved collaborative ease[8](https://www.zetaton.com/blog/dry-principle-in-software-development).

## The WET Alternative and Its Drawbacks
The opposing approach to DRY is called WET, which stands for various backronyms including "Write Everything Twice," "Write Every Time," "We Enjoy Typing," or "Waste Everyone's Time"[1](https://en.wikipedia.org/wiki/Don't_repeat_yourself)[9](https://blog.stackademic.com/dry-vs-wet-code-understanding-the-cost-of-repetition-in-software-development-a6600289a3e8). WET solutions are common in multi-tiered architectures where developers might repeat the same text strings, functions, or logic across multiple locations[1](https://en.wikipedia.org/wiki/Don't_repeat_yourself).

While WET code might seem faster to implement initially, DRY code provides superior long-term benefits by making codebases easier to manage and less prone to bugs[9](https://blog.stackademic.com/dry-vs-wet-code-understanding-the-cost-of-repetition-in-software-development-a6600289a3e8). WET approaches lead to bloated, harder-to-maintain codebases that require multiple updates whenever changes are needed[9](https://blog.stackademic.com/dry-vs-wet-code-understanding-the-cost-of-repetition-in-software-development-a6600289a3e8).

## When Not to Apply DRY

### Avoiding Premature Abstraction
Despite its benefits, the DRY principle should not be applied blindly in all situations[10](https://codeconservatory.com/blog/post/dry/)[11](https://dev.to/maximlogunov/when-not-to-use-the-dry-principle-exceptions-to-the-rule-4eda). One of the most common misapplications occurs when developers create abstractions too early in the development process[11](https://dev.to/maximlogunov/when-not-to-use-the-dry-principle-exceptions-to-the-rule-4eda). Before understanding how code will actually be used in multiple contexts, forcing DRY can create overly complex abstractions that are hard to understand and introduce unnecessary coupling between components[11](https://dev.to/maximlogunov/when-not-to-use-the-dry-principle-exceptions-to-the-rule-4eda).

### The Rule of Three
A practical guideline for avoiding premature DRY implementation is the "Three Strikes and You Refactor" rule[12](https://www.justinweiss.com/articles/i-dry-ed-up-my-code-and-now-its-hard-to-work-with-what-happened/). The first time you implement something, you simply do it[12](https://www.justinweiss.com/articles/i-dry-ed-up-my-code-and-now-its-hard-to-work-with-what-happened/). The second time you encounter something similar, you acknowledge the duplication but proceed with the duplicate implementation[12](https://www.justinweiss.com/articles/i-dry-ed-up-my-code-and-now-its-hard-to-work-with-what-happened/). The third time you encounter the pattern, you refactor to create a DRY solution[12](https://www.justinweiss.com/articles/i-dry-ed-up-my-code-and-now-its-hard-to-work-with-what-happened/). This approach helps developers distinguish between essential duplication (which should be eliminated) and accidental duplication (which may be coincidental)[12](https://www.justinweiss.com/articles/i-dry-ed-up-my-code-and-now-its-hard-to-work-with-what-happened/).

### Balancing Readability and Abstraction
Sometimes removing duplication can make code harder to understand[11](https://dev.to/maximlogunov/when-not-to-use-the-dry-principle-exceptions-to-the-rule-4eda). If extracting shared functionality requires jumping through multiple files to follow logic, introduces obscure naming to cover multiple use cases, or creates overly clever but confusing solutions, then the DRY principle might be causing more harm than good[11](https://dev.to/maximlogunov/when-not-to-use-the-dry-principle-exceptions-to-the-rule-4eda). In such cases, readable code may be more valuable than perfectly DRY code[11](https://dev.to/maximlogunov/when-not-to-use-the-dry-principle-exceptions-to-the-rule-4eda).

## Relationship to Other Design Principles
The DRY principle works in conjunction with other software design principles, particularly the SOLID principles[13](https://dev.to/yatendra2001/practical-insights-on-solid-dry-kiss-explained-in-noob-vs-pro-analogy-2a92). While DRY focuses on eliminating duplication, principles like Single Responsibility Principle (SRP) ensure that classes have focused purposes, and the Open-Closed Principle (OCP) allows for extension without modification[13](https://dev.to/yatendra2001/practical-insights-on-solid-dry-kiss-explained-in-noob-vs-pro-analogy-2a92). Together, these principles create a framework for writing modular, flexible, and robust code[13](https://dev.to/yatendra2001/practical-insights-on-solid-dry-kiss-explained-in-noob-vs-pro-analogy-2a92).

## Tools and Best Practices

### Implementation Support
Various tools and practices support DRY implementation, including version control systems, modular coding approaches, and continuous integration processes that enforce consistency[14](https://www.secoda.co/glossary/dry-dont-repeat-yourself). Code generators, automatic build systems, and scripting languages help developers observe the DRY principle across different layers of their applications[1](https://en.wikipedia.org/wiki/Don't_repeat_yourself).

### Documentation and Team Collaboration
One often overlooked benefit of DRY implementation is its positive impact on developer onboarding[8](https://www.zetaton.com/blog/dry-principle-in-software-development). In DRY-compliant codebases, new developers can understand core functionalities by studying well-documented reusable functions and modules rather than sifting through repetitive code blocks[8](https://www.zetaton.com/blog/dry-principle-in-software-development). This reduces onboarding time and allows new team members to contribute more quickly to projects[8](https://www.zetaton.com/blog/dry-principle-in-software-development).

## Conclusion
The DRY principle represents a cornerstone of effective software development, promoting maintainability, consistency, and efficiency through the elimination of code duplication[15](https://www.digitalocean.com/community/tutorials/what-is-dry-development)[3](https://www.plutora.com/blog/understanding-the-dry-dont-repeat-yourself-principle). While it requires careful consideration to avoid premature abstraction and over-engineering, when properly applied, DRY creates more robust systems that are easier to maintain and extend[4](https://scalastic.io/en/solid-dry-kiss/). By understanding both the benefits and limitations of this principle, developers can make informed decisions about when and how to implement DRY practices in their projects, ultimately leading to more sustainable and maintainable software systems[7](https://gazar.dev/clean-code/embracing-the-dry-principle-in-programming).

## External References
1. Hunt, A., & Thomas, D. (1999). _The Pragmatic Programmer: From Journeyman to Master_. Addison-Wesley Professional.
2. Meyer, B. (1988). _Object-Oriented Software Construction_. Prentice Hall.
3. Martin, R. C. (2008). _Clean Code: A Handbook of Agile Software Craftsmanship_. Prentice Hall.
4. Fowler, M. (1999). _Refactoring: Improving the Design of Existing Code_. Addison-Wesley Professional.
5. Beck, K. (2000). _Extreme Programming Explained: Embrace Change_. Addison-Wesley Professional.
6. [https://en.wikipedia.org/wiki/Don't_repeat_yourself](https://en.wikipedia.org/wiki/Don't_repeat_yourself)
7. [https://www.getdbt.com/blog/dry-principles](https://www.getdbt.com/blog/dry-principles)
8. [https://www.plutora.com/blog/understanding-the-dry-dont-repeat-yourself-principle](https://www.plutora.com/blog/understanding-the-dry-dont-repeat-yourself-principle)
9. [https://scalastic.io/en/solid-dry-kiss/](https://scalastic.io/en/solid-dry-kiss/)
10. [https://www.baeldung.com/cs/dry-software-design-principle](https://www.baeldung.com/cs/dry-software-design-principle)
11. [https://dev.to/officialozioma/the-dry-principle-in-software-development-10fn](https://dev.to/officialozioma/the-dry-principle-in-software-development-10fn)
12. [https://gazar.dev/clean-code/embracing-the-dry-principle-in-programming](https://gazar.dev/clean-code/embracing-the-dry-principle-in-programming)
13. [https://www.zetaton.com/blog/dry-principle-in-software-development](https://www.zetaton.com/blog/dry-principle-in-software-development)
14. [https://blog.stackademic.com/dry-vs-wet-code-understanding-the-cost-of-repetition-in-software-development-a6600289a3e8](https://blog.stackademic.com/dry-vs-wet-code-understanding-the-cost-of-repetition-in-software-development-a6600289a3e8)
15. [https://codeconservatory.com/blog/post/dry/](https://codeconservatory.com/blog/post/dry/)
16. [https://dev.to/maximlogunov/when-not-to-use-the-dry-principle-exceptions-to-the-rule-4eda](https://dev.to/maximlogunov/when-not-to-use-the-dry-principle-exceptions-to-the-rule-4eda)
17. [https://www.justinweiss.com/articles/i-dry-ed-up-my-code-and-now-its-hard-to-work-with-what-happened/](https://www.justinweiss.com/articles/i-dry-ed-up-my-code-and-now-its-hard-to-work-with-what-happened/)
18. [https://dev.to/yatendra2001/practical-insights-on-solid-dry-kiss-explained-in-noob-vs-pro-analogy-2a92](https://dev.to/yatendra2001/practical-insights-on-solid-dry-kiss-explained-in-noob-vs-pro-analogy-2a92)
19. [https://www.secoda.co/glossary/dry-dont-repeat-yourself](https://www.secoda.co/glossary/dry-dont-repeat-yourself)
20. [https://www.digitalocean.com/community/tutorials/what-is-dry-development](https://www.digitalocean.com/community/tutorials/what-is-dry-development)
21. [https://blog.pixelfreestudio.com/best-practices-for-writing-dry-dont-repeat-yourself-code/](https://blog.pixelfreestudio.com/best-practices-for-writing-dry-dont-repeat-yourself-code/)
22. [https://stackoverflow.com/questions/17788738/is-violation-of-dry-principle-always-bad](https://stackoverflow.com/questions/17788738/is-violation-of-dry-principle-always-bad)
23. [https://daedtech.com/subtle-naming-and-declaration-violations-of-dry/](https://daedtech.com/subtle-naming-and-declaration-violations-of-dry/)
24. [https://www.reddit.com/r/programming/comments/xn14lx/why_dry_is_the_most_overrated_programming/](https://www.reddit.com/r/programming/comments/xn14lx/why_dry_is_the_most_overrated_programming/)
25. [https://nkamphoa.com/dry-principle-object-oriented/](https://nkamphoa.com/dry-principle-object-oriented/)
26. [https://dev.to/moh_moh701/c-clean-codedry-principle-4e5c](https://dev.to/moh_moh701/c-clean-codedry-principle-4e5c)
27. [https://www.theserverside.com/tip/Code-refactoring-patterns-with-examples](https://www.theserverside.com/tip/Code-refactoring-patterns-with-examples)
28. [https://thevaluable.dev/dry-principle-cost-benefit-example/](https://thevaluable.dev/dry-principle-cost-benefit-example/)
29. [https://danielrotter.at/2021/01/16/code-comments-are-mostly-a-violation-of-dry.html](https://danielrotter.at/2021/01/16/code-comments-are-mostly-a-violation-of-dry.html)
