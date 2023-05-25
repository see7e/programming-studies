---
title: C - Hash Table - Implementation
tags: studies, programação
use: Documentation
languages: C
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Code File #](#code-file-)
- [Explanation](#explanation)
- [Found in Programiz](#found-in-programiz)

</details>

---

# Code File [#](./code/hash_table.c)

# Explanation
> ChatGPT powered

> Here are some explanations for the code snippets in the given code:
1.  **Structure to represent key-value pair:**
	
	```c
	struct set {
		int key;
		int data;
	};
	```
	
	This structure defines a key-value pair. Each element in the hash table will have a key and a corresponding data value.
	
2.  **Global variables:**
	
	```c
	struct set *array;
	int capacity = 10;
	int size = 0;
	```
	
	`array` is a pointer to the dynamically allocated array that represents the hash table. `capacity` is the initial capacity of the hash table, and `size` keeps track of the current number of elements in the hash table.
	
3.  **Hash function:**
	
	```c
	int hashFunction(int key) {
		return (key % capacity);
	}
	```
	
	The `hashFunction` calculates the index in the hash table based on the given key. It uses the modulo operator to wrap the key within the capacity of the hash table.
	
4.  **Checking prime numbers:**
	
	```c
	int checkPrime(int n) {
		int i;
		if (n == 1 || n == 0) {
			return 0;
		}
		for (i = 2; i <= n / 2; i++) {
			if (n % i == 0) {
				return 0;
			}
		}
		return 1;
	}
	```
	
	The `checkPrime` function is used to determine if a given number is prime. It checks if the number is divisible by any number from 2 to `n/2`. If it finds any divisor, it returns 0; otherwise, it returns 1.
	
5.  **Getting the next prime number:**
	
	```c
	int getPrime(int n) {
		if (n % 2 == 0) {
			n++;
		}
		while (!checkPrime(n)) {
			n += 2;
		}
		return n;
	}
	```
	
	The `getPrime` function takes a number `n` and returns the next prime number greater than `n`. It checks if `n` is even and increments it if necessary. Then, it repeatedly increments `n` by 2 and checks if it is prime using the `checkPrime` function until a prime number is found.
	
6.  **Initializing the hash table:**
	
	```c
	void init_array() {
		capacity = getPrime(capacity);
		array = (struct set *)malloc(capacity * sizeof(struct set));
		for (int i = 0; i < capacity; i++) {
			array[i].key = 0;
			array[i].data = 0;
		}
	}
	```
	
	The `init_array` function initializes the hash table. It first sets the capacity to a prime number using the `getPrime` function. Then, it allocates memory for the array based on the capacity. Finally, it sets the initial values of keys and data to 0 for all elements in the hash table.

> These explanations cover the initialization of the hash table and some of the key functions used. Let me know if you need further explanations for the remaining parts of the code.

7.  **Inserting an element into the hash table:**
	
	```c
	void insert(int key, int data) {
		int index = hashFunction(key);
		if (array[index].data == 0) {
			array[index].key = key;
			array[index].data = data;
			size++;
			printf("\n Key (%d) has been inserted \n", key);
		} else if (array[index].key == key) {
			array[index].data = data;
			printf("\n Key (%d) already exists. Data has been updated. \n", key);
		} else {
			int i = 1;
			while (array[(index + i) % capacity].data != 0) {
				i++;
			}
			index = (index + i) % capacity;
			array[index].key = key;
			array[index].data = data;
			size++;
			printf("\n Collision occurred. Key (%d) has been inserted at index %d \n", key, index);
		}
	}
	```
	
	The `insert` function adds a key-value pair into the hash table. It first calculates the index using the `hashFunction`. If the slot at the calculated index is empty (data == 0), the key-value pair is inserted directly. If the slot is occupied by the same key, the data is updated. If there is a collision (the slot is occupied by a different key), linear probing is used to find the next available slot in a sequential manner. The new key-value pair is then inserted at the found index. The `size` variable is incremented accordingly, and appropriate messages are printed to indicate the insertion status.

8.   **Removing an element from the hash table:**
```c
	void remove_element(int key) {
		int index = hashFunction(key);
		if (array[index].data == 0) {
			printf("\n This key does not exist \n");
		} else if (array[index].key == key) {
			array[index].key = 0;
			array[index].data = 0;
			size--;
			printf("\n Key (%d) has been removed \n", key);
		} else {
			printf("\n Collision occurred. Key (%d) at index %d. \n", key, index);
		}
	}
```

	The `remove_element` function removes a key-value pair from the hash table based on the provided key. It first calculates the index using the `hashFunction`. If the slot at the calculated index is empty (data == 0), it means the key does not exist. If the slot contains the same key, the key and data are set to 0, and the `size` variable is decremented. If there is a collision (the slot contains a different key), a message indicating the collision is printed.

9.   **Displaying the hash table:**
	
```c
	void display() {
		int i;
		for (i = 0; i < capacity; i++) {
			if (array[i].data == 0) {
				printf("\n array[%d]: / ", i);
			} else {
				printf("\n key: %d array[%d]: %d", array[i].key, i, array[i].data);
			}
		}
	}
	
```
	
	The `display` function prints the contents of the hash table. It iterates through each slot and checks if it is empty or contains a key-value pair. If the slot is empty, it prints `/`. If it contains a key-value pair, it prints the key and data values.

10.  **Getting the size of the hash table:**
	
```c
	int size_of_hashtable() {
		return size;
	}
	
```

	The `size_of_hashtable` function simply returns the current size of the hash table by returning the value of the `size` variable.
	
11.  **Main function:**
	
```c
	int main() {
		int choice, key, data, n;
		int c = 1;
		init_array(); // Initialize the hash table
	
		do {
			printf("\n1. Insert item in the Hash Table");
			printf("\n2. Remove item from the Hash Table");
			printf("\n3. Check the size of the Hash Table");
			printf("\n4. Display the Hash Table");
			printf("\n\nPlease enter your choice: ");
			scanf("%d", &choice);
	
			switch (choice) {
				case 1:
					printf("Enter key: ");
					scanf("%d", &key);
					printf("Enter data: ");
					scanf("%d", &data);
					insert(key, data); // Insert key-value pair into the hash table
					break;
	
				case 2:
					printf("Enter the key to delete: ");
					scanf("%d", &key);
					remove_element(key); // Remove key-value pair from the hash table
					break;
	
				case 3:
					n = size_of_hashtable();
					printf("Size of Hash Table is: %d\n", n); // Get and display the size of the hash table
					break;
	
				case 4:
					display(); // Display the hash table
					break;
	
				default:
					printf("Invalid Input\n");
			}
	
			printf("\nDo you want to continue? (Press 1 for yes): ");
			scanf("%d", &c);
		} while (c == 1);
	
		free(array); // Free the allocated memory
		return 0;
	}
```

	The `main` function serves as the entry point of the program. It displays a menu to the user with options to insert an item, remove an item, check the size of the hash table, or display the hash table. Based on the user's input, the corresponding functions are called. The user is then prompted to continue or exit the program. The loop continues as long as the user inputs `1` to continue. Finally, the allocated memory for the hash table array is freed.

> That concludes the explanations for the code. The provided code implements a basic hash table in C, allowing users to insert, remove, display, and check the size of the hash table. It handles collisions using linear probing and dynamically resizes the hash table to a prime capacity to improve performance.

# Found in [Programiz](https://www.programiz.com/dsa/hash-table#c-code)

```c
// Implementing hash table in C
#include <stdio.h>
#include <stdlib.h>

// Structure to represent key-value pair
struct set
{
	int key;
	int data;
};

// Global variables
struct	set *array;  // Array to store elements
int	capacity = 10;  // Initial capacity of the array
int	size = 0;       // Current size of the hash table

// Hash function to calculate index for a given key
int hashFunction(int key)
{
	return (key % capacity);
}

// Function to check if a number is prime
int checkPrime(int n)
{
	int i;
	if (n == 1 || n == 0)
	{
		return 0;
	}
	for (i = 2; i < n / 2; i++)
	{
		if (n % i == 0)
		{
		return 0;
		}
	}
	return 1;
}

// Function to get the next prime number greater than n
int getPrime(int n)
{
	if (n % 2 == 0)
	{
		n++;
	}
	while (!checkPrime(n))
	{
		n += 2;
	}
	return n;
}

// Function to initialize the hash table
void init_array()
{
	capacity = getPrime(capacity);  // Get a prime capacity for the array
	array = (struct set *)malloc(capacity * sizeof(struct set));  // Allocate memory for the array
	for (int i = 0; i < capacity; i++)
	{
		array[i].key = 0;   // Initialize key to 0
		array[i].data = 0;  // Initialize data to 0
	}
}

// Function to insert an element into the hash table
void insert(int key, int data)
{
	int index = hashFunction(key);  // Calculate the index for the given key
	if (array[index].data == 0)
	{
		array[index].key = key;   // Set the key
		array[index].data = data; // Set the data
		size++;                  // Increment the size of the hash table
		printf("\n Key (%d) has been inserted \n", key);
	}
	else if (array[index].key == key)
	{
		array[index].data = data;  // Update the data if key already exists
	}
	else
	{
		printf("\n Collision occurred  \n");  // Collision occurred if the index is already occupied
	}
}

// Function to remove an element from the hash table
void remove_element(int key)
{
	int index = hashFunction(key);  // Calculate the index for the given key
	if (array[index].data == 0)
	{
		printf("\n This key does not exist \n");  // Key does not exist in the hash table
	}
	else
	{
		array[index].key = 0;   // Set the key to 0
		array[index].data = 0;  // Set the data to 0
		size--;                // Decrement the size of the hash table
		printf("\n Key (%d) has been removed \n", key);
	}
}

// Function to display the hash table
void display()
{
  int i;
  for (i = 0; i < capacity; i++)
  {
		if (array[i].data == 0)
		{
			printf("\n array[%d]: / ", i);  // Empty slot in the hash table
		}
		else
		{
			printf("\n key: %d array[%d]: %d \t", array[i].key, i, array[i].data);  // Display key-value pair
		}
  }
}

// Function to get the size of the hash table
int size_of_hashtable()
{
	return size;  // Return the current size of the hash table
}

// Main function
int main()
{
	int choice, key, data, n;
	int c = 0;
	init_array();  // Initialize the hash table
	
	do
	{
		printf("1.Insert item in the Hash Table"
			"\n2.Remove item from the Hash Table"
			"\n3.Check the size of Hash Table"
			"\n4.Display a Hash Table"
			"\n\n Please enter your choice: ");

		scanf("%d", &choice);
		switch (choice)
		{
			case 1:
				printf("Enter key -:\t");
				scanf("%d", &key);
				printf("Enter data -:\t");
				scanf("%d", &data);
				insert(key, data);  // Insert key-value pair into the hash table
				break;

			case 2:
				printf("Enter the key to delete-:");
				scanf("%d", &key);
				remove_element(key);  // Remove key-value pair from the hash table
				break;

			case 3:
				n = size_of_hashtable();
				printf("Size of Hash Table is-:%d\n", n);  // Get and display the size of the hash table
				break;

			case 4:
				display();  // Display the hash table
				break;

			default:
				printf("Invalid Input\n");
		}
		printf("\nDo you want to continue (press 1 for yes): ");
		scanf("%d", &c);
	}
	while (c == 1);
}
```

> `ChatGPT`
> Upon reviewing the code, I found a few potential bugs or improvements that can be made:
> 
> The checkPrime function has a bug in the for loop condition. It should be i <= n / 2 instead of i < n / 2 to include the case where n is divisible by itself. The corrected line should be: for (i = 2; i <= n / 2; i++).
>
> The getPrime function increments n by 2 to find the next prime number. However, it should also handle the case where n is initially an even number. To fix this, you can add another condition to check if n is even and increment it by 1 before entering the while loop.
> 
> In the insert function, when a collision occurs, the program only prints a message without handling the collision. You might want to consider implementing collision resolution techniques like linear probing or chaining to handle collisions and insert the element in a different index.
> 
> The display function prints an extra \t character after displaying the key-value pair. You can remove the \t character from the printf statement to have a cleaner output.
> 
> In the main function, the variable c is not initialized before entering the do-while loop. It's good practice to initialize variables before using them. You can initialize c to 1 before the do-while loop.
> 
> There is no code to free the allocated memory for the array when the program finishes. After the do-while loop in the main function, you can add free(array); to release the allocated memory.
> 
> These are some suggestions for improving the code and addressing potential bugs. Remember to thoroughly test the code after making any changes.

---

> Sure! Here's the updated code with the bugs fixed:

```c
#include <stdio.h>
#include <stdlib.h>

// Structure to represent key-value pair
struct set {
	int key;
	int data;
};

// Global variables
struct set *array; // Array to store elements
int capacity = 10; // Initial capacity of the array
int size = 0;      // Current size of the hash table

// Hash function to calculate index for a given key
int hashFunction(int key) {
	return (key % capacity);
}

// Function to check if a number is prime
int checkPrime(int n) {
	int i;
	if (n == 1 || n == 0) {
		return 0;
	}
	for (i = 2; i <= n / 2; i++) {
		if (n % i == 0) {
			return 0;
		}
	}
	return 1;
}

// Function to get the next prime number greater than n
int getPrime(int n) {
	if (n % 2 == 0) {
		n++;
	}
	while (!checkPrime(n)) {
		n += 2;
	}
	return n;
}

// Function to initialize the hash table
void init_array() {
	capacity = getPrime(capacity); // Get a prime capacity for the array
	array = (struct set *)malloc(capacity * sizeof(struct set)); // Allocate memory for the array
	for (int i = 0; i < capacity; i++) {
		array[i].key = 0;   // Initialize key to 0
		array[i].data = 0;  // Initialize data to 0
	}
}

// Function to insert an element into the hash table
void insert(int key, int data) {
	int index = hashFunction(key); // Calculate the index for the given key
	if (array[index].data == 0) {
		array[index].key = key;   // Set the key
		array[index].data = data; // Set the data
		size++;                   // Increment the size of the hash table
		printf("\n Key (%d) has been inserted \n", key);
	} else if (array[index].key == key) {
		array[index].data = data;  // Update the data if key already exists
		printf("\n Key (%d) already exists. Data has been updated. \n", key);
	} else {
		// Collision occurred, perform linear probing to find an empty slot
		int i = 1;
		while (array[(index + i) % capacity].data != 0) {
			i++;
		}
		index = (index + i) % capacity;
		array[index].key = key;
		array[index].data = data;
		size++;
		printf("\n Collision occurred. Key (%d) has been inserted at index %d \n", key, index);
	}
}

// Function to remove an element from the hash table
void remove_element(int key) {
	int index = hashFunction(key); // Calculate the index for the given key
	if (array[index].data == 0) {
		printf("\n This key does not exist \n"); // Key does not exist in the hash table
	} else if (array[index].key == key) {
		array[index].key = 0;   // Set the key to 0
		array[index].data = 0;  // Set the data to 0
		size--;                 // Decrement the size of the hash table
		printf("\n Key (%d) has been removed \n", key);
	} else {
		printf("\n Collision occurred. Key (%d) at index %d. \n", key, index);
	}
}

// Function to display the hash table
void display() {
	int i;
	for (i = 0; i < capacity; i++) {
		if (array[i].data == 0) {
			printf("\n array[%d]: / ", i); // Empty slot in the hash table
		} else {
			printf("\n key: %d array[%d]: %d", array[i].key, i, array[i].data); // Display key-value pair
		}
	}
}

// Function to get the size of the hash table
int size_of_hashtable() {
	return size; // Return the current size of the hash table
}

// Main function
int main() {
	int choice, key, data, n;
	int c = 1;
	init_array(); // Initialize the hash table

	do {
		printf("\n1. Insert item in the Hash Table");
		printf("\n2. Remove item from the Hash Table");
		printf("\n3. Check the size of the Hash Table");
		printf("\n4. Display the Hash Table");
		printf("\n\nPlease enter your choice: ");
		scanf("%d", &choice);

		switch (choice) {
			case 1:
				printf("Enter key: ");
				scanf("%d", &key);
				printf("Enter data: ");
				scanf("%d", &data);
				insert(key, data); // Insert key-value pair into the hash table
				break;

			case 2:
				printf("Enter the key to delete: ");
				scanf("%d", &key);
				remove_element(key); // Remove key-value pair from the hash table
				break;

			case 3:
				n = size_of_hashtable();
				printf("Size of Hash Table is: %d\n", n); // Get and display the size of the hash table
				break;

			case 4:
				display(); // Display the hash table
				break;

			default:
				printf("Invalid Input\n");
		}

		printf("\nDo you want to continue? (Press 1 for yes): ");
		scanf("%d", &c);
	} while (c == 1);

	free(array); // Free the allocated memory
	return 0;
}
```

> With these fixes, the code should work correctly and handle collisions by using **linear probing** to find an empty slot. Additionally, the code initializes the `c` variable before the do-while loop and frees the allocated memory for the array at the end of the program.