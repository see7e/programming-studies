---
title: Python - Heap - Implementation
tags: studies, programação
use: Documentation
languages: Python
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Code File #](#code-file-)
- [Explanation](#explanation)
  - [Section 1:](#section-1)
  - [Section 2:](#section-2)
  - [Section 3:](#section-3)
  - [Section 4:](#section-4)
- [Found in Programiz](#found-in-programiz)

</details>

---

# Code File [#](heap.py)
> ChatGPT powered

The [code](#found-in-programiz) provided seems to have a few issues. Here are the bugs I found:

1.  In the `insert` function, you have a semicolon (`;`) after `array.append(newNum)`. Python does not require semicolons to terminate statements, so you can remove it.
    
2.  In the `deleteNode` function, you have a redundant `i = 0` initialization before the loop. Since you're reusing the `i` variable in the loop, you don't need to initialize it again.
    
3.  When swapping elements in the `deleteNode` function, you're swapping `array[i]` with `array[size-1]`, but the correct swap should be with `array[size-1]`. Update that line to `array[i], array[size-1] = array[size-1], array[i]`.
    
4.  In the `deleteNode` function, after removing the element with `array.remove(num)`, you need to update the `size` variable by subtracting 1, because the size of the array has decreased.
    
5.  The `heapify` function is not defined correctly. The condition `arr[i] < arr[l]` should be `arr[largest] < arr[l]`, and the condition `arr[largest] < arr[r]` should be `arr[largest] < arr[r]`. Update these conditions accordingly.

# Explanation
> ChatGPT powered

## Section 1:

```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[largest] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

> This section defines a function called `heapify` that helps organize a list of numbers in a special way called a "heap." A heap is a binary tree-like structure where each parent node is greater than or equal to its child nodes. The function takes three inputs: the list of numbers (`arr`), the size of the list (`n`), and the index of the current element (`i`). It compares the current element with its left and right child elements to find the largest element. If the largest element is not the current element, it swaps them and calls the `heapify` function again on the swapped element. This process helps maintain the heap property.

## Section 2:

```python
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)

```

> This section defines a function called `insert` that adds a new number (`newNum`) to a list of numbers (`array`) and organizes the list as a heap. If the list is empty, it simply adds the new number. Otherwise, it adds the new number to the list and rearranges the list using the `heapify` function. It starts from the middle of the list and goes to the beginning, calling `heapify` on each element to maintain the heap property.

## Section 3:

```python
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
    
    array[i], array[size - 1] = array[size - 1], array[i]
    
    array.remove(num)
    size -= 1
    
    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)
```

> This section defines a function called `deleteNode` that removes a specific number (`num`) from a list of numbers (`array`) and rearranges the list as a heap. It starts by finding the position of the number in the list and swaps it with the last element. Then it removes the number from the list and adjusts the size of the list. After that, it rearranges the list using the `heapify` function to maintain the heap property.

## Section 4:

```python
arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
```

> This section creates an empty list called `arr`. It then adds numbers to the list using the `insert` function to create a special type of list called a "max-heap" where the largest number is at the top. The numbers are 3, 4, 9, 5, and 2. After that, it prints the list as a max-heap. Next, it uses the `deleteNode` function to remove the number 4 from the list and rearranges the list as a max-heap again. Finally, it prints the updated list after the deletion.
> 
> Overall, this code helps organize a list of numbers as a max-heap and allows adding or removing numbers while maintaining the max-heap property.

# Found in [Programiz](https://www.programiz.com/dsa/heap-data-structure#python-code)

```python
# Max-Heap data structure in Python

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
        
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)
    
arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
```