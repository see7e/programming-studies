---
title: Data Structures - Queues
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents 🔖</summary>

- [Intro #](#intro-)
- [Operations](#operations)
- [Types](#types)
	- [Simple Queue](#simple-queue)
	- [Circular Queue](#circular-queue)
	- [Priority Queue](#priority-queue)
	- [Double Ended Queue](#double-ended-queue)
- [Code](#code)
- [A **real-world** example is...](#a-real-world-example-is)

</details>

---

# Intro [#](https://www.techtarget.com/whatis/definition/queue)

Commonly used in algorithms such as breadth-first search, scheduling, and simulations. *A queue stores a collection of items like a stack*; however, **the operation order can only be first in, first out (*FIFO*)**. You can relate as a row of people to buy some tickets, the first to arrive is the first to leave.
https://www.programiz.com/dsa

# Operations 

The basic operations that can be performed on a queue include **enqueue**, **dequeue**, **peek**, and **is_empty**.
- `enqueue()` operation is used to add an element to the back of the queue. `O()`
- `dequeue()` operation is used to remove the front element from the queue. `O()`
- `peek()` now sees the **first** element. `O()`
- `size()`: returns the size of the Queue. `O()`
- `isEmpty()`: check if the queue is empty. `O()`
- `isFull()`: check if the queue is full. `O()`

# Types

There are four different types of queues:

## Simple Queue
## Circular Queue
## Priority Queue
## Double Ended Queue

# Code

In pure `C` we need to create every method as a function that will be called in `main()`. Please see the [full code](queue_implementation.c).

```c
// Queue implementation in C
// [...]
// Main
int main()
{
  // Try to deQueue from an empty queue.
  deQueue();
  // Enqueue 5 elements to the queue.
  enQueue(1);
  enQueue(2);
  enQueue(3);
  enQueue(4);
  enQueue(5);
  // Try to enqueue a 6th element, which won't be possible because the queue is full.
  enQueue(6);
  // Display the elements of the queue.
  display();
  // Dequeue the first element from the queue, which is 1.
  deQueue();
  // Display the updated elements of the queue.
  display();
  // Return 0 to indicate successful execution of the program.
  return (0);
}
```

To create a Queue in Python is "simpler":

```python
class Queue:  
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.append(item)
	def dequeue(self):
		return self.items.pop(0)
	def peek(self):
		return self.items[0]
	def is_empty(self):
		return len(self.items) == 0
```

# A **real-world** example is...
- an application that handles booking reservations, or tickets, each new ticket enters in a line of precedence.
