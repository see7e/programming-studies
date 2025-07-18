/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/11 22:29:27 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/11 22:29:43 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_div_mod(int a, int b, int *div, int *mod) // recebe dois números inteiros "a" e "b" como argumentos, além de dois ponteiros para inteiros "div" e "mod" que serão utilizados para armazenar o resultado da divisão e do resto da divisão de "a" por "b"
{
	// calculam o resultado da divisão de "a" por "b" e o resto da divisão de "a" por "b", respectivamente, e armazenam nos ponteiros para as variáveis
	*div = a / b;
	*mod = a % b;
}
