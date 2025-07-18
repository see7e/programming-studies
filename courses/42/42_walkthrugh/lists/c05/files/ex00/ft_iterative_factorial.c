/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jfilguei <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/20 22:28:39 by jfilguei          #+#    #+#             */
/*   Updated: 2023/03/20 22:28:43 by jfilguei         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_factorial(int nb)
{
	int	number;

	number = 1;
	if (nb < 0)
		return (0);
	while (nb > 1)
		number = number * nb--;
	return (number);
}
