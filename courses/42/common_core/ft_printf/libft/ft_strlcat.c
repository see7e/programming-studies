/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 16:05:34 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/12 18:50:38 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

unsigned int	ft_strlcat(char *dest, const char *src, unsigned int size)
{
	unsigned int	count;
	unsigned int	src_len;
	unsigned int	dest_len;

	count = 0;
	src_len = ft_strlen(src);
	dest_len = ft_strlen(dest);
	if (dest_len >= size)
		return (size + ft_strlen(src));
	while (src[count] != '\0' && count < size - dest_len - 1)
	{
		dest[dest_len + count] = src[count];
		count++;
	}
	dest[dest_len + count] = '\0';
	return (dest_len + src_len);
}
