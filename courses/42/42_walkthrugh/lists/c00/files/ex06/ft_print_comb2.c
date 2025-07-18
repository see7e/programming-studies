/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/09 17:06:21 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/09 17:30:17 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void print_two_digit_number(int number)
{
	// Verifica se o número é menor que 10
	if (number < 10)
	{
		// Se for, imprime um 0 e o dígito único
		ft_putchar('0');
		ft_putchar(number + '0');
	}
	else
	{
		// Se não for, imprime o primeiro dígito e o segundo dígito separadamente
		ft_putchar(number / 10 + '0');
		ft_putchar(number % 10 + '0');
	}
}

void print_two_numbers(int first, int second)
{
	// Imprime o primeiro número com dois dígitos, seguido de um espaço
	print_two_digit_number(first);
	ft_putchar(' ');

	// Imprime o segundo número com dois dígitos
	print_two_digit_number(second);

	// Se não for o último par de números, imprime uma vírgula e um espaço
	if (first != 98 || second != 99)
	{
		ft_putchar(',');
		ft_putchar(' ');
	}
}

void ft_print_comb2(void)
{
	int first;
	int second;

	// Loop através de todos os pares de números possíveis de 0 a 99
	first = 0;
	second = 0;
	while (first <= 99)
	{
		second = first + 1;
		while (second <= 99)
		{
			// Imprime o par de números e passa para o próximo segundo número
			print_two_numbers(first, second);
			second++;
		}
		// Passa para o próximo primeiro número
		first++;
	}
}
