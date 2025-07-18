/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 16:06:20 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/12 18:50:24 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*ft_strcat(char *dest, const char *src)
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
	ft_memset(str, 0, len1 + len2 + 1);
	ft_strcat(str, s1);
	ft_strcat(str, s2);
	return (str);
}
