---
title: Big O Notation
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents 🔖</summary>

- [Big O](#big-o)
  - [The Significance of Time Complexity #](#the-significance-of-time-complexity-)
    - [Timing Your Code #](#timing-your-code-)
    - [Measuring Efficiency With Big O Notation #](#measuring-efficiency-with-big-o-notation-)
  - [Concept](#concept)

</details>

# Big O

## The Significance of Time Complexity [#](https://realpython.com/sorting-algorithms-python//#the-significance-of-time-complexity "Permanent link")

This tutorial covers two different ways to measure the **runtime** of sorting algorithms:

1.  For a practical point of view, you’ll measure the runtime of the implementations using the `timeit` module.
2.  For a more theoretical perspective, you’ll measure the **runtime complexity** of the algorithms using [**Big O notation**](https://en.wikipedia.org/wiki/Big_O_notation).

### Timing Your Code [#](https://realpython.com/sorting-algorithms-python//#timing-your-code "Permanent link")

When comparing two sorting algorithms in Python, it’s always informative to look at how long each one takes to run. The specific time each algorithm takes will be partly determined by your hardware, but you can still use the proportional time between executions to help you decide which implementation is more time efficient.

In this section, you’ll focus on a practical way to measure the actual time it takes to run to your sorting algorithms using the `timeit` module. For more information on the different ways you can time the execution of code in Python, check out [Python Timer Functions: Three Ways to Monitor Your Code](https://realpython.com/python-timer/).

Here’s a function you can use to time your algorithms:

```python
 1    from random import randint
 2    from timeit import repeat
 3
 4    def run_sorting_algorithm(algorithm, array):
 5    # Set up the context and prepare the call to the specified
 6    # algorithm using the supplied array. Only import the
 7    # algorithm function if it's not the built-in `sorted()`.
 8    setup_code = f"from __main__ import {algorithm}" \
 9        if algorithm != "sorted" else ""
10
11    stmt = f"{algorithm}({array})"
12
13    # Execute the code ten different times and return the time
14    # in seconds that each execution took
15    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
16
17    # Finally, display the name of the algorithm and the
18    # minimum time it took to run
19    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
```

In this example, `run_sorting_algorithm()` receives the name of the algorithm and the input array that needs to be sorted. Here’s a line-by-line explanation of how it works:

-   **Line 8** imports the name of the algorithm using the magic of [Python’s f-strings](https://realpython.com/python-f-strings/). This is so that `timeit.repeat()` knows where to call the algorithm from. Note that this is only necessary for the custom implementations used in this tutorial. If the algorithm specified is the built-in `sorted()`, then nothing will be imported.
    
-   **Line 11** prepares the call to the algorithm with the supplied array. This is the statement that will be executed and timed.
    
-   **Line 15** calls `timeit.repeat()` with the setup code and the statement. This will call the specified sorting algorithm ten times, returning the number of seconds each one of these executions took.
    
-   **Line 19** identifies the shortest time returned and prints it along with the name of the algorithm.
    

**Note:** A common misconception is that you should find the average time of each run of the algorithm instead of selecting the single shortest time. Time measurements are [noisy](https://en.wikipedia.org/wiki/Noisy_data) because the system runs other processes concurrently. The shortest time is always the least noisy, making it the best representation of the algorithm’s true runtime.

Here’s an example of how to use `run_sorting_algorithm()` to determine the time it takes to sort an array of ten thousand integer values using `sorted()`:

```python
21    ARRAY_LENGTH = 10000
22
23    if __name__ == "__main__":
24    # Generate an array of `ARRAY_LENGTH` items consisting
25    # of random integer values between 0 and 999
26    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
27
28    # Call the function using the name of the sorting algorithm
29    # and the array you just created
30    run_sorting_algorithm(algorithm="sorted", array=array)
```

If you save the above code in a `sorting.py` file, then you can run it from the [terminal](https://realpython.com/terminal-commands/) and see its output:

```python
$ python sorting.py
Algorithm: sorted. Minimum execution time: 0.010945824000000007
```

Remember that the time in seconds of every experiment depends in part on the hardware you use, so you’ll likely see slightly different results when running the code.

**Note:** You can learn more about the `timeit` module in the [official Python documentation](https://docs.python.org/2/library/timeit.html).

### Measuring Efficiency With Big O Notation [#](https://realpython.com/sorting-algorithms-python//#measuring-efficiency-with-big-o-notation "Permanent link")

The specific time an algorithm takes to run isn’t enough information to get the full picture of its [**time complexity**](https://en.wikipedia.org/wiki/Time_complexity). To solve this problem, you can use Big O (pronounced “big oh”) notation. Big O is often used to compare different implementations and decide which one is the most efficient, skipping unnecessary details and focusing on what’s most important in the runtime of an algorithm.

The time in seconds required to run different algorithms can be influenced by several unrelated factors, including processor speed or available memory. Big O, on the other hand, provides a platform to express runtime complexity in hardware-agnostic terms. With Big O, you express complexity in terms of how quickly your algorithm’s runtime grows relative to the size of the input, especially as the input grows arbitrarily large.

Assuming that _n_ is the size of the input to an algorithm, the Big O notation represents the relationship between _n_ and the number of steps the algorithm takes to find a solution. Big O uses a capital letter “O” followed by this relationship inside parentheses. For example, **_O(n)_** represents algorithms that execute a number of steps proportional to the size of their input.

Although this tutorial isn’t going to dive very deep into the details of Big O notation, here are five examples of the runtime complexity of different algorithms, **from lowest to fastest**:

| Big O              | Complexity  | Description                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _O(n<sup>2</sup>)_ | quadratic   | The runtime is a quadratic function of the size of the input. A naive implementation of finding duplicate values in a list, in which each item has to be checked twice, is an example of a quadratic algorithm.                                                                                                                                                                    |
| _O(2<sup>n</sup>)_ | exponential | The runtime grows exponentially with the size of the input. These algorithms are considered extremely inefficient. An example of an exponential algorithm is the [three-coloring problem](https://en.wikipedia.org/wiki/Graph_coloring).                                                                                                                                           |
| _O(n)_             | linear      | The runtime grows linearly with the size of the input. A function that checks a condition on every item of a list is an example of an _O(n)_ algorithm.                                                                                                                                                                                                                            |
| _O(log n)_         | logarithmic | The runtime grows linearly while the size of the input grows exponentially. For example, if it takes one second to process one thousand elements, then it will take two seconds to process ten thousand, three seconds to process one hundred thousand, and so on. [Binary search](https://realpython.com/binary-search-python/) is an example of a logarithmic runtime algorithm. |
| _O(1)_             | constant    | The runtime is constant regardless of the size of the input. Finding an element in a [hash table](https://realpython.com/python-hash-table/) is an example of an operation that can be performed in **constant time**.                                                                                                                                                             |

>This tutorial covers the Big O runtime complexity of each of the sorting algorithms discussed. It also includes a brief explanation of how to determine the runtime on each particular case. This will give you a better understanding of how to start using Big O to classify other algorithms.
>
> **Note:** For a deeper understanding of Big O, together with several practical examples in Python, check out [Big O Notation and Algorithm Analysis with Python Examples](https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/).

## Concept

Big O Notation is one of those things that I was taught at university but never really grasped the concept. I knew enough to answer very basic questions on it but that was about it. Nothing has changed since then as I have not used or heard any of my colleagues mention it since I started working. So I thought I’d spend some time going back over it and wrote this post summarising the basics of Big O Notation and along with some code examples to help explain it.

So what is Big O Notation? In simple terms:

-   It is the relative representation of complexity of an algorithm.
-   Describes how an algorithm performs and scales.
-   Describes the upper bound of the growth rate of a function and could be thought of a the _worst case scenario_.

Now for a quick look at the syntax.

> O(n<sup>2</sup>)

_n_ is the number of elements that the function receiving as inputs. So this example is saying for _n_ inputs its complexity is equal to _n<sup>2</sup>_.

Comparison of the common notations.

| n | Constant O(1) | Logarithmic O(log n) | Linear O(n) | Linear Logarithmic O(n log n) | Quadratic O(n<sup>2</sup> | Cubic O(n<sup>3</sup>) |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 2 | 1 | 4 | 8 |
| 4 | 1 | 2 | 4 | 8 | 16 | 64 |
| 8 | 1 | 3 | 8 | 24 | 64 | 512 |
| 16 | 1 | 4 | 16 | 64 | 256 | 4,096 |
| 1,024 | 1 | 10 | 1,024 | 10,240 | 1,048,576 | 1,073,741,824 |

As you can see from this table as the complexity of a function increases the amount of computations or time it takes to complete a function can rise quite significantly. Therefore we want to keep this growth as low as possible as performance problems might arise if the function does not scale well as inputs are increased.

![Graph showing how the number of operations increases with complexity](https://lankydan.dev/static/e400c3e7ffa7767eda4f91a01fbc568b/b13e1/complexity-graph.png "Graph showing how the number of operations increases with complexity")

Some code examples should help clear things up a bit regarding how complexity effects performance. The code below is written in Java but obviously could be written in other languages.

**O(1)**

```java
public boolean isFirstNumberEqualToOne(List<Integer> numbers) {
  return numbers.get(0) == 1;
}
```

O(1) represents a function that always takes the same take regardless of input size.

**O(n)**

```java
public boolean containsNumber(List<Integer> numbers, int comparisonNumber) {
  for(Integer number : numbers) {
    if(number == comparisonNumber) {
      return true;
    }
  }
  return false;
}
```

O(n) represents the complexity of a function that increases linearly and in direct proportion to the number of inputs. This is a good example of how Big O Notation describes the _worst case scenario_ as the function could return the _true_ after reading the first element or _false_ after reading all _n_ elements.

**O(n<sup>2</sup>)**

```java
public static boolean containsDuplicates(List<String> input) {
  for (int outer = 0; outer < input.size(); outer++) {
    for (int inner = 0; inner < input.size(); inner++) {
      if (outer != inner && input.get(outer).equals(input.get(inner))) {
        return true;
      }
    }
  }
  return false;
}
```

O(n<sup>2</sup>) represents a function whose complexity is directly proportional to the square of the input size. Adding more nested iterations through the input will increase the complexity which could then represent O(n<sup>3</sup>) with 3 total iterations and O(n<sup>4</sup>) with 4 total iterations.

**O(2<sup>n</sup>)**

```java
public int fibonacci(int number) {
  if (number <= 1) {
    return number;
  } else {
    return fibonacci(number - 1) + fibonacci(number - 2);
  }
}
```

O(2<sup>n</sup>) represents a function whose performance doubles for every element in the input. This example is the recursive calculation of Fibonacci numbers. The function falls under O(2<sup>n</sup>) as the function recursively calls itself twice for each input number until the number is less than or equal to one.

**O(log n)**

```java
public boolean containsNumber(List<Integer> numbers, int comparisonNumber) {
  int low = 0;
  int high = numbers.size() - 1;
  while (low <= high) {
    int middle = low + (high - low) / 2;
    if (comparisonNumber < numbers.get(middle)) {
      high = middle - 1;
    } else if (comparisonNumber > numbers.get(middle)) {
      low = middle + 1;
    } else {
      return true;
    }
  }
  return false;
}
```

O(log n) represents a function whose complexity increases logarithmically as the input size increases. This makes O(log n) functions scale very well so the handling of larger inputs is much less likely to cause performance problems. The example above uses a binary search to check if the input list contains a certain number. In simple terms it splits the list in two on each iteration until the number is found or the last element is read. If you noticed this method has the same functionality as the O(n) example although the implementation is completely different and more difficult to understand. But, this is rewarded with a much better performance with larger inputs (as seen in the table).

The downside of this sort of implementation is that a Binary Search relies on the elements to already be in the correct order. This adds a bit of overhead performance wise if the elements need to be ordered before traversing through them.

There is much more to cover about Big O Notation but hopefully you now have a basic idea of what Big O Notation means and how that can translate into the code that you write.