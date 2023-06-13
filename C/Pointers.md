---
title: Pointers
tags: studies, programação
use: Documentation
languages: C
dependences: NULL
---

# Pointers [#](https://pt.wikipedia.org/wiki/Ponteiro_(programa%C3%A7%C3%A3o))

Are variables in which are stored in the program's memory. A pointer could be use to access the content of a variable receiving (by pointing to) the memory address or even modify the content.

In C, the declaration of a pointer is done using the `*` operator. The type of the pointer must be the same of the pointee (the data or object referenced by a pointer). For example, if we want to declare a pointer to an integer, we can do it as follows:

```c
int *ptr;
```

In this example, `ptr` is a pointer to an integer. It can be initialized with the memory address of a variable of type int using the `&` operator. For example:

```c
int n = 10;
int *ptr = &n;
```

In this case, the pointer `ptr` is being initialized with the memory address of the variable `n`. This allows accessing and modifying the content of the variable `n` through the pointer `ptr`.

To access the content of the variable pointed to by a pointer, we use the `*` operator. This is called **dereferencing**. For example:

```c
int n = 10;
int *ptr = &n;
printf("The value of n is: %d\n", *ptr);
```

In this example, the `*` operator is used to access the content of the variable `n` through the pointer `ptr`. The result of executing this code will be the printing of the following line: The value of `n` is: 10.

We can also use a pointer to modify the content of the variable pointed to by it. For example:

```c
int n = 10;
int *ptr = &n;
*ptr = 20;
printf("The value of n is: %d\n", n);
```

In this example, the value of the variable `n` is modified to `20` using the pointer `ptr`. This is done in line 3, where the content of the memory address pointed to by `ptr` is modified to the value `20`. In line 4, the value of the variable `n` is printed, which will now be `20`.

A problem that can occur is if you define a pointer and dereference it without initializing (pointing to a location). This can be done in two ways:

- Reserving memory space using `malloc()` or,
	```c
	int *x;
	x = malloc(...);
	x* = 50;
	```

- Giving an used/existing memory address
	```c
	int *x = 7;
	int *y;
	
	y = x;
	y* = 42;
	printf("%i\n", y*);
	```

> Pointers are widely used in C to efficiently access and modify variables, especially in functions that need to manipulate large amounts of data. However, they can also be a source of errors and bugs, especially when used improperly. It is important to be careful when working with pointers and always verify that memory addresses are being manipulated correctly.

### Pointer to a String

Using pointers is useful to manage strings like copying, for this exists the `char* strcpy()` function (this is a special function, called [pointer function](#pointer-functions))

```c
char* strcpy(const char* src)
{
    // Allocate memory for another string with the same size of `src`
    char* t = malloc(strlen(src) + 1);
    
    // Copy string into memory, including '\0'
    for (int i = 0, n = strlen(src); i <= n; i++)
    {
        t[i] = src[i];
    }
    
    return t;
}
```

A pointer could be confused with an Array. They have a close relationship. Still, both are different concepts in C programming. A set of items stored in contiguous [memory](https://www.codingninjas.com/codestudio/library/main-memory) locations is called an [array](https://www.codingninjas.com/codestudio/library/introduction-to-array). In comparison, a variable whose value is the address of another variable is referred to as a pointer. 
> This blog will show the concept of arrays and pointers and the difference between [arrays and pointers.](https://www.codingninjas.com/codestudio/library/array-and-pointers)

## Double Pointers

A double pointer is a pointer that points to another pointer. In other words, it stores the memory address of another pointer. This is useful in situations where we need to modify the value of a pointer by reference, i.e., without modifying the original value of the variable pointed to by the pointer.

Example:

```c
#include <stdio.h>

int main() {
  int x = 10;
  int *p1 = &x; // pointer to x
  int **p2 = &p1; // pointer to p1

  printf("Value of x: %d\n", x);
  printf("Value of p1: %p\n", p1);
  printf("Value of p2: %p\n", p2);

  **p2 = 20; // modifying the value of x through p2

  printf("New value of x: %d\n", x);

  return 0;
}
```

A double pointer can be used to represent a matrix in C. This is because, in essence, a matrix in C is a contiguous block of memory, where each element is accessed using index notation.

To represent a matrix using double pointers, we can dynamically allocate a contiguous block of memory using the `malloc` function, which returns a pointer to the start of the allocated memory. Then, we can use double pointers to access the elements of the matrix, as if we were using index notation.

Example:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
  int **matrix;
  int i, j;

  // allocating memory for the matrix
  matrix = (int**) malloc(2 * sizeof(int*));
  for (i = 0; i < 2; i++) {
    matrix[i] = (int*) malloc(3 * sizeof(int));
  }

  // filling the matrix
  for (i = 0; i < 2; i++) {
    for (j = 0; j < 3; j++) {
      matrix[i][j] = i + j;
    }
  }

  // printing the matrix
  for (i = 0; i < 2; i++) {
    for (j = 0; j < 3; j++) {
      printf("%d ", matrix[i][j]);
    }
    printf("\n");
  }

  // freeing the allocated memory
  for (i = 0; i < 2; i++) {
    free(matrix[i]);
  }
  free(matrix);

  return 0;
}
```

In this example, we are dynamically allocating (using [`malloc()`](https://pt.wikipedia.org/wiki/Aloca%C3%A7%C3%A3o_din%C3%A2mica_de_mem%C3%B3ria_em_C)) a 2x3 matrix and filling its elements with simple values. Note that to access the elements of the matrix, we are using index notation through the double pointer `matrix[i][j]`. At the end of the program, we are freeing the allocated memory using the `free` function.

## Pointer Functions

Functions in C can receive pointers as arguments and can also return pointers. This is useful in situations where we need to pass a large amount of data to a function or when we want to dynamically allocate memory inside a function and return a pointer to that allocated memory.

Example:

```c
#include <stdio.h>
#include <stdlib.h>

void allocate_memory(int **p) {
  *p = (int*) malloc(sizeof(int));
}

int main() {
  int *p;

  allocate_memory(&p); // allocating memory inside the function

  *p = 10;

  printf("Value of p: %p\n", p);
  printf("Value pointed by p: %d\n", *p);

  free(p); // freeing the allocated memory

  return 0;
}
```

___