---
title: Architecture Principles
tags:
  - studies
  - programming
  - software-architecture
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [NEW INFO (#to\_review) # Application Architecture](#new-info-to_review--application-architecture)
  - [Service Layer](#service-layer)
    - [Helpers `vs` Service Layer](#helpers-vs-service-layer)
  - [Related Architectural Terms and Topics](#related-architectural-terms-and-topics)

</details>

---
# NEW INFO (#to_review) # Application Architecture

## Service Layer
A **Service Layer** is an architectural pattern that encapsulates business logic into discrete services. Each service handles a specific operation or use case, such as processing reservations or managing user notifications. This separation ensures that models focus solely on data representation and persistence, while views handle HTTP requests and responses.

### Helpers `vs` Service Layer
Handling some of the domain logic outside of the important modules and debloating them, this may resembles a simple helper file/function/class. But **a Service Layer is *not quite* the same as a helper**, although they *can seem similar* at a glance. Here's a breakdown of the difference:

| Aspect               | **Service Layer**                                             | **Helper**                                                  |
| -------------------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| **Purpose**          | Encapsulates business or application logic (use cases)        | Provides small, reusable utility functions                  |
| **Scope**            | Larger, focused on actions (e.g., "create user + send email") | Small, general-purpose (e.g., "slugify", "format_datetime") |
| **Examples**         | `create_order()`, `send_reset_email()`                        | `calculate_tax()`, `convert_currency()`                     |
| **Placement**        | Typically in `services/` or `usecases/` module                | Often in `utils/`, `helpers/`, or even inside a model/view  |
| **Responsibility**   | Coordinates domain entities, logic, and infrastructure        | Performs a stateless, specific function                     |
| **Test Granularity** | Tested for behavior and interaction                           | Tested for input-output correctness                         |

> [!TIP]
> ### Rule of Thumb
> **Helpers = small tools.**  
> **Service Layer = structured workflows.**
> 
> You *might* use helpers **inside** services, but services are not just helpers with a fancy name — they serve different architectural purposes.

## Related Architectural Terms and Topics
- **Domain-driven design (DDD)**: Service Layer is a key concept.
- **Domain Services** (in DDD, similar idea when logic doesn’t belong to one entity)
- **Use Case Layer** (aka Application Layer): Sometimes used as a synonym for Service Layer.
- **Utility Functions / Modules**
- **Manager Methods** (model-level encapsulation)
- **Fat models vs service layer**: Use models for simple domain logic, service layer for orchestration.
- **Command-Query Responsibility Segregation (CQRS)**: Commands (create/update) fit well into services.
- **Form handling and form services**: Complex form processing can live in services.
- **Signals vs Service Layer**: Signals are decoupled but hard to trace/debug. Services offer **explicit** logic flow.