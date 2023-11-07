#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *prev = NULL;
	listint_t *next;
	listint_t *mid = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	next = slow;
	prev->next = NULL;
	while (slow != NULL)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	fast = *head;
	slow = prev;

	while (slow != NULL)
	{
		if (fast->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}
		fast = fast->next;
		slow = slow->next;
	}

	while (prev != NULL)
	{
		next = prev->next;
		prev->next = next;
		prev = next;
	}

	if (mid != NULL)
	{
		prev = mid;
		next = mid->next;
		prev->next = *head;
		*head = prev;
	}

	return (is_palindrome);
}
