#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is palindrome
 *
 * @head: pointer that points to head of list
 * Return: 1 if check, 0 if no
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr_h, *ptr_t, *ptr_next;
	int i, len, b_len;

	len = b_len = 0;
	ptr_h = ptr_t = *head;
	ptr_next = NULL;

	if (head != NULL || *head != NULL)
		return (1);

	for (; ptr_t->next != NULL; len++)
		ptr_t = ptr_t->next;

	b_len = len;
	ptr_next = ptr_t;
	ptr_t->next = *head;

	i = 0;
	while (i < len / 2)
	{
		if (ptr_h->n == ptr_t->n)
		{
			ptr_h = ptr_h->next;
			while (b_len-- > 0)
				ptr_t = ptr_t->next;
		}
		else
			return (0);

		b_len = len;
		i += 1;
	}
	ptr_next->next = NULL;

	return (1);
}
