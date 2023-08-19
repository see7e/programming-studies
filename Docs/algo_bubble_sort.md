---
title: Bubble Sort - Algorithm
tags: studies, programação
use: Documentation, Algorithms
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Implementing Bubble Sort #](#implementing-bubble-sort-)
- [Measuring Bubble Sort’s Big O Runtime Complexity #](#measuring-bubble-sorts-big-o-runtime-complexity-)
- [Timing Your Bubble Sort Implementation #](#timing-your-bubble-sort-implementation-)
- [Analyzing the Strengths and Weaknesses of Bubble Sort #](#analyzing-the-strengths-and-weaknesses-of-bubble-sort-)
- [References](#references)

</details>

---

# Implementing Bubble Sort [#](https://realpython.com/sorting-algorithms-python//#implementing-bubble-sort-in-python "Permanent link")

Here’s an implementation of a bubble sort algorithm in `Python`:

```embed-cpp
PATH: "vault://GAB/Estudos-Trabalhos/PROGRAMAÇÃO/programing-studies/Languages/PYTHON/code/algo_bubble_sort.py"
TITLE: "Bubble.py"
```

<details> <summary>Or if you like a bit more intricate one, an implementation in `C`:</summary>

```embed-cpp
PATH: "vault://GAB/Estudos-Trabalhos/PROGRAMAÇÃO/programing-studies/Languages/C/code/algo_bubble_sort.c"
TITLE: "Bubble.c"
```

</details>

Since this implementation sorts the array in ascending order, each step *“bubbles”* the largest element to the end of the array. This means that each iteration takes fewer steps than the previous iteration because a continuously larger portion of the array is sorted.

The loops in **lines 4 and 10** determine the way the algorithm runs through the list. Notice how `j` initially goes from the first element in the list to the element immediately before the last. During the second iteration, `j` runs until two items from the last, then three items from the last, and so on. At the end of each iteration, the end portion of the list will be sorted.

As the loops progress, **line 15** compares each element with its adjacent value, and **line 18** swaps them if they are in the incorrect order. This ensures a sorted list at the end of the function.

**Note:** The `already_sorted` flag in **lines 13, 23, and 27** of the code above is an optimization to the algorithm, and it’s not required in a fully functional bubble sort implementation. However, it allows the function to save unnecessary steps if the list ends up wholly sorted before the loops have finished.

As an exercise, you can remove the use of this flag and compare the runtimes of both implementations.

To properly analyze how the algorithm works, consider a list with values `[8, 2, 6, 4, 5]`. Assume you’re using `bubble_sort()` from above. Here’s a figure illustrating what the array looks like at each iteration of the algorithm:

![Bubble Sort Algorithm|500](https://files.realpython.com/media/python-sorting-algorithms-bubble-sort.216ab9a52018.png)

The Bubble Sort Process

Now take a step-by-step look at what’s happening with the array as the algorithm progresses:

1.  The code starts by comparing the first element, `8`, with its adjacent element, `2`. Since `8 > 2`, the values are swapped, resulting in the following order: `[2, 8, 6, 4, 5]`.

2.  The algorithm then compares the second element, `8`, with its adjacent element, `6`. Since `8 > 6`, the values are swapped, resulting in the following order: `[2, 6, 8, 4, 5]`.
   
3.  Next, the algorithm compares the third element, `8`, with its adjacent element, `4`. Since `8 > 4`, it swaps the values as well, resulting in the following order: `[2, 6, 4, 8, 5]`.
   
4.  Finally, the algorithm compares the fourth element, `8`, with its adjacent element, `5`, and swaps them as well, resulting in `[2, 6, 4, 5, 8]`. At this point, the algorithm completed the first pass through the list (`i = 0`). Notice how the value `8` bubbled up from its initial location to its correct position at the end of the list.
   
5.  The second pass (`i = 1`) takes into account that the last element of the list is already positioned and focuses on the remaining four elements, `[2, 6, 4, 5]`. At the end of this pass, the value `6` finds its correct position. The third pass through the list positions the value `5`, and so on until the list is sorted.

# Measuring Bubble Sort’s [Big O](big_o_notation.md) Runtime Complexity [#](https://realpython.com/sorting-algorithms-python//#measuring-bubble-sorts-big-o-runtime-complexity "Permanent link")

Your implementation of bubble sort consists of two nested [`for` loops](https://realpython.com/python-for-loop/) in which the algorithm performs _n - 1_ comparisons, then _n - 2_ comparisons, and so on until the final comparison is done. This comes at a total of _(n - 1) + (n - 2) + (n - 3) + … + 2 + 1 = n(n-1)/2_ comparisons, which can also be written as _½n<sup>2</sup> - ½n_.

You learned earlier that Big O focuses on how the runtime grows in comparison to the size of the input. That means that, in order to turn the above equation into the Big O complexity of the algorithm, you need to remove the constants because they don’t change with the input size.

Doing so simplifies the notation to _n<sup>2</sup> - n_. Since _n<sup>2</sup>_ grows much faster than _n_, this last term can be dropped as well, leaving bubble sort with an average- and worst-case complexity of **_O(n<sup>2</sup>)_**.

In cases where the algorithm receives an array that’s already sorted—and assuming the implementation includes the `already_sorted` flag optimization explained before—the runtime complexity will come down to a much better _O(n)_ because the algorithm will not need to visit any element more than once.

_O(n)_, then, is the best-case runtime complexity of bubble sort. But keep in mind that best cases are an exception, and you should focus on the average case when comparing different algorithms.

# Timing Your Bubble Sort Implementation [#](https://realpython.com/sorting-algorithms-python//#timing-your-bubble-sort-implementation "Permanent link")

Using your `run_sorting_algorithm()` from earlier in this tutorial, here’s the time it takes for bubble sort to process an array with ten thousand items. **Line 8** replaces the name of the algorithm and everything else stays the same:

```python
 1    if __name__ == "__main__":
 2    # Generate an array of `ARRAY_LENGTH` items consisting
 3    # of random integer values between 0 and 999
 4    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
 5
 6    # Call the function using the name of the sorting algorithm
 7    # and the array you just created
 8    run_sorting_algorithm(algorithm="bubble_sort", array=array)

```

You can now run the script to get the execution time of `bubble_sort`:

```powershell
$ python sorting.py
Algorithm: bubble_sort. Minimum execution time: 73.21720498399998
```

It took `73` seconds to sort the array with ten thousand elements. This represents the fastest execution out of the ten repetitions that `run_sorting_algorithm()` runs. Executing this script multiple times will produce similar results.

**Note:** A single execution of bubble sort took `73` seconds, but the algorithm ran ten times using `timeit.repeat()`. This means that you should expect your code to take around `73 * 10 = 730` seconds to run, assuming you have similar hardware characteristics. Slower machines may take much longer to finish.

# Analyzing the Strengths and Weaknesses of Bubble Sort [#](https://realpython.com/sorting-algorithms-python//#analyzing-the-strengths-and-weaknesses-of-bubble-sort "Permanent link")

The main advantage of the bubble sort algorithm is its **simplicity**. It is straightforward to both implement and understand. This is probably the main reason why most computer science courses introduce the topic of sorting using bubble sort.

As you saw before, the disadvantage of bubble sort is that it is **slow**, with a runtime complexity of _O(n<sup>2</sup>)_. Unfortunately, this rules it out as a practical candidate for sorting large arrays.

# References

- https://www.geeksforgeeks.org/bubble-sort/