---
title: Sorting Algorithms
tags: studies, programação
use: Documentation, Algorithms
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Sorting](#sorting)
  - [Python’s Built-In Sorting Algorithm #](#pythons-built-in-sorting-algorithm-)
  - [The Bubble Sort Algorithm #](#the-bubble-sort-algorithm-)
    - [Analyzing the Strengths and Weaknesses of Bubble Sort #](#analyzing-the-strengths-and-weaknesses-of-bubble-sort-)
  - [The Insertion Sort Algorithm #](#the-insertion-sort-algorithm-)
    - [Analyzing the Strengths and Weaknesses of Insertion Sort #](#analyzing-the-strengths-and-weaknesses-of-insertion-sort-)
  - [The Merge Sort Algorithm #](#the-merge-sort-algorithm-)
    - [Analyzing the Strengths and Weaknesses of Merge Sort #](#analyzing-the-strengths-and-weaknesses-of-merge-sort-)
  - [The Quicksort Algorithm #](#the-quicksort-algorithm-)
    - [Analyzing the Strengths and Weaknesses of Quicksort #](#analyzing-the-strengths-and-weaknesses-of-quicksort-)
  - [The Timsort Algorithm #](#the-timsort-algorithm-)
    - [Analyzing the Strengths and Weaknesses of Timsort #](#analyzing-the-strengths-and-weaknesses-of-timsort-)
- [References](#references)

</details>

---

# Sorting

is a basic building block that many other algorithms are built upon. It’s related to several exciting ideas that you’ll see throughout your programming career. Understanding how sorting algorithms in Python work behind the scenes is a fundamental step toward implementing correct and efficient algorithms that solve real-world problems.

You can use sorting to solve a wide range of problems:

- **Searching:** Searching for an item on a [list](https://realpython.com/python-lists-tuples/) works much faster if the list is sorted.
- **Selection:** Selecting items from a list based on their relationship to the rest of the items is easier with sorted data. For example, finding the _kth_-largest or smallest value, or finding the median value of the list, is much easier when the values are in ascending or descending order.
- **Duplicates:** Finding duplicate values on a list can be done very quickly when the list is sorted.
- **Distribution:** Analyzing the frequency distribution of items on a list is very fast if the list is sorted. For example, finding the element that appears most or least often is relatively straightforward with a sorted list.

## Python’s Built-In Sorting Algorithm [#](https://realpython.com/sorting-algorithms-python//#pythons-built-in-sorting-algorithm "Permanent link")

The Python language, like many other high-level programming languages, offers the ability to sort data out of the box using `sorted()`. Here’s an example of sorting an integer array:

```python
>>> array = [8, 2, 6, 4, 5]
>>> sorted(array)
### [2, 4, 5, 6, 8]
```

You can use `sorted()` to sort any list as long as the values inside are comparable.

> **Note:** For a deeper dive into how Python’s built-in sorting functionality works, check out [How to Use sorted() and sort() in Python](https://realpython.com/python-sort/) and [Sorting Data With Python](https://realpython.com/courses/python-sorting-data/).

## The [Bubble Sort Algorithm](algo_bubble_sort.md) [#](https://realpython.com/sorting-algorithms-python//#the-bubble-sort-algorithm-in-python "Permanent link")

**Bubble Sort** is one of the most straightforward sorting algorithms. Its name comes from the way the algorithm works: With every new pass, the largest element in the list “bubbles up” toward its correct position.

Bubble sort consists of making multiple passes through a list, comparing elements one by one, and swapping adjacent items that are out of order.

### Analyzing the Strengths and Weaknesses of Bubble Sort [#](https://realpython.com/sorting-algorithms-python//#analyzing-the-strengths-and-weaknesses-of-bubble-sort "Permanent link")

The main advantage of the bubble sort algorithm is its **simplicity**. It is straightforward to both implement and understand. This is probably the main reason why most computer science courses introduce the topic of sorting using bubble sort.

As you saw before, the disadvantage of bubble sort is that it is **slow**, with a runtime complexity of _O(n<sup>2</sup>)_. Unfortunately, this rules it out as a practical candidate for sorting large arrays.

## The [Insertion Sort Algorithm](algo_insertion_sort.md) [#](https://realpython.com/sorting-algorithms-python//#the-insertion-sort-algorithm-in-python "Permanent link")

Like bubble sort, the **insertion sort** algorithm is straightforward to implement and understand. But unlike bubble sort, it builds the sorted list one element at a time by comparing each item with the rest of the list and inserting it into its correct position. This “insertion” procedure gives the algorithm its name.

An excellent analogy to explain insertion sort is the way you would sort a deck of cards. Imagine that you’re holding a group of cards in your hands, and you want to arrange them in order. You’d start by comparing a single card step by step with the rest of the cards until you find its correct position. At that point, you’d insert the card in the correct location and start over with a new card, repeating until all the cards in your hand were sorted.

### Analyzing the Strengths and Weaknesses of Insertion Sort [#](https://realpython.com/sorting-algorithms-python//#analyzing-the-strengths-and-weaknesses-of-insertion-sort "Permanent link")

Just like bubble sort, the insertion sort algorithm is very uncomplicated to implement. Even though insertion sort is an _O(n<sup>2</sup>)_ algorithm, it’s also much more efficient in practice than other quadratic implementations such as bubble sort.

There are more powerful algorithms, including merge sort and Quicksort, but these implementations are recursive and usually fail to beat insertion sort when working on small lists. Some Quicksort implementations even use insertion sort internally if the list is small enough to provide a faster overall implementation. [**Timsort**](https://en.wikipedia.org/wiki/Timsort) also uses insertion sort internally to sort small portions of the input array.

That said, **insertion sort is not practical for large arrays, opening the door to algorithms that can scale in more efficient ways**.

## The [Merge Sort Algorithm](algo_merge_sort.md) [#](https://realpython.com/sorting-algorithms-python//#the-merge-sort-algorithm-in-python "Permanent link")

**Merge sort** is a very efficient sorting algorithm. It’s based on the [divide-and-conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm) approach, a powerful algorithmic technique used to solve complex problems.

To properly understand divide and conquer, you should first understand the concept of [**recursion**](./recursion.md). Recursion involves breaking a problem down into smaller subproblems until they’re small enough to manage. In programming, recursion is usually expressed by a function calling itself.

> **Note**: This tutorial doesn’t explore recursion in depth. To better understand how recursion works and see it in action using Python, check out [Thinking Recursively in Python](https://realpython.com/python-thinking-recursively/) and [Recursion in Python: An Introduction](https://realpython.com/python-recursion/).

Divide-and-conquer algorithms typically follow the same structure:

1.  The original input is broken into several parts, each one representing a subproblem that’s similar to the original but simpler.
2.  Each subproblem is solved recursively.
3.  The solutions to all the subproblems are combined into a single overall solution.

In the case of merge sort, the divide-and-conquer approach divides the set of input values into two equal-sized parts, sorts each half recursively, and finally merges these two sorted parts into a single sorted list.

### Analyzing the Strengths and Weaknesses of Merge Sort [#](https://realpython.com/sorting-algorithms-python//#analyzing-the-strengths-and-weaknesses-of-merge-sort "Permanent link")

Thanks to its runtime complexity of _O(n log<sub>2</sub>n)_, merge sort is a very efficient algorithm that scales well as the size of the input array grows. It’s also straightforward to [**parallelize**](https://en.wikipedia.org/wiki/Parallel_algorithm) because it breaks the input array into chunks that can be distributed and processed in parallel if necessary.

That said, for small lists, the time cost of the recursion allows algorithms such as bubble sort and insertion sort to be faster. For example, running an experiment with a list of ten elements results in the following times:

```powershell
Algorithm: bubble_sort. Minimum execution time: 0.000018774999999998654
Algorithm: insertion_sort. Minimum execution time: 0.000029786000000000395
Algorithm: merge_sort. Minimum execution time: 0.00016983000000000276
```

Both bubble sort and insertion sort beat merge sort when sorting a ten-element list.

Another drawback of merge sort is that it creates copies of the array when calling itself recursively. It also creates a new list inside `merge()` to sort and return both input halves. This makes merge sort use much more memory than bubble sort and insertion sort, which are both able to sort the list in place.

Due to this limitation, you may not want to use merge sort to sort large lists in memory-constrained hardware.

## The [Quicksort Algorithm](algo_quicksort.md) [#](https://realpython.com/sorting-algorithms-python//#the-quicksort-algorithm-in-python "Permanent link")

Just like merge sort, the **Quicksort** algorithm applies the divide-and-conquer principle to divide the input array into two lists, the first with small items and the second with large items. The algorithm then sorts both lists recursively until the resultant list is completely sorted.

Dividing the input list is referred to as **partitioning** the list. Quicksort first selects a `pivot` element and partitions the list around the `pivot`, putting every smaller element into a `low` array and every larger element into a `high` array.

Putting every element from the `low` list to the left of the `pivot` and every element from the `high` list to the right positions the `pivot` precisely where it needs to be in the final sorted list. This means that the function can now recursively apply the same procedure to `low` and then `high` until the entire list is sorted.

### Analyzing the Strengths and Weaknesses of Quicksort [#](https://realpython.com/sorting-algorithms-python//#analyzing-the-strengths-and-weaknesses-of-quicksort "Permanent link")

True to its name, Quicksort is _very fast_. Although its worst-case scenario is theoretically _O(n<sup>2</sup>)_, in practice, a good implementation of Quicksort beats most other sorting implementations. Also, just like merge sort, Quicksort is straightforward to **parallelize**.

One of Quicksort’s main disadvantages is the lack of a guarantee that it will achieve the average runtime complexity. Although worst-case scenarios are rare, certain applications can’t afford to risk poor performance, so they opt for algorithms that stay within _O(n log<sub>2</sub>n)_ regardless of the input.

Just like merge sort, Quicksort also trades off memory space for speed. This may become a limitation for sorting larger lists.

A quick experiment sorting a list of ten elements leads to the following results:

```powershell
Algorithm: bubble_sort. Minimum execution time: 0.0000909000000000014
Algorithm: insertion_sort. Minimum execution time: 0.00006681900000000268
Algorithm: quicksort. Minimum execution time: 0.0001319930000000004
```

The results show that Quicksort also pays the price of recursion when the list is sufficiently small, taking longer to complete than both insertion sort and bubble sort.

## The [Timsort Algorithm](algo_timsort.md) [#](https://realpython.com/sorting-algorithms-python//#the-timsort-algorithm-in-python "Permanent link")

The **Timsort** algorithm is considered a **hybrid** sorting algorithm because it employs a best-of-both-worlds combination of insertion sort and merge sort. Timsort is near and dear to the Python community because it was created by Tim Peters in 2002 to be used as the [standard sorting algorithm of the Python language](https://en.wikipedia.org/wiki/Timsort).

The main characteristic of Timsort is that it takes advantage of already-sorted elements that exist in most real-world datasets. These are called **natural runs**. The algorithm then iterates over the list, collecting the elements into runs and merging them into a single sorted list.

### Analyzing the Strengths and Weaknesses of Timsort [#](https://realpython.com/sorting-algorithms-python//#analyzing-the-strengths-and-weaknesses-of-timsort "Permanent link")

The main disadvantage of Timsort is its complexity. Despite implementing a very simplified version of the original algorithm, it still requires much more code because it relies on both `insertion_sort()` and `merge()`.

One of Timsort’s advantages is its ability to predictably perform in _O(n log<sub>2</sub>n)_ regardless of the structure of the input array. Contrast that with Quicksort, which can degrade down to _O(n<sup>2</sup>)_. Timsort is also very fast for small arrays because the algorithm turns into a single insertion sort.

For real-world usage, in which it’s common to sort arrays that already have some preexisting order, Timsort is a great option. Its adaptability makes it an excellent choice for sorting arrays of any length.


---

# References

- https://realpython.com/sorting-algorithms-python 
- CS50x 2023 - Week3
- https://github.com/python/cpython