/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/30 12:43:04 by gabrodri          #+#    #+#             */
/*   Updated: 2023/11/06 11:47:32 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h> // for the variadic arguments handling
# include "libft/libft.h" // for the other functions

// Define an array of characters for digits
# define DEC_DIGITS "0123456789"
# define HEX_DIGITS_LOWER "0123456789abcdef"
# define HEX_DIGITS_UPPER "0123456789ABCDEF"

/* Remodeled `printf` function, handles `%c`, `%s`, `%p`, `%d`, `%u`, `%x`,
* `%X`, `%%`, don´t handle any buffer for better I/O efficiency*/
int				ft_printf(const char *format, ...);

/* Handles the `%c` format specifier passed to `ft_printf` and prints the
 * corresponding argument. It returns the number of characters printed. */
int				ft_print_char(int c);

/* Handles the `%s` format specifier passed to `ft_printf` and prints the
 * corresponding argument. It returns the number of characters printed. */
int				ft_print_string(const char *s);

/* Handles the `%p` format specifier passed to `ft_printf` and prints the
 * corresponding argument. It returns the number of characters printed. */
int				ft_print_pointer(void *ptr);

/* Handles the `%d` and `%i` format specifiers passed to `ft_printf` and prints
 * the corresponding argument. It returns the number of characters printed. */
int				ft_print_decimal(int n);

/* Handles the `%u` format specifier passed to `ft_printf` and prints the
 * corresponding argument. It returns the number of characters printed. */
int				ft_print_unsigned_decimal(unsigned int n);

/* Handles the `%x` and `%X` format specifiers passed to `ft_printf` and prints
 * the corresponding argument. It returns the number of characters printed. */
int				ft_print_hexadecimal(unsigned long long n, char type);

#endif