---
title: A Fresh Start
tags:
  - studies
  - programação
use: Documentation, Roadmap
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [Intro](#intro)
- [Roadmap Mind Map](#roadmap-mind-map)
- [Studies List](#studies-list)
  - [42 related topics](#42-related-topics)

</details>

---

#to_review #to_translate

> [!INFO] 
> [101 Code Concepts](./101_code_concepts.md)
> [Usefull links ](links.md) 

# Intro
> based on [Programação para Iniciantes](https://www.youtube.com/playlist?list=PLdsnXVqbHDUc7htGFobbZoNen3r_wm3ki) (pt-br)
> and https://roadmap.sh/computer-science

# Roadmap Mind Map

![cs-canvas](./canvas/cs-canvas.canvas)

# Studies List 

Here's an updated table that includes the additional topics and breaks down your schedule for each day of the week:

| Day of the Week | Morning                             | Afternoon                                      | Evening                         |
|-----------------|-------------------------------------|------------------------------------------------|---------------------------------|
| Monday          | Software Architecture                | Virtualization                                | Low-Level Programming (C - 42) |
| Tuesday         | APIs                                | GitHub Actions and Docker                     | Memory Management and Garbage Collection |
| Wednesday       | Authentication Systems (LDAP, OAuth, SAML) | Low-Level Programming (C - 42)          | Sockets and Networking         |
| Thursday        | Backend Development (Go, Python)    | Virtualization                                | Operating Systems (Kernel, Userland) |
| Friday          | Virtualization                       | GitHub Actions and Docker                     | Code Cohesion and Coupling     |
| Saturday        | Low-Level Programming (C - 42)       | Code Diagnosis (Debugging)    | -    |
| Sunday (Relax)  | -                   | -                            | -            |


## 42 related topics 

1. **C Programming:** Understanding the C programming language is crucial, as most low-level projects at 42 are done in C. Focus on data types, pointers, memory management, and the standard library functions.

2. **Memory Management:** Learn about memory allocation, pointers, and dynamic memory management using functions like `malloc` and `free`.

3. **Bit Manipulation:** Study bitwise operations and bit manipulation techniques, which are often used in low-level programming for tasks like optimizing code and handling hardware registers.

4. **Assembly Language:** Familiarize yourself with assembly language, as some projects may require writing inline assembly or understanding assembly code for system calls and optimization.

5. **Operating System Fundamentals:** Gain knowledge about how operating systems work, including process management, file systems, and system calls.

6. **File I/O:** Learn how to read and write files at a low level using functions like `open`, `read`, and `write`.

7. **Data Structures:** Understand data structures like linked lists, stacks, and queues, which are often used in low-level projects.

8. **System Calls:** Study the system calls of the operating system you're working on (e.g., Linux system calls) to interact with the kernel and perform various tasks.

9. **Debugging:** Master debugging techniques and tools for low-level code, like using `gdb` for debugging C and assembly code.

10. **Compilation Process:** Learn about the compilation process, including the preprocessor, compiler, assembler, linker, and how they transform source code into executable files.

11. **Makefiles:** Understand how to create and use Makefiles for building and managing projects with multiple source files.

12. **Hardware Concepts:** Familiarize yourself with hardware-related concepts, such as registers, memory management units, and system architecture.

13. **Optimization Techniques:** Explore methods for optimizing code for performance, including loop unrolling, inline assembly, and using compiler-specific flags.

14. **Low-Level Libraries:** Get to know low-level libraries like the Standard C Library (libc) and system-specific libraries (e.g., the Linux API) that can help in your projects.


> [!NOTE]
> Currently listing all that I want to read/study before writing
> Work:
> - APIs
> - Backend (Go, Python)
> - Systems Architecture
> - Authentication Systems (LDAP, OAuth, SAML)
> - Azure Cloud
> 
> 42:
> - Algorithms (C)
> - Data Structures
> - Linux / Unix / Shell / POSIX
> - Understanding C Compilation
> - Memory Management, Garbage Collection
> 
> Myself:
> - Sockets
> - Threads
> - Time to Live (TTL)
> - Networking (TCP/IP, UDP, HTTP, HTTPS, WebSocket, REST, SOAP, RPC)
> - Operating Systems
>   - Kernel, Device Drivers
>   - Userland
> - Code Cohesion
> - Code Coupling
> - Code Diagnosis (Debugging)
>   - Log Levels: Debug, Info, Warning, Error, Critical

---

> [!TIP]
> to implement
> - Using `type-hints` in Python code improves clarity and understanding.
>   ```python
>   def greeting(name: str) -> str:
>     return 'Hello ' + name
>   ```
> 	- `docstrings` can be used to document functions, methods, classes, and modules, and tools like > Auto `docstring` can assist in generating them.
> 	- use of `mkdocs` alongside of `docstrings`

---

> - SOLID
> - CRUD
> - pcre [re(oniguruma), re2] / icu - regex
> - cpython q= `ifdef MS_WINDOWS` > `PYErr_SetFromWindosErr(err.ws);`
> - preprocessamento em C
> - libuv (node.js)
> - deno x node.js
> - openssl
> - abi - applcation bin interface
> - xml <-> jsn (marcheling / unmarsh)
> - cyton (.pyx) - FFI function interface
> - PONTOS FORTES LIGUAGES
>   - construção de ferramentas de adm/infra (cli, scripts, automação)
>   - Alacritty (terminal)
> 	- o que muda de uma para a outra?
> 		- seleção de apps
> 		- forma de configuração 
> 		- gerenciamento de pacotes
> 		- ecosistema
> 	- [ArchWiki](https://wiki.archlinux.org/)
> - daemons
> - linguagens 
> 	- virtual env ou asdf
> 	- interpretadores (o que é uma linguagem inerpretada)
> 	- compiladores (o que é uma linguagem compilada)
> 	- debugger (como um debugger funciona e como configurar)
> 	- libs / custom libs
