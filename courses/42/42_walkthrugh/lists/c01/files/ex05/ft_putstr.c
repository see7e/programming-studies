/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/11 22:42:28 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/11 22:42:41 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putstr(char *str) // recebe um ponteiro para um caractere char * como argumento e não retorna nada void.
{
	int	i; // declarada uma variável i do tipo inteiro, para contagem dos ciclos.

	i = 0; // variável i é inicializada com o valor 0, pois str[] começa sempre com o índice [0].
	while (str[i] != '\0') // loop while que será executado enquanto o caractere atual em str[i] não for o caractere nulo '\0'.
	{
		ft_putchar(str[i]); //  ft_putchar para escrever o caractere atual str[i] na tela.
		i++; // i é incrementada para apontar para o próximo caractere na string str.
	}
} // fim da função ft_putstr.
