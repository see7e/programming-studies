/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_numeric.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/12 15:24:30 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/12 15:24:38 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int ft_str_is_numeric(char *str) // recebe um ponteiro para uma string str como argumento e retorna um inteiro indicando se a string contém apenas caracteres numéricos.
{
	int i; // contador int

	i = 0;
	while (str[i] != '\0') // Loop while que percorre cada caractere da string, enquanto não chegar ao fim da string (ou seja, enquanto não encontrar o caractere nulo '\0').
	{
		if (str[i] < '0' || str[i] > '9') // verificação condicional que testa se o caractere atual não é um número. Se for verdadeiro, a função retorna 0, indicando que a string não contém apenas caracteres numéricos.
			return (0);
		i++; // Incremento da variável i para passar para o próximo caractere da string.
	}
	return (1); // Se o loop terminar sem encontrar nenhum caractere.
}