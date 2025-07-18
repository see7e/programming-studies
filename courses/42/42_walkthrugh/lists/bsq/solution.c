/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_find_solution.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jfilguei <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/28 19:45:59 by jfilguei          #+#    #+#             */
/*   Updated: 2023/03/28 19:46:04 by jfilguei         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/bsq.h"

int	ft_min(int a, int b, int c)
{
	if (a <= b && a <= c)
		return (a);
	else if (b <= a && b <= c)
		return (b);
	else
		return (c);
}

int	**ft_generate_map(int l, int c)
{
	int	**map2;
	int	i;

	i = 0;
	map2 = malloc(l * sizeof(int *));
	if (map2 == NULL)
		return (NULL);
	while (i < l)
	{
		map2[i] = malloc(c * sizeof(int));
		if (map2[i] == NULL)
			return (NULL);
		i++;
	}
	return (map2);
}

int	ft_biggest_square(char **map, int c, int l, char o)
{
	int	i;
	int	j;
	int	**m;
	int	count_max;

	i = -1;
	count_max = 0;
	m = ft_generate_map(l, c);
	while (++i < l)
	{
		j = -1;
		while (++j < c - 1)
		{
			if (map[i][j] == o)
				m[i][j] = 0;
			else if (i == 0 || j == 0)
				m[i][j] = 1;
			else
				m[i][j] = ft_min(m[i -1][j], m[i][j -1], m[i -1][j -1]) + 1;
			if (m[i][j] > count_max)
				count_max = m[i][j];
		}
	}
	free(m);
	return (count_max);
}

int	ft_find_position_square(char **map, int c, int l, char o)
{
	int	i;
	int	j;
	int	**m;

	i = -1;
	m = ft_generate_map(l, c);
	while (++i < l)
	{
		j = -1;
		while (++j < c - 1)
		{
			if (map[i][j] == o)
				m[i][j] = 0;
			else if (i == 0 || j == 0)
				m[i][j] = 1;
			else
				m[i][j] = ft_min(m[i -1][j], m[i][j -1], m[i -1][j -1]) + 1;
			if (m[i][j] == ft_biggest_square(map, c, l, o))
			{
				free(m);
				return (i * (c - 1) + j);
			}
		}
	}
	return (0);
}
