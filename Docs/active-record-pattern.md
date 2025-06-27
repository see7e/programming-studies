---
title: Active Record Pattern
tags:
  - studies
  - programming
  - design
  - design-patterns
  - architecture
  - active-record
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [Active Record Pattern](#active-record-pattern)
  - [What Is the Active Record Pattern?](#what-is-the-active-record-pattern)
    - [Example Conceptual Flow](#example-conceptual-flow)
  - [Core Characteristics](#core-characteristics)
  - [Benefits](#benefits)
  - [Drawbacks](#drawbacks)
  - [Use Cases \& When to Use](#use-cases--when-to-use)
  - [Related Concepts](#related-concepts)
  - [Frameworks That Use It](#frameworks-that-use-it)
- [References](#references)

</details>

---

# Active Record Pattern
Is a widely-used architectural approach that **==combines the data access logic and the domain model into a single object==**. It's straightforward, easy to use, and often the first encounter developers have with [Object-Relational Mapping (ORM)](orm.md).

## What Is the Active Record Pattern?
An **Active Record** is an object that:
- Represents a row in a database table
- Knows how to **persist** itself (save, update, delete)
- Often includes **business logic** along with persistence logic

### Example Conceptual Flow

```plaintext
[ Domain Object ] ⇄ [ Database Row ]
```

In code, this looks like:

```python
user = User.find(1)
user.name = "Alice"
user.save()
```

Here, `User` is not only a model but also manages its own persistence. There’s no need for a separate service to update the database — it’s baked in.

## Core Characteristics
- Combines **data** and **behavior** into one class
- Each object is tightly coupled with a single database table
- Offers simple, intuitive CRUD operations (Create, Read, Update, Delete)
- Often includes **validation**, **callbacks**, and **associations**

## Benefits
1. **Simplicity**: Ideal for small-to-medium applications and rapid prototyping.
2. **Reduced Boilerplate**: Fewer layers mean faster development.
3. **Developer Productivity**: High-level abstraction speeds up CRUD tasks.
4. **Community & Ecosystem**: Supported by many mature frameworks.

## Drawbacks
- **Tight Coupling**: Business logic is bound to persistence, making testing harder.
- **Scalability Limitations**: Difficult to maintain with complex domain logic.
- **Database-Centric Thinking**: Model design is driven by schema, not behavior or intent.
- **Difficult to Reuse**: Sharing logic across models often leads to duplication.

## Use Cases & When to Use

| Use Case                           | Active Record Recommended? |
| ---------------------------------- | -------------------------- |
| Prototyping or MVP                 | ✅ Yes                      |
| Simple CRUD applications           | ✅ Yes                      |
| Complex domain logic or aggregates | ❌ No                       |
| Cross-database operations          | ❌ No                       |

Active Record fits naturally in monoliths, admin dashboards, and standard web apps, but less so in distributed systems or rich domain models.

## Related Concepts
- **[Data Mapper Pattern](data-mapper-pattern.md)**: In contrast, separates persistence from domain logic.
- **Repository Pattern**: Often used to abstract persistence in complex apps — not usually needed with Active Record.
- **Service Layer**: Sometimes introduced to remove domain logic from Active Record models, though this *can get messy*.

## Frameworks That Use It
Many modern ORMs use or encourage Active Record:
- **Ruby on Rails** – `ActiveRecord`
- **Laravel** (PHP) – `Eloquent`
- **[Django](django-active_record-pattern.md)** (Python) – Model layer
- **Phoenix (Elixir)** – `Ecto` schemas (somewhat similar)

---

The Active Record pattern is a pragmatic and powerful tool — when used in the right context. It optimizes for speed and simplicity, not for architectural purity. As your system grows, it may be worth decoupling concerns via patterns like **Data Mapper**, **Repository**, or **Service Layers**.

Choose Active Record when your model _is_ your data — not when your model _does things_ beyond it.

# References
1. Martin Fowler - _Patterns of Enterprise Application Architecture_  
    [https://martinfowler.com/eaaCatalog/activeRecord.html](https://martinfowler.com/eaaCatalog/activeRecord.html)
2. Django Models - [https://docs.djangoproject.com/en/stable/topics/db/models/](https://docs.djangoproject.com/en/stable/topics/db/models/)
3. Ruby on Rails ActiveRecord - [https://guides.rubyonrails.org/active_record_basics.html](https://guides.rubyonrails.org/active_record_basics.html)
4. Laravel Eloquent ORM - [https://laravel.com/docs/eloquent](https://laravel.com/docs/eloquent)
5. "Architecture the Lost Years" - Uncle Bob Martin (on limitations of Active Record in complex domains)
