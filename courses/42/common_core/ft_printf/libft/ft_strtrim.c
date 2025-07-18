/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 16:06:19 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/23 18:45:59 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_char_in_set(char c, const char *set)
{
	size_t	counter;

	counter = 0;
	while (set[counter])
	{
		if (set[counter] == c)
			return (1);
		counter++;
	}
	return (0);
}

char	*ft_strtrim(const char *s1, const char *set)
{
	size_t	counter;
	size_t	start;
	size_t	end;
	size_t	trimmed_len;
	char	*str;

	if (!s1 || !set)
		return (NULL);
	start = 0;
	end = ft_strlen(s1);
	while (s1[start] && ft_char_in_set(s1[start], set))
		start++;
	while (end > start && ft_char_in_set(s1[end - 1], set))
		end--;
	trimmed_len = end - start;
	str = (char *)malloc(trimmed_len + 1);
	if (!str)
		return (NULL);
	counter = 0;
	while (start < end)
		str[counter++] = s1[start++];
	str[counter] = '\0';
	return (str);
}
