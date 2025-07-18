/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush01.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/11 18:52:52 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/11 18:52:56 by gabrodri         ###   ########.fr       */
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
			if ((j == 1 && i == 1) || (x > 1 && y > 1 && j == x && i == y))
				ft_putchar('/');
			else if ((j == 1 && i == y) || (j == x && i == 1))
				ft_putchar('\\');
			else if (((j > 1 && j < x) && (i == 1 || i == y))
				|| ((i > 1 && i < y) && (j == 1 || j == x)))
				ft_putchar('*');
			else
				ft_putchar(' ');
			j++;
		}
		ft_putchar('\n');
		i++;
	}
}
