/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jfilguei <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/26 02:49:38 by jfilguei          #+#    #+#             */
/*   Updated: 2023/03/26 02:49:39 by jfilguei         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

void	fill_array(int *array, int range, int min)
{
	int	i;

	i = 0;
	while (i < range)
	{
		array[i] = min + i;
		i++;
	}
}

int	ft_ultimate_range(int **range, int min, int max)
{
	int	*array;
	int	n;

	if (min >= max)
	{
		range = NULL;
		return (0);
	}
	n = (max - min);
	array = (int *)malloc(n * sizeof(int));
	if (!array)
		return (-1);
	fill_array(array, n, min);
	*range = array;
	return (max - min);
}
