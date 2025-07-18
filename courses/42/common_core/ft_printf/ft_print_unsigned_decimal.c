/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_unsigned_decimal.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/30 12:43:39 by gabrodri          #+#    #+#             */
/*   Updated: 2023/11/06 11:19:46 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	unsigned_num_len(unsigned int n)
{
	int	i;

	i = 0;
	if (n == 0)
		return (1);
	while (n != 0)
	{
		n /= 10;
		i++;
	}
	return (i);
}

static char	*unsigned_itoa(unsigned int n)
{
	char	*nbr;
	int		length;

	length = unsigned_num_len(n);
	nbr = (char *)malloc(sizeof(char) * (length + 1));
	if (!nbr)
		return (0);
	nbr[length] = '\0';
	if (n == 0)
		nbr[0] = '0';
	while (n != 0)
	{
		nbr[length - 1] = n % 10 + '0';
		n /= 10;
		length--;
	}
	return (nbr);
}

int	ft_print_unsigned_decimal(unsigned int n)
{
	int		count;
	char	*number;

	count = unsigned_num_len(n);
	number = unsigned_itoa(n);
	ft_print_string(number);
	free(number);
	return (count);
}
