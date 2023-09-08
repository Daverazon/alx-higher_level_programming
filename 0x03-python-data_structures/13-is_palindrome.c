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
	int *arr;

	if (!head)
		return (0);
	if (!*head)
		return (1);
	/*count how many elements there are*/
	while (current->next)
	{
		count++;
		current = current->next;
	}

	arr = malloc(sizeof(int) * count);
	if (!arr)
		return (0);

	for (

}
