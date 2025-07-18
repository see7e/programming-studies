/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcat.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/18 22:38:58 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/18 22:39:17 by gabrodri         ###   ########.fr       */
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

char	*ft_strcat(char *dest, char *src) // recebe dois ponteiros para caracteres como argumentos (dest e src). A função concatena a string src à string dest e retorna o ponteiro para a string resultante.
/*Essa função concatena a string src ao final da string dest, supondo que dest tenha espaço suficiente para acomodar a concatenação. A função não verifica o tamanho de dest antes da concatenação, o que pode levar a problemas de estouro de buffer se dest não tiver espaço suficiente.*/
{
	// Declaração das variáveis i e k. k é inicializada com zero, enquanto i é inicializada com o comprimento da string dest usando a função ft_strlen.
	int	i;
	int	k;

	k = 0;
	i = ft_strlen(dest);
	while (src[k] != '\0') // itera enquanto o caractere atual de src não for o caractere nulo \0. Dentro do laço, cada caractere de src é copiado para a posição adequada em dest. Para isso, adiciona-se k à posição de dest onde a cópia deve começar (ou seja, a posição atual de dest mais o comprimento de dest), e o caractere atual de src é atribuído a essa posição. Depois, a variável k é incrementada em 1, para avançar para o próximo caractere de src.
	{
		dest[i + k] = src[k];
		k++;
	}
	dest[i + k] = '\0'; // Fora do laço, adiciona-se o caractere nulo \0 ao final da string dest, indicando que a string termina ali. Isso é feito atribuindo-se o caractere nulo à posição de dest imediatamente após o último caractere copiado de src.
	return (dest); // retorna o ponteiro para a string concatenada dest.
}
