/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strndup.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/05 13:57:30 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/12 18:50:51 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	char	*dest_start;

	dest_start = dest;
	while (n > 0 && *src != '\0')
	{
		*dest++ = *src++;
		n--;
	}
	while (n > 0)
	{
		*dest++ = '\0';
		n--;
	}
	return (dest_start);
}

char	*ft_strndup(const char *src, size_t length)
{
	char	*dst;

	if (src == NULL)
		return (NULL);
	dst = (char *)malloc(length + 1);
	if (!dst)
		return (NULL);
	ft_strncpy(dst, (char *)src, length);
	dst[length] = '\0';
	return (dst);
}
