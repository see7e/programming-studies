/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gabrodri <gabrodri@student.42.fr>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 16:06:43 by gabrodri          #+#    #+#             */
/*   Updated: 2023/10/11 14:26:47 by gabrodri        ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new_list;
	t_list	*new_node;
	void	*data;

	if (!f || !del)
		return (NULL);
	new_list = NULL;
	while (lst)
	{
		data = (*f)(lst->content);
		new_node = ft_lstnew(data);
		if (!new_node)
		{
			ft_lstclear(&new_list, del);
			del(data);
			return (NULL);
		}
		ft_lstadd_back(&new_list, new_node);
		lst = lst->next;
	}
	return (new_list);
}
