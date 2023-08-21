---
title: Code Concepts
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---

<details> <summary>Table of Contents 🔖</summary>

- [Intro](#intro)
- [101](#101)

</details>

# Intro

> Currently listing all that I want to read before writing

- code cohesion
- code coupling
- project documentation
	- Code should be written in a way that promotes `readability` and is easy to understand for other developers.
	- Good documentation can take different forms such as comments, documentation sites, and API documentation.
	- Comments should provide meaningful explanations and not simply describe the syntax of the code.
	- Using `type-hints` in Python code improves clarity and understanding.
	- `docstrings` can be used to document functions, methods, classes, and modules, and tools like Auto `docstring` can assist in generating them.
	- use of `mkdocs` alongside of `docstrings`
- code diagnosis
- UML
- SOLID
- CRUD
- Programming Patterns
	- Collection Classes 
	- Junction Classes 
- Object structure
	- Service
	- Interface
	- Implementation (data and code)
- OOD Object Oriented Design
- OOA Object Oriented Analysis



> [!INFO] 
> [Usefull links ](links.md) 

# 101

## The Computer

`The computer` it's just a piece of tape that holds ones and zeros along with a device that can read and write to it it's called a `turing machine` and in theory it can compute anything. 

At the core of modern computers we have the central processing unit if we crack it open we find a piece of silicon that contains billions of tiny `transistors` which are like microscopic on off switches the value at one of these switches is called a `bit` and is the smallest piece of information a computer can use however one bit by itself is not very useful so they come in a package of eight called a `byte`

A byte it represent 256 different values like all the characters that you type on your keyboard in fact when you type into your keyboard the character produced is actually mapped to a value in a character encoding like `ascii` or `utf-8`.

### `Binary`

Is just a system for counting like the base 10 system you normally use when counting on your fingers but it only has two characters one and zero humans have a hard time reading it.

### `Hexadecimal`

So most often it's represented in a base 16 format where ten numbers and six letters can represent a four bit group called a `nibble`.

### `Machine Code`

As a developer when you write code in a `programming language` it will eventually be converted into *machine code* which is a *binary* format that can be decoded and executed by the `CPU` the Command Proccessing Unit.

### `RAM`

What it doesn't do though is store data for your applications for that computers have Random Access Memory or *RAM* it's like a neighborhood and inside of every house lives a *byte* every location has a `memory address` which the *CPU* can read and write to.

You can think of the *CPU* and *RAM* as the brain of the computer.

### Input and Output (I/O)

But in order for a computer to be useful it needs to handle `input and output`. An input device might be the keyboard and mouse while an output device might be your monitor.

### `Kernel` - `Shell`

Luckily most developers don't need to worry about how this hardware fits together because we have operating system kernels like linux mac and windows that control all hardware resources via device drivers now to start hacking on the operating system your first entry point is the *shell* which is a program that exposes the operating system to the end user it's called a
shell because it wraps the *Kernel*

It takes a line of text as input and produces an output this is called a `command line interface` not only can it connect to your own computer but with the `secure shell protocol` it can also connect to remote computers over a network now that you have access to the `mainframe`.

## Programming Languages

It's time to pick a `programming language` which is a tool that uses the `abstraction principle` to make computers practical to work with for humans by simplifying different systems layer by layer.

Some languages like **Python** are `interpreted` that means there's a program called an interpreter that will execute each line of code one by one other languages like **C+** are `compiled` they use a compiler to convert the entire program into *machine code*.

In advance before the *CPU* attempts to execute it this results in an `executable` file that can be run by the operating system without any extra dependencies.

## Data Types / Variables

Every *programming language* has a variety of built-in `data types` to represent the data we're working with in our code instead of *bytes* we work with more human-friendly things like characters and numbers.

The most fundamental way to use data in your application is to declare a `variable` this attaches a name to a data point allowing you to reuse it somewhere else in your code. 

**Python** is a `dynamically typed` language which means we don't need to tell the program exactly which data type is assigned to a *variable* it just figures it out automatically. However other languages like **C** are `statically typed` and that means you need to specify the data type of a *variable* in your code when you declare it.

The value of the *variable* is stored somewhere in memory on the hardware and you may need to allocate and free up memory throughout the program. A `pointer` is a *variable* whose value is the *memory address* of another *variable* which can be used for low-level memory control many languages don't want to deal with low-level memory management and instead implement a `garbage collector` which automatically allocates and de-allocates memory when an object is no longer referenced in the program.

Typically you'll find `int` to represent whole numbers which may or may not be `signed` or unsigned to represent negative numbers as well.

When numbers require a decimal point they typically use the `floating point` type it's called a float because there's only enough memory to represent a certain range of numbers at a certain precision and is basically a form of scientific notation to make computers faster.

If you need more range or precision many languages also have a `double` that doubles the amount of memory used for the number now.

When it comes to characters you'll typically find the `char` data type to represent a single character or more commonly a `string` to represent multiple characters together.

When comparing two values if the first one is greater than the second then it forms a value of true but if b is greater than a then the value is false.  
true false is what's known as a `boolean` data type.

The `void` data type has no values and no operations. It's a data type that represents the lack of a data type. Many programming languages need a data type to define the lack of return value to indicate that nothing is being returned.

Ultimately these characters get stored in a *memory address* somewhere but they need to be stored in a certain order when the order starts with the most significant *byte* and the smallest *memory address* it's called `big endian` or vice versa if the least significant *byte* is stored in the smallest address it's called `little endian`.

## Data Structures

When it comes to practical software engineering one of the most fundamental things we do is organize data into `data structures`.

### Array

The most useful data structure is probably the `array` or list just like a shopping list it organizes multiple data points in order however it also maintains an index of integers that starts at zero and goes up for every new item in the list that can be useful but you don't actually need an index to create a list of items.

### Linked List

Another option is a `linked list` where each item has a *pointer* to the next item in front of it.

### Stack

Another option is a `stack` that follows the **last in first out** principle it's like stacking a set of plates then when you want to access the data you pop the last one off the top.

### Queue

The inverse option of the stack is a `queue` which is **first in first out** just like when you get into the red line the first person there is the first one to be fed now.

### Hash

Another extremely useful data structure is the `hash` which might also be called a map or dictionary it's like an *array* but instead of an index of integers you define the keys that point to each individual item giving you a collection of key value pairs.

### Tree

In many cases though it's not efficient to organize data in a linear way to address that problem we have `tree`s which organize nodes together in a hierarchy that can often be traversed more quickly this can sometimes be too rigid of a data structure.

### Graph

Instead of *tree*, a `graph` can be created to connect multiple nodes together in a virtually unlimited number of ways a *graph* has a `node` for the data and an `edge` for the relationship between the data points.

## Algorithms

Data structures are essential but they don't do anything by themselves to do something useful you'll need to code up an `algorithm` which is just code that solves a problem.

### Functions

The most fundamental of which is a `function` which is a block of code that takes an input then does something and returns an output like a variable a function has a name and it can be called from other parts of your code with different input parameters called `arguments`.

One thing you might do in the function body is compare one value to another every language has a variety of built-in `operators` like equality greater than and less than that you can use to compare things, that may result in another value and whenever your code produces a value like this it's known as an `expression`.  
But not all code will produce a value sometimes your code will simply do something which is known as a `statement` a good example is the if statement which handles `conditional logic` for example if the condition is true it will execute this code otherwise it will short circuit and run the code inside of the else block.

### Loops

Another very common type of statement is a loop a `while loop` will run this block of code over and over again until the condition in the parentheses becomes false that can be useful but more often than not you'll want to loop over an `iterable` data type like an array.

Most languages have a `for loop` that can run some code for every object in the array or iterable data structure now in some cases a function may not have an output, called the `return` which is generally called a *void*.

### Recursion - Memory

An interesting thing about functions is that they can call themselves when a function calls itself it's called `recursion` because when done like this by default it will recurse forever creating an infinite loop that happens because when you call a function the programming language will put it into memory on what's known as the `call stack` which is a short-term chunk of memory for executing your code.

When a function keeps calling itself the language will keep pushing frames onto the call stack until you get a `stack overflow` error to avoid this your algorithm needs a `base condition` so it knows when to terminate the loop.

Another area of memory is the `heap` which unlike the call stack can grow and shrink based on how your application is used.


### Performance

When you write an algorithm you'll need to determine if it's any good and the system for doing that is called `big-o-notation` it's a standard format for approximating the performance of an algorithm at scale it may `reference`

- `time complexity` which is how fast your algorithm will run and
- `space complexity` which deals with how much memory is required to run it.


Developers have many different algorithm types at their disposal the most crude option is `brute force` where you might loop over every possible combination to hack somebody's credit card pin a more sophisticated approach might be `divide and conquer` like
`binary search` where you cut the problem in half multiple times until you find what you're looking for.

### Dynamic Programming

`dynamic programming`algorithms where a problem is broken down into multiple smaller sub-problems and the result of each computation is stored for later use using a technique called `memoization` that means if a function has already been called it will use the existing value instead of recomputing it again from scratch.

We have `greedy` algorithms that will make the choice that is most beneficial in the short term without considering the problem as a whole.

One example of this is `dijkstra`'s shortest path algorithm on the flip side we have `backtracking` algorithms which take a more incremental approach by looking at all the possible options like a rat and a maze exploring all the different potential paths.

## Paradigms

### Declarative

When it comes to implementing your code there are always multiple ways to get the job done one programming paradigm is `declarative` where your code describes what the program does and the outcome but doesn't care about things like control flow this style of programming is often associated with `functional languages`.

### Imperative

Other paradigm is `imperative` programming where your code uses statements like if and while providing explicit instructions about how to produce an outcome it's associated with `procedural` languages like C today most general purpose languages like Python, Javascript, Kotlin, Swift and so on are `multi-paradigm` which means they support all these options at the same time in addition to `object-oriented programming`.

### `Object-oriented programming`

The idea behind **OOP** is that you use classes to write a blueprint for the data or objects in your code.  
A `class` can encapsulate variables which are commonly called properties as well as functions which are usually called methods in this context it's a common way to organize and reuse code because classes can share behaviors between each other through `inheritance` where a subclass can extend and override the behaviors of the parent class and it opens the door to all kinds of other ideas called `design patterns`.

A class by itself doesn't actually do anything instead it's used to `instantiate` objects which are actual chunks of data that live in your computer's memory.

Often you'll want to `reference` the same object over and over again in your code when data is long-lived it can't go in the call stack instead, to it's stored in the heap, it also allows you to pass objects by reference which means you can use the same object in multiple variables without increasing the memory footprint because it always points to the same chunk of memory in the heap.

## Threads

If we go back to the CPU that we talked about in the beginning you'll notice that it contains multiple `threads` a thread takes the physical CPU core and breaks it into virtual cores that allow it to run code simultaneously there are some programming languages that support `parallelism` where you can write code that literally executes on two different threads at the same time.

However many languages out there are only single threaded but that doesn't mean they can't do two things at the same time instead they implement `concurrency` models like an event loop or co-routines that can pause or delay the normal execution of code to handle multiple jobs on a single thread at the same time,

## Network

In modern computing we're rarely working with the `bare metal` CPU and RAM instead we work in the cloud with a `virtual machine` which is just a piece of software that simulates hardware that allows us to take really big computers and split them up into a bunch of smaller virtual computers.

These machines are the backbone of the internet and are connected via the internet protocol each machine has a unique `IP` address to identify it on the network.

IP address is usually alias to a `URL` that is registered in a global database called the Domain Name Service (`DNS`).

To establish a connection the two computers will perform a `TCP` handshake which will allow them to exchange messages called `packets` on top of that there's usually a Security Layer Like (`SSL`) to encrypt and decrypt the messages over the network.

Now the two computers can securely share data with the HyperText Transfer Protocol (`HTTP`) the client may request a web page then the server will respond with some html.

Modern servers provide a standardized way for a client to request data which is called an Application Programming Interface (`API`) the most common architecture is `REST` where URLs are mapped to different data entities available on the server.

> 108