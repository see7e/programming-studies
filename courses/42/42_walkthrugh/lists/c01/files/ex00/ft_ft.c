/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ft.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/11 21:43:07 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/11 21:43:39 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
/*A função "ft_ft" recebe um ponteiro para um número inteiro como argumento. Dentro da função, o valor apontado pelo ponteiro é definido como 42. Em outras palavras, a função muda o valor da variável que o ponteiro está apontando para o valor 42.*/
void	ft_ft(int *nbr)
{
	*nbr = 42;
}
