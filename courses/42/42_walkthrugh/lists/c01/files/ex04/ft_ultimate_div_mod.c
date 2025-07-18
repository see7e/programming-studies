/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/11 22:35:01 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/11 22:35:07 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_ultimate_div_mod(int *a, int *b) //  Ela recebe dois ponteiros para inteiros como argumentos.
{	
	// Duas variáveis locais do tipo inteiro são declaradas e inicializadas com os valores apontados pelos ponteiros "a" e "b", respectivamente.
	int	aa;
	int	bb;

	// Os valores apontados pelos ponteiros "a" e "b" são copiados para as variáveis locais "aa" e "bb".
	aa = *a;
	bb = *b;
	*a = aa / bb;
	*b = aa % bb;
}

/*A divisão inteira entre "aa" e "bb" é armazenada no local de memória apontado por "a". O restante da divisão inteira entre "aa" e "bb" é armazenado no local de memória apontado por "b".
Em resumo, a função "ft_ultimate_div_mod" divide o valor apontado por "a" pelo valor apontado por "b" e armazena o resultado da divisão no local de memória apontado por "a" e o resto da divisão no local de memória apontado por "b".*/