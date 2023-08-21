---
title: Data Structures - Hash Tables
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents 🔖</summary>

- [Intro](#intro)
- [Hashing (Hash Function)](#hashing-hash-function)
	- [Good Hash Functions](#good-hash-functions)
- [Hash Collision](#hash-collision)
- [A **real-world** example is...](#a-real-world-example-is)

</details>

---

# Intro

<details> <summary>Implementations</summary>

[`C`](../C/HashTable_implementation.md) | [`Python`](HashTable_implementation.md) | [`JavaScript`](../Front_End/JS/HashTable_implementation.md)

</details>

A hash table -- *also known as a hash map, map, dictionary, associative array* -- stores a collection of items in an associative array that plots keys to values. A hash table uses a hash function to convert an index into an array of buckets that contain the desired data item.

![Hash table diagram](https://cdn.ttgtmedia.com/rms/onlineimages/sqlserver-hash_table_example-f_mobile.png)
> Hashing is a data structure technique where key values are converted into indexes of an array where the data is stored.

These are considered complex data structures as they can store large amounts of interconnected data.

**Operations**
- Search `O(1)`
- Insert `O(1)`
- Delete `O(1)`

https://www.programiz.com/dsa/hash-table

The Hash table data structure stores elements in key-value pairs where

-   **Key**\- unique integer that is used for indexing the values
-   **Value** - data that are associated with keys.

# Hashing (Hash Function)

Beneath the hood, there's and Array that will store the values of each key and to link the keys to it's related values a Hash Function will do the job. This process is called **hashing**.
It receives as input the key and returns the index value of the position in the Array. This process goes in a two way drive:
- To add a new element, the keys is passed to the function and it returns the position and modify along the given value. 
- If only the key is passed the function returns the index and the value of the element. 

**The function must always return the same value given the same key.**

Let k be a key and h(x) be a hash function.

Here, h(k) will give us a new index to store the element linked with k.

<img src="https://cdn.programiz.com/sites/tutorial2program/files/Hash-2_0.png" alt="Hash Table representation" style="background-color:white" width="500">

To learn more, visit [Hashing](https://www.programiz.com/dsa/hashing "Hashing").

## Good Hash Functions

A good hash function may not prevent the collisions completely however it can reduce their number.

Here, we will look into different methods to find a good hash function

1. Division Method
	If `k` is a key and `m` is the size of the hash table, the hash function `h()` is calculated as:
	`h(k) = k mod m`
	For example, If the size of a hash table is `10` and `k = 112` then `h(k) = 112` mod `10 = 2`. The value of `m` must not be the powers of `2`. This is because the powers of `2` in binary format are `10, 100, 1000, …`. When we find `k mod m`, we will always get the lower order p-bits.

	```
	if m = 22, k = 17, then h(k) = 17 mod 22 = 10001 mod 100 = 01
	if m = 23, k = 17, then h(k) = 17 mod 22 = 10001 mod 100 = 001
	if m = 24, k = 17, then h(k) = 17 mod 22 = 10001 mod 100 = 0001
	if m = 2p, then h(k) = p lower bits of m
	```

2. Multiplication Method
	`h(k) = ⌊m(kA mod 1)⌋`
	where,
	-   `kA mod 1` gives the fractional part `kA`,
	-   `⌊ ⌋` gives the floor value
	-   `A` is any constant. The value of `A` lies between 0 and 1. But, an optimal choice will be `≈ (√5-1)/2` suggested by Knuth.

3. Universal Hashing
	In Universal hashing, the hash function is chosen at random independent of keys.

# Hash Collision

When the hash function generates the same index for multiple keys, there will be a conflict (what value to be stored in that index). This is called a **hash collision.**

We can resolve the hash collision using one of the following techniques.

-   Collision resolution by chaining
-   Open Addressing: Linear/Quadratic Probing and Double Hashing


1. Collision resolution by chaining

	In chaining, if a hash function produces the same index for multiple elements, these elements are stored in the same index by using a doubly-linked list.
	
	If `j` is the slot for multiple elements, it contains a pointer to the head of the list of elements. If no element is present, `j` contains `NIL`.

	<img src="https://cdn.programiz.com/sites/tutorial2program/files/Hash-3_1.png" alt="chaining method used to resolve collision in hash table" style="background-color:white" width="500">
	> Collision Resolution using chaining
	
	**Pseudocode for operations**
	```
	chainedHashSearch(T, k)
	return T[h(k)]
	chainedHashInsert(T, x)
	T[h(x.key)] = x //insert at the head
	chainedHashDelete(T, x)
	T[h(x.key)] = NIL
	```

2. Open Addressing

	Unlike chaining, open addressing doesn't store multiple elements into the same slot. Here, each slot is either filled with a single key or left `NIL`.
	
	Different techniques used in open addressing are:
	
   1. Linear Probing
		In linear probing, collision is resolved by checking the next slot.
		$h(k, i) = (h′(k) + i) mod m$
		where:
		-   $i = {0, 1, ...}$
		-   $h'(k)$ is a new hash function
		If a collision occurs at $h(k, 0)$, then $h(k, 1)$ is checked. In this way, the value of `i` is incremented linearly.
		The problem with linear probing is that a cluster of adjacent slots is filled. When inserting a new element, the entire cluster must be traversed. This adds to the time required to perform operations on the hash table. 
	
	2. Quadratic Probing
		It works similar to linear probing but the spacing between the slots is increased (greater than one) by using the following relation.
		$h(k, i) = (h'(k) + c_1i + c_2i^2) mod (m)$
		where:
		-   $c_1$ and $c^2$ are positive auxiliary constants,
		-   $i = {0, 1, ...}$

	3. Double hashing
		If a collision occurs after applying a hash function $h(k)$, then another hash function is calculated for finding the next slot.
		$h(k, i) = (h_1(k) + ih_2(k)) mod (m)$

# A **real-world** example is...
- phone books or dictionaries.

