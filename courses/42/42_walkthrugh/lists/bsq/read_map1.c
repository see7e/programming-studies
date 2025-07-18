/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_read_map1.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/28 19:38:14 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/28 19:38:15 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/bsq.h"

int	ft_size_file(char *argv)
{
	int		size;
	int		fd;
	char	buf;

	size = 0;
	fd = open(argv, O_RDONLY);
	while (read(fd, &buf, 1))
	{
		size++;
	}
	close(fd);
	return (size);
}

int	row_nbr(char *argv)
{
	int		i;
	int		nb_l;
	int		fd;
	char	*buf;

	i = 0;
	nb_l = 0;
	fd = open(argv, O_RDONLY);
	buf = malloc(80 * sizeof(char));
	if (buf == NULL)
		return (0);
	while (read(fd, &buf[i], 1))
	{
		if (buf[i] > 58 || buf[i] < 47)
			break ;
		nb_l = nb_l * 10 + (buf[i] - 48);
		i++;
	}
	free (buf);
	close(fd);
	return (nb_l);
}

int	col_nbr(char *argv)
{
	char	*buf;
	int		j;
	int		size_file;
	int		fd;

	j = 0;
	fd = open(argv, O_RDONLY);
	size_file = ft_size_file(argv);
	ft_get_second_line(fd);
	buf = malloc(size_file * sizeof(char));
	if (buf == NULL)
		return (0);
	while (read(fd, &buf[j], 1))
	{
		if (buf[j] == '\n')
			break ;
		j++;
	}
	free (buf);
	close(fd);
	return (j + 1);
}

void	ft_get_second_line(int fd)
{
	int		i;
	char	*buf;

	i = 0;
	buf = malloc(4096 * sizeof(char));
	if (buf == NULL)
		return ;
	while (read(fd, &buf[i], 1))
	{
		if (buf[i] == '\n')
			break ;
		i++;
	}
}
