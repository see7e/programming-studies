/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_memory.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jfilguei <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/12 15:47:39 by jfilguei          #+#    #+#             */
/*   Updated: 2023/03/12 15:47:45 by jfilguei         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <string.h>
#include <stdio.h>

void    ft_putchar(char c)
{
    write(1, &c, 1);
}

void    print_spaces(int num_chars)
{
    int    k;

    k = 0;
    write(1, "  ", 2);
    if (num_chars % 2 == 1)
        ft_putchar(' ');
    while (k < 40 - 2 * (num_chars + 1) - (num_chars + 1) / 2)
    {
        ft_putchar(' ');
        k++;
    }
}

void	coluna_1(unsigned char *addr)
{
	int	i;
	char	hexcode[16];
	unsigned long int	address;

	i = 16;
	address = addr;
	while (i > 0)
	{
        if (address % 16 < 10)
            hexcode[i - 1] = (address % 16) + '0';
        else
            hexcode[i - 1] = (address % 16) + ('a' - 10);
        address /= 16;
        i--;
    }
	write(1, hexcode, 16);
	ft_putchar(':');
	ft_putchar(' ');
}

void	coluna_2(unsigned char *str, int tamanho)
{
    int        i;

    i = 0;
    while (i < tamanho && i < 16)
    {
        ft_putchar("0123456789abcdef"[str[i] / 16]);
        ft_putchar("0123456789abcdef"[str[i] % 16]);
        i++;
        if (i % 2 == 0)
            ft_putchar(' ');
    }
    if (i < 15)
    {
        print_spaces(i);
    }
}

void    coluna_3(unsigned char *str, int tamanho)
{
    int    i;

    i = 0;
    while (i < tamanho && i < 16)
    {
        if (str[i] < 32 || str[i] > 126)
            write(1, ".", 1);
        else
            write(1, &str[i], 1);
        i++;
    }
	ft_putchar('\n');
}

void    *ft_print_memory(void *addr, unsigned int size)
{
    unsigned int    i;

    i = 0;
    while (i < size)
    {
        coluna_1(addr + i);
        coluna_2(addr + i, size - i);
        coluna_3(addr + i, size - i);
        i += 16;
    }
    return (addr);
}

int    main(void)
{
    char *str = "Bonjour les aminches\n\b\rc  est fou\ntout\rce qu on peut faire avec\r\n\tprint_memory\n\n\r\blol\rlol\r \b";

    ft_print_memory(str, 300);
    return (0);
}