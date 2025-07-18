/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_pointer.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/30 12:43:25 by gabrodri          #+#    #+#             */
/*   Updated: 2023/11/06 11:32:25 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_pointer(void *ptr)
{
	unsigned long long	n;
	int					count;

	count = 0;
	if (!ptr)
		return (write(1, "(nil)", 5));
	n = (unsigned long long)ptr;
	count += write(1, "0x", 2);
	if (n == 0)
		count += ft_print_char('0');
	else
		count += ft_print_hexadecimal(n, 'x');
	return (count);
}
