/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/12 15:22:22 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/12 15:22:26 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

char	*ft_strncpy(char *dest, char *src, unsigned int n) // recebe três argumentos: um ponteiro para uma string de destino (dest), um ponteiro para uma string de origem (src) e um inteiro sem sinal que representa o número máximo de caracteres a serem copiados da string de origem para a string de destino (n). A função retorna um ponteiro para a string de destino.
{
	unsigned int	i; // usada como um contador para percorrer a string de origem e a string de destino. Unsigned (inteiro sem sinal que especifica o número máximo de caracteres que devem ser copiados da origem para o destino)

	i = 0; // Inicialização da variável i com zero.
	while (i < n && src[i] != '\0') // Este loop verifica se a variável i é menor que o número máximo de caracteres a serem copiados (n) e se o caractere atual da string de origem não é nulo ('\0'). Se ambas as condições forem verdadeiras, o loop continuará.
	{
		dest[i] = src[i];
		i++;
	}
	while (i < n) // O segundo loop while preenche o restante do destino com caracteres nulos ('\0'). Isso garante que o destino tenha exatamente n caracteres no final da cópia.
	{
		dest[i] = '\0';
		i++;
	}
	return (dest); // Por fim, a função retorna um ponteiro para o destino, que agora contém a cópia da string de origem com tamanho n.
}