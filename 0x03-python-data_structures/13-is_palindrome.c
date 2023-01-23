#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if a list is palindrome.
 * @head: pointer to head node.
 * Return: 1 if palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	int *lst = NULL, len = 0, i, *tail;

	listint_t *ptr = *head;

	while (ptr != NULL)
	{
		lst = realloc(lst, sizeof(int) * (len + 1));
		if (!lst)
		{
			perror("not available space, cant alloc");
			exit(98);
		}
		lst[len] = ptr->n;
		ptr = ptr->next;
		len++;
	}

	tail = lst;
	for (i = len; i > 1; i--)
		tail++;
	ptr = *head;
	for (i = len / 2; i > 0; i--)
	{
		if (*tail != ptr->n)
		{
			free(lst);
			return (0);
		}
		tail--;
		ptr = ptr->next;
	}
	free(lst);
	return (1);
}
