/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 14:50:34 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/11 13:07:37 by gabrodri        ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stddef.h>
# include <string.h>
# include <unistd.h>
# include <stdlib.h>

/* Is often used to create linked lists in C */
typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

/* Is a data structure used to store information about the start and length of a
 * substring or segment within a larger string. It typically serves as a data
 * structure to represent substrings extracted from a larger string during
 * string processing or parsing operations. Is particularly useful when working
 * with text processing tasks where you need to manipulate and extract
 * substrings from a larger text or data */
typedef struct structs_split_next
{
	size_t	start;
	size_t	length;
}	t_split_next;

/* Part 1 */

/* Determine whether a given integer corresponds to an alphabetic character. It
 * is commonly used in C programs that need to process text data, such as
 * parsers, compilers, and text editors. */
int				ft_isalpha(int c);

/* Verifies if a given integer is a nummeric character */
int				ft_isdigit(int c);

/* Is commonly used in string manipulation functions. Is used to check
 * whether a character is alphanumeric in the ASCII character set. */
int				ft_isalnum(int c);

/* Takes an integer `c` as input. The return statement directly evaluates the
 * condition `(c >= 0 && c <= 127)` */
int				ft_isascii(int c);

/* Verifies if the string input is a printable character */
int				ft_isprint(int c);

/* This function returns the lengh of the string */
unsigned int	ft_strlen(const char *s);

/* It fills a given block of memory with a specified value up to a certain
 * length */
void			*ft_memset(void *block, int value, size_t leng);

/* This function is used to clear a specific amount of memory by setting all the
 * bytes within that memory range to zero. It's commonly used to clear sensitive
 * data or initialize memory buffers before use, especially in cases where
 * security and predictability of data are important */
void			ft_bzero(void *block, size_t n);

/* Used to copy a specified number of bytes from a source memory location to a
 * target memory location */
void			*ft_memcpy(void *target, const void *source, size_t n);

/* Is a versatile memory copy function that ensures safe copying of data even
 * when there is an overlap between source and destination memory regions. This
 * makes it suitable for various applications where data integrity is essential,
 * such as working with arrays, strings, or dynamic memory allocation */
void			*ft_memmove(void *dst, const void *src, size_t len);

/* Provides a safe way to copy strings, preventing buffer overflows by 
 * specifying a size limit. It returns the length of the source string, which
 * can be useful in various string manipulation tasks */
unsigned int	ft_strlcpy(char *dest, const char *src, unsigned int size);

/* Provides a safe way to concatenate strings while preventing buffer overflows
 * by specifying a size limit. It returns the total length of the concatenated
 * string, which can be useful for various string manipulation tasks */
unsigned int	ft_strlcat(char *dest, const char *src, unsigned int size);

/* Is a simple and efficient way to convert a lowercase letter to uppercase.
 * However, it only works for single characters and does not handle strings. */
int				ft_toupper(int c);

/*  Is a simple and efficient way to convert a uppercase letter to lowercase.
 * However, it only works for single characters and does not handle strings. */
int				ft_tolower(int c);

/* Provides a straightforward way to search for a character in a string and
 * return a pointer to its first occurrence. If the character is not found, it
 * returns NULL. Additionally, it can be used to check for the presence of the
 * null terminator in the string when c is '\0' */
char			*ft_strchr(const char *s, int c);

/* Provides a simple way to search for the last occurrence of a character in a
 * string and returns a pointer to it. If the character is not found, it returns
 * NULL. Additionally, it can be used to check for the presence of the null
 * terminator in the string when c is '\0' */
char			*ft_strrchr(const char *s, int c);

/* Is used to compare two strings up to a specified number of characters. It
 * returns 0 if the strings are equal up to that point, a negative value if s1
 * is lexicographically smaller than s2, and a positive value if s1 is
 * lexicographically greater than s2. It allows for controlled string
 * comparison, which can be useful in sorting or searching algorithms */
int				ft_strncmp(const char *s1, const char *s2, size_t n);

/* Provides a way to search for a specific character within a memory block of a
 * specified size. It returns a pointer to the first occurrence of the character
 * or NULL if the character is not found in the memory block. This function is
 * commonly used in low-level memory manipulation tasks */
void			*ft_memchr(const void *s, int c, size_t n);

/* Provides a way to compare two blocks of memory up to a specified number of
 * bytes. It returns 0 if the memory blocks are equal up to that point, a
 * negative value if the memory block pointed to by s1 is lexicographically
 * smaller than the one pointed to by s2, and a positive value if s1 is 
 * lexicographically greater than s2. This function is commonly used in low-lvl
 * memory comparison tasks */
int				ft_memcmp(const void *s1, const void *s2, size_t n);

/* Provides a way to search for a substring within a larger string while
 * limiting the search to a specified maximum length. It returns a pointer to
 * the first occurrence of little within big (within the specified len) or NULL
 *if little is not found */
char			*ft_strnstr(const char *big, const char *little, size_t len);

/* Provides a way to convert a string representing an int into the actual int
 * value, considering signs and leading whitespace characters. It's a commonly
 * used function for converting user input or text-based data into numerical
 * values in C programming */
int				ft_atoi(const char *str);

/* Is used to allocate memory for an array of elements and initialize that
 * memory to zero. It's a useful function when you want to ensure that allocated
 * memory starts with all zero values */
void			*ft_calloc(size_t nmemb, size_t size);

/* Provides a way to create a duplicate of a given string, allocating memory for
 * the duplicate and copying the contents of the original string into it. This
 * function is useful when you need to work with a copy of a string and want to
 * manage memory allocation and deallocation */
char			*ft_strdup(const char *s);

/* Part 2 */
/* Is a utility function for extracting substrings from input strings, taking
 * into account the starting index and the desired length. It handles memory
 * allocation and ensures that the extracted substring is null-terminated,
 * making it a valid C string */
char			*ft_substr(char const *s, unsigned int start, size_t len);

/* Is used to concatenate (join) two strings, `s1` and `s2`, into a single
 * string. It allocates memory for the result, copies both input strings into
 * it, and returns a pointer to the concatenated string. This function is useful
 * when you need to combine strings into a single string dynamically allocated
 * in memory */
char			*ft_strjoin(const char *s1, const char *s2);

/* Is used to remove specified leading and trailing characters from a string,
 * creating a new dynamically allocated string in the process. It's useful for
 * cleaning up strings and is often used in situations where input data needs to
 * be sanitized */
char			*ft_strtrim(const char *s1, const char *set);

/* Works together with `h_count_words` and `ft_strndup` to split a string into
 * an array of words based on a specified separator character `c`. They handle
 * memory allocation and duplication of substrings, resulting in an array of
 * dynamically allocated strings representing the words in the input string */
char			**ft_split(char const *s, char c);

/* Is used to convert an integer into a string. It allocates memory for the
 * resulting string, handles negative numbers, and reverses the digits to create
 * the correct string representation. It's a versatile function for converting
 * integers into strings for various purposes */
char			*ft_itoa(int n);

/* Is used to apply a custom function to each character of a string and create a
 * new string with the modified characters. It duplicates the input string to
 * avoid modifying the original, processes each character individually, and
 * returns a pointer to the resulting string. This function is useful for
 * various string transformation tasks where character-wise modification is
 * required */
char			*ft_strmapi(char const *s, char (*f)(unsigned int, char));

/* Is used to apply a custom function to each character of a string while
 * providing the character and its index as arguments to the function. This
 * allows for in-place modifications of the characters in the string. It's a
 * useful function for various string processing tasks where you need to access
 * and modify characters with knowledge of their positions in the string */
void			ft_striteri(char *s, void (*f)(unsigned int, char *));

/* Is a simple function used to write a single character to a specified file
* descriptor. It relies on the `write` system call to perform the output
* operation, making it a versatile utility for character-based output to various
* destinations, including standard output and files */
void			ft_putchar_fd(char c, int fd);

/* Is a utility function used to write a null-terminated string to a specified
 * file descriptor. It relies on the `write` system call to perform the output
 * operation, making it a versatile tool for string-based output to various
 * destinations, including standard output and files */
void			ft_putstr_fd(char *s, int fd);

/* Is a utility function used to write a null-terminated string followed by a
 * newline character to a specified file descriptor. It relies on the `write`
 * system call to perform the output operation, making it a versatile utility
 * for outputting strings with proper line breaks to various destinations,
 * including standard output and files */
void			ft_putendl_fd(const char *s, int fd);

/* Is a utility function used to write an integer to a specified `fd`. It
 * converts the integer to a string representation, handles negative integers,
 * and prevents buffer overflow. This function is useful for outputting integers
 * to various destinations, including standard output and files, while ensuring
 * proper formatting and error handling */
void			ft_putnbr_fd(int n, int fd);

/* Bonus Part */
/* Is used to create a new node with integer data and add it to a linked list */
t_list			*ft_lstnew(void *content);

/* Is used to add a new node to the front of a linked list */
void			ft_lstadd_front(t_list **alst, t_list *new);

/* Is used to calculate and return the number of nodes (elements) in a singly-
 - linked list. It takes a pointer to the head of the list (`t_list *lst`) as
 * its argument and returns an integer representing the size of the list */
int				ft_lstsize(t_list *lst);

/* Is used to find and return a `ptr` to the last node in a singly-linked list.
 * It takes a `ptr` to the head of the list (`t_list *lst`) as its argument and
 * returns a `ptr` to the last node in the list. If the list is empty (i.e.,
 * `lst` is `NULL`), the function returns `NULL` */
t_list			*ft_lstlast(t_list *lst);

/* Is used to add a new node to the end (tail) of a singly-linked list */
void			ft_lstadd_back(t_list **alst, t_list *new);

/* Is used to delete (remove and deallocate memory for) a single node in a
 * singly-linked list */
void			ft_lstdelone(t_list *lst, void (*del)(void*));

/* Is used to clear (delete and deallocate memory for) an entire singly-linked
 *list */
void			ft_lstclear(t_list **lst, void (*del)(void*));

/* Is used to apply a given function `f` to the content of each node in a
 * singly-linked list */
void			ft_lstiter(t_list *lst, void (*f)(void*));

/* Is used to create a new linked list by applying a function `f` to each
 * element of the original linked list `lst`. It also takes an additional
 * function `del` to handle the deallocation of any resources if an error occurs
 * during the process */
t_list			*ft_lstmap(t_list *lst,
					void *(*f)(void *), void (*del)(void *));

#endif