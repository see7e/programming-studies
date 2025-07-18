/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_alphabet.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/08 20:55:59 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/08 21:03:44 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_print_alphabet(void) //function called ft_print_alphabet that takes no arguments and returns no value.
{	
	char	letter; //declares a variable called letter of type char.

	letter = 'a'; //initializes the letter variable to the ASCII code for lowercase 'a'.
	while (letter <= 'z') //starts a loop that will continue executing as long as the value of letter is less than or equal to the ASCII code for lowercase 'z'.
	{
		write (1, &letter, 1); 
		letter++;//increments the value of letter by one, so that it will eventually reach the ASCII code for lowercase 'z' and exit the loop.
	} //marks the end of the while loop 
} //end of the ft_print_alphabet function.
