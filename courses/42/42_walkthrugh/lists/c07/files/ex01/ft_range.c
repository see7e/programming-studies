/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jfilguei <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/26 02:49:58 by jfilguei          #+#    #+#             */
/*   Updated: 2023/03/26 02:50:00 by jfilguei         ###   ########.fr       */
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

int	*ft_range(int min, int max)
{
	int	*array;
	int	n;

	if (min >= max)
		return (NULL);
	n = (max - min);
	array = (int *)malloc(n * sizeof(int));
	if (array == NULL)
		return (NULL);
	fill_array(array, n, min);
	return (array);
}
