/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_combn.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/09 18:19:20 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/09 19:50:10 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	print_number(int digits[], int n)
{
	/*Essa função é responsável por imprimir um número de n dígitos na tela. Ela recebe um vetor digits com os dígitos do número e um inteiro n com o número de dígitos.*/
	int	i;

	i = 0;
	while (i < n)
	{
		ft_putchar(digits[i] + '0'); // converte o número para o seu caractere ASCII correspondente e imprime na tela
		i++;
	}
	if (digits[0] != 9 - n + 1) // verifica se o primeiro dígito é menor que 9 - n + 1
	{
		ft_putchar(',');
		ft_putchar(' ');
	}
}

void	ft_print_combn_vector(int pos, int digits[], int n, int prev)
{
	/*Essa função é responsável por gerar todas as combinações de n dígitos distintos em ordem crescente. Ela recebe quatro parâmetros: a posição atual (pos) que está sendo preenchida no vetor digits, o vetor digits com os dígitos já preenchidos, o número de dígitos n e o último dígito preenchido prev.
	Ela utiliza a recursão para preencher o vetor digits com todas as combinações possíveis*/

	int	i;

	if (pos != n)
	{
		i = prev + 1;
		while (i <= 9)
		{
			digits[pos] = i;
			ft_print_combn_vector(pos + 1, digits, n, digits[pos]);
			if (pos == n - 1)
			{
				print_number(digits, n); // imprime o número formado pelos dígitos do vetor
			}
			i++;
		}
	}
}

void	ft_print_combn(int n)
{
	int	digits[10];

	ft_print_combn_vector(0, digits, n, -1);
}
