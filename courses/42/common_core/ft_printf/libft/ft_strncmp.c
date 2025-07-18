/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 16:05:20 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/12 18:50:47 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	unsigned int	counter;

	counter = 0;
	while (n > 0 && s1[counter] != '\0'
		&& (unsigned char)s1[counter] == (unsigned char)s2[counter])
	{
		counter++;
		n--;
	}
	if (n == 0 || (s1[counter] == '\0' && s2[counter] == '\0'))
		return (0);
	return ((int)((unsigned char)s1[counter] - (unsigned char)s2[counter]));
}
