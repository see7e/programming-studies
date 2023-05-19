#include <stdio.h>

// Function to swap two elements
void swap(int *a, int *b) {
	int temp = *b;
	*b = *a;
	*a = temp;
}

// Function to heapify a subtree rooted at index i
void heapify(int array[], int size, int i) {
	int largest = i;
	int l = 2 * i + 1; // Calculate index of left child
	int r = 2 * i + 2; // Calculate index of right child

	// Check if left child is larger than the current largest element
	if (l < size && array[l] > array[largest])
		largest = l;

	// Check if right child is larger than the current largest element
	if (r < size && array[r] > array[largest])
		largest = r;

	// If the largest element is not the current root, swap them and recursively heapify the affected subtree
	if (largest != i) {
		swap(&array[i], &array[largest]);
		heapify(array, size, largest);
	}
}

// Function to insert a new element into the heap
void insert(int array[], int* size, int newNum) {
	if (*size == 10) {
		printf("Heap is full. Cannot insert element.\n");
		return;
	}

	int i = *size;
	array[i] = newNum;
	*size += 1;

	// Heapify the heap starting from the newly inserted element to maintain the Max-Heap property
	for (int j = i; j > 0; j = (j - 1) / 2) {
		int parent = (j - 1) / 2;
		if (array[j] > array[parent]) {
			swap(&array[j], &array[parent]);
		} else {
			break;
		}
	}
}

// Function to delete the root element of the heap
void deleteRoot(int array[], int* size) {
	if (*size == 0) {
		printf("Heap is empty. Cannot delete root.\n");
		return;
	}

	int root = array[0];
	array[0] = array[*size - 1];
	*size -= 1;

	// Heapify the heap starting from the root to restore the Max-Heap property
	heapify(array, *size, 0);

	printf("Deleted root element: %d\n", root);
}

// Function to print the elements of the heap array
void printArray(int array[], int size) {
	for (int i = 0; i < size; ++i)
		printf("%d ", array[i]);
	printf("\n");
}

int main() {
	int array[10];
	int size = 0;

	// Insert elements into the heap
	insert(array, &size, 3);
	insert(array, &size, 4);
	insert(array, &size, 9);
	insert(array, &size, 5);
	insert(array, &size, 2);

	printf("Max-Heap array: ");
	printArray(array, size);

	// Delete the root element of the heap
	deleteRoot(array, &size);

	printf("After deleting the root element: ");
	printArray(array, size);

	return 0;
}
