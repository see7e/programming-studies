/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_hexadecimal.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/30 12:43:10 by gabrodri          #+#    #+#             */
/*   Updated: 2023/11/06 12:24:39 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	print_single_hex_char(int n, char type)
{
	if (type == 'x')
		return (ft_print_char(HEX_DIGITS_LOWER[n]));
	else
		return (ft_print_char(HEX_DIGITS_UPPER[n]));
}

int	ft_print_hexadecimal(unsigned long long n, char type)
{
	int	count;

	count = 0;
	if (n < 16)
		return (print_single_hex_char(n, type));
	count += ft_print_hexadecimal(n / 16, type);
	count += print_single_hex_char(n % 16, type);
	return (count);
}
