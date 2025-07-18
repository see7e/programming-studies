/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 16:06:22 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/12 18:50:14 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	h_count_words(const char *s, char c)
{
	size_t	count;
	int		is_inside_word;

	count = 0;
	is_inside_word = 0;
	while (*s)
	{
		if (*s == c)
			is_inside_word = 0;
		else if (!is_inside_word)
		{
			is_inside_word = 1;
			count++;
		}
		s++;
	}
	return (count);
}

char	**ft_split(char const *s, char c)
{
	char	**split;
	size_t	idx;
	size_t	len;

	split = malloc(sizeof(char *) * (h_count_words(s, c) + 1));
	if (!s || !split)
		return (NULL);
	idx = 0;
	while (*s)
	{
		if (*s == c)
			s++;
		else
		{
			len = 0;
			while (s[len] && s[len] != c)
				len++;
			split[idx++] = ft_substr(s, 0, len);
			s += len;
		}
	}
	split[idx] = NULL;
	return (split);
}
