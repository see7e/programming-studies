/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/12 15:21:43 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/12 15:21:57 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

char	*ft_strcpy(char *dest, char *src) // recebe dois argumentos: um ponteiro para um char char *dest e um ponteiro para um char char *src, e retorna um ponteiro para um char.
{
	int	i; // contador

	i = 0;
	while (src[i] != '\0') // loop while que irá copiar cada caractere do array src para o array dest até que seja encontrado um caractere nulo '\0' em src. Em cada iteração do loop, o caractere atual de src é copiado para o índice correspondente de dest, e o contador i é incrementado
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0'; // Após a cópia de todos os caracteres, é adicionado um caractere nulo '\0' ao final de dest, para marcar o final da string.
	return (dest); // Por fim, a função retorna um ponteiro para dest, que agora contém a string copiada de src
}