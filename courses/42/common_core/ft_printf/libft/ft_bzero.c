/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 16:05:04 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/06 16:01:23 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_bzero(void *block, size_t n)
{
	size_t	i;
	char	*ptr;

	if (!n)
		return ;
	ptr = block;
	i = 0;
	while (i < n)
		*(ptr + i++) = 0;
}
