/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/20 13:14:44 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/20 13:14:45 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//https://github.com/pasqualerossi/42-Piscine/blob/ca25ca7379cf2c99b001ba4b91da645cc30749dd/42%20Piscine%20Exam/Exam%20Answers/Level%202/ft_atoi/ft_atoi.c*/
/* PASSA SOMENTE NOS DOIS PRIMEIROS - PQ?
int	ft_atoi(char *str)
{
	int result;
	int sign;

	result = 0;
	sign = 1;
	while (*str == ' ' || (*str >= 9 && *str <= 13))
		str++;
	if (*str == '-')
		sign = -1;
	if (*str == '-' || *str == '+')
		str++;
	while (*str >= '0' && *str <= '9')
	{
		result = result * 10 + *str - '0';
		str++;
	}
	return (sign * result);
}
*/
//https://github.com/7eith/Piscine42/blob/master/c04/ex03/ft_atoi.c
/* FUNFA SUAVE */
int		ft_atoi(char *str)
{
	int		count;
	int		negative;
	int		number;

	count = 0;
	negative = 0;
	number = 0;
	//verifica a ocorrencia de elem especiais
	while ((str[count] > 8 && str[count] < 14) || (str[count] == 32))
		count++;
	//verifica a ocorrencia de +-(usado em teste logico)
	while ((str[count] != '\0') && (str[count] == '+' || str[count] == '-'))
	{
		if (str[count] == '-')
			negative++;
		count++;
	}
	//verifica se esta dentro da escala dos numer
	while ((str[count] != '\0') && (str[count] >= 48 && str[count] <= 57))
	{
		//subtrai 48(0) p/ buscar a distancia p/ o 0
		//no prox ciclo o numero passado vai aumentar uma dezena
		number = number * 10 + str[count] - 48;
		count++;
	}
	//se a quant de +- for par, o numero e positivo
	if (negative % 2 != 0)
		return (number * -1);
	return (number);
}

//https://github.com/julekgwa/exams/blob/master/exam_prac_01/ft_atoi.c
/* NAO PASSA EM NENHUM
int	ft_atoi(char *str)
{
	int	sum;
	int	sign;
	int	found;

	sum = 0;
	sign = 1;
	found = 1;
	while (*str == ' ' || *str == '\t' || *str == '\n' || *str == '\f' || *str == '\r')
		str++;
	if (*str == '-')
		sign = -1;
	if (*str == '-' || *str == '+')
		str++;
	while (*str && found)
	{
		if (*str >= '0' && *str <= '9')
			sum = sum * 10 + *str - '0';
		else
			found = 0;
		str++;
	}
	return (sign * sum);
}
*/
//https://github.com/Stroi/42/blob/master/42/42exams/lvl2/ft_atoi/ft_atoi.c
/* CONFUSO DEMAIS
int		is_digit(char c)
{
	if (c >= '0' && c <= '9')
	{
		return (1);
	}
	return (0);
}

int		is_space(char c)
{
	if (c == ' ' || c == '\t' || c == '\n')
	{
		return (1);
	}
	if (c == '\f' || c == '\v')
	{
		return (1);
	}
	return (0);
}

int		ft_atoi(const char *str)
{
	int result;
	int sign;
	int i;

	result = 0;
	sign = 1;
	i = 0;
	// Going through spaces
	while (is_space(str[i]))
	{
		i++;
	}
    // Checking the sings, if there is '-' change "sign" to "-1" 
	if (str[i] == '-')
        sign = -1;
    // Increase the index after first sign
    if (str[i] == '-' || str[i] == '+')
        i++;
	// If there are numbers after spaces or signs, loop will go through them until the end of first number.
	while (is_digit(str[i]))
	{
		// Add current number to the result
		result = result + (str[i] - '0'); 
		// Check if there is a number after this one, if yes multiply by ten
		// Example: 123asd
		// result = 1 
		// next character is a number therefore:
		// result * 10 (= 10)
		// i++;
		// current number is 2
		// result + 2 (= 12)
		// ...
		// next is a, therefore don't multiply 10'
		// loop ends
		if (is_digit(str[i + 1]))
			result = result * 10;
		i++;
	}
	return (result * sign);
}
*/
