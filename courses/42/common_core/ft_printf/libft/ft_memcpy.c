/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 16:05:43 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/10 18:51:17 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *target, const void *source, size_t n)
{
	size_t	i;
	char	*ptr;
	char	*ptr2;

	if (!target && !source)
		return (NULL);
	ptr = target;
	ptr2 = (char *)source;
	i = -1;
	while (++i < n)
		*(ptr + i) = *(ptr2 + i);
	return (ptr);
}
