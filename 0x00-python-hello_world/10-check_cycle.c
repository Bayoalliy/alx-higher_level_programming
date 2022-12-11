#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * check_cycle - checks if a linked list has a cycle.
 * @list: pointer to the head node.
 * Return: 1(if true), 0(if false).
 */

int check_cycle(listint_t *list)
{
	listint_t **arr;

	int i = 0, j = 3;

	if (list)
	{
		arr = malloc(sizeof(int *) * 2);
		arr[0] = list;
		arr[1] = NULL;
	}
	while (list)
	{
		i = 0;
		while (arr[i])
		{
			if (list->next  == arr[i])
			{
				free(arr);
				return (1);
			}
			i++;
		}
		list = list->next;
		arr = realloc(arr, sizeof(int *) * j++);
		arr[i] = list;
		arr[i + 1] = NULL;
	}
	free(arr);
	return (0);
}
