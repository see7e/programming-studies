/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/09 16:03:25 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/09 16:03:38 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	print_three_numbers(char first, char second, char third)
{
	ft_putchar(first);	// imprime o primeiro caractere
	ft_putchar(second);	// imprime o segundo caractere
	ft_putchar(third);	// imprime o terceiro caractere
	if (first != '7' | second != '8' | third != '9')	// verifica se os caracteres são diferentes de "789"
	{
		ft_putchar(',');	// imprime uma vírgula
		ft_putchar(' ');	// imprime um espaço em branco
	}
}

void	ft_print_comb(void)
{
	char	first;
	char	second;
	char	third;

	first = '0';	// inicializa o primeiro caractere com '0'
	second = '0';	// inicializa o segundo caractere com '0'
	third = '0';	// inicializa o terceiro caractere com '0'
	while (first <= '9')	// enquanto o primeiro caractere for menor ou igual a '9'
	{
		second = first + 1;	// inicializa o segundo caractere com o caractere seguinte ao primeiro
		while (second <= '9')	// enquanto o segundo caractere for menor ou igual a '9'
		{
			third = second + 1;	// inicializa o terceiro caractere com o caractere seguinte ao segundo
			while (third <= '9')	// enquanto o terceiro caractere for menor ou igual a '9'
			{
				print_three_numbers(first, second, third);	// chama a função para imprimir os três caracteres
				third++;	// incrementa o terceiro caractere
			}
			second++;	// incrementa o segundo caractere
		}
		first++;	// incrementa o primeiro caractere
	} // fim do loop
} // fim da função
