#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is palindrome
 *
 * @head: pointer that points to head of list
 * Return: 1 if check, 0 if no
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr_h, *ptr_t;
	int i, len, len2;

	len = len2 = 0;
	ptr_h = ptr_t = *head;

	if (head != NULL || *head != NULL)
		return (1);

	for (; ptr_t->next != NULL; len++)
		ptr_t = ptr_t->next;


	ptr_t->next = *head; /* pos = 0 */
	/* ptr_t            pos = len*/
	len2 = len;
	i = 0;
	while (i <= len / 2)
	{
		if (ptr_h->n == ptr_t->n)
		{
			ptr_h = ptr_h->next;
			while (len2-- > 0)
				ptr_t = ptr_t->next;
		}
		else
			return (0);

		len2 = len;
		i += 1;
	}


	return (1);
}
