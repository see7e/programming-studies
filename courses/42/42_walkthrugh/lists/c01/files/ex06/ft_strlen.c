/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/11 22:56:18 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/11 22:56:27 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	ft_strlen(char *str) // recebe um ponteiro para um caractere char * como argumento e retorna um inteiro int.
{
	int	i; // contador.

	i = 0; // inicializada com o valor 0 (str[0]).
	while (str[i] != '\0') // loop while que será executado enquanto o caractere atual em str[i] não for o caractere nulo '\0'. Dentro do loop, a variável i é incrementada para apontar para o próximo caractere na string str.
		i++;
	return (i); // Quando o loop termina, o valor da variável i é retornado pela função ft_strlen. Isso representa o comprimento da string str.
}
