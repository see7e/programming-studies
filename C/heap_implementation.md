---
title: C - Heap - Implementation
tags: studies, programação
use: Documentation
languages: C
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Code File #](#code-file-)
- [Explanation](#explanation)
- [Found in Programiz](#found-in-programiz)

</details>

---

# Code File [#](./code/heap.c)
> ChatGPT powered

Upon reviewing the [code](#found-in-programiz), I have identified several bugs in the provided Max-Heap implementation:

-   In the `heapify` function, the parameter `size` is used both as a function parameter and as a global variable. This can lead to confusion and incorrect results. It's recommended to remove the global variable `size` and use the function parameter `size` consistently throughout the code.
    
-   The `insert` function does not handle the case when the heap is already full. It assumes that the array has a maximum capacity of 10 elements. To fix this, you can add a check to ensure the heap is not full before inserting a new element.
    
-   In the `deleteRoot` function, the loop variable `i` is reused in the inner loop without declaring it again. This can cause unexpected behavior and should be avoided. It's better to use a different variable name for the inner loop.
    
-   The `deleteRoot` function performs a linear search to find the element to be deleted. This approach has a time complexity of O(n), where n is the size of the heap. Since the Max-Heap structure can be optimized to provide a time complexity of O(log n) for deletion, it's recommended to modify the implementation to achieve this complexity.
    
-   The `printArray` function is using the global variable `size`, which is not updated correctly in the `deleteRoot` function. As mentioned before, it's better to use the function parameter `size` consistently to avoid confusion and incorrect results.
    
-   In the `main` function, the `size` variable is not initialized before calling the `insert` function. This can lead to unpredictable behavior. It's better to initialize `size` to 0 before inserting elements into the heap.

# Explanation
> ChatGPT powered

```c
#include <stdio.h>

// Function to swap two elements
void swap(int *a, int *b) {
    int temp = *b;
    *b = *a;
    *a = temp;
}
```

This part of the code defines a function called `swap` that helps us swap the positions of two numbers.

```c
// Function to heapify a subtree rooted at index i
void heapify(int array[], int size, int i) {
    int largest = i;
    int l = 2 * i + 1; // Calculate index of left child
    int r = 2 * i + 2; // Calculate index of right child

    // Check if left child is larger than the current largest element
    if (l < size && array[l] > array[largest])
        largest = l;

    // Check if right child is larger than the current largest element
    if (r < size && array[r] > array[largest])
        largest = r;

    // If the largest element is not the current root, swap them and recursively heapify the affected subtree
    if (largest != i) {
        swap(&array[i], &array[largest]);
        heapify(array, size, largest);
    }
}
```

This part of the code defines a function called `heapify` that helps us maintain a special order called "Max-Heap." It takes an array of numbers and makes sure that if we consider a particular number as the "root" of a tree, the numbers below it are smaller than the root. It does this by checking the left and right child of the current root and swapping them if necessary. Then, it recursively calls itself to check if the swapped child becomes a new root and continues this process until the entire tree is a Max-Heap.

```c
// Function to insert a new element into the heap
void insert(int array[], int* size, int newNum) {
    // Check if the heap is already full
    if (*size == 10) {
        printf("Heap is full. Cannot insert element.\n");
        return;
    }

    int i = *size;
    array[i] = newNum;
    *size += 1;

    // Rearrange the elements of the heap to maintain the Max-Heap property
    for (int j = i; j > 0; j = (j - 1) / 2) {
        int parent = (j - 1) / 2;
        if (array[j] > array[parent]) {
            swap(&array[j], &array[parent]);
        } else {
            break;
        }
    }
}
```

This part of the code defines a function called `insert` that allows us to add a new number to the Max-Heap. It checks if there is space in the heap (we can only have 10 numbers in our example) and if there is space, it adds the new number to the heap. Then, it rearranges the numbers to maintain the Max-Heap property, which means making sure that the new number is in the right position compared to its parent and other elements.

```c
// Function to delete the root element of the heap
void deleteRoot(int array[], int* size) {
    // Check if the heap is already empty
    if (*size == 0) {
        printf("Heap is empty. Cannot delete root.\n");
        return;
    }

    int root = array[0];
    array[0] = array[*size - 1];
    *size -= 1;

    // Rearrange the elements of the heap to maintain the Max-Heap property
    heapify(array, *size, 0);
    printf("Deleted root element: %d\n", root);
}
```
This part of the code defines a function called `deleteRoot` that allows us to remove the largest number (root) from the Max-Heap. It checks if there are any numbers in the heap, and if there are, it removes the root element. Then, it rearranges the other elements to maintain the Max-Heap property.

```c
// Function to print the elements of the heap array
void printArray(int array[], int size) {
    for (int i = 0; i < size; ++i)
        printf("%d ", array[i]);
    printf("\n");
}
```

This part of the code defines a function called `printArray` that helps us display all the numbers in the heap array.

```c
int main() {
    int array[10];
    int size = 0;

    // Insert elements into the heap
    insert(array, &size, 3);
    insert(array, &size, 4);
    insert(array, &size, 9);
    insert(array, &size, 5);
    insert(array, &size, 2);

    printf("Max-Heap array: ");
    printArray(array, size);

    // Delete the root element of the heap
    deleteRoot(array, &size);

    printf("After deleting the root element: ");
    printArray(array, size);

    return 0;
}
```

This part of the code is the main program. It creates an empty array and a variable to keep track of the size of the heap. Then, it inserts some numbers into the heap using the `insert` function and prints the resulting Max-Heap. After that, it deletes the root element using the `deleteRoot` function and displays the Max-Heap again.

Overall, the code allows us to create a Max-Heap, add numbers to it, remove the largest number, and see the result at each step.

# Found in [Programiz](https://www.programiz.com/dsa/heap-data-structure#c-code)

```c
// Max-Heap data structure in C

#include <stdio.h>
int size = 0;
void swap(int *a, int *b)
{
  int temp = *b;
  *b = *a;
  *a = temp;
}
void heapify(int array[], int size, int i)
{
  if (size == 1)
  {
    printf("Single element in the heap");
  }
  else
  {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    if (l < size && array[l] > array[largest])
      largest = l;
    if (r < size && array[r] > array[largest])
      largest = r;
    if (largest != i)
    {
      swap(&array[i], &array[largest]);
      heapify(array, size, largest);
    }
  }
}
void insert(int array[], int newNum)
{
  if (size == 0)
  {
    array[0] = newNum;
    size += 1;
  }
  else
  {
    array[size] = newNum;
    size += 1;
    for (int i = size / 2 - 1; i >= 0; i--)
    {
      heapify(array, size, i);
    }
  }
}
void deleteRoot(int array[], int num)
{
  int i;
  for (i = 0; i < size; i++)
  {
    if (num == array[i])
      break;
  }

  swap(&array[i], &array[size - 1]);
  size -= 1;
  for (int i = size / 2 - 1; i >= 0; i--)
  {
    heapify(array, size, i);
  }
}
void printArray(int array[], int size)
{
  for (int i = 0; i < size; ++i)
    printf("%d ", array[i]);
  printf("\n");
}
int main()
{
  int array[10];

  insert(array, 3);
  insert(array, 4);
  insert(array, 9);
  insert(array, 5);
  insert(array, 2);

  printf("Max-Heap array: ");
  printArray(array, size);

  deleteRoot(array, 4);

  printf("After deleting an element: ");

  printArray(array, size);
}
```