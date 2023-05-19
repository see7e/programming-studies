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
