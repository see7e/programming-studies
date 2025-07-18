/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/08 20:29:04 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/08 21:06:33 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*função chamada ft_putchar que escreve um
caractere na saída padrão (stdout) usando a
função write da biblioteca unistd.h.*/

#include <unistd.h> //fornece acesso a vários recursos do sistema operacional, incluindo funções para interagir com arquivos, diretórios, processos e para a execução de chamadas de sistema.

void	ft_putchar(char c) // função ft_putchar que recebe um argumento char c e não retorna nada (void). Essa função é responsável por escrever o caractere c na saída padrão.
{
	write(1, &c, 1);
}

/*A função write é uma chamada de sistema que escreve um número especificado de bytes para um arquivo.

Nesse caso, o primeiro argumento 1 é o descritor de arquivo para a saída padrão, o segundo argumento &c é um ponteiro para o caractere que será escrito, e o terceiro argumento 1 é o número de bytes que serão escritos, que é sempre igual a 1,*/