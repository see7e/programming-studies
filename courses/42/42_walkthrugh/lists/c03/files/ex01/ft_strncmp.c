/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/18 22:16:36 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/18 22:16:40 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
/*Se todas as letras de ambas as strings forem iguais até o número máximo permitido, a função retornará 0. Se a primeira string for maior que a segunda string em ordem lexicográfica, a função retornará um valor positivo. Se a primeira string for menor que a segunda string em ordem lexicográfica, a função retornará um valor negativo.*/
int ft_strncmp(char *s1, char *s2, unsigned int n) // recebe dois ponteiros para strings como argumentos (s1 e s2) e um inteiro sem sinal (n) que indica o número máximo de caracteres a serem comparados. A função retorna um valor inteiro.
{
	unsigned int	i; //usada como índice para percorrer as strings.

	i = 0;
	while(s1[i] != '\0' && s1[i] == s2[i] && i < n) // itera enquanto o caractere atual das duas strings (s1[i] e s2[i]) não for o caractere nulo \0, enquanto eles forem iguais e enquanto o número de caracteres comparados (i) for menor que o número máximo de caracteres a serem comparados (n). Ou seja, o laço percorre as duas strings enquanto elas forem iguais e o número de caracteres comparados for menor que o número máximo permitido.
		i++; // incrementada em 1, para avançar para o próximo caractere das strings.
	if (i >= n) // verifica-se se o número de caracteres comparados (i) é maior ou igual ao número máximo permitido (n). Se for, significa que todas as strings foram iguais até o final do número máximo permitido e a função retorna 0.
		return (0);
	return(s1[i]-s2[i]); // Se não for o caso acima, a função retorna a diferença entre o valor ASCII do caractere atual de s1 e o valor ASCII do caractere atual de s2. Isso é feito subtraindo-se o valor ASCII do caractere atual de s2 do valor ASCII do caractere atual de s1.
}
