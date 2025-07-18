/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: fernacar <fernacar@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/20 21:02:50 by fernacar          #+#    #+#             */
/*   Updated: 2023/03/20 22:21:07 by fernacar         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] == s2[i] && s1[i] != '\0' && s2[i] != '\0')
	{
		i++;
	}
	return (s1[i] - s2[i]);
}

void	print_params(int argc, char **argv)
{
	int	i;
	int	j;

	i = 1;
	while (i < argc)
	{
		j = 0;
		while (argv[i][j])
		{
			write(1, &argv[i][j], 1);
			j++;
		}
		write(1, "\n", 1);
		i++;
	}
}

int	main(int argc, char **argv)
{
	int		moved;
	int		i;
	int		diff;
	char	*temp;

	moved = 1;
	while (moved)
	{
		moved = 0;
		i = 1;
		while (i < argc - 1)
		{
			diff = ft_strcmp(argv[i], argv[i + 1]);
			if (diff > 0)
			{
				temp = argv[i];
				argv[i] = argv[i + 1];
				argv[i + 1] = temp;
				moved = 1;
			}
			i++;
		}
	}
	print_params(argc, argv);
	return (0);
}
