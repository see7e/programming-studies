/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush02.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: fernacar <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/11 16:36:53 by fernacar          #+#    #+#             */
/*   Updated: 2023/03/11 16:49:16 by fernacar         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
void	ft_putchar(char c);

void	rush(int x, int y)
{
	int	i;
	int	j;

	i = 1;
	while (i <= y)
	{
		j = 1;
		while (j <= x)
		{
			if (j == 1 && (i == 1 || i == y))
				ft_putchar('A');
			else if (j == x && (i == 1 || i == y))
				ft_putchar('C');
			else if (((j > 1 && j < x) && (i == 1 || i == y))
				|| ((i > 1 && i < y) && (j == 1 || j == x)))
				ft_putchar('B');
			else
				ft_putchar(' ');
			j++;
		}
		ft_putchar('\n');
		i++;
	}
}
