---
title: Data Mapper Pattern
tags:
  - studies
  - programming
  - design
  - design-patterns
  - architecture
  - data-mapping
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [Data Mapper Pattern](#data-mapper-pattern)
  - [What Is the Data Mapper?](#what-is-the-data-mapper)
    - [Example Conceptual Flow](#example-conceptual-flow)
  - [Core Benefits](#core-benefits)
  - [Use Cases \& When to Use](#use-cases--when-to-use)
  - [Related Concepts](#related-concepts)
  - [Implementation Tip](#implementation-tip)
- [References](#references)

</details>

---

# Data Mapper Pattern
Is a structural software design pattern that **==separates the in-memory objects from the database layer==**. Instead of letting domain objects manage their own persistence (as in [Active Record](active-record-pattern.md)), the Data Mapper serves as a middle layer responsible for transferring data between objects and a relational database — keeping them independent of each other.

## What Is the Data Mapper?
At its core, the Data Mapper handles the translation between:
- **In-memory domain objects** — often modeled using classes like `User`, `Invoice`, or `Product`.
- **Database representations** — typically rows in a table or records in a document store.

This separation allows for greater **testability**, **maintainability**, and **scalability** in complex systems, especially in **domain-driven design** contexts.

### Example Conceptual Flow

```plaintext
[ Database Table ] ←→ [ Data Mapper ] ←→ [ Domain Object ]
```

Rather than an object saving itself (e.g., `user.save()`), it becomes:

```plaintext
user = UserMapper.find_by_id(1)
UserMapper.save(user)
```

## Core Benefits
1. **Separation of Concerns**: Business logic remains independent of persistence logic.
2. **Testability**: Domain logic can be tested without involving the database.
3. **Flexibility**: Works well with complex schemas, aggregate roots, or multiple data sources.
4. **Maintainability**: Adapts easily to database schema changes without altering domain models.

## Use Cases & When to Use

| Use Case                             | Data Mapper Recommended? |
| ------------------------------------ | ------------------------ |
| Simple CRUD with few tables          | ❌ Prefer Active Record   |
| Large-scale enterprise systems       | ✅ Yes                    |
| Heavy domain logic or aggregates     | ✅ Yes                    |
| Data must come from multiple sources | ✅ Yes                    |

It shines in **enterprise applications**, **DDD (Domain-Driven Design)** projects, or systems following **Hexagonal Architecture** or **Clean Architecture** principles.

## Related Concepts
- **Active Record Pattern**: Opposes Data Mapper by embedding persistence logic in the domain model. Simpler but tightly coupled.
- **Repository Pattern**: Often layered over a Data Mapper to act as a collection-like abstraction over aggregates.
- **Unit of Work**: Coordinates the writing out of changes and manages concurrency, often paired with Data Mapper.

## Implementation Tip
When implementing a Data Mapper:
- Define clear **DTOs (Data Transfer Objects)**.
- Keep **ORM logic out** of your domain models.
- Use mapping layers or libraries to handle transformation cleanly.

Languages such as Java (e.g., MyBatis), Python (e.g., SQLAlchemy with separate model/mapping), and C# (e.g., Dapper) are frequently used to implement this pattern.

---

The Data Mapper pattern is a powerful architectural strategy for decoupling complex business logic from data access concerns. While it may introduce more boilerplate compared to simpler patterns like Active Record, it pays dividends in modularity, testability, and alignment with modern software architecture practices.

# References
1. Martin Fowler - _Patterns of Enterprise Application Architecture_ ([https://martinfowler.com/eaaCatalog/dataMapper.html](https://martinfowler.com/eaaCatalog/dataMapper.html))
2. Domain-Driven Design by Eric Evans
3. SQLAlchemy Documentation - [https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html#imperative-mapping](https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html#imperative-mapping)
4. MyBatis Data Mapper Framework - [https://mybatis.org/mybatis-3/](https://mybatis.org/mybatis-3/)
5. Dapper Micro ORM - [https://github.com/DapperLib/Dapper](https://github.com/DapperLib/Dapper)
