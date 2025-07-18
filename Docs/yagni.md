---
title: YAGNI – You Aren’t Gonna Need It
tags:
  - studies
  - programming
  - yagni
  - design
  - principle
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [YAGNI – You Aren’t Gonna Need It](#yagni--you-arent-gonna-need-it)
  - [Why YAGNI Matters](#why-yagni-matters)
  - [Practical Example](#practical-example)
  - [YAGNI in Agile and XP](#yagni-in-agile-and-xp)
  - [Common Misconceptions](#common-misconceptions)
  - [Related Principles](#related-principles)
- [References](#references)

</details>

---

# YAGNI – You Aren’t Gonna Need It
It's a foundational principle in software development that originated from *Extreme Programming (XP)*. This approach counters the common developer tendency to *over-engineer* solutions by building for hypothetical scenarios. Instead, YAGNI *insists on focusing on current requirements, delivering only what is necessary for the present moment*.

The essence of YAGNI is simple:
> [!QUOTE]
> "Always implement things when you actually need them, never when you just foresee that you [will] need them."  
> — Ron Jeffries, XP co-founder

![meme](https://poisonedyouth.github.io/assets/images/posts/2024/09/13/header.png)

## Why YAGNI Matters
- **Reduces Complexity**: Every unnecessary feature adds complexity, making code harder to understand, maintain, and debug.
- **Speeds Up Development**: By limiting work to immediate needs, teams can deliver value faster, iterate more quickly, and respond to real user feedback.
- **Prevents Waste**: Resources spent on unused features are wasted. YAGNI aligns with *lean* and *agile* philosophies by minimizing this waste.
- **Improves Maintainability**: Less code means fewer bugs, easier refactoring, and lower long-term maintenance costs.

## Practical Example
Suppose you need a method to fetch a user by ID:

```csharp
public User GetUserById(long id) {
	// logic to fetch user by id
}
```

If you preventively add methods to fetch by first or last name without a current requirement, you introduce unnecessary complexity. If requirements change, you have to maintain and possibly refactor unused code, increasing overhead without delivering value. This also can be related with SRP from [SOLID](solid.md).

## YAGNI in Agile and XP
YAGNI is closely tied to other agile and XP practices, such as:
- **Do the Simplest Thing That Could Possibly Work (DTSTTCPW)**
- **Continuous Refactoring**
- **Automated Testing**
- **Continuous Integration (CI)**.

YAGNI works best when combined with these practices, ensuring the codebase remains flexible and easy to change as new requirements emerge.

## Common Misconceptions
- **Not Anti-Abstraction**: YAGNI is often misunderstood as being against abstraction. In reality, it cautions against unnecessary *abstractions that are not currently needed and may never be used*.
- **Not Against Refactoring**: Efforts to make code easier to modify (like refactoring) do not violate YAGNI. In fact, *regular refactoring is essential* to keep the codebase adaptable for future needs.

## Related Principles
YAGNI complements other software development principles:
- **[KISS (Keep It Simple, Stupid)](kiss.md)**
- **[DRY (Don’t Repeat Yourself)](dry.md)**
- **Minimum Viable Product (MVP)**
- **Avoiding Feature Creep and Overengineering**


YAGNI encourages developers to stay focused on current goals, avoid speculative work, and deliver value efficiently. By resisting the urge to build for imagined future scenarios, teams can keep codebases lean, maintainable, and responsive to real user needs.

# References
1. [Wikipedia: "You aren't gonna need it"](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)
2. [Martin Fowler: Yagni](https://martinfowler.com/bliki/Yagni.html)
3. [TechTarget: What is YAGNI principle?](https://www.techtarget.com/whatis/definition/You-arent-gonna-need-it)
4. [LinkedIn: Overview of YAGNI Principle](https://www.linkedin.com/pulse/yagni-ashish-shukla)
5. [Understanding the YAGNI Principle: A Key to Efficient Software Development](https://poisonedyouth.github.io/YAGNI_principle)
6. [YAGNI Principle – only implement features that are really needed](https://t2informatik.de/en/smartpedia/yagni-principle/)
7. [Reddit: YAGNI is a good principle, but many devs miss the point](https://www.reddit.com/r/ExperiencedDevs/comments/11vonwg/yagni_is_a_good_principle_but_many_devs_miss_the/)
8. [OODesign - YAGNI Principle: You Aren't Gonna Need It](https://www.oodesign.com/yagni-you-arent-gonna-need-it)
9. [YAGNI Software Development Principles | Software design principles YAGNI](https://www.youtube.com/watch?v=b2AsHd-5qhk)