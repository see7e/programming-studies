---
title: File descriptor
tags: studies, programação
use: Documentation
languages: NULL
dependences: NULL
---
#REVISAR
# File descriptor

> [font](https://www.computerhope.com/jargon/f/file-descriptor.htm)

A **file descriptor** is a unique numeric identifier associated with an open resource, such as a file or network socket, in an operating system. It serves as a means to access and interact with that resource. File descriptors are essential for managing I/O operations in various programming and scripting languages.

Here's a more concise explanation with additional examples and updated information:

1. **Creation of File Descriptors:**
   - When a program requests to access a file or resource, the operating system's kernel performs the following actions:
     - Grants access to the requested resource.
     - Creates an entry in the global file table.
     - Provides the software with a file descriptor, which is a unique non-negative integer, to access that entry.

   For instance, file descriptors like 0, 12, or 567 may represent open files, and there is at least one file descriptor for each open resource on the system.

2. **Usage Across Operating Systems:**
   - File descriptors were initially introduced in Unix-based systems and are still extensively used in modern operating systems such as Linux, macOS, and BSD. In the Windows operating system, the equivalent concept is referred to as "file handles."

3. **File Descriptor Overview:**
   - When a process successfully opens a file, the kernel provides a file descriptor that points to an entry in its global file table. This entry contains critical information, including the file's inode (a unique identifier for a file), byte offset, and access permissions (read-only, write-only, etc.).

   ![File descriptor diagram](https://www.computerhope.com/jargon/f/file-descriptor.png)

4. **Standard Input (stdin), Standard Output (stdout), and Standard Error (stderr):**
   - In Unix-like systems, the first three file descriptors have predefined meanings:
     - Standard Input (stdin, file descriptor 0): The default input stream, typically used for reading data. In a terminal, this corresponds to keyboard input.
     - Standard Output (stdout, file descriptor 1): The default output stream, used for displaying regular program output. In a terminal, this represents the user's screen.
     - Standard Error (stderr, file descriptor 2): Reserved for error messages and is also displayed on the user's screen in a terminal.

5. **Redirecting File Descriptors:**
   - File descriptors can be manipulated in the command-line interface using shell commands, such as Bash. For instance, when executing the `find` command, successful output goes to stdout (file descriptor 1), while error messages are sent to stderr (file descriptor 2). You can redirect stderr to a special device called `/dev/null` to discard error messages and keep only the standard output.

     ```
     find / -name '*something*' 2>/dev/null
     ```

   - Understanding the distinction between stdout and stderr is crucial when working with program output. For instance, you can redirect stderr to stdout to process both types of output with a single command:

     ```
     find / -name '*something*' 2>&1 | grep 'something'
     ```

   In the command above, `2>&1` redirects standard error (file descriptor 2) to standard output (file descriptor 1), allowing `grep` to filter both types of output.

   For more examples of using file descriptors in Bash, refer to the [exec builtin command examples](https://www.computerhope.com/unix/bash/exec.htm#examples).

In summary, file descriptors are fundamental for managing resources in an operating system, and they play a crucial role in I/O operations and error handling when working with various programs and scripts.