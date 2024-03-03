---
title: Database Game Programming
description: Tyler Cloutier discusses the challenges of game programming and the development of SpaceTimeDB, a database designed for game development.
date: 2021-10-20
tags:
    - game development
    - database
    - SpaceTimeDB
    - MMO
    - RPG
    - client-server
    - synchronization
    - subscription
    - stored procedures
    - permissions
    - security
    - Rust
    - actor model
    - concurrency control
    - query engine
    - BitCraft
    - performance optimization
---


<iframe width="560" height="315" src="https://www.youtube.com/embed/roEsJcQYjd8?si=ViclD42S4zv5JeJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


- [00:00](https://www.youtube.com/watch?v=roEsJcQYjd8&t=0s) 🎮 Overview of Game Programming Challenges

  - Game programming faces similar issues as industrial programming but under harsher conditions.
  - Challenges include global networking, concurrency, massive data volumes, and low latency requirements.
  - Unique approaches are often taken to solve these problems.

- [02:49](https://www.youtube.com/watch?v=roEsJcQYjd8&t=169s) 🎓 Tyler Cloutier's Background and Role in Game Development

  - Tyler's background spans chemical engineering, computer science, and game development.
  - He worked in data science and engineering, focusing on player behavior prediction in games.
  - His experience includes handling data pipelines and building predictive models for game monetization.

- [04:42](https://www.youtube.com/watch?v=roEsJcQYjd8&t=282s) 💰 Monetization in Free-to-Play Games

  - Free-to-play games often rely on selling in-game speed-ups and upgrades.
  - Some players spend significant amounts, with reports of individuals spending millions of dollars.
  - Unique spending behaviors and motivations, including the desire to simulate power or form social connections, drive monetization.

- [07:28](https://www.youtube.com/watch?v=roEsJcQYjd8&t=448s) 📊 Challenges with Historical Data in Games

  - Traditional infrastructure struggles to capture and manage historical game data effectively.
  - Snapshots and event data streams provide incomplete and cumbersome solutions.
  - The Lambda architecture, combining batch and real-time processing, addresses historical data challenges.

- [10:43](https://www.youtube.com/watch?v=roEsJcQYjd8&t=643s) 🕹️ Introduction to SpaceTimeDB for Game Development

  - SpaceTimeDB is a database designed for game development, focusing on persistence.
  - It allows for storing and replaying detailed game states, including player movements and interactions.
  - The architecture simplifies game development by abstracting away distributed system complexities.

- [12:03](https://www.youtube.com/watch?v=roEsJcQYjd8&t=723s) 🌐 Challenges of Distributed Systems in Game Development

  - Games like BitCraft Online face challenges of managing a large, mutable, and persistent global state.
  - SpaceTimeDB addresses these challenges by providing a centralized database for all game data.
  - The approach simplifies game development and ensures data consistency across distributed environments.

- [15:17](https://www.youtube.com/watch?v=roEsJcQYjd8&t=917s) 💡 Implementation Details of SpaceTimeDB

  - SpaceTimeDB integrates directly with game clients, leveraging reducers to manipulate data on the server.
  - Client-side prediction enables smooth gameplay by anticipating server actions.
  - The system ensures data consistency and enables seamless synchronization between clients and the central database.

- [20:23](https://youtu.be/roEsJcQYjd8?t=1223s) 💣 Client-server interaction and reconciliation:

  - Explanation of client-server interaction in games.
  - Reconciliation process when client actions conflict with server updates.
  - Comparison to transactional processes on the client side.

- [21:21](https://youtu.be/roEsJcQYjd8?t=1281s) 🎮 Client-side simulation in games:

  - Different approaches to client-side simulation in games.
  - Deterministic simulation requiring total knowledge of game state.
  - Use cases for deterministic simulation in match-based games.

- [24:41](https://youtu.be/roEsJcQYjd8?t=1481s) 🌐 Server-client synchronization in MMOs:

  - Challenges of server-client synchronization in MMOs.
  - Overview of the typical architecture for MMOs.
  - Implications of baked-in client knowledge on server code complexity.

- [27:03](https://youtu.be/roEsJcQYjd8?t=1623s) 🔄 Subscription-based streaming architecture:

  - Description of Space Time DB's subscription-based streaming architecture.
  - Explanation of prefix consistency in client replicas.
  - Comparison to eventual consistency in traditional game servers.

- [29:40](https://youtu.be/roEsJcQYjd8?t=1780s) 💡 Unification of game and non-game applications:

  - Discussion on the similarities and differences between game and non-game architectures.
  - Importance of unifying backend systems for diverse applications.
  - Comparison to existing game engine frameworks like Unity and Unreal.

- [33:21](https://youtu.be/roEsJcQYjd8?t=2001s) 🚀 Performance considerations in transactional databases:

  - Addressing concerns about performance in transactional databases for real-time applications.
  - Comparison to existing database architectures like Times 10.
  - Flexibility in configuring durability and persistency guarantees at a per-subscriber level.

- [40:09](https://youtu.be/roEsJcQYjd8?t=2409s) 🎮 Subscribing to Data Updates in MMO RPGs

  - Subscribing to various data updates in MMO RPGs involves strategies like subscribing to piece positions, scores, or other relevant game states.
  - Developers typically utilize SQL queries to manage data subscriptions, leveraging techniques like semi-joins and union operations.
  - Game programming often requires a mix of SQL and coding, with modules typically written in languages like WebAssembly, supporting Rust and C-sharp.

- [43:32](https://youtu.be/roEsJcQYjd8?t=2612s) 🛠️ Improving Developer Experience with Stored Procedures

  - The developer experience with stored procedures can be enhanced by simplifying language syntax and improving management systems.
  - SpaceTimeDB focuses on developer experience by centralizing stored procedures in version-controlled repositories and simplifying permission management.
  - Emphasizing the importance of developer experience, SpaceTimeDB aims to streamline the process of database management and stored procedure implementation.

- [46:22](https://youtu.be/roEsJcQYjd8?t=2782s) 🛡️ Implementing Permissions and Security in SpaceTimeDB

  - SpaceTimeDB implements permissions for both read and write operations, ensuring data integrity and preventing unauthorized access.
  - Developers can define security rules using a general-purpose language like Rust, enabling fine-grained control over data access.
  - Security measures include write permissions for database updates, private tables, and future support for column and row-level security.

- [51:30](https://youtu.be/roEsJcQYjd8?t=3090s) 💻 Client-Side Programming in SpaceTimeDB

  - SpaceTimeDB facilitates server-side programming in Rust while offering a Rust SDK for client-side development.
  - Developers currently write server modules in Rust and interact with the database using provided SDK functions.
  - Future plans include enabling SpaceTimeDB to run on both server and client sides, allowing automatic synchronization and client-side prediction.

- [59:18](https://www.youtube.com/watch?v=roEsJcQYjd8&t=3558s) ⚙️ Actor Model and Concurrency Control

  - Actors in SpaceTimeDB are akin to units of processing.
  - Multi-version concurrency control enables running numerous transactions within a single actor, optimizing performance.
  - Maximizing the size of each actor before distributing them is crucial for efficiency.

- [01:00:13](https://www.youtube.com/watch?v=roEsJcQYjd8&t=3613s) 🔄 Building Subscription System and Query Engine

  - In implementing a system like SpaceTimeDB, building a subscription system is essential.
  - Actors need to be capable of sending relevant data upon subscription requests.
  - Developing a query engine for efficient data retrieval is a critical aspect of the system's architecture.

- [01:00:42](https://www.youtube.com/watch?v=roEsJcQYjd8&t=3642s) 🛠️ Accessing SpaceTimeDB and Future Developments

  - Users can access SpaceTimeDB for experimentation through the demo, Quick Start Guide, or testnet.
  - The testnet allows users to interact with a cloud-based version of SpaceTimeDB, offering a glimpse into future functionalities.
  - SpaceTimeDB's upcoming 1.0 release aims to provide a stable, reliable platform for application development.

- [01:02:35](https://www.youtube.com/watch?v=roEsJcQYjd8&t=3755s) 🚀 Integration with BitCraft and Performance Optimization

  - BitCraft, a game built on SpaceTimeDB, is already running on the testnet.
  - Performance optimization efforts are underway to ensure BitCraft can handle concurrent users effectively.
  - The upcoming BitCraft alpha release promises significant improvements in scalability and performance.
