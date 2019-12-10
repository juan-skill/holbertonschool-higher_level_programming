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

	if (head == NULL)
		return (0);

	tmp1 = tmp2 = head;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		tmp2 = tmp2->next->next;
		if (tmp1 == tmp2)
			return (1);
		if (tmp2 == NULL)
			return (0);
		tmp2 = tmp2->next->next;
		if (tmp1 == tmp2)
			return (1);
		tmp1 = tmp1->next;
	}

	return (0);
}
