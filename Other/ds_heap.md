---
title: Data Structures - Heaps
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Intro #](#intro-)
- [Opearations](#opearations)
- [Crucial Terms](#crucial-terms)
- [Strengths and Weaknesses](#strengths-and-weaknesses)
	- [Strengths](#strengths)
	- [Weaknesses](#weaknesses)
- [Funcrions](#funcrions)
	- [Heapify](#heapify)
- [In Interviews, Use Heaps When ...](#in-interviews-use-heaps-when-)

</details>

---

# Intro [#](https://www.techtarget.com/whatis/definition/heap)

<details> <summary>Implementations</summary>

[`C`](../C/heap_implementation.md) | [`Python`](../PYTHON/heap_implementation.md) | [`JavaScript`](../Front_End/JS/heap_implementation.md)

</details>

Heap data structure is [a complete binary tree](#binary-tree) [#](https://www.programiz.com/dsa/complete-binary-tree) that satisfies **the heap property**, where any given node is:

-   always greater than its child node/s and the key of the root node is the largest among all other nodes. This property is also called **max heap property**.
	<img src="https://www.programiz.com/sites/tutorial2program/files/maxheap_1.png" alt="Max-heap" style="background-color:white" width="300">
-   always smaller than the child node/s and the key of the root node is the smallest among all other nodes. This property is also called **min heap property**.
	<img src="https://www.programiz.com/sites/tutorial2program/files/minheap_0.png" alt="Min-heap" style="background-color:white" width="300">

# Opearations

- Heapify `O(n)`
- Insert Element `O(log n)`
- Delete Element `O(n)`
- Peek (Find max/min) `O(1)`
- Extract-Max/Min `O(log n)`

# Crucial Terms

-   **key:** The values that determine the order. If you're storing numbers, the numbers can be the keys. If you're storing more complicated objects, the key is the data field that we're comparing by. Unlike in hash tables, keys in heaps do **not** have to be unique.

-   **extract\_min:** The method of (quickly) being able to extract the minimum element from the min-heap.

# Strengths and Weaknesses

## Strengths

-   A min-heap is able to quickly extract the minimum value on the heap. Repeated extractions from a min-heap into an array will yield a sorted array.
    

## Weaknesses

-   There's no convenient way of searching for a particular `key` value in a heap. Entries are only partially ordered; clever use of the heap property can allow for some pruning of searches.
    

# Funcrions

## Heapify

Heapify is the process of creating a heap data structure from a binary tree. It is used to create a Min-Heap or a Max-Heap.

1. Let the input array be

| 0   | 1   | 2   | 3   | 4   | 5   |
| --- | --- | --- | --- | --- | --- |
| 3   | 9   | 2   | 1   | 4   | 5   |

1. Create a complete binary tree from the array
	<img src="https://www.programiz.com/sites/tutorial2program/files/completebt-1_0.png" alt="Complete binary tree" style="background-color:white" width="300">
	
2. Start from the first index of non-leaf node whose index is given by n/2 - 1.
	<img src="https://www.programiz.com/sites/tutorial2program/files/start_1.png" alt="start from the first on leaf node" style="background-color:white" width="300">

4.   Set current element `i` as `largest`.

5.   The index of left child is given by `2i + 1` and the right child is given by `2i + 2`.  
    If `leftChild` is greater than `currentElement` (i.e. element at `ith` index), set `leftChildIndex` as largest.  
    If `rightChild` is greater than element in `largest`, set `rightChildIndex` as `largest`.

6.   Swap `largest` with `currentElement`
	<img src="https://www.programiz.com/sites/tutorial2program/files/swap_1.png" alt="swap if necessary" style="background-color:white" width="300">

7.   Repeat steps 3-7 until the subtrees are also heapified.

# In Interviews, Use Heaps When ...

- Heap is used while implementing a priority queue.
- Dijkstra's Algorithm
- Heap Sort

Heaps are designed to do one specific thing well, so the answer to _when you should use a heap_ is repetitive: You use one when you have to do repeated minimum (or maximum) extractions. The problems where you would want to do this might look quite different from each other, however. Below we have selected some examples of common interview questions that benefit from heaps.

-   **Finding the minimum distance between two nodes in a graph:** The standard approach to this problem is to use Dijkstra's algorithm. One of the key steps in Dijkstra's algorithm is to select the node closest to a node that you have already completed, which is a minimum calculation.

-   **Getting the next event that is scheduled to occur:** Storing events in a heap with a timestamp as the key gives you a fast way to extract the next event (the event with the smallest timestamp will occur next).

-   **Keep track of the median value while streaming:** This is the running median problem, where two heaps are maintained: a max-heap for values below the current median and a min-heap for values above the current median. When a new value is inserted, it is placed in the low or high pile as appropriate (and the maximum of the low values or minimum of the low values are extracted as necessary to keep the two heaps sizes' different by at most one element).

-   **Find the first `k` non-repeating characters in a string in a single traversal.**
