/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_negative.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/09 15:50:15 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/09 15:50:21 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c) //function named "ft_putchar" which takes a single argument of type char.
{
	write(1, &c, 1); //write function
}

void	ft_is_negative(int n) //function named "ft_is_negative" which takes a single argument of type int.
{
	/*This is the implementation of the "ft_is_negative" function. It checks if the 
	argument "n" is less than zero, and if it is, it calls the "ft_putchar" function 
	with the character 'N' as an argument (indicating a negative number). If "n" is 
	greater than or equal to zero, it calls "ft_putchar" with the character 'P' as an 
	argument (indicating a positive number).*/
	if (n < 0)
	{
		ft_putchar('N');
	}
	else
	{
		ft_putchar('P');
	}
}
