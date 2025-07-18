/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/12 15:46:29 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/12 15:46:33 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

unsigned int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}

unsigned int	ft_strlcpy(char *dest, char *src, unsigned int size)
/*recebe três parâmetros:
dest, um ponteiro para uma string que será preenchida com a cópia da string src.
src, um ponteiro para a string que será copiada para dest.
size, um inteiro sem sinal que representa o tamanho máximo de caracteres que podem ser copiados de src para dest.*/
{
	unsigned int	i; // Declaração da variável inteira sem sinal i, que será utilizada como um contador no loop a seguir.

	i = 0;
	if (size != 0) // Verifica se size é diferente de zero, para evitar acessar uma posição inválida de memória em dest.
	{
		while (src [i] != '\0' && i < size - 1) // Enquanto o caractere atual de src for diferente de '\0' (o que indica o final da string) e i for menor que size - 1, copia o caractere atual de src para dest e incrementa i.
		{
			dest[i] = src[i];
			i++;
		}
		dest[i] = '\0'; // Adiciona o caractere nulo ('\0') no final da string em dest, indicando o fim da string.
	}
	return (ft_strlen(src)); // Retorna o tamanho da string original src usando a função ft_strlen. Note que a função não retorna o tamanho da string em dest, que pode ser menor que src.
}
