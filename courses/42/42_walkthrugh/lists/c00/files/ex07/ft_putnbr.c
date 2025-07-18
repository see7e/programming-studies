/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/09 18:10:04 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/09 18:11:48 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putnbr(int nb) // função ft_putnbr, que recebe um argumento int chamado nb e não retorna nada (void).
{
	long int	n; // variável do tipo long int chamada n e atribuição do valor de nb a ela. Isso é feito para garantir que o valor passado como argumento possa ser negativo, sem causar erros devido a um overflow.

	n = nb;
	if (nb < 0) // Testa se o valor de nb é negativo. Se for, imprime um sinal de menos (-) na tela e converte n em um valor positivo equivalente (multiplicando por -1).
	{
		ft_putchar('-');
		n = -n;
	}
	if (n < 10) // Se n for menor que 10, significa que n é um único dígito e pode ser impresso diretamente na tela usando a função ft_putchar. O valor de n é convertido para um caractere usando a tabela ASCII, adicionando o valor do caractere 0 (que tem um valor ASCII de 48).
	{
		ft_putchar(n + '0');
	}
	else // Se n não for menor que 10, significa que n tem dois ou mais dígitos. Nesse caso, a função é chamada recursivamente com o quociente da divisão de n por 10 (ou seja, o número sem o último dígito) e o último dígito é impresso na tela usando ft_putchar da mesma maneira explicada anteriormente. A recursão é usada para imprimir todos os dígitos na ordem correta, um de cada vez, até que o número completo seja impresso.
	{
		ft_putnbr(n / 10);
		ft_putchar(n % 10 + '0');
	}
}
