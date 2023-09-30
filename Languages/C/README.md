---
title: C - Basics
tags: studies, programação
use: Documentation
languages: C
dependences: NULL
---
> Focused in the python roadmap and cs50x course (c)

- Struct
- Nul (`nil`) x `NULL`


---

## Static Variables

**What are Static Variables?**

A static variable is a type of variable that retains its value across multiple function calls or throughout the lifetime of a program. Unlike local variables, which are created and destroyed every time a function is called, static variables persist and maintain their value between function invocations. They are often used to store information that needs to be shared or preserved across function calls within the same scope.

**How Do Static Variables Work?**

Static variables are typically declared within a function or method, and they are initialized only once during the program's lifetime. When a function containing a static variable is called for the first time, the variable is initialized, and its value is retained in memory. Subsequent calls to the same function do not reinitialize the static variable but continue to use its existing value.

Here's an example in C:

```c
#include <stdio.h>

void countCalls() {
    static int counter = 0;  // Static variable
    counter++;
    printf("Function has been called %d times.\n", counter);
}

int main() {
    countCalls();  // Output: Function has been called 1 times.
    countCalls();  // Output: Function has been called 2 times.
    countCalls();  // Output: Function has been called 3 times.

    return 0;
}
```

When to Use Static Variables

Static variables are beneficial in various scenarios, such as:

1. **Counting Function Calls:** As shown in the example above, static variables can be used to keep track of how many times a function is called, which can be helpful for debugging or implementing specific behaviors after a certain number of calls.

2. **Caching Data:** Static variables are often used to cache data that takes time to compute but remains constant throughout the program's execution. By storing the computed result in a static variable, you can avoid recomputation.

3. **Preserving State:** When you need to maintain state information across function calls without exposing it globally, static variables offer an elegant solution. They encapsulate the state within the function or class, making it more modular and easier to manage.

Static variables are a powerful feature in programming that allows data to persist across function calls or throughout a program's execution. They are particularly useful for scenarios where you need to maintain state, count events, or cache data efficiently. However, it's essential to use them judiciously and understand their scope to avoid unexpected behavior in your code. When employed correctly, static variables can enhance the clarity and efficiency of your programs.

## Variadic Functions

[Variadic functions](https://www.geeksforgeeks.org/variadic-function-templates-c/) are [functions](https://www.geeksforgeeks.org/functions-in-c/) that can take a variable number of [arguments](https://www.geeksforgeeks.org/command-line-arguments-in-c-cpp/). In [C programming](https://www.geeksforgeeks.org/c/), a variadic function adds flexibility to the program. It takes one fixed argument and then any number of arguments can be passed. The variadic function consists of at least one fixed variable and then an ellipsis(…) as the last parameter.

**Syntax:**

```
int function_name(data_type variable_name, ...);
```

Values of the passed arguments can be accessed through the [header file](https://www.geeksforgeeks.org/header-files-in-c-cpp-and-its-uses/) named as:

```
#include <stdarg.h>
```

[<stdarg.h>](https://www.geeksforgeeks.org/header-files-in-c-c-with-examples/) includes the following methods:

The main used elements, that are essential when working with variadic functions in C, enable you to access and manipulate variable arguments in a safe and controlled manner, making it possible to write functions that accept a variable number of arguments.

- `va_list args`:
   - `va_list` is a data type defined in the `<stdarg.h>` header.
   - It's used to declare a variable that will store the information needed to access the variable arguments passed to a variadic function, i.e. a list of values.

- `va_start(args, num)`:
   - `va_start` is a macro.
   - It initializes the `va_list` variable (`args`) to start processing the variable arguments.
   - The first argument is the `va_list` variable, and the second argument is the last named parameter before the ellipsis (`...`) in the function declaration. This parameter is used as a reference point to locate the variable arguments.

- `va_arg(args, type)`:
   - It retrieves the next argument of the specified type from the variable argument list.
   - The first argument is the `va_list` variable (`args`), and the second argument is the data type of the argument you want to retrieve.
   - It's crucial to specify the correct data type to ensure proper typecasting.

- `va_copy(va_list dest, va_list src)`:
	- This makes a copy of the variadic function arguments.

- `va_end(args)`:
   - It performs necessary cleanup after processing variable arguments.
   - It takes the `va_list` variable (`args`) as its argument and ensures that any resources allocated for handling variable arguments are released.


Here, **va\_list** holds the information needed by **va\_start**, **va\_arg**, **va\_end**, and **va\_copy**.

**Program 1:**

The following simple [C program](https://www.geeksforgeeks.org/c/) will demonstrate the working of the variadic function **AddNumbers()**:

```c
// C program for the above approach

#include <stdarg.h>
#include <stdio.h>

// Variadic function to add numbers
int AddNumbers(int n, ...)
{
	int Sum = 0;

	// Declaring pointer to the
	// argument list
	va_list ptr;

	// Initializing argument to the
	// list pointer
	va_start(ptr, n);

	for (int i = 0; i < n; i++)

		// Accessing current variable
		// and pointing to next one
		Sum += va_arg(ptr, int);

	// Ending argument list traversal
	va_end(ptr);

	return Sum;
}

// Driver Code
int main()
{
	printf("\n\n Variadic functions: \n");

	// Variable number of arguments
	printf("\n 1 + 2 = %d ",
		AddNumbers(2, 1, 2));

	printf("\n 3 + 4 + 5 = %d ",
		AddNumbers(3, 3, 4, 5));

	printf("\n 6 + 7 + 8 + 9 = %d ",
		AddNumbers(4, 6, 7, 8, 9));

	printf("\n");

	return 0;
}

```

**Output:** 

```
Variadic functions: 

 1 + 2 = 3 
 3 + 4 + 5 = 12 
 6 + 7 + 8 + 9 = 30
```

**Program 2:** Below is the C program consisting of the variadic function **LargestNumber()**:

```c
// C program for the above approach
#include <stdarg.h>
#include <stdio.h>

// Variadic function to find the largest number
int LargestNumber(int n, ...)
{
	// Declaring pointer to the
	// argument list
	va_list ptr;

	// Initializing argument to the
	// list pointer
	va_start(ptr, n);

	int max = va_arg(ptr, int);

	for (int i = 0; i < n-1; i++) {

		// Accessing current variable
		// and pointing to next
		int temp = va_arg(ptr, int);
		max = temp > max ? temp : max;
	}

	// End of argument list traversal
	va_end(ptr);

	return max;
}

// Driver Code
int main()
{
	printf("\n\n Variadic functions: \n");

	// Variable number of arguments
	printf("\n %d ",
		LargestNumber(2, 1, 2));

	printf("\n %d ",
		LargestNumber(3, 3, 4, 5));

	printf("\n %d ",
		LargestNumber(4, 6, 7, 8, 9));

	printf("\n");

	return 0;
}

```

**Output:** 

```
Variadic functions: 

 2 
 5 
 9
```


## Libraries

### Static x Dynamic

### `ar` commands

Is typically used for creating and manipulating static libraries in Unix-like operating systems, including Linux. A static library is a collection of object files (compiled code) bundled together into a single file that can be linked with a program at compile time.

Here's how you can use the `ar` command to create a static library:

1. **Compile Your Source Files**: First, you need to compile your source code files (the ones containing the functions you want to include in the library) into object files (`.o` files). For example:

   ```bash
   gcc -c -o function1.o function1.c
   gcc -c -o function2.o function2.c
   ```

2. **Create the Library**: Use the `ar` command to create the static library by bundling the object files together. The basic syntax is as follows:

   ```bash
   ar rcs libyourlibrary.a function1.o function2.o
   ```

   - `r`: Replace or add files to the archive.
   - `c`: Create the archive if it doesn't exist.
   - `s`: Add an index to the archive (this is optional but useful for faster linking).

   Replace `libyourlibrary.a` with the desired library name, and list all the object files you want to include in the library.

3. **Verify the Library**: You can use the `ar t` command to list the contents of the library:

   ```bash
   ar t libyourlibrary.a
   ```

4. **Link with Your Program**: To use the functions from the static library in your C program, you need to include the library when compiling. For example:

   ```bash
   gcc -o myprogram myprogram.c -L/path/to/library -lyourlibrary
   ```

   - `-L` specifies the directory where the library is located.
   - `-lyourlibrary` tells the linker to use `libyourlibrary.a`.

### Libtool

Is a utility designed to simplify the creation and management of shared libraries (also known as dynamic libraries) on Unix-like operating systems. Shared libraries are files that contain compiled code and data that multiple programs can use simultaneously. Unlike static libraries, shared libraries are loaded into memory at runtime, allowing multiple programs to share a single copy of the library, thus reducing memory usage and providing other benefits.

Here are the key aspects of Libtool:

1. **Abstraction of Platform Differences**: One of the primary purposes of Libtool is to abstract away the platform-specific details and complexities involved in building and using shared libraries. Different Unix-like systems (Linux, macOS, BSD, etc.) may have varying requirements and naming conventions for shared libraries. Libtool aims to provide a consistent interface for library management across these platforms.

2. **Creation of Shared Libraries**: Libtool facilitates the creation of shared libraries by wrapping the compilation and linking processes. It generates platform-specific shell scripts or commands that ensure the correct flags and options are used for creating shared libraries on the target system. This process includes handling compiler flags, versioning, and naming conventions.

3. **Versioning and Compatibility**: Shared libraries often have version information embedded in their filenames to manage compatibility. Libtool helps manage versioning by allowing developers to specify version numbers for libraries. It ensures that multiple versions of the library can coexist on the system without conflicts.

4. **Ease of Use**: Libtool provides a simplified and consistent command-line interface for building and linking shared libraries. Developers can use Libtool commands to compile and link their code without worrying about the specifics of different platforms.

5. **Support for Various Languages**: Libtool is not limited to C; it supports a wide range of programming languages. You can use Libtool for projects written in C, C++, Fortran, and other languages.

6. **Wrapper Libraries**: In some cases, Libtool generates small "wrapper" libraries (`.la` files) that contain information about how to link with the shared library. These wrapper libraries make it easier for other programs to link with the shared library without needing to understand all the platform-specific details.

Here's a basic example of using Libtool to create a shared library:

```bash
libtool --mode=compile gcc -c mylib.c -o mylib.lo
libtool --mode=link gcc -shared -o libmylib.la mylib.lo -version-info 1:0:0
```

In this example, `libtool` is used to compile `mylib.c` into a position-independent object file (`mylib.lo`) and then link it into a shared library (`libmylib.la`) with version information. The resulting `libmylib.so` (or equivalent) can be used by other programs.

Libtool is a valuable tool for developers working on multi-platform projects or projects that require shared libraries. It simplifies the process of creating and managing shared libraries, making it easier to ensure compatibility and ease of use across different Unix-like systems.