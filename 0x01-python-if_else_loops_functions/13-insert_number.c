#include "lists.h"

/**
 *insert_node - inserts a number into a sorted singly linked list.
 *
 *@head: pointer that point to head of list
 *@number: element to store inside new node
 *Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_node, *current;

	n_node = NULL;

	if (!head)
		return (NULL);

	n_node = malloc(sizeof(listint_t));
	if (!n_node)
		return (NULL);

	n_node->n = number;

	current = *head;
	if (*head == NULL)
	{
		*head = n_node;
		n_node->next = NULL;
	}
	else if (number < current->n)
	{
		n_node->next = current;
		*head = n_node;
	}
	else
	{
		while (number > current->next->n && current)
		{

			current = current->next;
		}
		n_node->next = current->next;
		current->next = n_node;
	}

	return (n_node);
}
