---
title: Garbage Collector Documentation
aliases:
    - /gc
    - /garbage-collector
    - /garbage-collector-documentation
tags: studies, programação
use: Documentation, Garbage Collector
languages: C
dependences: gc.h
author: Anirudh Rowjee
---

<details> <summary>Table of Contents</summary>

- [Garbage Collector Documentation](#garbage-collector-documentation)
  - [Introduction](#introduction)
  - [Usage](#usage)
  - [Example](#example)
  - [Functions](#functions)
    - [`void gc_init()`](#void-gc_init)
    - [`void* gc_malloc(size_t size)`](#void-gc_mallocsize_t-size)
    - [`void gc_free(void* ptr)`](#void-gc_freevoid-ptr)
    - [`void gc_collect()`](#void-gc_collect)
    - [`void push(object* obj)` and `object* pop()`](#void-pushobject-obj-and-object-pop)
    - [`void markObject(object* obj)`](#void-markobjectobject-obj)
  - [Garbage Collection Process](#garbage-collection-process)
  - [****Mark Roots**: This step identifies objects that are reachable from the root set, typically including objects currently in use. The garbage collector marks these objects as reachable**.](#mark-roots-this-step-identifies-objects-that-are-reachable-from-the-root-set-typically-including-objects-currently-in-use-the-garbage-collector-marks-these-objects-as-reachable)
  - [****Mark All**: All objects stored in the heap are traversed, marking them as reachable if they are still in use**.](#mark-all-all-objects-stored-in-the-heap-are-traversed-marking-them-as-reachable-if-they-are-still-in-use)
  - [****Sweep**: Unmarked (unreachable) objects are removed from memory, freeing up resources**.](#sweep-unmarked-unreachable-objects-are-removed-from-memory-freeing-up-resources)
  - [Best Practices](#best-practices)
  - [Limitations](#limitations)
  - [License](#license)
- [Core concepts](#core-concepts)
  - [Garbage Collection:](#garbage-collection)
  - [Mark-and-Sweep Algorithm:](#mark-and-sweep-algorithm)
  - [Data Structures:](#data-structures)
  - [Initialization and Cleanup:](#initialization-and-cleanup)
  - [Memory Allocation and Deallocation:](#memory-allocation-and-deallocation)
  - [Stack Management:](#stack-management)
  - [Root Set:](#root-set)
  - [Best Practices and Limitations:](#best-practices-and-limitations)

</details>

---

#to_review 
# Garbage Collector Documentation

## Introduction

This C code implements a simple mark-and-sweep garbage collector to automatically manage memory allocation and deallocation, helping to prevent memory leaks and memory-related issues in a C program. This documentation provides an overview of how the garbage collector works and how to effectively use it in your programs.

## Usage

To use the garbage collector in your C program, follow these steps:

1. Include the `gc.h` header file in your source code.
2. Call `gc_init()` at the beginning of your program to initialize the garbage collector.
3. Use `gc_malloc(size_t size)` to allocate memory dynamically.
4. Use `gc_free(void* ptr)` to free memory when it is no longer needed.

The garbage collector will automatically manage memory and periodically reclaim memory that is no longer in use.

## Example

```c
#include "gc.h"
#include <stdio.h>

int main() {
    gc_init();

    int* dynamicInt = (int*)gc_malloc(sizeof(int));
    *dynamicInt = 42;

    // No need to manually free memory; the garbage collector will handle it

    return 0;
}
```

## Functions

### `void gc_init()`

This function initializes the garbage collector, setting up data structures for memory management.

### `void* gc_malloc(size_t size)`

Allocate memory of the specified size using the garbage collector. Returns a pointer to the allocated memory. No need to manually free the memory; the garbage collector will do this.

### `void gc_free(void* ptr)`

Frees memory allocated by `gc_malloc`. It marks the memory as unallocated, allowing the garbage collector to reclaim it when necessary.

### `void gc_collect()`

This function manually triggers the garbage collection process. It identifies and reclaims memory that is no longer in use.

### `void push(object* obj)` and `object* pop()`

These functions allow you to push and pop objects onto/from the garbage collector's stack. They are used internally and are not typically needed for regular use.

### `void markObject(object* obj)`

Marks a specific object as reachable, ensuring that it will not be collected during the next garbage collection cycle.

## Garbage Collection Process

## ****Mark Roots**: This step identifies objects that are reachable from the root set, typically including objects currently in use. The garbage collector marks these objects as reachable**.

## ****Mark All**: All objects stored in the heap are traversed, marking them as reachable if they are still in use**.

## ****Sweep**: Unmarked (unreachable) objects are removed from memory, freeing up resources**.

## Best Practices

- Always initialize the garbage collector with `gc_init` at the beginning of your program.
- Use `gc_malloc` for dynamic memory allocation instead of `malloc`.
- Don't manually free memory allocated with `gc_malloc` using `free`.
- Call `gc_collect` if you want to manually trigger garbage collection.
- Avoid creating unnecessary objects or holding onto objects for longer than necessary to optimize memory usage.

## Limitations

- The garbage collector provided here is a basic implementation and may not be suitable for complex applications.
- The garbage collector does not handle cyclic references.

## License

This code and documentation are provided under an open-source license. You are free to use, modify, and distribute them in accordance with the terms of the license.

---

Please note that while this garbage collector can help simplify memory management in C programs, it is not a replacement for proper memory management practices. Always be mindful of memory allocation and deallocation in your programs, and use the garbage collector as an aid to reduce the risk of memory-related bugs.

```c
// This code implements a simple mark-and-sweep garbage collector for a generalist program in C.
// The garbage collector is responsible for automatically freeing memory that is no longer in use
// by the program, preventing memory leaks and other memory-related issues.

// To use the garbage collector, simply include the gc.h header file in your program and call
// gc_init() at the beginning of your program to initialize the garbage collector. Then, use
// gc_malloc() and gc_free() to allocate and free memory as needed. The garbage collector will
// automatically track which memory is in use and which is not, and free any unused memory
// periodically.

// Note that the garbage collector is not a replacement for good memory management practices.
// It is still important to allocate and free memory carefully and efficiently in your program,
// and to avoid creating unnecessary objects or holding onto objects for longer than necessary.
// However, the garbage collector can help simplify memory management in some cases and reduce
// the risk of memory-related bugs.

// For more information on how the garbage collector works and how to use it effectively, see
// the documentation for the gc.h header file and the accompanying example programs.

#include <stdlib.h>
#include <stdio.h>

#define STACK_MAX 256

// Define a struct to represent a garbage collector object
typedef struct object {
    unsigned char marked;
    struct object* next;
} object;

// Define a struct to represent the garbage collector itself
typedef struct {
    object* stack[STACK_MAX];
    int stackSize;

    object* firstObject;

    int numObjects;
    int maxObjects;
} VM;

// Define a global garbage collector instance
VM* gc;

// Define a function to initialize the garbage collector
void gc_init() {
    gc = (VM*)malloc(sizeof(VM));
    gc->stackSize = 0;
    gc->firstObject = NULL;
    gc->numObjects = 0;
    gc->maxObjects = 8;
}

// Define a function to create a new object
object* newObject() {
    if (gc->numObjects == gc->maxObjects) gc_collect();

    object* obj = (object*)malloc(sizeof(object));
    obj->marked = 0;

    obj->next = gc->firstObject;
    gc->firstObject = obj;

    gc->numObjects++;

    return obj;
}

// Define a function to push an object onto the garbage collector's stack
void push(object* obj) {
    if (gc->stackSize == STACK_MAX) {
        printf("Stack overflow!\n");
        exit(1);
    }

    gc->stack[gc->stackSize++] = obj;
}

// Define a function to pop an object from the garbage collector's stack
object* pop() {
    if (gc->stackSize == 0) {
        printf("Stack underflow!\n");
        exit(1);
    }

    return gc->stack[--gc->stackSize];
}

// Define a function to mark an object as reachable
void mark(object* obj) {
    if (obj->marked) return;

    obj->marked = 1;

    push(obj);
}

// Define a function to mark all objects reachable from the root set
void markRoots() {
    for (int i = 0; i < gc->stackSize; i++) {
        mark(gc->stack[i]);
    }
}

// Define a function to mark all objects reachable from a given object
void markObject(object* obj) {
    if (obj == NULL) return;

    mark(obj);
}

// Define a function to mark all objects reachable from the heap
void markAll() {
    object* obj = gc->firstObject;
    while (obj != NULL) {
        markObject(obj);
        obj = obj->next;
    }
}

// Define a function to sweep all unmarked objects from the heap
void sweep() {
    object** obj = &gc->firstObject;
    while (*obj != NULL) {
        if (!(*obj)->marked) {
            object* unreached = *obj;
            *obj = unreached->next;
            free(unreached);
            gc->numObjects--;
        } else {
            (*obj)->marked = 0;
            obj = &(*obj)->next;
        }
    }
}

// Define a function to perform garbage collection
void gc_collect() {
    int numObjects = gc->numObjects;

    markRoots();
    markAll();
    sweep();

    gc->maxObjects = gc->numObjects * 2;

    printf("Collected %d objects, %d remaining.\n", numObjects - gc->numObjects, gc->numObjects);
}

// Define a function to allocate memory using the garbage collector
void* gc_malloc(size_t size) {
    object* obj = newObject();
    void* ptr = (void*)(obj + 1);
    return ptr;
}

// Define a function to free memory using the garbage collector
void gc_free(void* ptr) {
    object* obj = (object*)((unsigned char*)ptr - sizeof(object));
    obj->marked = 0;
}
```

---

# Core concepts

Certainly! To improve the code and your understanding of garbage collection in C, it's essential to grasp the core concepts involved. Here are the key concepts to study and understand:

## Garbage Collection:
   - **Garbage Collection (GC)** is the process of automatically identifying and reclaiming memory that is no longer in use by the program. It helps prevent memory leaks and manage memory efficiently.

## Mark-and-Sweep Algorithm:
   - The code you provided implements a simple Mark-and-Sweep garbage collection algorithm. It consists of two main phases: marking and sweeping.
   - **Marking** involves identifying and marking objects in memory that are still reachable (in use) from the root set (objects in current use). It typically starts from the root set and traverses all reachable objects.
   - **Sweeping** involves cleaning up memory by removing unmarked (unreachable) objects and reclaiming their memory. It effectively frees up memory that is no longer needed.

## Data Structures:
   - **Object**: In this code, the `object` struct represents a garbage collector object. It contains information about whether an object is marked and a reference to the next object in the linked list.
   - **VM (Virtual Machine)**: The `VM` struct represents the garbage collector itself and contains data structures like a stack for managing objects, the first object in the heap, and counters for the number of objects and the maximum number of objects.

## Initialization and Cleanup:
   - `gc_init()`: This function initializes the garbage collector. It sets up the initial data structures and should be called at the beginning of your program.
   - `gc_collect()`: This function manually triggers the garbage collection process, marking and sweeping objects.

## Memory Allocation and Deallocation:
   - `gc_malloc(size_t size)`: This function is used to allocate memory dynamically. It creates new objects, and memory is allocated from the heap. No manual memory deallocation is required.
   - `gc_free(void* ptr)`: This function is used to free memory allocated with `gc_malloc`. It marks the memory as unallocated but doesn't immediately release it. The memory is only released during the next garbage collection cycle.

## Stack Management:
   - `push(object* obj)`: Pushes an object onto the garbage collector's stack. This is part of the marking phase.
   - `pop()`: Pops an object from the stack, used during the marking phase.

## Root Set:
   - The root set is a collection of objects that are known to be in use by the program. In the code, the root set is typically managed manually, and objects in the root set are marked as reachable during the marking phase.

## Best Practices and Limitations:
   - Ensure that you always initialize the garbage collector with `gc_init`.
   - Use `gc_malloc` for memory allocation and avoid using `malloc`.
   - Do not manually free memory allocated with `gc_malloc`.
   - Be aware of the limitations of this simple garbage collection implementation, such as not handling cyclic references.

To improve the code and your understanding, you might want to study more advanced garbage collection algorithms (e.g., generational, copying, reference counting), handle more complex data structures, and address the limitations of this basic implementation. Additionally, consider learning about memory profiling tools and techniques for memory optimization in C programs.