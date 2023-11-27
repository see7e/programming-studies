---
title: Go - Basics
tags: studies, programação
use: Documentation
languages: Go
dependences: NULL
---

<details> <summary>Table of Contents 🔖</summary>

- [Go - Basics](#go---basics)
  - [Compilation](#compilation)
  - [Typing system](#typing-system)
  - [Performance](#performance)
- [Basic Types](#basic-types)
  - [Variables](#variables)
  - [Short Variable Declaration](#short-variable-declaration)
  - [Same Line Declarations](#same-line-declarations)
- [Which Type Should I Use?](#which-type-should-i-use)
- [Constants](#constants)
  - [Computed Constants](#computed-constants)
- [Formatting Strings in Go](#formatting-strings-in-go)
  - [Examples](#examples)
    - [Interpolate the default representation](#interpolate-the-default-representation)
    - [Interpolate a string](#interpolate-a-string)
    - [Interpolate an integer in decimal form](#interpolate-an-integer-in-decimal-form)
    - [Interpolate a decimal](#interpolate-a-decimal)
- [Conditionals](#conditionals)
  - [Operators](#operators)
  - [Branchless](#branchless)
  - [The initial statement of an if block](#the-initial-statement-of-an-if-block)
  - [Why would I use this?](#why-would-i-use-this)
- [Functions](#functions)
  - [Multiple return values](#multiple-return-values)
  - [Named return values](#named-return-values)
  - [Early returns / Guard clauses](#early-returns--guard-clauses)
- [Loops](#loops)
  - [1. `for` Loop](#1-for-loop)
  - [2. `range` Loop](#2-range-loop)
  - [Infinite Loops](#infinite-loops)
  - [Breaking and Continuing](#breaking-and-continuing)
  - [Nested Loops](#nested-loops)
- [Data Structures](#data-structures)
  - [Structs](#structs)
    - [Anonymous Structs](#anonymous-structs)
  - [Nested Structs](#nested-structs)
  - [When should you use an anonymous struct?](#when-should-you-use-an-anonymous-struct)
  - [Embedded Structs](#embedded-structs)
- [(Struct) Methods](#struct-methods)
- [Interfaces](#interfaces)
  - [Key points about Go interfaces](#key-points-about-go-interfaces)

</details>

---

# Go - Basics
> following [Go Programming](https://www.youtube.com/watch?v=un6ZyFkqFKo) by [bootdotdev](https://www.youtube.com/channel/UC9HOZ53gnHP3f_b-wixS74g)

## Compilation

Go is a compiled language, so we need to compile it before running it.

```bash
go build main.go
```

This will create an executable file named `main` (or `main.exe` on Windows). In terms of efficiency, Go code is compiled faster than other compiled languages, like C or C++. This is because Go is a simpler language, with less features. But it's still a compiled language, so it's faster than interpreted languages like Python or JavaScript.

![compiled vs interpreted|300](https://i.imgur.com/ovHaWmS.jpg)


## Typing system

Go is a statically typed language, which means that we need to declare the type of a variable before we can use it. This is different from dynamically typed languages like Python or JavaScript, where we don't need to declare the type of a variable before using it.

> Go enforces strong and static typing, meaning variables can only have a single type. A `string` variable like "hello world" can not be changed to an `int`, such as the number `3`.
> 
> One of the biggest benefits of strong typing is that errors can be caught at "compile time". In other words, bugs are more easily caught ahead of time because they are detected when the code is compiled before it even runs.
> 
> Contrast this with most interpreted languages, where the variable types are dynamic. Dynamic typing can lead to subtle bugs that are hard to detect. With interpreted languages, the code _must_ be run to catch syntax and type errors. (sometimes in production if you are unlucky 😨)
> 
> ## Concatenating strings
> 
> Two strings can be [concatenated](https://en.wikipedia.org/wiki/Concatenation) with the `+` operator. Because Go is strongly typed, it won't allow you to concatenate a string variable with a numeric variable.
> 
> ## Assignment
> 
> We'll be using simple [basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) for the Textio API. This is how our users will communicate to us who they are and how many features they are paying for with each request to our API.
> 
> The code on the right has a type error. Change the type of `password` to a string (but use the same numeric value) so that it can be concatenated with the `username` variable.

## Performance

> Go programs are fairly lightweight. Each program includes a small amount of "extra" code that's included in the executable binary. This extra code is called the [Go Runtime](https://go.dev/doc/faq#runtime). One of the purposes of the Go runtime is to cleanup unused memory at runtime.
> 
> In other words, the Go compiler includes a small amount of extra logic in every Go program to make it easier for developers to write code that's memory efficient.
> 
> ### Comparison
> 
> As a general rule Java programs use _more_ memory than comparable Go programs because Go doesn't use an entire virtual machine to run its programs, just a small runtime. The Go runtime is small enough that it is included directly in each Go program's compiled machine code.
> 
> As another general rule Rust and C++ programs use slightly _less_ memory than Go programs because more control is given to the developer to optimize memory usage of the program. The Go runtime just handles it for us automatically.
> 
> ## Idle memory usage
> 
> ![idle memory](https://miro.medium.com/max/1400/1*Ggs-bJxobwZmrbfuoWGpFw.png)
> 
> In the chart above, [Dexter Darwich compares the memory usage](https://medium.com/@dexterdarwich/comparison-between-java-go-and-rust-fdb21bd5fb7c) of three _very_ simple programs written in Java, Go, and Rust. As you can see, Go and Rust use _very_ little memory when compared to Java.

In the case of Java the JVM handles the garbage collection, but in Go the garbage collection is handled by the Go runtime. Go runtinme is a small amount of extra code that's included in every Go program. This extra code is included in the executable binary.

---

# Basic Types

Go's basic variable types are:

- `string` (text)
- `int` (integer) [`int8`, `int16`, `int32`, `int64`]
- `bool` (boolean) [`true`, `false`]
- floats (floating point) [`float32`, `float64`]
- complex (complex numbers) [`complex64`, `complex128`]
- `byte` (alias for `uint8`)
- `rune` (alias for `int32`)
- `uint` (unsigned integer) [`uint8`, `uint16`, `uint32`, `uint64`]
- `uintptr` (unsigned integer large enough to store the uninterpreted bits of a pointer value)

> We talked about `string`s and `int`s previously, and those two types should be fairly self-explanatory. A `bool` is a boolean variable, meaning it has a value of `true` or `false`. The [floating point](https://en.wikipedia.org/wiki/Floating-point_arithmetic) types (`float32` and `float64`) are used for numbers that are not integers -- that is, they have digits to the right of the decimal place, such as `3.14159`. The `float32` type uses 32 bits of precision, while the `float64` type uses 64 bits to be able to more precisely store more digits. Don't worry too much about the intricacies of the other types for now. We will cover some of them in more detail as the course progresses.

`rune` is an alias for `int32` and is used to represent a Unicode code point. A `byte` is an alias for `uint8` and is used to represent a single byte of data. A `uint` is an unsigned integer, meaning it can only be positive. The `uintptr` type is an unsigned integer large enough to store the uninterpreted bits of a pointer value.

The size (8, 16, 32, 64, 128, etc) indicates how many bits in memory will be used to store the variable. The default `int` and `uint` types are just aliases that refer to their respective 32 or 64 bit sizes depending on the environment of the user.

The standard sizes that should be used unless the developer has a specific need are:

-   `int`
-   `uint`
-   `float64`
-   `complex128`

## Variables

> Variables are declared using the `var` keyword. For example, to declare a variable called `number` of type `int`, you would write:

```go
var number int
```

To declare a variable called `pi` to be of type `float64` with a value of `3.14159`, you would write:

```go
var pi float64 = 3.14159
```

The value of an initialized variable with no assignment will be its [zero value](https://tour.golang.org/basics/12).

```go
func main() {
	// initialize variables here
  var (
    smsSendingLimit int
    costPerSMS float64
    hasPermission bool
    username string
  )
  
	fmt.Printf("%v %f %v %q\n", smsSendingLimit, costPerSMS, hasPermission, username)
}
```

**Variables in Go must be used. If you declare a variable and don't use it, the compiler will throw an error**. This is to prevent developers from accidentally declaring variables that they don't use.

## Short Variable Declaration

> Inside a function (even the main function), the `:=` short assignment statement can be used in place of a `var` declaration. The `:=` operator infers the type of the new variable based on the value.
> 
> ```go
> var empty string
> ```
> 
> Is the same as
> 
> ```go
> empty := ""
> ```
> 
> ```go
> numCars := 10 // inferred to be an integer
> 
> temperature := 0.0 // temperature is inferred to be a floating point value because it has a decimal point
> 
> var isFunny = true // isFunny is inferred to be a boolean
> ```
> 
> Outside of a function (in the [global/package scope](https://dave.cheney.net/2017/06/11/go-without-package-scoped-variables)), every statement begins with a keyword (`var`, `func`, and so on) and so the `:=` construct is not available.
> 
> To declare a variable without specifying an explicit type (either by using the `:=` syntax or `var = expression` syntax), the variable's type is _inferred_ from the value on the right hand side.
> 
> When the right hand side of the declaration is typed, the new variable is of that same type:
> 
> ```go
> var i int
> j := i // j is also an int
> ```
> 
> However, when the right hand side is a literal value (an untyped numeric constant like `42` or `3.14`), the new variable will be an `int`, `float64`, or `complex128` depending on its precision:
> 
> ```go
> i := 42           // int
> f := 3.14         // float64
> g := 0.867 + 0.5i // complex128
> ```

## Same Line Declarations

> We can declare multiple variables on the same line:
> 
> ```go
> mileage, company := 80276, "Tesla"
> 
> // is the same as
> 
> mileage := 80276
> company := "Tesla"
> ```

> [!INFO]
> Some types can be converted the following way:
> 
> ```go
> temperatureFloat := 88.26
> temperatureInt := int64(temperatureFloat)
> ```
> 
> Casting a float to an integer in this way [truncates](https://techterms.com/definition/truncate) the floating point portion.

---

# Which Type Should I Use?

> With so many types for what is essentially just a number, developers coming from languages that only have one kind of `Number` type (like JavaScript) may find the choices daunting.
> 
> ## Prefer "default" types
> 
> A problem arises when we have a `uint16`, and the function we are trying to pass it into takes an `int`. We're forced to write code riddled with type casts like `int(myUint16)`.
> 
> This style of development can be slow and annoying to read. When Go developers stray from the “default” type for any given type family, the code can get messy quickly.
> 
> Unless you have a good reason to, stick to the following types:
> 
> -   `bool`
> -   `string`
> -   `int`
> -   `uint32`
> -   `byte`
> -   `rune`
> -   `float64`
> -   `complex128`
> 
> ## When should I use a more specific type?
> 
> When you're super concerned about performance and memory usage.
> 
> That’s about it. The only reason to deviate from the defaults is to squeeze out every last bit of performance when you are writing an application that is resource-constrained. (Or, in the special case of `uint64`, you need an absurd range of unsigned integers).
> 
> You can [read more on this subject here](https://blog.boot.dev/golang/default-native-types-golang/) if you'd like, but it's not required.

---

# Constants

> Constants are declared like variables but use the `const` keyword. **Constants can't use the `:=` short declaration syntax**. Can be character, string, boolean, or numeric values. They _can not_ be more complex types like slices, maps and structs, which are > types we will explain later.
>
> ```go
> const pi = 3.14159
> const isFunny = true
> const hello = "hello"
> ```

They dont need the type declaration because they are always the same type. They can't be changed, so they are always the same type.

## Computed Constants

> Constants must be known at compile time. More often than not they will be declared with a static value:
> 
> ```go
> const myInt = 15
> ```
> 
> However, constants _can be computed_ so long as the computation can happen at _compile time_.
> 
> For example, this is valid:
> 
> ```go
> const firstName = "Lane"
> const lastName = "Wagner"
> const fullName = firstName + " " + lastName
> ```
> 
> That said, you _cannot_ declare a constant that can only be computed at run-time.

---

# Formatting Strings in Go

Go follows the [printf tradition](https://cplusplus.com/reference/cstdio/printf/) from the C language. In my opinion, string formatting/interpolation in Go is currently _less_ elegant than JavaScript and Python.

-   [fmt.Printf](https://pkg.go.dev/fmt#Printf) - Prints a formatted string to [standard out](https://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr).
-   [fmt.Sprintf()](https://pkg.go.dev/fmt#Sprintf) - Returns the formatted string

## Examples

These formatting verbs work with both `fmt.Printf` and `fmt.Sprintf`:

| Verb | Description                                                            |
| ---- | ---------------------------------------------------------------------- |
| `%v` | The default representation of the value                                |
| `%s` | The string representation of the value                                 |
| `%d` | A decimal representation of the value                                  |
| `%f` | A floating point representation of the value                           |
| `%t` | The word `true` or `false`                                             |
| `%q` | A double-quoted string safely escaped with Go syntax                   |
| `%p` | The base 16 notation of a pointer, with leading `0x`                   |
| `%b` | The base 2 representation of a value                                   |
| `%o` | The base 8 representation of a value                                   |
| `%x` | The base 16 representation of a value, with lower-case letters for a-f |
| `%X` | The base 16 representation of a value, with upper-case letters for A-F |
| `%U` | The Unicode format: `U+1234`, `U+10AC`                                 |
| `%T` | The type of the value                                                  |
| `%%` | A literal percent sign `%`                                             |

### Interpolate the default representation

The `%v` variant prints the Go syntax representation of a value. You can usually use this if you're unsure what else to use. That said, it's better to use the type-specific variant if you can.

```go
s := fmt.Sprintf("I am %v years old", 10)
// I am 10 years old

s := fmt.Sprintf("I am %v years old", "way too many")
// I am way too many years old
```

### Interpolate a string

```go
s := fmt.Sprintf("I am %s years old", "way too many")
// I am way too many years old
```

### Interpolate an integer in decimal form

```go
s := fmt.Sprintf("I am %d years old", 10)
// I am 10 years old
```

### Interpolate a decimal

```go
s := fmt.Sprintf("I am %f years old", 10.523)
// I am 10.523000 years old

// The ".2" rounds the number to 2 decimal places
s := fmt.Sprintf("I am %.2f years old", 10.523)
// I am 10.52 years old
```

> If you're interested in all the formatting options, feel free to take a look at the `fmt` package's [docs here](https://pkg.go.dev/fmt#hdr-Printing).


# Conditionals

`if` statements in Go don't use parentheses around the condition like JavaScript or Python. The opening curly brace `{` must be on the same line as the `if` statement. The closing curly brace `}` must be on its own line.

```go
if height > 4 {
    fmt.Println("You are tall enough!")
}
```

`else if` and `else` are supported as you would expect:

```go
if height > 6 {
    fmt.Println("You are super tall!")
} else if height > 4 {
    fmt.Println("You are tall enough!")
} else {
    fmt.Println("You are not tall enough!")
}
```

## Operators

| Common Operators | Description              |
| ---------------- | ------------------------ |
| ==               | Equal to                 |
| ` != `           | Not equal to             |
| ` < `            | Less than                |
| ` > `            | Greater than             |
| ` <= `           | Less than or equal to    |
| ` >= `           | Greater than or equal to |
| ` && `           | And                      |
| \|\|             | Or                       |

| Bitwise Operators | Description            |
| ----------------- | ---------------------- |
| ` & `             | And                    |
| \|                | Or                     |
| ` ^ `             | Xor                    |
| ` &^ `            | And not                |
| ` << `            | Left shift             |
| ` >> `            | Right shift            |
| ` <<= `           | Left shift assignment  |
| ` >>= `           | Right shift assignment |
| ` &= `            | And assignment         |
| \|=               | Or assignment          |
| ` ^= `            | Xor assignment         |
| ` &^= `           | And not assignment     |
| ` ++ `            | Increment              |
| ` -- `            | Decrement              |
| ` += `            | Add assignment         |
| ` -= `            | Subtract assignment    |
| ` *= `            | Multiply assignment    |
| ` /= `            | Divide assignment      |
| ` %= `            | Modulo assignment      |


## Branchless

Theres's not ternary operator in Go. A branchless approach typically involves using bitwise operations or arithmetic operations to achieve conditional behavior without explicit branching. In Go, you can achieve a branchless approach using bitwise operations in some cases.

Here's a simple example using bitwise operations for a boolean condition:

```go
package main

import "fmt"

func main() {
    condition := true

    trueValue := "TrueValue"
    falseValue := "FalseValue"

    result := (1 & int(condition)) * len(trueValue) + (0 & int(^condition)) * len(falseValue)

    fmt.Println(result)
}
```

Explanation:

- `int(condition)` converts the boolean `condition` to an integer (1 for true, 0 for false).
- `(1 & int(condition))` evaluates to 1 if the condition is true and 0 otherwise.
- `(^condition)` flips the bits of the condition.
- `(0 & int(^condition))` evaluates to 0 if the condition is true and 0 otherwise.
- The expressions `(1 & int(condition)) * len(trueValue)` and `(0 & int(^condition)) * len(falseValue)` result in the lengths of the corresponding strings when the condition is true or false, respectively.
- The final result is the sum of these two expressions.

This is a contrived example, and in many cases, a branchless approach might not be necessary or might not result in more readable or maintainable code. It's important to weigh the benefits of branchless code against readability and maintainability, as code clarity is often more important than micro-optimizations.

## The initial statement of an if block

An `if` conditional can have an "initial" statement. The variable(s) created in the initial statement are _only_ defined within the scope of the `if` body.

```go
if INITIAL_STATEMENT; CONDITION {
  // do something
}
```

## Why would I use this?

This is just some syntactic sugar that Go offers to shorten up code in some cases. For example, instead of writing:

```go
length := getLength(email)
if length < 1 {
    fmt.Println("Email is invalid")
}
```

We can do:

```go
if length := getLength(email); length < 1 {
    fmt.Println("Email is invalid")
}
```

Not only is this code a bit shorter, but it also removes `length` from the parent scope, which is convenient because we don't need it there - we only need access to it while checking a condition.

---

# Functions

Functions in Go can take zero or more arguments. **Arguments (variables, functions, etc) are passed by value, meaning that the function receives a copy of the argument, not the original argument**. This is different from languages like JavaScript, where objects are passed by reference.

> To make Go code easier to read, the variable type comes _after_ the variable name.

For example, the following function:

```go
func add(x int, y int) int {
  return x+y
}
```

Here, `func sub(x int, y int) int` is known as the "function signature" and it accepts two integer parameters and returns another integer. The function signature can be shortened to: `func sub(x, y int) int {...}` because both parameters are of the same type.

Go functions can achieve a certain level of complexity. For example, the expression `f func(func(int, int) int, int) int` is declaring a function signature in Go programming language syntax. Let's break down the components:

1. **Function Name:**
   - The function is named `f`.

2. **Function Parameters:**
   - The function takes two parameters:
     - The first parameter is a function itself, denoted as `func(int, int) int`. This means it's a function that takes two integers as parameters and returns an integer.
     - The second parameter is a single integer.

3. **Return Type:**
   - The function returns an integer.

Putting it all together, the `f` function takes two parameters. The first parameter is expected to be a function, **Go needs to know if a function is received by another function how many parameters the argument function takes and what type of value it returns**, in this case it that takes two integers and returns an integer, and the second parameter is an integer. The function itself returns an integer.

Here's a simplified example to illustrate how you might use this function:

```go
package main

import "fmt"

// Function signature: f func(func(int, int) int, int) int
func f(g func(int, int) int, x int) int {
    // Call the function g with two integers and store the result
    result := g(3, 4)

    // Add the result to the second parameter x
    finalResult := result + x

    // Return the final result
    return finalResult
}

func main() {
    // Define a function that adds two integers
    add := func(a, b int) int {
        return a + b
    }

    // Call the f function with the add function and an integer
    result := f(add, 5)

    // Print the result
    fmt.Println(result) // Output: 12 (3 + 4 + 5)
}
```

In this example, the `f` function takes the `add` function and the integer `5` as parameters. It calls the `add` function with the values `3` and `4` (as specified in the `g(3, 4)` line), then adds the result to `5`. The final result is `12`, which is printed

> [!INFO]
> Just to remember the arguments are passed by value, meaning that the function receives a copy of the argument, not the original argument. This is different from languages like JavaScript, where objects are passed by reference.
> 
> ```go
> func main(){
>     x := 5
>     increment(x)
> 
>     fmt.Println(x)
>     // still prints 5, because the increment function received a copy of x
> }
> 
> func increment(x int){
>     x++
> }
> ```
> 
> A way to solve this is to update the increment function and pass the argument as a pointer: `increment(&x)`
>
> ```go	
> func increment(x *int){
>     *x++
> }
> ```
> 
> Or return the value and assign it to the variable: `x = increment(x)`

## Multiple return values

Go functions can return multiple values. For example, the following function returns two integers:

```go
func addAndSubtract(x int, y int) (int, int) {
  return x+y, x-y
}
```
These return values can be assigned to variables or ignored by using the `_` character, known as the "blank identifier" (following the declared function above):

```go
func main() {
  add, sub := addAndSubtract(10, 5)
  fmt.Println(add, sub) // 15 5

  add, _ = addAndSubtract(10, 5)
  fmt.Println(add) // 15

  _, sub = addAndSubtract(10, 5)
  fmt.Println(sub) // 5
}
```

## Named return values

Go functions can also return named values. This helps to improve the readability of the code. For example, the following function returns two integers:

```go
func addAndSubtract(x int, y int) (add int, sub int) {
  add = x+y
  sub = x-y
  return // implicit return add, sub
  // but we can also use return add, sub
  // return add, sub
}
```

## Early returns / Guard clauses

Go functions can return early. This is useful for checking for errors or other conditions that would cause the function to fail. For example, the following function returns early if the `email` is empty:

```go
func validateEmail(email string) error {
  if email == "" {
    return errors.New("Email can't be empty")
  }
  // do other validation here
  return nil
}

// or

func divide(x, y float64) (float64, error) {
  if y == 0 {
    return 0, errors.New("Can't divide by zero")
  }
  return x / y, nil
}
```

---

# Loops

In Go, there are two primary types of loops: the `for` loop and the `range` loop. Let's take a closer look at both:

## 1. `for` Loop

The basic syntax for a `for` loop in Go is as follows:

```go
for initialization; condition; post {
    // Loop body
}
```

- `initialization`: Executed before the first iteration.
- `condition`: Evaluated before each iteration. If false, the loop exits.
- `post`: Executed after each iteration.

Here's an example of a simple `for` loop that prints numbers 1 to 5:

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 5; i++ {
        fmt.Println(i)
    }
}
```

## 2. `range` Loop

The `range` keyword is used to iterate over elements of an array, slice, string, map, or channel.

```go
for index, value := range iterable {
    // Loop body
}
```

- `index`: Index or key of the current iteration (not applicable for all types).
- `value`: Value at the current index or key.
- `iterable`: Array, slice, string, map, or channel being iterated.

Example using a slice:

```go
package main

import "fmt"

func main() {
    numbers := []int{1, 2, 3, 4, 5}

    for index, value := range numbers {
        fmt.Printf("Index: %d, Value: %d\n", index, value)
    }
}
```

## Infinite Loops

Go allows you to create infinite loops using a `for` loop without any conditions:

```go
package main

import "fmt"

func main() {
    // Infinite loop
    for {
        fmt.Println("This will run forever!")
    }
}
```

## Breaking and Continuing

- The `break` statement is used to exit a loop prematurely.
- The `continue` statement is used to skip the rest of the loop body and start the next iteration.

Example using `break`:

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 10; i++ {
        if i > 5 {
            break // exit the loop when i is greater than 5
        }
        fmt.Println(i)
    }
}
```

Example using `continue`:

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 5; i++ {
        if i%2 == 0 {
            continue // skip even numbers
        }
        fmt.Println(i)
    }
}
```

## Nested Loops

Go allows you to nest loops inside other loops. For example, the following code prints a multiplication table:

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 10; i++ {
        for j := 1; j <= 10; j++ {
            fmt.Printf("%d * %d = %d\n", i, j, i*j)
        }
    }
}
```

---
> [!ATTENTION]
> Go isn't a purely object-oriented programming (OOP) language like Java or Python, but it does support certain object-oriented programming principles. It follows a different paradigm known as "**composition over inheritance**" and is often referred to as a "**concurrent**" or "procedural" language with support for some OOP features.
> While Go incorporates some concepts from OOP, it doesn't have all the traditional features of classic OOP languages. It's designed to be simple, efficient, and easy to use for concurrent programming. The emphasis is on composition, interfaces, and practicality.
> 
> Here are some key points regarding Go's approach to object-oriented programming:
> 
> 1. **Structs for Data Structures**
>    1. Nested
>    2. Emmbbeded
> 2. **Methods**
> 3. **Interfaces**

# Data Structures

## Structs

Go, just like C, has a `struct` type. A `struct` is a collection of fields. For example, we can create a `struct` to represent a person:

```go
type Person struct {
  name string
  age int
  father *Person
  mother *Person
}
```

They can have fields of any type, including other `struct`s. In the above scenario, we have a `Person` `struct` that has a `name` and an `age`. We also have two other fields that are pointers to other `Person` `struct`s. This allows us to create a family tree of `Person` `struct`s. The reason of `father` and `mother` being pointers is to avoid infinite loops. If we don't use pointers, we will have a `Person` `struct` that has a `father` field that has a `father` field that has a `father` field, and so on.

The attributes of the `struct` are called "fields", and they have two parts: a **key** (name) and a **type** (value) separated by a space. The `struct` is defined using the `type` keyword, followed by the name of the `struct` (`Person`), followed by the keyword `struct`, and then the fields inside curly braces `{}`.
An intatiation example of the above struct is:

```go
// witohout the fields values
person := Person{}

// with the fields names
person := Person{name: "John", age: 30, father: &father, mother: &mother}

// or without the fields names
person := Person{"John", 30, &father, &mother}

// or as function parameter
func getName(p Person) {
  fmt.Println(p.name, p.age, p.father, p.mother)
}
```

To access the fields of a `struct`, we use the `.` operator:

```go
func main() {
  person := Person{name: "John", age: 30, father: &father, mother: &mother}
  fmt.Println(person.name) // John
  fmt.Println(person.age) // 30
  fmt.Println(person.father) // &{Jack 60 <nil> <nil>}
  fmt.Println(person.mother) // &{Jill 55 <nil> <nil>}
}
```

### Anonymous Structs

Go allows you to create anonymous `struct`s. These are `struct`s that don't have a name. They are useful when you need to create a `struct` that is only used in one place. **They create the `struct` and instantiate it in the same point**. Here's an example:

```go
package main

import "fmt"

func main() {
    person := struct {
        name string
        age  int
    } {
        name: "John",
        age:  30,
    }

    fmt.Println(person) // {John 30}
}
```

Often used in situations where a named type would be overkill. For instance, you might see them used as parameters or return values in functions, especially for cases where the structure is simple and specific to that particular function. Here's the above example but used as a return type for a function:

```go
package main

import "fmt"

func getPerson() struct { /*func argument*/
    Name string
    Age  int
} {
    return struct { /*struct definition*/
        
        Name string
        Age  int
    }{ /*struct instantiation*/
        Name: "Alice",
        Age:  25,
    }
}

func main() {
    person := getPerson()
    fmt.Println("Name:", person.Name)
    fmt.Println("Age:", person.Age)
}
```

In this case, the `getPerson` function returns an anonymous struct. The advantage is that you don't have to create a named type just for this function's return type.

Anonymous structs are concise and convenient, but keep in mind that they lack reusability. If you find yourself needing the same structure in multiple places, it might be more appropriate to define a named struct type.

## Nested Structs

They are used to represent more complex data structures. For example:

```go
package main

import "fmt"

// Address struct
type Address struct {
    Street  string
    City    string
    Country string
}

// Person struct with a nested Address struct
type Person struct {
    Name    string
    Age     int
    Contact Address // Nested struct
}

func main() {
    // Create an instance of the Person struct with a nested Address
    person := Person{
        Name: "Alice",
        Age:  25,
        Contact: Address{ // note that the Contact field receives the name of the already defined Address struct
            Street:  "123 Main St",
            City:    "Anytown",
            Country: "USA",
        },
    }

    // Access fields from both structs
    fmt.Println("Name:", person.Name)
    fmt.Println("Age:", person.Age)
    fmt.Println("Street:", person.Contact.Street)
    fmt.Println("City:", person.Contact.City)
    fmt.Println("Country:", person.Contact.Country)
}
```

## When should you use an anonymous struct?

In general, _prefer named structs_. Named structs make it easier to read and understand your code, and they have the nice side-effect of being reusable. I sometimes use anonymous structs when I _know_ I won't ever need to use a struct again. For example, sometimes I'll use one to create the shape of some JSON data in HTTP handlers.

If a struct is only meant to be used once, then it makes sense to declare it in such a way that developers down the road won’t be tempted to accidentally use it again.

You can read more about [anonymous structs here](https://blog.boot.dev/golang/anonymous-structs-golang/) if you're curious.


## Embedded Structs

Go allows you to embed one `struct` inside another `struct`. It's a form of composition where the fields and methods of the embedded struct become part of the outer struct. Embedded structs are also sometimes referred to as "anonymous fields.". For example:

```go
package main

import "fmt"

// Car struct
type Car struct {
  Make string
  Model string
  Height int
  Width int
}

// Car model struct
type Tesla struct {
  Car // embedded struct
  Range int
}

// Person struct
type Person struct {
    Name string
    Age  int
}

// Employee struct embeds the Person struct
type Employee struct {
    Person   // Embedded struct
    JobTitle string
}

func main() {
    // Create an instance of the Tesla struct
    car := Tesla{
        Car: Car{ // note that the Car field receives the Car struct type itself
            Make:   "Tesla",
            Model:  "Model S",
            Height: 60,
            Width:  80,
        },
        Range: 300,
    }

    // Access fields from the embedded Car struct
    fmt.Println("Make:", car.Make)
    fmt.Println("Model:", car.Model)
    fmt.Println("Height:", car.Height)
    fmt.Println("Width:", car.Width)
    fmt.Println("Range:", car.Range)    

    fmt.Println("===============================")

    // Create an instance of the Employee struct
    emp := Employee{
        Person:   Person{Name: "John", Age: 30},
        JobTitle: "Developer",
    }

    // Access fields from the embedded Person struct
    fmt.Println("Name:", emp.Name)
    fmt.Println("Age:", emp.Age)
    fmt.Println("Job Title:", emp.JobTitle)

}
```

> [!INFO]
> Emebedded structs are commomly used in user credential where you have some information that is public and some that is private. And deppending on the context some information (like a password hash) can be ommited i.e. nullified. As shown in the example below:
>
> ```go
> package main
> 
> import (
> 	"fmt"
> 	//"crypto/sha256" // This line to use the sha256 hash function
> )
> 
> // PublicInfo struct contains public user information
> type PublicInfo struct {
> 	Username string
> 	Email    string
> }
> 
> // PrivateInfo struct contains private user information
> type PrivateInfo struct {
> 	PasswordHash string
> 	SecretToken  string
> }
> 
> // User struct embeds both public and private information
> type User struct {
> 	PublicInfo  // Embedded public information
> 	PrivateInfo // Embedded private information
> }
> 
> // NewUser creates a new user with default public and private information
> func NewUser(username, email, password string) *User {
> 	// For simplicity, this example uses a simple hash for the password
> 	passwordHash := hashPassword(password)
> 
> 	return &User{
> 		PublicInfo: PublicInfo{
> 			Username: username,
> 			Email:    email,
> 		},
> 		PrivateInfo: PrivateInfo{
> 			PasswordHash: passwordHash,
> 			SecretToken:  generateSecretToken(),
> 		},
> 	}
> }
> 
> // hashPassword hashes the user's password (not suitable for production)
> func hashPassword(password string) string {
> 	// Implementation of password hashing goes here
> 	return fmt.Sprintf("%x", hash)
> }
> 
> // generateSecretToken generates a random secret token (not suitable for production)
> func generateSecretToken() string {
> 	// Implementation of secret token generation goes here
> 	return "randomSecretToken"
> }
> 
> func main() {
> 	// Create a new user
> 	user := NewUser("john_doe", "john@example.com", "secretpassword")
> 
> 	// Access public information
> 	fmt.Println("Username:", user.Username)
> 	fmt.Println("Email:", user.Email)
> 
> 	// Access private information
> 	// Note: In a real-world scenario, you would typically control access to these fields
> 	// based on the context and permissions of the user or application.
> 	fmt.Println("Password Hash:", user.PasswordHash)
> 	fmt.Println("Secret Token:", user.SecretToken)
> }
> ```


# (Struct) Methods

In Go, **a method is a function associated with a particular type, known as the method's receiver type**. Struct methods allow you to associate functions with structs, enabling you to encapsulate behavior related to the struct. **Methods in Go can be defined for named types, including structs**. This promotes encapsulation and code organization. Whether to use value receivers or pointer receivers depends on the desired semantics and the need for modifications to the original struct.

Here's a basic example of a **method associated with a struct**:

```go
package main

import "fmt"

// Rectangle struct with width and height
type Rectangle struct {
    Width  float64
    Height float64
}

// Area method for calculating the area of the rectangle
// func (struct_name struct_type) method_name() return_type {
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

func main() {
    // Create an instance of the Rectangle struct
    rectangle := Rectangle{Width: 3, Height: 4}

    // Call the Area method
    area := rectangle.Area()

    fmt.Println("Area:", area)
}
```

In this example, the `Rectangle` struct has a method called `Area`, which calculates and returns the area of the rectangle. The method is associated with the `Rectangle` struct using the `(r Rectangle)` syntax, where `r` is the receiver parameter.

Key points about struct methods in Go:

1. **Receiver Type:**
   - The receiver type is the type on which the method is defined. In the example, `Rectangle` is the receiver type.

2. **Value Receiver vs. Pointer Receiver:**
   - Methods can have either a value receiver or a pointer receiver.
   - Value receiver (`func (r Rectangle) Area() float64`): The method operates on a copy of the struct. Changes made inside the method do not affect the original struct.
   - Pointer receiver (`func (r *Rectangle) Scale(factor float64)`): The method operates directly on the original struct. Changes made inside the method affect the struct.

3. **Value Semantics vs. Pointer Semantics:**
   - Value semantics: Methods with value receivers operate on a copy of the struct, maintaining immutability.
   - Pointer semantics: Methods with pointer receivers operate directly on the original struct, allowing modifications.

Here's an example **with a pointer receiver**:

```go
package main

import "fmt"

// Rectangle struct with width and height
type Rectangle struct {
    Width  float64
    Height float64
}

// Scale method for scaling the dimensions of the rectangle
func (r *Rectangle) Scale(factor float64) {
    r.Width *= factor
    r.Height *= factor
}

func main() {
    // Create an instance of the Rectangle struct
    rectangle := Rectangle{Width: 3, Height: 4}

    // Call the Scale method
    rectangle.Scale(2)

    fmt.Println("Width:", rectangle.Width)
    fmt.Println("Height:", rectangle.Height)
}
```

In this example, the `Scale` method has a pointer receiver (`(r *Rectangle)`), and it modifies the original `Rectangle` struct by scaling its dimensions.


# Interfaces

In Go, an interface is a type that specifies a set of method signatures. A type in Go is said to satisfy an interface if it implements all the methods declared by that interface. Unlike some other languages, Go interfaces are implicitly satisfied, meaning that you don't need to explicitly declare that a type implements an interface.

Here's a basic example of an interface:

1. Interface declaration
2. Structs that will implement the interface
3. Methods of the struct
4. Interface functions

```go
package main

import "fmt"

// INTERFACE: Shape defines a method for calculating the area
type Shape interface {
    Area() float64
}

// STRUCT: Circle, implements the Shape interface
type Circle struct {
    Radius float64
}

// (Circle) METHOD: Area for calculating the area of the circle
func (c Circle) Area() float64 {
    return /*pi*/3.14 * c.Radius * c.Radius
}

// STRUCT: Rectangle, implements the Shape interface
type Rectangle struct {
    Width  float64
    Height float64
}

// (Rectangle) METHOD: Area for calculating the area of the rectangle
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

// INTERFACE FUNCTION: printArea takes a Shape and prints the area
func printArea(s Shape) {
    fmt.Println("Area:", s.Area())
}

func main() {
    // Create instances of Circle and Rectangle
    circle := Circle{Radius: 2}
    rectangle := Rectangle{Width: 3, Height: 4}

    // Call the printArea function with Circle and Rectangle instances
    fmt.Println("Passing the struct instance")
    printArea(circle)
    printArea(rectangle)

    // or passing the struct directly
    ftm.Println("Passing the struct directly")
    printArea(Circle{Radius: 2})
    printArea(Rectangle{Width: 3, Height: 4})
}
```

In this example:

- The `Shape` interface declares a method `Area()` that returns a float64.
- The `Circle` and `Rectangle` types both implement the `Shape` interface by providing their own `Area` method implementations.

The `printArea` function takes a parameter of type `Shape` and calls its `Area` method. This function can accept any type that satisfies the `Shape` interface.

## Key points about Go interfaces

1. **Implicit Satisfaction:**
   - A type implicitly satisfies an interface if it implements all the methods declared by the interface.

2. **Interface Values:**
   - An interface value is represented by a pair of values: a concrete value and a dynamic type.
   - An interface with a `nil` concrete value is called a "nil interface."

3. **Empty Interface (`interface{}`):**
   - The empty interface represents any type, as it has no methods. It's commonly used when you want to work with values of unknown types.

```go
// Example of an empty interface
func describe(i interface{}) {
    fmt.Printf("(%v, %T)\n", i, i)
}

func main() {
    describe(42)
    describe("hello")
    describe([]int{1, 2, 3})
}
```

4. **Type Assertion:**
   - Type assertion is used to extract the underlying value of an interface. It returns two values: the underlying value and a boolean indicating whether the assertion was successful.

```go
// Type assertion example
var i interface{} = "hello"
s, ok := i.(string)
if ok {
    fmt.Println(s)
}
```

5. **Interface Composition:**
   - Interfaces can be composed of multiple smaller interfaces, allowing you to build up larger interfaces.

```go
// Interface composition example
type Writer interface {
    Write([]byte) (int, error)
}

type Closer interface {
    Close() error
}

// File interface is composed of Writer and Closer
type File interface {
    Writer
    Closer
}
```

Go interfaces provide a powerful mechanism for achieving polymorphism and abstraction while maintaining simplicity and flexibility. They play a central role in enabling decoupling between components in Go programs.

---
