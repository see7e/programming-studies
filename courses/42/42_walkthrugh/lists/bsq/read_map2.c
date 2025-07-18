/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_read_map2.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/28 19:38:14 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/28 19:38:15 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "./include/bsq.h"

char	**ft_read_file(char *argv)
{
	char	**buf;
	int		i;
	int		fd;

	i = -1;
	fd = open(argv, O_RDONLY);
	ft_get_second_line(fd);
	buf = malloc(row_nbr(argv) * sizeof(char *));
	if (buf == NULL)
		return (NULL);
	while (++i < row_nbr(argv))
	{
		buf[i] = malloc(col_nbr(argv) * sizeof(char));
		if (buf[i] == NULL)
			return (NULL);
	}
	i = 0;
	while (i < row_nbr(argv))
	{
		if (read(fd, buf[i], col_nbr(argv)) == -1)
			return (NULL);
		buf[i++][col_nbr(argv) - 1] = '\0';
	}
	close (fd);
	return (buf);
}
