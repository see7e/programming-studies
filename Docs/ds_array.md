---
title: Data Structures - Arrrays
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Arrays](#arrays)
	- [Code](#code)
	- [Operations](#operations)
- [Lists](#lists)
	- [Code](#code-1)
	- [Operations](#operations-1)

</details>

---

# Arrays

An array stores a collection of items at adjoining memory locations. Items that are the same type are stored together so the position of each element can be calculated or retrieved easily by an index. Arrays can be fixed or flexible in length depending of the language.

![Abstract array data structure diagram](https://cdn.ttgtmedia.com/rms/onlineimages/sqlserver-one_dimensional_array_four_elements-f_mobile.png)
> An array can hold a collection of integers, floating-point numbers, stings or even other arrays.

## Code

To define an Array in `C`:
```c
>>> int numbers[3] = {1, 2, 3};
```

But in some languages like `JavaScript`, the size of these elements can be mofified with the `.push()` method. Behind the scenes what the program will do is:
	1. Check if there's space for the new feature in the next block of memory. 
	2. If not possible,
		1. The program will allocate a new space in memory where the Array fits.
		2. Move all the features to each new space.
		3. Free the previous allocated space.
		4. Push (or append) the newly feature into the Array. 


For the Mixed Type Arrays, the program will verify the maximum length (bites) of the elements and alocate this amount of bits for the others.

```javascript
>>> const mixed = [true, 7, "druid"];
//			       1bite,2b, 5bites
```

The "problem" is that it will store more space in memory that it actually needs.

## Operations
- Add new element `O(n)`
- Remove element `O(n)`
- Accessing an element `O(1)`

# Lists
## Code
## Operations