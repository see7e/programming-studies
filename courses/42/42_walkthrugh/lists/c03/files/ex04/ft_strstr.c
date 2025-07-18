/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/19 01:04:47 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/19 01:04:49 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	needle_in_haystack(char *haystack, char *needle)
/*Executa o teste lógico de resultado 0(false) ou 1(true), usado dentro da função "principal".*/
{
	int	i;

	i = 0;
	while (needle[i] != '\0')
	{
		if (needle[i] != haystack[i])
			return (0);
		i++;
	}	
	return (1);
}

char	*ft_strstr(char *str, char *to_find) // recebe dois argumentos: um ponteiro para a string principal str e um ponteiro para a string a ser encontrada to_find.
/*Em resumo, a função ft_strstr procura a string to_find na string str. Se to_find for encontrada em str, a função retorna um ponteiro para a primeira ocorrência de to_find em str. Se to_find não for encontrada em str, a função retorna um ponteiro nulo.*/
{
	// Inicialização da variável i e verificação se a string a ser encontrada to_find é vazia. Se to_find for uma string vazia, então ela já foi encontrada em qualquer posição de str, e a função retorna um ponteiro para o início de str.
	int	i;

	i = 0;
	if (to_find[0] == '\0')
		return (str);
	while (str[i] != '\0') // Laço de repetição while que itera enquanto o caractere atual de str não for o caractere nulo \0. Dentro do laço, a função verifica se o caractere atual de str é igual ao primeiro caractere da string a ser encontrada to_find. Se sim, a função chama a função auxiliar needle_in_haystack para verificar se o restante de to_find coincide com os caracteres correspondentes de str a partir da posição atual. Se needle_in_haystack retornar verdadeiro (ou seja, se to_find for encontrado em str), a função retorna um ponteiro para a posição atual de str. Se to_find não for encontrado nesta posição de str, o laço continua verificando o próximo caractere de str.
	{
		if (str[i] == to_find[0])
			if (needle_in_haystack(str + i, to_find))
				return (str + i);
		i++;
	}
	return ((void *)0); // Se o laço terminar sem encontrar to_find em str, a função retorna um ponteiro nulo (void *)0.
}
/*Um ponteiro nulo (void *)0 é um ponteiro que não aponta para nenhuma posição válida de memória. Em outras palavras, é um ponteiro que não possui referência para nenhum objeto ou valor.
Quando um ponteiro nulo é retornado por uma função, significa que a função não conseguiu encontrar ou retornar um valor válido. Por exemplo, na função ft_strstr, se a string to_find não for encontrada na string str, a função retorna um ponteiro nulo para indicar que não foi possível encontrar a string to_find.
O ponteiro nulo é representado pela macro NULL na linguagem C. É importante verificar se um ponteiro é nulo antes de acessar o valor ou o objeto que ele aponta, para evitar erros de segmentação ou outros problemas de memória.*/