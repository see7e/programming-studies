---
title: LIFO x FIFO
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

- [LIFO - Last in / First Out](#lifo---last-in--first-out)
- [FIFO - First in / First Out](#fifo---first-in--first-out)

# LIFO - Last in / First Out
Which means that the last element added to the stack is the first element to be removed. Therefore, the first element to be entered in this approach, gets out Last.

In computing, LIFO approach is used as a queuing theory that refers to the way items are stored in types of data structures. Time complexity of inserting element in LIFO is O(1). The data structure that implements LIFO is Stack.

## Where is LIFO used:
1.  **Data Structures:**  
    Certain data structures like Stacks and other variants of Stacks use LIFO approach for processing data.
2.  **Extracting latest information:**  
    Sometimes computers use LIFO when data is extracted from an array or data buffer. When it is required to get the most recent information entered, the LIFO approach is used.

## Complexity Analysis:
-   **Time Complexity: O(n)**
-   **Auxiliary Space: O(n)**

# FIFO - First in / First Out
It stands for First-In-First-Out approach in programming. In this, the new element is inserted below the existing element, So that the oldest element can be at the top and taken out first. Therefore, the first element to be entered in this approach, gets out First.

In computing, FIFO approach is used as an operating system algorithm, which gives every process CPU time in the order they arrive. Time complexity of inserting element in FIFO is O(1). The data structure that implements FIFO is Queue.

## Where is FIFO used:
1.  **Data Structures:**
    -   Certain data structures like Queue and other variants of Queue uses FIFO approach for processing data. 
2.  **Disk scheduling:**
    -   Disk controllers can use the FIFO as a disk scheduling algorithm to determine the order in which to service disk I/O requests. 
3.  **Communications and networking”**
    -   Communication network bridges, switches and routers used in computer networks use FIFOs to hold data packets en route to their next destination.

## Complexities Analysis:
-   **Time Complexity: O(N)**
-   **Space Complexity: O(N)**