---
title: Data Structures - Stacks
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents 🔖</summary>

- [Intro #](#intro-)
- [Operations](#operations)
- [Code](#code)
- [A **real-world** example is...](#a-real-world-example-is)

</details>

---

# Intro [#](https://www.techtarget.com/whatis/definition/stack)

Commonly used in algorithms such as depth-first search, expression evaluation, and backtracking. *A stack stores a collection of items in the linear order* that operations are applied. The order is generaly reffered as **Last-in-Fisrt-Out ([`LIFO`](lifo_fifo.md))**. You can relate as a pile of plates, one on top of another.
> could be first in, first out ([FIFO](https://www.techtarget.com/whatis/definition/FIFO-first-in-first-out))?

# Operations

Include **push**, **pop**, **peek**, and **is_empty**.

 - `is_empty()` operation is used to check if the stack is empty. `O(1)`
 - `push(value)` operation is used to add an element to the top of the stack. `O(1)`
 - `pop()` operation is used to remove the top element from the stack. `O(1)`
 - `peek()` operation is used to view the top element without removing it. `O(1)`
 - `size()` returns the current size of the Stack. `O(1)`

# Code

In pure `C` we need to create every method as a function that will be called in `main()`. Please see the [full code](stack_implementation.c).
Other difference the need to create the space in the memory before allocating the element.

```c
// Stack implementation in C
// [...]
// Main
int	main()
{
	int ch;
	st *s = (st *)malloc(sizeof(st));

	createEmptyStack(s);

	push(s, 1);
	push(s, 2);
	push(s, 3);
	push(s, 4);

	printStack(s);

	pop(s);

	printf("\nAfter popping out\n");
	printStack(s);
}
```

For Python is quite simpler:

```python
class Stack:  
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[-1]
	def is_empty(self):
		return len(self.items) == 0
```

# A **real-world** example is...
- an `undo / redo` feature, that stores a stack list of every action or command executed and in a moment of need, the program can retrive the steps in a reverse order 
- to do a backtrack, like a make solve program that count the steps taken if it hits a dead end. 
