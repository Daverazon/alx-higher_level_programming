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
	listint_t *nextNode = NULL;
	int *pali = malloc(sizeof(int)), size = 1, idx = 0;

	if (!head || !pali)
		return (0);
	if (!*head)
		return (1);

	pali[0] = (*head)->n;
	nextNode = (*head)->next;
	while (nextNode)
	{
		size++;
		pali = realloc(pali, sizeof(int) * size);
		if (!pali)
		{
			free(pali);
			return (0);
		}
		pali[size - 1] = nextNode->n;
		nextNode = nextNode->next;
	}
	for (; idx < size / 2; idx++)
	{
		if (pali[idx] != pali[size - (idx + 1)])
		{
			free(pali);
			return (0);
		}
	}
	return (1);
}
