/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/30 12:42:28 by gabrodri          #+#    #+#             */
/*   Updated: 2023/11/03 20:45:59 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	ft_handle_format_specifier(char format, va_list args)
{
	int	count;

	count = 0;
	if (format == 'c')
		count += ft_print_char(va_arg(args, int));
	else if (format == 's')
		count += ft_print_string(va_arg(args, char *));
	else if (format == 'p')
		count += ft_print_pointer(va_arg(args, void *));
	else if (format == 'd' || format == 'i')
		count += ft_print_decimal(va_arg(args, int));
	else if (format == 'u')
		count += ft_print_unsigned_decimal(va_arg(args, unsigned int));
	else if (format == 'x' || format == 'X')
		count += ft_print_hexadecimal(va_arg(args, unsigned int), format);
	else if (format == '%')
		count += ft_print_char('%');
	return (count);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		count;

	count = 0;
	va_start(args, format);
	while (*format)
	{
		if (*format != '%')
			count += write(1, format, 1);
		else
		{
			format++;
			count += ft_handle_format_specifier(*format, args);
		}
		format++;
	}
	va_end(args);
	return (count);
}
