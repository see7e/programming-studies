/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_decimal.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/30 12:42:42 by gabrodri          #+#    #+#             */
/*   Updated: 2023/11/06 12:14:39 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

#include "ft_printf.h"

static int	ft_print_positive_decimal(int n)
{
	int		length;
	char	digit;

	length = 0;
	if (n >= 10)
		length += ft_print_positive_decimal(n / 10);
	digit = '0' + (n % 10);
	write(1, &digit, 1);
	length++;
	return (length);
}

static int	ft_print_negative_decimal(int n)
{
	int		length;
	char	digit;

	length = 0;
	if (n <= -10)
		length += ft_print_negative_decimal(n / 10);
	digit = '0' - (n % 10);
	write(1, &digit, 1);
	length++;
	return (length);
}

int	ft_print_decimal(int n)
{
	int	length;

	length = 0;
	if (n < 0)
	{
		write(1, "-", 1);
		length++;
		length += ft_print_negative_decimal(n);
	}
	else
		length += ft_print_positive_decimal(n);
	return (length);
}
