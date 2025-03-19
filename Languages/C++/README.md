---
title: C++ - Developer Roadmap
tags: studies, programming
use: Documentation
languages: C++
dependences: NULL
---

> [!NOTE]
> This guide follows the [C++ Developer Roadmap](https://roadmap.sh/cpp)

# Introduction to C++

C++ is a general-purpose, high-performance programming language. It was developed by Bjarne Stroustrup at Bell Labs starting in 1979. C++ is an extension of the C programming language, adding features such as classes, objects, and exceptions. See [C vs C++](./c_vs_cpp.md)


## Why C++
C++ is a popular and widely used programming language for various reasons. Here are some of the reasons why you might choose to utilize C++:

### Performance
C++ is designed to provide high performance and efficiency. It offers fine-grained control over system resources, making it easier to optimize your software.

### Portability
C++ is supported on different computer architectures and operating systems, allowing you to write portable code that runs on various platforms without making major modifications.

### Object-Oriented Programming
C++ supports object-oriented programming (OOP) - a paradigm that allows you to design programs using classes and objects, leading to better code organization and reusability.

```cpp
class MyClass {
    public:
        void myFunction() {
            // Code here
        }
};

int main() {
    MyClass obj;
    obj.myFunction();
}
```

### Support for low-level and high-level programming
C++ allows you to write both low-level code, like memory manipulation, as well as high-level abstractions, like creating classes and using the Standard Template Library (STL).

```cpp
#include <iostream>
#include <vector>

int main() {
    // Low-level programming
    int number = 42;
    int* ptr_number = &number;

    // High-level programming
    std::vector<int> myVector = {1, 2, 3};
    for (const auto &i: myVector) {
        std::cout << i << std::endl;
    }
}
```

### Extensive Libraries
C++ offers a vast range of libraries and tools, such as the Standard Template Library (STL), Boost, and Qt, among others, that can aid in the development of your projects and make it more efficient.

### Combination with C language
C++ can be combined with C, offering the capabilities of both languages and allowing you to reuse your existing C code. By incorporating C++ features, you can enhance your code and improve its functionality.

### Active Community
C++ has been around for a long time and has a large, active community of users who contribute to the growth of the language, express new ideas, and engage in discussions that help develop the language further. This makes finding solutions to any problems you experience much easier.


## Basics of C++ Programming

Here are some basic components and concepts in C++ programming:

## Including Libraries

In C++, the same way as C, we use the `#include` directive to include libraries or header files into our program. For example, to include the standard input/output library, we write:

```cpp
#include <iostream>
```

## Main Function

The entry point of a C++ program is the `main` function. Every C++ program must have a `main` function:

```cpp
int main() {
    // Your code goes here
    return 0;
}
```

## Input/Output

To perform input and output operations in C++, we can use the built-in objects `std::cin` for input and `std::cout` for output, available in the `iostream` library. Here’s an example of reading an integer and printing its value:

```cpp
#include <iostream>

int main() {
    int number;
    std::cout << "Enter an integer: ";
    std::cin >> number;
    std::cout << "You entered: " << number << std::endl;
    return 0;
}
```

> [!TIP]
> Defined in the `<cstdio>` header file, `printf` and `scanf` functions can also be used for input/output operations in C++. Both returns integer values.
> 
> For `printf(const char* format, ...);`:
> -   On Success - the number of characters written
> -   On failure - a negative value
>
> For `scanf(const char* format, ...);`:
> -   If successful, it returns the number of receiving arguments successfully assigned.
> -   If a matching failure occurs before the first receiving argument was assigned, returns `0`.
> -   If input failure occurs before the first receiving argument was assigned, `EOF` is returned.


## Variables and Data Types

Data types in C++ are divided into four categories: Basic, Derived, User-defined and Special. Variables must be declared with a data type before they can be used: `int x;`

### Basic Data Types

Are built-in or primitive data types that are used to store simple values.

-   `int`: Integer type (e.g., 42)
-   `float`: Floating-point type (e.g., 3.14)
-   `double`: Double-precision floating-point type (e.g., 3.14159)
-   `char`: Character type (e.g., 'A')
-   `bool`: Boolean type (e.g., true or false)

### Derived Data Types

Are data types derived from basic types.

-   `arrays`: A collection of elements of the same data type
-   `pointers`: A variable that stores the memory address of another variable
-   `references`: An alias for a variable
-   `functions`: A block of code that performs a specific task

### User-defined Data Types

Custom data types created by the user according to their need.

-   `class`: A blueprint for creating objects
-   `struct`: A collection of variables of different data types
-   `union`: A data structure that stores different data types in the same memory location
-   `typedef`: A keyword used to create an alias for a data type
-   `using`: A keyword used to create an alias for a data type

### Special Data Types

Special data types in C++.

-   `void`: Represents the absence of type
-   `nullptr`: Represents a null pointer
-   `auto`: Automatically deduces the data type of a variable
-   `decltype`: Returns the data type of an expression
-   `enum`: A data type consisting of a set of named constants (unmutable)


## Control Structures

C++ provides control structures for conditional execution and iteration, such as `if`, `else`, `while`, `for`, and `switch` statements.

### If-Else Statement

```cpp
if (condition) {
    // Code to execute if the condition is true
} else {
    // Code to execute if the condition is false
}
```

### While Loop

```cpp
while (condition) {
    // Code to execute while the condition is true
}
```

### For Loop

```cpp
for (initialization; condition; update) {
    // Code to execute while the condition is true
}
```

### Switch Statement

```cpp
switch (variable) {
    case value1:
        // Code to execute if variable == value1
        break;
    case value2:
        // Code to execute if variable == value2
        break;
    // More cases...
    default:
        // Code to execute if variable does not match any case value
}
```

## Functions

Functions are reusable blocks of code that can be called with arguments to perform a specific task. Functions are defined with a return type, a name, a parameter list, and a body.

```cpp
ReturnType functionName(ParameterType1 parameter1, ParameterType2 parameter2) {
    // Function body ...
    return returnValue;
}
```

For example, here’s a function that adds two integers and returns the result:

```cpp
int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 4);
    printf("Result: %d\n", result);
    return 0;
}
```

This basic introduction to C++ should provide you with a good foundation for further learning. Explore more topics such as classes, objects, inheritance, polymorphism, templates, and the Standard Template Library (STL) to deepen your understanding of C++ and start writing more advanced programs.

Learn more from the following resources:

-   article [LearnC++](https://www.learncpp.com/)
-   video [C++ Full Course by freeCodeCamp](https://youtu.be/vLnPwxZdW4Y)