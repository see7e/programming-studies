/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 16:05:32 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/23 18:45:36 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

unsigned int	ft_strlcpy(char *dest, const char *src, unsigned int size)
{
	size_t	idx;
	size_t	len;

	idx = 0;
	len = 0;
	if (!dest && !src)
		return (0);
	while (src[len])
		len++;
	if (size > 0)
	{
		while ((src[idx]) && (idx < (size - 1)))
		{
			dest[idx] = src[idx];
			idx++;
		}
		dest[idx] = '\0';
	}
	return (len);
}
