/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lib1.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/27 18:39:01 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/27 18:39:03 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/bsq.h"

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		ft_putchar(str[i]);
		i++;
	}
}

void	ft_putnbr(int nb)
{
	int		i;
	char	array[10];

	i = 0;
	if (nb < 0)
	{
		ft_putchar('-');
		nb = -nb;
	}
	if (nb == 0)
		ft_putchar(48);
	while (nb > 0)
	{
		array[i] = nb % 10;
		i++;
		nb /= 10;
	}
	while (i > 0)
	{
		i--;
		ft_putchar(array[i] + 48);
	}
}

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (*(str + i) != '\0')
		i++;
	return (i);
}

char	*ft_strcpy(char *dest, char *src)
{
	int	i;

	i = 0;
	while (src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = src[i];
	return (dest);
}
