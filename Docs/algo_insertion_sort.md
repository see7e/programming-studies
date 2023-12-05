---
title: Insertion Sort - Algorithm
tags: studies, programação
use: Documentation, Algorithms
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents 🔖</summary>

- [Implementing Insertion/Selection Sort #](#implementing-insertionselection-sort-)
- [Measuring Insertion Sort’s Big O Runtime Complexity #](#measuring-insertion-sorts-big-o-runtime-complexity-)
- [Timing Your Insertion Sort Implementation #](#timing-your-insertion-sort-implementation-)
- [Analyzing the Strengths and Weaknesses of Insertion Sort #](#analyzing-the-strengths-and-weaknesses-of-insertion-sort-)
- [References](#references)

</details>

---


# Implementing Insertion/Selection Sort [#](https://realpython.com/sorting-algorithms-python//#implementing-insertion-sort-in-python "Permanent link")

The insertion sort algorithm works exactly like the example with the deck of cards. Here’s the implementation in Python:

```embed-cpp
PATH: "vault://GAB/Estudos-Trabalhos/PROGRAMAÇÃO/programming-studies/Languages/Python/code/algo_insertion_sort.py"
TITLE: "Insertion.py"
```

<details> <summary>Or if you like a bit more intricate one, an implementation in `C`:</summary>

```embed-cpp
PATH: "vault://GAB/Estudos-Trabalhos/PROGRAMAÇÃO/programming-studies/Languages/C/code/algo_insertion_sort.c"
TITLE: "Insertion.c"
```

</details>

Unlike bubble sort, this implementation of insertion sort constructs the sorted list by pushing smaller items to the left. Let’s break down `insertion_sort()` line by line:

-   **Line 4** sets up the loop that determines the `key_item` that the function will position during each iteration. Notice that the loop starts with the second item on the list and goes all the way to the last item.

-   **Line 7** initializes `key_item` with the item that the function is trying to place.
   
-   **Line 12** initializes a variable that will consecutively point to each element to the left of `key item`. These are the elements that will be consecutively compared with `key_item`.
   
-   **Line 18** compares `key_item` with each value to its left using a `while` loop, shifting the elements to make room to place `key_item`.
   
-   **Line 27** positions `key_item` in its correct place after the algorithm shifts all the larger values to the right.
   
Here’s a figure illustrating the different iterations of the algorithm when sorting the array `[8, 2, 6, 4, 5]`:

![Insertion Sort Algorithm|500](https://files.realpython.com/media/python-sorting-algorithms-insertion-sort.a102f819b3d7.png)

The Insertion Sort Process

Now here’s a summary of the steps of the algorithm when sorting the array:

1.  The algorithm starts with `key_item = 2` and goes through the subarray to its left to find the correct position for it. In this case, the subarray is `[8]`.

2.  Since `2 < 8`, the algorithm shifts element `8` one position to its right. The resultant array at this point is `[8, 8, 6, 4, 5]`.
   
3.  Since there are no more elements in the subarray, the `key_item` is now placed in its new position, and the final array is `[2, 8, 6, 4, 5]`.
   
4.  The second pass starts with `key_item = 6` and goes through the subarray located to its left, in this case `[2, 8]`.
   
5.  Since `6 < 8`, the algorithm shifts 8 to its right. The resultant array at this point is `[2, 8, 8, 4, 5]`.
   
6.  Since `6 > 2`, the algorithm doesn’t need to keep going through the subarray, so it positions `key_item` and finishes the second pass. At this time, the resultant array is `[2, 6, 8, 4, 5]`.
   
7.  The third pass through the list puts the element `4` in its correct position, and the fourth pass places element `5` in the correct spot, leaving the array sorted.   

# Measuring Insertion Sort’s Big O Runtime Complexity [#](https://realpython.com/sorting-algorithms-python//#measuring-insertion-sorts-big-o-runtime-complexity "Permanent link")

Similar to your bubble sort implementation, the insertion sort algorithm has a couple of nested loops that go over the list. The inner loop is pretty efficient because it only goes through the list until it finds the correct position of an element. That said, the algorithm still has an **_O(n<sup>2</sup>)_** runtime complexity on the average case.

The worst case happens when the supplied array is sorted in reverse order. In this case, the inner loop has to execute every comparison to put every element in its correct position. This still gives you an _O(n<sup>2</sup>)_ runtime complexity.

The best case happens when the supplied array is already sorted. Here, the inner loop is never executed, resulting in an _O(n)_ runtime complexity, just like the best case of bubble sort.

Although bubble sort and insertion sort have the same Big O runtime complexity, in practice, insertion sort is considerably more efficient than bubble sort. If you look at the implementation of both algorithms, then you can see how insertion sort has to make fewer comparisons to sort the list.

# Timing Your Insertion Sort Implementation [#](https://realpython.com/sorting-algorithms-python//#timing-your-insertion-sort-implementation "Permanent link")

To prove the assertion that insertion sort is more efficient than bubble sort, you can time the insertion sort algorithm and compare it with the results of bubble sort. To do this, you just need to replace the call to `run_sorting_algorithm()` with the name of your insertion sort implementation:

```python
 1    if __name__ == "__main__":
 2    # Generate an array of `ARRAY_LENGTH` items consisting
 3    # of random integer values between 0 and 999
 4    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
 5
 6    # Call the function using the name of the sorting algorithm
 7    # and the array we just created
 8    run_sorting_algorithm(algorithm="insertion_sort", array=array)

```

You can execute the script as before:

```powershell
$ python sorting.py
Algorithm: insertion_sort. Minimum execution time: 56.71029764299999
```

Notice how the insertion sort implementation took around `17` fewer seconds than the bubble sort implementation to sort the same array. Even though they’re both _O(n<sup>2</sup>)_ algorithms, insertion sort is more efficient.

# Analyzing the Strengths and Weaknesses of Insertion Sort [#](https://realpython.com/sorting-algorithms-python//#analyzing-the-strengths-and-weaknesses-of-insertion-sort "Permanent link")

Just like bubble sort, the insertion sort algorithm is very uncomplicated to implement. Even though insertion sort is an _O(n<sup>2</sup>)_ algorithm, it’s also much more efficient in practice than other quadratic implementations such as bubble sort.

There are more powerful algorithms, including merge sort and Quicksort, but these implementations are recursive and usually fail to beat insertion sort when working on small lists. Some Quicksort implementations even use insertion sort internally if the list is small enough to provide a faster overall implementation. [**Timsort**](https://en.wikipedia.org/wiki/Timsort) also uses insertion sort internally to sort small portions of the input array.

That said, insertion sort is not practical for large arrays, opening the door to algorithms that can scale in more efficient ways.

# References

- https://www.geeksforgeeks.org/insertion-sort/