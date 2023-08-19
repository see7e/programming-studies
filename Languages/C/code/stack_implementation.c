// Including standard input/output and standard library headers
#include <stdio.h>
#include <stdlib.h>

// Defining maximum capacity of the stack
#define MAX 10

// Global variable to track number of items in the stack
int count = 0;

// Defining a structure for stack
struct stack
{
	int items[MAX]; // Array to store items in the stack
	int top; // Index of the top element of the stack
};

// Typedefining the structure as 'st'
typedef struct stack st;

// Function to create an empty stack
void createEmptyStack(st *s)
{
	s->top = -1; // Initializing the top index to -1 to indicate empty stack
}

// Function to check if the stack is full
int isfull(st *s)
{
	if (s->top == MAX - 1) // If top index is equal to the maximum capacity, then stack is full
		return 1;
	else
		return 0;
}

// Function to check if the stack is empty
int isempty(st *s)
{
	if (s->top == -1) // If top index is -1, then stack is empty
		return 1;
	else
		return 0;
}

// Function to add new items into the stack
void push(st *s, int newitem)
{
	if (isfull(s)) // Checking if the stack is full
		printf("STACK FULL");
	else
	{
		s->top++; // Incrementing the top index
		s->items[s->top] = newitem; // Adding new item to the top of the stack
	}
	count++; // Incrementing the global count variable to keep track of items in the stack
}

// Function to remove an item from the top of the stack
void pop(st *s)
{
	if (isempty(s)) { // Checking if the stack is empty
		printf("\n STACK EMPTY \n");
	}
	else
	{
		printf("Item popped= %d", s->items[s->top]); // Printing the item that is being removed
		s->top--; // Decrementing the top index
	}
	count--; // Decrementing the global count variable to keep track of items in the stack
	printf("\n");
}

// Function to print all the items in the stack
void printStack(st *s)
{
	int i = 0;

	printf("Stack: ");
	while(i < count) // Looping through all the items in the stack and printing them
	{
		printf("%d ", s->items[i]);
		i++;
	}
	printf("\n");
}

// Main function
int	main()
{
	int ch;
	st *s = (st *)malloc(sizeof(st)); // Dynamically allocating memory for the stack

	createEmptyStack(s); // Initializing the stack as empty

	push(s, 1); // Adding items to the stack
	push(s, 2);
	push(s, 3);
	push(s, 4);

	printStack(s); // Printing all the items in the stack

	pop(s); // Removing the top item from the stack

	printf("\nAfter popping out\n");
	printStack(s); // Printing all the items in the stack after removing an item
}
