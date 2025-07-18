/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lib2.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/27 18:39:09 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/27 18:39:15 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/bsq.h"

char	get_void(char *argv)
{
	int		i;
	int		fd;
	char	v;
	char	*buf;

	i = 0;
	fd = open(argv, O_RDONLY);
	buf = malloc(80 * sizeof(char));
	if (buf == NULL)
		return (0);
	while (read(fd, &buf[i], 1))
	{
		if (buf[i] == '\n')
			break ;
		i++;
	}
	v = buf[i - 3];
	free (buf);
	close(fd);
	return (v);
}

char	get_obst(char *argv)
{
	int		i;
	int		fd;
	char	o;
	char	*buf;

	i = 0;
	fd = open(argv, O_RDONLY);
	buf = malloc(80 * sizeof(char));
	if (buf == NULL)
		return (0);
	while (read(fd, &buf[i], 1))
	{
		if (buf[i] == '\n')
			break ;
		i++;
	}
	o = buf[i - 2];
	free (buf);
	close(fd);
	return (o);
}

char	ft_get_char_full(char *argv)
{
	int		i;
	int		fd;
	char	p;
	char	*buf;

	i = 0;
	fd = open(argv, O_RDONLY);
	buf = malloc(80 * sizeof(char));
	if (buf == NULL)
		return (0);
	while (read(fd, &buf[i], 1))
	{
		if (buf[i] == '\n')
			break ;
		i++;
	}
	p = buf[i - 1];
	free (buf);
	close(fd);
	return (p);
}
