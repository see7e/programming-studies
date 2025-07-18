/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/19 01:00:05 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/19 01:00:20 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}

char	*ft_strncat(char *dest, char *src, unsigned int nb) // recebe três argumentos: um ponteiro para o caractere de destino (dest), um ponteiro para a string de origem (src) e um inteiro sem sinal nb que indica o número máximo de caracteres a serem concatenados.
/*Essa função concatena a string src ao final da string dest, limitando o número de caracteres copiados pelo valor de nb. A função não verifica o tamanho de dest antes da concatenação, o que pode levar a problemas de estouro de buffer se dest não tiver espaço suficiente.*/
{
	// Declaração das variáveis j e k. k é inicializada com zero, enquanto j é inicializada com o comprimento da string dest usando a função ft_strlen
	unsigned int	j;
	unsigned int	k;

	k = 0;
	j = ft_strlen(dest);
	while (src[k] != '\0' && k < nb) // Laço de repetição while que itera enquanto o caractere atual de src não for o caractere nulo \0 e o número de caracteres copiados não exceder o valor de nb. Dentro do laço, cada caractere de src é copiado para a posição adequada em dest. Para isso, adiciona-se j à posição de dest onde a cópia deve começar (ou seja, a posição atual de dest mais o comprimento de dest), e o caractere atual de src é atribuído a essa posição. Depois, a variável k é incrementada em 1, para avançar para o próximo caractere de src.
	{
		dest[j + k] = src[k];
		k++;
	}
	dest[j + k] = '\0'; // Fora do laço, adiciona-se o caractere nulo \0 ao final da string dest, indicando que a string termina ali. Isso é feito atribuindo-se o caractere nulo à posição de dest imediatamente após o último caractere copiado de src.
	return (dest); // Por fim, a função retorna o ponteiro para a string concatenada dest.
}
