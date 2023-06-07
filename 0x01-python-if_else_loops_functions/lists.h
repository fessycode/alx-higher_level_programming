#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked node structure.
 * @i: integer
 * @nt: points to the next node
 *
 */
typedef struct listint_s
{
	int i;
	struct listint_s *nt;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int i);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
