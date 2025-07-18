/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_alpha.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/12 15:22:51 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/12 15:22:55 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int ft_str_is_alpha(char *str) // recebe um ponteiro para uma string str como argumento e retorna um inteiro indicando se a string contém apenas caracteres alfabéticos.
{
	int i; // contador int

	i = 0;
	while (str[i] != '\0') // Loop while que percorre cada caractere da string, enquanto não chegar ao fim da string (ou seja, enquanto não encontrar o caractere nulo '\0').
	{
		// Dentro do loop, há uma verificação condicional que testa se o caractere atual não é uma letra maiúscula ou minúscula. Se for verdadeiro, a função retorna 0, indicando que a string não contém apenas caracteres alfabéticos.
		if ((str[i] < 'a' || str[i] > 'z') && (str[i] < 'A' || str[i] > 'Z'))
			return (0);
		i++; // Incremento da variável i para passar para o próximo caractere da string.
	}
	return (1); // Se o loop terminar sem encontrar nenhum caractere não-alfabético, a função retorna 1, indicando que a string contém apenas caracteres alfabéticos.
}