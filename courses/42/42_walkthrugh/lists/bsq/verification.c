/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_verif_map.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/28 21:00:56 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/28 21:00:58 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/bsq.h"

int	ft_verif_chars(char *argv)
{
	int		i;
	int		fd;
	int		size_file;
	char	*buf;

	i = -1;
	size_file = ft_size_file(argv);
	buf = malloc(size_file * sizeof(char));
	fd = open(argv, O_RDONLY);
	ft_get_second_line(fd);
	if (buf == NULL)
		return (0);
	while (read(fd, buf, size_file))
		buf[read(fd, buf, size_file)] = '\0';
	while (buf[++i])
	{
		if (buf[i] != get_void(argv)
			&& buf[i] != get_obst(argv) && buf[i] != '\n')
			return (1);
	}
	close(fd);
	free(buf);
	return (0);
}

int	ft_get_next_columns(char *argv, int fd)
{
	char	*buf;
	int		j;
	int		size_file;

	j = 0;
	size_file = ft_size_file(argv);
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
	return (j + 1);
}

int	ft_verif_columns(char *argv)
{
	int	i;
	int	fd;
	int	j;
	int	c;
	int	l;

	i = 0;
	j = 0;
	c = col_nbr(argv);
	l = row_nbr(argv);
	fd = open(argv, O_RDONLY);
	ft_get_second_line(fd);
	while (i < l)
	{
		j = ft_get_next_columns(argv, fd);
		if (j != c)
			return (1);
		i++;
	}
	close(fd);
	return (0);
}

int	ft_verif_returns(char *argv)
{
	char	*buf;
	int		fd;
	int		size_file;
	int		ret;
	int		c;

	ret = 0;
	c = col_nbr(argv);
	size_file = ft_size_file(argv);
	fd = open(argv, O_RDONLY);
	ft_get_second_line(fd);
	buf = malloc(size_file * sizeof(char));
	ret = read(fd, buf, c);
	if (buf == NULL)
		return (0);
	while (!ret)
	{
		if (buf[ret - 1] != '\n')
			return (1);
	}
	free(buf);
	close(fd);
	return (0);
}

int	ft_verif_map(char *argv)
{
	if (col_nbr(argv) < 1 || row_nbr(argv) < 1)
	{
		ft_putstr("map error\n");
		return (1);
	}
	if (ft_verif_chars(argv) == 1 || ft_verif_returns(argv) == 1)
	{
		ft_putstr("map error\n");
		return (1);
	}
	if (ft_verif_columns(argv) == 1)
	{
		ft_putstr("map error\n");
		return (1);
	}
	return (0);
}
