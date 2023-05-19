---
title: Data Structures
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Definition](#definition)
- [Characteristics of data structures](#characteristics-of-data-structures)
- [Why are data structures important?](#why-are-data-structures-important)
- [How are data structures used?](#how-are-data-structures-used)
- [Data types](#data-types)
- [How to choose a data structure](#how-to-choose-a-data-structure)
- [Types of data structures](#types-of-data-structures)
	- [Arrays](#arrays)
	- [Linked Lists](#linked-lists)
	- [Stacks](#stacks)
	- [Queues](#queues)
	- [Hash Tables](#hash-tables)
	- [Trees](#trees)
	- [Heaps](#heaps)
	- [Graphs](#graphs)
- [References](#references)

</details>

---

# Definition

A data structure is a specialized format **for organizing, processing, retrieving and storing data**. There are several basic and advanced types of data structures, all designed to arrange data to suit a specific purpose. Data structures make it easy for users to access and work with the data they need in appropriate ways. Most importantly, data structures frame the organization of information so that machines and humans can better understand it.

In computer science and computer programming, a data structure may be selected or designed to store data for the purpose of using it with various [algorithms](https://www.techtarget.com/whatis/definition/algorithm). In some cases, the algorithm's basic operations are tightly coupled to the data structure's design. Each data structure contains information about the data values, relationships between the data and -- in some cases -- functions that can be applied to the data.

For instance, in an [object-oriented programming](https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP) language, the data structure and its associated methods are bound together as part of a class definition. In non-object-oriented languages, there may be functions defined to work with the data structure, but they are not technically part of the data structure.

# Characteristics of data structures

Data structures are often classified by their characteristics. The following three characteristics are examples:

1.  **Linear or non-linear.** This characteristic describes whether the data items are arranged in sequential order. Describles *cronological* and *unordered* data respectivily. Such as with an array, or in an unordered sequence, such as with a graph.

2.  **Homogeneous or heterogeneous.** This characteristic describes whether all data items in a given repository *are of the same type or not*. One example is a collection of elements in an array, or of various types, such as an abstract data type defined as a structure in C or a class specification in Java.

3.  **[Static or dynamic](https://www.techtarget.com/searchnetworking/definition/dynamic-and-static).** This characteristic *describes how the data structures are compiled*.
	-  Static data structures have **fixed** sizes, structures and memory locations at compile time.
	-  Dynamic data structures have sizes, structures and memory locations that **can shrink or expand**, depending on the use.


# Why are data structures important?

Typical base [data types](https://www.techtarget.com/searchapparchitecture/definition/data-type), such as integers or floating-point values, that are available in most computer programming languages are generally insufficient to capture the logical intent for data processing and use. Yet applications that ingest, manipulate and produce information must understand how data should be organized to simplify processing. Data structures bring together the data elements in a logical way and facilitate the effective use, persistence and sharing of data. They provide a formal model that describes the way the data elements are organized.

Data structures are the [building blocks for more sophisticated applications](https://www.techtarget.com/searchdatamanagement/feature/Why-understanding-data-structures-is-so-important-to-coders). They are designed by composing data elements into a logical unit representing an abstract data type that has relevance to the algorithm or application. An example of an abstract data type is a "customer name" that is composed of the character strings for "first name," "middle name" and "last name."

It is not only important to use data structures, but it is also important to choose the proper data structure for each task. Choosing an ill-suited data structure could result in slow [runtimes](https://www.techtarget.com/searchsoftwarequality/definition/runtime) or unresponsive code. Five factors to consider when picking a data structure include the following:

1.  What kind of information will be stored?
2.  How will that information be used?
3.  Where should data persist, or be kept, after it is created?
4.  What is the best way to organize the data?
5.  What aspects of memory and storage reservation management should be considered?

# How are data structures used?

In general, data structures are used to implement the physical forms of abstract [data types](https://www.techtarget.com/searchapparchitecture/definition/data-type). Data structures are a crucial part of designing efficient software. They also play a critical role in algorithm design and how those algorithms are used within computer programs.

Early programming languages -- [such as Fortran, C and C++](https://www.techtarget.com/searchwindowsserver/definition/C) -- enabled programmers to define their own data structures. Today, many programming languages include an extensive collection of built-in data structures to organize code and information. For example, [Python](https://www.techtarget.com/whatis/definition/Python) lists and dictionaries, and [JavaScript](https://www.theserverside.com/definition/JavaScript) arrays and objects are common coding structures used for storing and retrieving information.

Software engineers use algorithms that are tightly coupled with the data structures -- such as lists, queues and mappings from one set of values to another. This approach can be fused in a variety of applications, including managing collections of records in a [relational database](https://www.techtarget.com/searchdatamanagement/definition/relational-database) and creating an index of those records using a data structure called a binary tree.

Some examples of how data structures are used include the following:

-   **Storing data.** Data structures are used for [efficient data persistence](https://www.techtarget.com/searchapparchitecture/answer/What-is-the-best-pattern-to-use-for-data-persistence), such as specifying the collection of attributes and corresponding structures used to store records in a database management system.
-   **Managing resources and services.** Core operating system (OS) resources and services are enabled through the use of data structures such as linked lists for memory allocation, file directory management and file structure trees, as well as process scheduling queues.
-   **Data exchange.** Data structures define the organization of information shared between applications, such as TCP/IP packets.
-   **Ordering and sorting.** Data structures such as binary search trees -- also known as an ordered or sorted binary tree -- provide efficient methods of sorting objects, such as character strings used as tags. With data structures such as [**priority queues**](./ds_queue.md#priority-queue), programmers can manage items organized according to a specific priority.
-   **Indexing**. Even more sophisticated data structures such as B-trees are used to index objects, such as those stored in a database.
-   **Searching.** Indexes created using binary search trees, B-trees or hash tables speed the ability to find a specific sought-after item.
-   **Scalability.** Big data applications use data structures for allocating and managing data storage across distributed storage locations, ensuring scalability and performance. Certain big data programming environments -- such as [Apache Spark](https://www.techtarget.com/searchdatamanagement/definition/Apache-Spark) -- provide data structures that mirror the underlying structure of database records to simplify querying.

# Data types

If data structures are the building blocks of algorithms and computer programs, the primitive -- or base -- data types are the building blocks of data structures. The typical base data types include the following:

-   **[Boolean](https://www.techtarget.com/whatis/definition/Boolean)**, which stores logical values that are either true or false.
-   **integer**, which [stores a range on mathematical integers](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/int-vs-Integer-java-difference-comparison-primitive-object-types) -- or counting numbers. Different sized integers hold a different range of values -- e.g., a signed 8-bit integer holds values from -128 to 127, and an unsigned long 32-bit integer holds values from 0 to 4,294,967,295.
-   **Floating-point numbers**, which store a formulaic representation of real numbers.
-   **Fixed-point numbers**, which are used in some programming languages and hold real values but are managed as digits to the left and the right of the decimal point.
-   **Character**, which uses symbols from a defined mapping of integer values to symbols.
-   **Pointers,** which are reference values that point to other values.
-   **String**, which is an array of characters followed by a stop code -- usually a "0" value -- or is managed using a length field that is an integer value.

![Data structure hierarchy](https://cdn.ttgtmedia.com/rms/onlineimages/whatis-data_structure_mobile.png)
> The data structure hierarchy shows how data types and data structures are related.

# How to choose a data structure

When choosing a data structure for a program or application, developers should consider the answers to the following three questions:

1.  **Supported operations.** What functions and operations does the program need?
2.  **Computational complexity.** What level of computational performance is tolerable? For speed, a data structure whose operations execute in time linear to the number of items managed -- using [Big O Notation: O(n)](./big_o_notation.md) (https://lankydan.dev/2017/04/23/learning-big-o-notation-with-on-complexity) -- will be faster than a data structure whose operations execute in time proportional to the square of the number of items managed -- O(n^2).
3.  **Programming elegance.** Are the organization of the data structure and its functional interface easy to use?


# Types of data structures

The data structure type used in a particular situation is determined by the type of operations that will be required or the kinds of algorithms that will be applied. The various data structure types include the following:

## [Arrays](./ds_array.md)
## [Linked Lists](./ds_linked_list.md)
## [Stacks](./ds_stack.md)
## [Queues](./ds_queue.md)
## [Hash Tables](./ds_hash_table.md)
## [Trees](./ds_tree.md)
## [Heaps](./ds_heap.md)
## [Graphs](./ds_graph.md)

# References

- [programiz](https://www.programiz.com/dsa)
- [stephanosterburg](https://stephanosterburg.gitbook.io/scrapbook/coding/coding-interview/data-structures/)
- [roadmap](https://roadmap.sh/python)