/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/11/08 09:38:24 by gabrodri          #+#    #+#             */
/*   Updated: 2023/11/08 16:27:27 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *str)
{
	const char	*ptr;

	ptr = str;
	while (*ptr)
	{
		ptr++;
	}
	return (ptr - str);
}

void	*ft_memcpy(void *target, const void *source, size_t n)
{
	size_t	i;
	char	*ptr;
	char	*ptr2;

	ptr = target;
	ptr2 = (char *)source;
	i = -1;
	while (++i < n)
		*(ptr + i) = *(ptr2 + i);
	return (target);
}

char	*ft_strcat(char *dest, const char *src)
{
	size_t	dest_len;
	size_t	src_len;

	dest_len = ft_strlen(dest);
	src_len = ft_strlen(src);
	ft_memcpy(dest + dest_len, src, src_len + 1);
	return (dest);
}

char	*ft_strjoin(const char *s1, const char *s2)
{
	size_t	len1;
	size_t	len2;
	char	*str;

	len1 = ft_strlen(s1);
	len2 = ft_strlen(s2);
	str = (char *)malloc(len1 + len2 + 1);
	if (!str)
		return (NULL);
	ft_strcat(str, s1);
	ft_strcat(str, s2);
	return (str);
}

char	*ft_strdup(const char *s)
{
	size_t	size;
	char	*dup;

	size = ft_strlen(s) + 1;
	dup = (char *)malloc(size);
	if (!dup)
		return (NULL);
	ft_memcpy(dup, s, size);
	return (dup);
}
