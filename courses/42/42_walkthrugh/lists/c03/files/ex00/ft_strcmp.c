/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/18 20:05:14 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/18 20:05:16 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int ft_strcmp(char *s1, char *s2) // recebe dois ponteiros para strings como argumentos (s1 e s2) e retorna um valor inteiro.
{
	int	i; // contador.
	
	i = 0;
	while(s1[i] != '\0' && s1[i] == s2[i]) // itera enquanto o caractere atual das duas strings (s1[i] e s2[i]) não for o caractere nulo \0 e enquanto eles forem iguais. Ou seja, o laço percorre as duas strings enquanto elas forem iguais, caractere por caractere.
		i++; // incrementada em 1, para avançar para o próximo caractere das strings.
	return(s1[i]-s2[i]); // Fora do laço, a função retorna a diferença entre o valor ASCII do caractere atual de s1 e o valor ASCII do caractere atual de s2. Isso é feito subtraindo-se o valor ASCII do caractere atual de s2 do valor ASCII do caractere atual de s1.
}
/*Se todas as letras de ambas as strings forem iguais, a função retornará 0. Se a primeira string for maior que a segunda string em ordem lexicográfica, a função retornará um valor positivo. Se a primeira string for menor que a segunda string em ordem lexicográfica, a função retornará um valor negativo.*/