---
title: Merge Sort - Algorithm
tags: studies, programação
use: Documentation, Algorithms
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Implementing Merge Sort in Python #](#implementing-merge-sort-in-python-)
- [Measuring Merge Sort’s Big O Complexity #](#measuring-merge-sorts-big-o-complexity-)
- [Timing Your Merge Sort Implementation #](#timing-your-merge-sort-implementation-)
- [Analyzing the Strengths and Weaknesses of Merge Sort #](#analyzing-the-strengths-and-weaknesses-of-merge-sort-)

</details>

---

# Implementing Merge Sort in Python [#](https://realpython.com/sorting-algorithms-python//#implementing-merge-sort-in-python "Permanent link")

The implementation of the merge sort algorithm needs two different pieces:

1.  A function that recursively splits the input in half
2.  A function that merges both halves, producing a sorted array

Here’s the code to merge two different arrays:

```python
 1    def merge(left, right):
 2    # If the first array is empty, then nothing needs
 3    # to be merged, and you can return the second array as the result
 4    if len(left) == 0:
 5        return right
 6
 7    # If the second array is empty, then nothing needs
 8    # to be merged, and you can return the first array as the result
 9    if len(right) == 0:
10        return left
11
12    result = []
13    index_left = index_right = 0
14
15    # Now go through both arrays until all the elements
16    # make it into the resultant array
17    while len(result) < len(left) + len(right):
18        # The elements need to be sorted to add them to the
19        # resultant array, so you need to decide whether to get
20        # the next element from the first or the second array
21        if left[index_left] <= right[index_right]:
22            result.append(left[index_left])
23            index_left += 1
24        else:
25            result.append(right[index_right])
26            index_right += 1
27
28        # If you reach the end of either array, then you can
29        # add the remaining elements from the other array to
30        # the result and break the loop
31        if index_right == len(right):
32            result += left[index_left:]
33            break
34
35        if index_left == len(left):
36            result += right[index_right:]
37            break
38
39    return result

```

`merge()` receives two different sorted arrays that need to be merged together. The process to accomplish this is straightforward:

-   **Lines 4 and 9** check whether either of the arrays is empty. If one of them is, then there’s nothing to merge, so the function returns the other array.

-   **Line 17** starts a [`while` loop](https://realpython.com/courses/mastering-while-loops/) that ends whenever the result contains all the elements from both of the supplied arrays. The goal is to look into both arrays and combine their items to produce a sorted list.
   
-   **Line 21** compares the elements at the head of both arrays, selects the smaller value, and [appends](https://realpython.com/python-append/) it to the end of the resultant array.
   
-   **Lines 31 and 35** append any remaining items to the result if all the elements from either of the arrays were already used.
   

With the above function in place, the only missing piece is a function that recursively splits the input array in half and uses `merge()` to produce the final result:

```python
41    def merge_sort(array):
42    # If the input array contains fewer than two elements,
43    # then return it as the result of the function
44    if len(array) < 2:
45        return array
46
47    midpoint = len(array) // 2
48
49    # Sort the array by recursively splitting the input
50    # into two equal halves, sorting each half and merging them
51    # together into the final result
52    return merge(
53        left=merge_sort(array[:midpoint]),
54        right=merge_sort(array[midpoint:]))
```

Here’s a quick summary of the code:

-   **Line 44** acts as the stopping condition for the recursion. If the input array contains fewer than two elements, then the function returns the array. Notice that this condition could be triggered by receiving either a single item or an empty array. In both cases, there’s nothing left to sort, so the function should return.

-   **Line 47** computes the middle point of the array.
   
-   **Line 52** calls `merge()`, passing both sorted halves as the arrays.

Notice how this function calls itself **recursively**, halving the array each time. Each iteration deals with an ever-shrinking array until fewer than two elements remain, meaning there’s nothing left to sort. At this point, `merge()` takes over, merging the two halves and producing a sorted list.

Take a look at a representation of the steps that merge sort will take to sort the array `[8, 2, 6, 4, 5]`:

![Merge Sort Algorithm|500](https://files.realpython.com/media/python-sorting-algorithms-merge-sort.d6b5c7dec9ef.png)

The Merge Sort Process

The figure uses yellow arrows to represent halving the array at each recursion level. The green arrows represent merging each subarray back together. The steps can be summarized as follows:

1.  The first call to `merge_sort()` with `[8, 2, 6, 4, 5]` defines `midpoint` as `2`. The `midpoint` is used to halve the input array into `array[:2]` and `array[2:]`, producing `[8, 2]` and `[6, 4, 5]`, respectively. `merge_sort()` is then recursively called for each half to sort them separately.

2.  The call to `merge_sort()` with `[8, 2]` produces `[8]` and `[2]`. The process repeats for each of these halves.
   
3.  The call to `merge_sort()` with `[8]` returns `[8]` since that’s the only element. The same happens with the call to `merge_sort()` with `[2]`.
  
4.  At this point, the function starts merging the subarrays back together using `merge()`, starting with `[8]` and `[2]` as input arrays, producing `[2, 8]` as the result.
  
5.  On the other side, `[6, 4, 5]` is recursively broken down and merged using the same procedure, producing `[4, 5, 6]` as the result.
  
6.  In the final step, `[2, 8]` and `[4, 5, 6]` are merged back together with `merge()`, producing the final result: `[2, 4, 5, 6, 8]`.


# Measuring Merge Sort’s Big O Complexity [#](https://realpython.com/sorting-algorithms-python//#measuring-merge-sorts-big-o-complexity "Permanent link")

To analyze the complexity of merge sort, you can look at its two steps separately:

1.  `merge()` has a linear runtime. It receives two arrays whose combined length is at most _n_ (the length of the original input array), and it combines both arrays by looking at each element at most once. This leads to a runtime complexity of _O(n)_.

2.  The second step splits the input array recursively and calls `merge()` for each half. Since the array is halved until a single element remains, the total number of halving operations performed by this function is _log<sub>2</sub>n_. Since `merge()` is called for each half, we get a total runtime of **_O(n log<sub>2</sub>n)_**.


Interestingly, _O(n log<sub>2</sub>n)_ is the best possible worst-case runtime that can be achieved by a sorting algorithm.

# Timing Your Merge Sort Implementation [#](https://realpython.com/sorting-algorithms-python//#timing-your-merge-sort-implementation "Permanent link")

To compare the speed of merge sort with the previous two implementations, you can use the same mechanism as before and replace the name of the algorithm in **line 8**:

```python
 1    if __name__ == "__main__":
 2    # Generate an array of `ARRAY_LENGTH` items consisting
 3    # of random integer values between 0 and 999
 4    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
 5
 6    # Call the function using the name of the sorting algorithm
 7    # and the array you just created
 8    run_sorting_algorithm(algorithm="merge_sort", array=array)
```

You can execute the script to get the execution time of `merge_sort`:

```powershell
$ python sorting.py
Algorithm: merge_sort. Minimum execution time: 0.6195857160000173
```

Compared to bubble sort and insertion sort, the merge sort implementation is extremely fast, sorting the ten-thousand-element array in less than a second!

# Analyzing the Strengths and Weaknesses of Merge Sort [#](https://realpython.com/sorting-algorithms-python//#analyzing-the-strengths-and-weaknesses-of-merge-sort "Permanent link")

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