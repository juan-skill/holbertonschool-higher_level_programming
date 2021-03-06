#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @head: head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *tmp1, *tmp2;

	tmp1 = tmp2 = NULL;

	if (!head)
		return (0);

	tmp1 = tmp2 = head;

	while (tmp1 && tmp2 && tmp2->next)
	{
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;
		if (tmp1 == tmp2)
			return (1);
	}

	return (0);
}
