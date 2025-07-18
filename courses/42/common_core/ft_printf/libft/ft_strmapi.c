/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 16:06:19 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/06 16:01:23 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	size_t	idx;
	char	*str;

	str = ft_strdup(s);
	if (!(str))
		return (NULL);
	idx = 0;
	while (str[idx])
	{
		str[idx] = (*f)(idx, str[idx]);
		idx++;
	}
	return (str);
}
