/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/11 22:28:07 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/11 22:28:24 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
/*a função ft_swap troca os valores de duas variáveis inteiras passadas como parâmetros, usando ponteiros para manipular seus valores.*/
void	ft_swap(int *a, int *b) // recebe dois ponteiros para inteiros como parâmetros.
{
	int	tmp; //  declara-se a variável tmp que será usada para armazenar o valor de a antes de ser sobrescrito.

	tmp = *a; // o valor de a é atribuído a tmp, ou seja, a variável tmp agora contém o valor de a.
	*a = *b; // o valor de b é atribuído a a, ou seja, a agora contém o valor de b.
	*b = tmp; // o valor de tmp é atribuído a b, ou seja, b agora contém o valor original de a.
}
