/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/11/08 09:38:27 by gabrodri          #+#    #+#             */
/*   Updated: 2023/11/08 16:20:55 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static void	ft_free(char **str)
{
	if (str && *str)
	{
		free(*str);
		*str = NULL;
	}
}

static int	ft_read(int fd, char **line_buffer, char *buffer)
{
	int		bytes;
	char	*aux;

	ft_memcpy(buffer, 0, BUFFER_SIZE + 1);
	bytes = read(fd, buffer, BUFFER_SIZE);
	if (bytes < 0 || buffer == NULL)
	{
		ft_free(line_buffer);
		return (-1);
	}
	if (bytes == 0)
		return (bytes);
	aux = ft_strjoin(*line_buffer, buffer);
	ft_free(line_buffer);
	*line_buffer = aux;
	return (bytes);
}

char	*get_next_line(int fd)
{
	int			bytes;
	char		*buffer;
	char		*result;
	static char	*line_buffer;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	buffer = (char *)malloc((BUFFER_SIZE + 1) * sizeof(char));
	if (!buffer)
		return (NULL);
	bytes = ft_read(fd, &line_buffer, buffer);
	while (ft_strcat(line_buffer, "\n") == NULL && (bytes) > 0)
	{
		bytes = ft_read(fd, &line_buffer, buffer);
	}
	ft_free(&buffer);
	if (bytes == -1 || ft_strlen(line_buffer) == 0)
		return (NULL);
	result = ft_strdup(line_buffer);
	ft_free(&line_buffer);
	return (result);
}
