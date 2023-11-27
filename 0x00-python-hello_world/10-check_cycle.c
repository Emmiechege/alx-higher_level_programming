#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: a pointer to the singly linked list
 * Return; 1 if it has a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *start_ptr = list;
	listint_t *end_ptr = list;

	if(!list)
		return (0);

	while (start_ptr && end_ptr && end_ptr->next)
	{
		start_ptr = start_ptr->next;
		end_ptr = end_ptr->next->next;
		if (start_ptr == end_ptr)
			return (1);
	}
	return (0);
}
