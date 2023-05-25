---
title: Timsort - Algorithm
tags: studies, programação
use: Documentation, Algorithms
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Implementing Timsort in Python #](#implementing-timsort-in-python-)
- [Measuring Timsort’s Big O Complexity #](#measuring-timsorts-big-o-complexity-)
- [Timing Your Timsort Implementation #](#timing-your-timsort-implementation-)
- [Analyzing the Strengths and Weaknesses of Timsort #](#analyzing-the-strengths-and-weaknesses-of-timsort-)

</details>

---

# Implementing Timsort in Python [#](https://realpython.com/sorting-algorithms-python//#implementing-timsort-in-python "Permanent link")

In this section, you’ll create a barebones Python implementation that illustrates all the pieces of the Timsort algorithm. If you’re interested, you can also check out the [original C implementation of Timsort](https://github.com/python/cpython/blob/master/Objects/listobject.c).

The first step in implementing Timsort is modifying the implementation of `insertion_sort()` from before:

```python
 1    def insertion_sort(array, left=0, right=None):
 2    if right is None:
 3        right = len(array) - 1
 4
 5    # Loop from the element indicated by
 6    # `left` until the element indicated by `right`
 7    for i in range(left + 1, right + 1):
 8        # This is the element we want to position in its
 9        # correct place
10        key_item = array[i]
11
12        # Initialize the variable that will be used to
13        # find the correct position of the element referenced
14        # by `key_item`
15        j = i - 1
16
17        # Run through the list of items (the left
18        # portion of the array) and find the correct position
19        # of the element referenced by `key_item`. Do this only
20        # if the `key_item` is smaller than its adjacent values.
21        while j >= left and array[j] > key_item:
22            # Shift the value one position to the left
23            # and reposition `j` to point to the next element
24            # (from right to left)
25            array[j + 1] = array[j]
26            j -= 1
27
28        # When you finish shifting the elements, position
29        # the `key_item` in its correct location
30        array[j + 1] = key_item
31
32    return array
```

This modified implementation adds a couple of parameters, `left` and `right`, that indicate which portion of the array should be sorted. This allows the Timsort algorithm to sort a portion of the array in place. Modifying the function instead of creating a new one means that it can be reused for both insertion sort and Timsort.

Now take a look at the implementation of Timsort:

```python
 1    def timsort(array):
 2    min_run = 32
 3    n = len(array)
 4
 5    # Start by slicing and sorting small portions of the
 6    # input array. The size of these slices is defined by
 7    # your `min_run` size.
 8    for i in range(0, n, min_run):
 9        insertion_sort(array, i, min((i + min_run - 1), n - 1))
10
11    # Now you can start merging the sorted slices.
12    # Start from `min_run`, doubling the size on
13    # each iteration until you surpass the length of
14    # the array.
15    size = min_run
16    while size < n:
17        # Determine the arrays that will
18        # be merged together
19        for start in range(0, n, size * 2):
20            # Compute the `midpoint` (where the first array ends
21            # and the second starts) and the `endpoint` (where
22            # the second array ends)
23            midpoint = start + size - 1
24            end = min((start + size * 2 - 1), (n-1))
25
26            # Merge the two subarrays.
27            # The `left` array should go from `start` to
28            # `midpoint + 1`, while the `right` array should
29            # go from `midpoint + 1` to `end + 1`.
30            merged_array = merge(
31                left=array[start:midpoint + 1],
32                right=array[midpoint + 1:end + 1])
33
34            # Finally, put the merged array back into
35            # your array
36            array[start:start + len(merged_array)] = merged_array
37
38        # Each iteration should double the size of your arrays
39        size *= 2
40
41    return array
```

Although the implementation is a bit more complex than the previous algorithms, we can summarize it quickly in the following way:

-   **Lines 8 and 9** create small slices, or runs, of the array and sort them using insertion sort. You learned previously that insertion sort is speedy on small lists, and Timsort takes advantage of this. Timsort uses the newly introduced `left` and `right` parameters in `insertion_sort()` to sort the list in place without having to create new arrays like merge sort and Quicksort do.

-   **Line 16** merges these smaller runs, with each run being of size `32` initially. With each iteration, the size of the runs is doubled, and the algorithm continues merging these larger runs until a single sorted run remains.

Notice how, unlike merge sort, Timsort merges subarrays that were previously sorted. Doing so decreases the total number of comparisons required to produce a sorted list. This advantage over merge sort will become apparent when running experiments using different arrays.

Finally, **line 2** defines `min_run = 32`. There are two reasons for using `32` as the value here:

1.  Sorting small arrays using insertion sort is very fast, and `min_run` has a small value to take advantage of this characteristic. Initializing `min_run` with a value that’s too large will defeat the purpose of using insertion sort and will make the algorithm slower.
 
2.  Merging two balanced lists is much more efficient than merging lists of disproportionate size. Picking a `min_run` value that’s a power of two ensures better performance when merging all the different runs that the algorithm creates.

Combining both conditions above offers several options for `min_run`. The implementation in this tutorial uses `min_run = 32` as one of the possibilities.

**Note:** In practice, Timsort does something a little more complicated to compute `min_run`. It picks a value between 32 and 64 inclusive, such that the length of the list divided by `min_run` is exactly a power of 2. If that’s not possible, it chooses a value that’s close to, but strictly less than, a power of 2.

If you’re curious, you can read the [complete analysis on how to pick `min_run`](https://hg.python.org/cpython/file/tip/Objects/listsort.txt) under the _Computing minrun_ section.

# Measuring Timsort’s Big O Complexity [#](https://realpython.com/sorting-algorithms-python//#measuring-timsorts-big-o-complexity "Permanent link")

On average, the complexity of Timsort is **_O(n log<sub>2</sub>n)_**, just like merge sort and Quicksort. The logarithmic part comes from doubling the size of the run to perform each linear merge operation.

However, Timsort performs exceptionally well on already-sorted or close-to-sorted lists, leading to a best-case scenario of _O(n)_. In this case, Timsort clearly beats merge sort and matches the best-case scenario for Quicksort. But the worst case for Timsort is also _O(n log<sub>2</sub>n)_, which surpasses Quicksort’s _O(n<sup>2</sup>)_.

# Timing Your Timsort Implementation [#](https://realpython.com/sorting-algorithms-python//#timing-your-timsort-implementation "Permanent link")

You can use `run_sorting_algorithm()` to see how Timsort performs sorting the ten-thousand-element array:

```python
 1    if __name__ == "__main__":
 2    # Generate an array of `ARRAY_LENGTH` items consisting
 3    # of random integer values between 0 and 999
 4    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
 5
 6    # Call the function using the name of the sorting algorithm
 7    # and the array you just created
 8    run_sorting_algorithm(algorithm="timsort", array=array)
```

Now execute the script to get the execution time of `timsort`:

```powershell
$ python sorting.py
Algorithm: timsort. Minimum execution time: 0.5121690789999998
```

At `0.51` seconds, this Timsort implementation is a full `0.1` seconds, or 17 percent, faster than merge sort, though it doesn’t match the `0.11` of Quicksort. It’s also a ridiculous 11,000 percent faster than insertion sort!

Now try to sort an already-sorted list using these four algorithms and see what happens. You can modify your `__main__` section as follows:

```python
 1    if __name__ == "__main__":
 2    # Generate a sorted array of ARRAY_LENGTH items
 3    array = [i for i in range(ARRAY_LENGTH)]
 4
 5    # Call each of the functions
 6    run_sorting_algorithm(algorithm="insertion_sort", array=array)
 7    run_sorting_algorithm(algorithm="merge_sort", array=array)
 8    run_sorting_algorithm(algorithm="quicksort", array=array)
 9    run_sorting_algorithm(algorithm="timsort", array=array)
```

If you execute the script now, then all the algorithms will run and output their corresponding execution time:

```powershell
Algorithm: insertion_sort. Minimum execution time: 53.5485634999991
Algorithm: merge_sort. Minimum execution time: 0.372304601
Algorithm: quicksort. Minimum execution time: 0.24626494199999982
Algorithm: timsort. Minimum execution time: 0.23350277099999994
```

This time, Timsort comes in at a whopping thirty-seven percent faster than merge sort and five percent faster than Quicksort, flexing its ability to take advantage of the already-sorted runs.

Notice how Timsort benefits from two algorithms that are much slower when used by themselves. The genius of Timsort is in combining these algorithms and playing to their strengths to achieve impressive results.

# Analyzing the Strengths and Weaknesses of Timsort [#](https://realpython.com/sorting-algorithms-python//#analyzing-the-strengths-and-weaknesses-of-timsort "Permanent link")

The main disadvantage of Timsort is its complexity. Despite implementing a very simplified version of the original algorithm, it still requires much more code because it relies on both `insertion_sort()` and `merge()`.

One of Timsort’s advantages is its ability to predictably perform in _O(n log<sub>2</sub>n)_ regardless of the structure of the input array. Contrast that with Quicksort, which can degrade down to _O(n<sup>2</sup>)_. Timsort is also very fast for small arrays because the algorithm turns into a single insertion sort.

For real-world usage, in which it’s common to sort arrays that already have some preexisting order, Timsort is a great option. Its adaptability makes it an excellent choice for sorting arrays of any length.

