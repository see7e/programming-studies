/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_int_tab.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/12 00:02:57 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/12 00:03:02 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_swap(int *a, int *b)
{
	int	tmp;

	tmp = *a;
	*a = *b;
	*b = tmp;
}

void	ft_sort_int_tab(int *tab, int size) // recebe um ponteiro para um inteiro int *tab e um inteiro int size como argumentos e não retorna nada void.
{
	// Aqui são declaradas duas variáveis aux1 e aux2 do tipo inteiro e inicializadas com os valores 0 e 1, respectivamente.
	int	aux1;
	int	aux2;

	aux1 = 0;
	aux2 = 1;

	/*loop while aninhado que irá comparar cada par de elementos consecutivos no
	array tab e, se o elemento à esquerda for maior do que o elemento à direita,
	chama a função ft_swap para trocá-los de lugar. O loop interno começa em 
	aux2 e percorre até o final do array tab, comparando cada elemento com 
	tab[aux1]. O loop externo avança para o próximo elemento em tab[aux1] e 
	reinicia o loop interno em aux2 = aux1 + 1.*/
	while (aux1 < size)
	{
		while (aux2 < size)
		{
			if (tab[aux1] > tab[aux2])
				ft_swap(&tab[aux1], &tab[aux2]);
			aux2++;
		}
		aux1++;
		aux2 = aux1 + 1;
	}
}
