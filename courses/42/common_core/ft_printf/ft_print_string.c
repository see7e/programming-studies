/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_string.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/30 12:43:30 by gabrodri          #+#    #+#             */
/*   Updated: 2023/11/06 12:01:14 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_string(const char *s)
{
	int	count;

	count = 0;
	if (s == NULL)
		return (write(1, "(null)", 6));
	while (*s)
	{
		ft_putchar_fd(*s, 1);
		s++;
		count++;
	}
	return (count);
}
