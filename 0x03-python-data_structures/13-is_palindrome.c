#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int count = 0, x = 0;
	int *arr = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	/*count how many elements there are*/
	while (current)
	{
		count++;
		current = current->next;
	}

	arr = malloc(sizeof(int) * count);
	if (arr == NULL)
		return (0);

	current = *head;

	for (x = 0; x < count; x++)
	{
		arr[x] = current->n;
		current = current->next;
	}

	for (x = 0; x < count / 2; x++)
	{
		if (arr[x] != arr[count - (x + 1)])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
