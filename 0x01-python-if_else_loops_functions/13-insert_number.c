#include "lists.h"

/**
 * insertNode - Inserts a new nodeat a given position.
 * @H: Head of a list.
 * @num: index of the list where the new node is
 * added.
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insertNode(listint_t **H, int num)
{
	listint_t *new;
	listint_t *h;
	listint_t *h_prev;

	h = *H;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->i > num)
			break;
		h_prev = h;
		h = h->nt;
	}

	new->i = num;

	if (*H == NULL)
	{
		new->nt = NULL;
		*H = new;
	}
	else
	{
		new->nt = h;
		if (h == *H)
			*H = new;
		else
			h_prev->nt = new;
	}

	return (new);
}
