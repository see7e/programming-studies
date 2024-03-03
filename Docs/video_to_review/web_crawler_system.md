---
title: Web Crawler System Design
description: System design for a web crawler that scrapes and indexes web pages for search engines in the context of a 
date: 2021-10-20
tags:
    - web crawler
    - search engine
    - data mining
    - archiving
    - DNS resolution
    - caching
    - column-oriented databases
    - distributed file systems
    - Kafka
    - Redis Bloom
    - Memcached
    - server-side rendering
    - horizontal scaling
    - politeness
    - URL prioritization
    - modular services
    - image downloaders
    - analytic services
    - seed URLs
    - HTML fetcher
    - HTML parser
    - duplicate detection
    - URL extractor
    - URL Frontier
    - front queue prioritizer
    - back queue selector
    - server-side rendering
    - horizontal scaling
    - caching mechanisms
    - politeness
    - URL prioritization
    - modular services
    - image downloaders
    - analytic services
    - seed URLs
    - HTML fetcher
    - HTML parser
    - duplicate detection
    - URL extractor
    - URL Frontier
    - front queue prioritizer
    - back queue selector
    - server-side rendering
    - horizontal scaling
    - caching mechanisms
    - politeness
    - URL prioritization
    - modular services
    - image downloaders
    - analytic services
    - seed URLs
    - HTML fetcher
    - HTML parser
    - duplicate detection
    - URL extractor
    - URL Frontier
    - front queue prioritizer
    - back queue selector
    - server-side rendering
    - horizontal scaling
    - caching mechanisms
    - politeness
    - URL prioritization
    - modular services
    - image downloaders
    - analytic services
    - seed URLs
    - HTML fetcher
    - HTML parser
    - duplicate detection
    - URL extractor
    - URL Frontier
    - front queue prioritizer
    - back queue selector
    - server-side rendering
    - horizontal scaling
    - caching mechanisms
    - politeness
    - URL prioritization
    - modular services
    - image downloaders
    - analytic services
    - seed URLs
    - HTML fetcher
    - HTML parser
    - duplicate detection
    - URL extractor
    - URL Frontier
    - front queue prioritizer
    - back queue selector
    - server-side rendering
    - horizontal scaling
    - caching


- [00:01](https://youtu.be/5DTxuMDYvNc?t=1s) 🕷️ Overview of WebCrawler System Design Question

  - A WebCrawler is crucial for tasks like indexing for search engines, data mining, and archiving.
  - Functional requirements include crawling related pages and avoiding duplicate pages.
  - Nonfunctional requirements involve prioritizing URLs and being polite to avoid overloading sites.

- [01:27](https://youtu.be/5DTxuMDYvNc?t=87s) 📊 Estimation and Storage Capacity Calculation

  - Understanding the amount of data to be stored monthly, yearly, and over several years.
  - Calculation of storage requirements based on average page size and monthly page count.
  - Conversion of storage needs into petabytes for scalability considerations.

- [03:04](https://youtu.be/5DTxuMDYvNc?t=184s) 🏗️ System Architecture Components

  - Exploring components like Seed URLs, HTML fetcher, HTML parser, and duplicate detection.
  - Consideration of scalable solutions for DNS resolution and caching.
  - Evaluation of storage options such as column-oriented databases and distributed file systems.

- [07:02](https://youtu.be/5DTxuMDYvNc?t=422s) 🔗 URL Extraction and Modular Services

  - Discussing the role of URL extractor and the potential use of Kafka for extensibility.
  - Importance of modular services like image downloaders and analytic services for system flexibility.
  - Utilizing tools like Redis Bloom and Memcached for implementing caching mechanisms.

- [09:19](https://youtu.be/5DTxuMDYvNc?t=559s) ⚙️ URL Frontier and Prioritization

  - Detailed explanation of URL prioritization and politeness in the URL Frontier.
  - Implementation of front queue prioritizer and back queue selector for prioritizing URLs.
  - Ensuring politeness by delaying requests and avoiding excessive requests to specific domains.

- [11:24](https://youtu.be/5DTxuMDYvNc?t=684s) 🔄 Recap and Additional Talking Points

  - Recap of the entire system architecture from seed URLs to URL Frontier.
  - Discussion of additional topics like server-side rendering, horizontal scaling, and caching mechanisms.
  - Suggestions for expanding the system with additional services for enhanced functionality.