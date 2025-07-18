/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/12 15:46:07 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/12 15:46:11 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

char	ft_strlowcase(char *str)
{
	if (*str >= 'A' && *str <= 'Z')
		*str += 32;
	return *str;
}

char	ft_strupcase(char *str)
{
	if (*str >= 'a' && *str <= 'z')
		*str -= 32;
	return *str;
}

char	*ft_strcapitalize(char *str)
{
	int		i; // Contador do loop.
	char	a;
	char	novo;
	
	i = 0;  // Inicializa a variável "i" com 0
	a = '1'; // Inicializa a variável "a" com o caractere '1'
	while (str[i] != '\0') // Loop para percorrer cada caractere da string até o final
	{
		if (i == 0) // Condição para o primeiro caractere da string
			novo = ft_strupcase(&str[i]); // Transforma o primeiro caractere em maiúsculo
		else if (!((a >= 'a' && a <= 'z') || (a >= 'A' && a <= 'Z')
				|| (a >= '0' && a <= '9'))) // Condição para transformar em maiúsculo o caractere após um espaço ou sinal de pontuação
			novo = ft_strupcase(&str[i]); // Transforma o caractere em maiúsculo
		else 
			novo = ft_strlowcase(&str[i]); // Transforma o caractere em minúsculo
		a = str[i]; // Armazena o caractere atual na variável "a"
		str[i] = novo; // Atribui o novo valor do caractere à string
		i++; // Incrementa a variável "i" para ir para o próximo caractere
	}
	return (str); // Retorna a string transformada
}