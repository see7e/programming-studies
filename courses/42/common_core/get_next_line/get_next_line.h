/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/11/08 09:38:29 by gabrodri          #+#    #+#             */
/*   Updated: 2023/11/08 16:26:54 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>
/* tool for controlling files and file descriptors,essential for working with
files */
# include <fcntl.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 42
# endif

char			*get_next_line(int fd);

// Utils
// Already in Libft
size_t			ft_strlen(const char *str);
void			*ft_memcpy(void *target, const void *source, size_t n);
char			*ft_strcat(char *dest, const char *src);
char			*ft_strjoin(const char *s1, const char *s2);
char			*ft_strdup(const char *s);

#endif