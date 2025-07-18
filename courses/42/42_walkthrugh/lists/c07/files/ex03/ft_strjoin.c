/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jfilguei <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/26 02:50:18 by jfilguei          #+#    #+#             */
/*   Updated: 2023/03/26 02:50:20 by jfilguei         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

char	*ft_strcpy(char *dest, char *src)
{
	int	i;

	i = 0;
	while (src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}

int	final_len(char **strings, int size, int sep_length)
{
	int	len;
	int	i;

	len = 0;
	i = 0;
	while (i < size)
	{
		len += ft_strlen(strings[i]);
		len += sep_length;
		i++;
	}
	len -= sep_length;
	return (len);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	int		total_len;
	int		i;
	char	*str_final;
	char	*d;

	if (size == 0)
		return ((char *)malloc(sizeof(char)));
	total_len = final_len(strs, size, ft_strlen(sep));
	d = ((char *)malloc((total_len + 1) * sizeof(char)));
	str_final = d;
	if (!d)
		return (0);
	i = -1;
	while (++i < size)
	{
		ft_strcpy(d, strs[i]);
		d += ft_strlen(strs[i]);
		if (i < size - 1)
		{
			ft_strcpy(d, sep);
			d += ft_strlen(sep);
		}
	}
	*d = '\0';
	return (str_final);
}
