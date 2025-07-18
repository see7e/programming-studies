/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strupcase.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/12 15:28:45 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/12 15:28:50 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

char	*ft_strupcase(char *str) // recebe um ponteiro para um caractere (ou seja, uma string) como argumento e retorna um ponteiro para um caractere (ou seja, a mesma string, mas com todos os caracteres em maiúsculas). O modificador "char *" indica que o valor de retorno é um ponteiro para um caractere.
{
	int	i; // usada para percorrer a string.

	i = 0;
	while (str[i] != '\0') //percorre a string "str" caractere por caractere, até encontrar o caractere nulo '\0'. A instrução condicional dentro do loop verifica se o caractere atual é uma letra minúscula (entre 'a' e 'z') e, se for, converte-o para maiúscula (subtraindo 32 do valor ASCII do caractere, que é a diferença entre as tabelas ASCII de caracteres maiúsculos e minúsculos). O contador "i" é incrementado a cada iteração do loop, para avançar para o próximo caractere da string.
	{
		if (str[i] >= 'a' &&  str[i] <= 'z' )
			str[i] -= 32;
		i++;
	}
	return (str); // retorna o ponteiro para a string "str" (que agora tem todos os caracteres em maiúsculas), após o loop ter sido concluído.
}