/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bsq.h                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/27 18:38:51 by gabrodri          #+#    #+#             */
/*   Updated: 2023/03/27 18:38:53 by gabrodri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef BSQ_H
# define BSQ_H
# include <unistd.h>
# include <stdio.h>
# include <fcntl.h>
# include <stdlib.h>
# include <errno.h>
# include <sys/types.h>
# include <sys/uio.h>

void	ft_putchar(char c);
void	ft_putstr(char *str);
void	ft_putnbr(int nb);
void	ft_cat(void);
void	ft_get_second_line(int fd);
void	ft_print_names(int i, int argc, char **argv);
void	ft_display_file(int i, int fd, int argc, char **argv);
void	ft_print_solution(int i, char **argv);
int		col_nbr(char *argv);
int		row_nbr(char *argv);
int		ft_strlen(char *str);
int		ft_verif_chars(char *argv);
int		ft_verif_columns(char *argv);
int		ft_verif_returns(char *argv);
int		ft_verif_map(char *argv);
int		ft_get_next_columns(char *argv, int fd);
int		ft_atoi(char *str);
int		ft_size_file(char *argv);
int		ft_min(int a, int b, int c);
int		**ft_generate_map(int l, int c);
int		ft_biggest_square(char **map, int c, int l, char o);
int		ft_find_position_square(char **map, int c, int l, char o);
char	get_void(char *argv);
char	get_obst(char *argv);
char	ft_get_char_full(char *argv);
char	*ft_strcpy(char *dest, char *src);
char	**ft_read_file(char *argv);
char	**ft_fill_map(char **map, int c, int l, char *argv);

#endif