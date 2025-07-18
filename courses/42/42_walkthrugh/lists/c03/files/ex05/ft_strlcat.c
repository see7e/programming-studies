/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/19 01:20:36 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/19 01:20:38 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

unsigned int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}

unsigned int	ft_strlcat(char *dest, char *src, unsigned int size) // recebe duas strings (dest e src) e um tamanho máximo de caracteres (size), e retorna o tamanho total das strings dest e src.
{
	unsigned int	dest_len;
	unsigned int	src_len;
	unsigned int	k;

	k = 0; // Inicializa a variável k com 0
	dest_len = ft_strlen(dest); // Calcula o tamanho da string dest
	src_len = ft_strlen(src); // Calcula o tamanho da string src
	if (dest_len >= size) // Verifica se dest já está cheio
		return (size + ft_strlen(src)); // Retorna o tamanho total caso dest esteja cheio
	while (src[k] != '\0' && k < size - dest_len - 1) // Copia a string src para dest, enquanto há espaço em dest
	{
		dest[dest_len + k] = src[k];
		k++;
	}
	dest[dest_len + k] = '\0'; // Adiciona o caractere nulo no final da string em dest
	return (dest_len + src_len); // Retorna o tamanho total das strings
}
