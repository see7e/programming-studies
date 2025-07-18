/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/11 23:11:50 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/11 23:12:11 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_rev_int_tab(int *tab, int size) // recebe um ponteiro para um inteiro int *tab e um inteiro int size como argumentos e não retorna nada void.
{
	int	i;	// contador
	int	tmp;

	i = 0;
	while (i < (size / 2)) // executado enquanto i for menor que a metade do tamanho size do array tab.
	{
		// swap
		tmp = tab[i]; // valor atual do elemento tab[i] é armazenado em uma variável auxiliar tmp.
		tab [i] = tab [size - 1 - i]; // O valor do elemento tab[i] é substituído pelo valor do elemento correspondente no final do array tab[size - 1 - i].
		tab [size - 1 - i] = tmp; // O valor do elemento correspondente no final do array tab[size - 1 - i] é substituído pelo valor armazenado na variável auxiliar tmp.
		i++; // A variável i é incrementada para avançar para o próximo par de elementos no array tab.
	}
}
