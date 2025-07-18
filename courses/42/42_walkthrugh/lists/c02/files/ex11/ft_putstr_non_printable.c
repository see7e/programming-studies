/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_non_printable.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jfilguei <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/12 15:47:11 by jfilguei          #+#    #+#             */
/*   Updated: 2023/03/12 15:47:15 by jfilguei         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putstr_non_printable(char *str) // recebe um ponteiro para uma string como argumento. Ela não retorna nenhum valor (void).
{
	int	i; // usada como índice para percorrer a string.

	i = 0;
	while (str[i] != '\0') // enquanto o caractere atual da string não é o caractere nulo \0, que indica o final da string.
	/*Dentro do laço while, primeiro é verificado se o caractere atual é um caractere imprimível (ou seja, um caractere ASCII entre 32 e 126), ou se é um caractere não-imprimível (fora desse intervalo). Se for não-imprimível, os próximos três comandos vão escrever a sequência de escape \xy, onde xy são os dois dígitos hexadecimais que representam o valor ASCII do caractere. Isso é feito usando a função ft_putchar, que escreve um único caractere na saída padrão. A função usa um array de caracteres "0123456789abcdef" para converter o valor ASCII do caractere em dois dígitos hexadecimais.

Se o caractere atual for imprimível, a função simplesmente escreve o caractere na saída padrão usando ft_putchar.
No final do laço, a variável i é incrementada em 1, para avançar para o próximo caractere da string. Quando o laço chegar ao final da string (ou seja, quando o caractere atual for o caractere nulo \0), a função terminará e não haverá mais saída na saída padrão.*/
	{
		if (str[i] < 32 || str[i] > 126)
		{
			ft_putchar('\\');
			ft_putchar("0123456789abcdef"[str[i] / 16]);
			ft_putchar("0123456789abcdef"[str[i] % 16]);
		}
		else
			ft_putchar(str[i]);
		i++;
	}
}