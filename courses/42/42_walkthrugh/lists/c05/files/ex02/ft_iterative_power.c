/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jfilguei <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/20 22:29:45 by jfilguei          #+#    #+#             */
/*   Updated: 2023/03/20 22:29:56 by jfilguei         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_power(int nb, int power)
{
	int	i;
	int	number;

	i = 0;
	number = 1;
	if (power == 0)
		return (1);
	else if (power < 0)
		return (0);
	while (i++ < power)
		number *= nb;
	return (number);
}
