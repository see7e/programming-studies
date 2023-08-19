// Include the standard input/output library.
#include <stdio.h>

// Define the size of the queue.
#define SIZE 5

// Function prototypes for queue operations.
void enQueue(int);
void deQueue();
void display();

// Declare the queue as a global array and the front and rear indices.
int items[SIZE], front = -1, rear = -1;

// The main function.
int main() {
  // Try to deQueue from an empty queue.
  deQueue();

  // Enqueue 5 elements to the queue.
  enQueue(1);
  enQueue(2);
  enQueue(3);
  enQueue(4);
  enQueue(5);

  // Try to enqueue a 6th element, which won't be possible because the queue is full.
  enQueue(6);

  // Display the elements of the queue.
  display();

  // Dequeue the first element from the queue, which is 1.
  deQueue();

  // Display the updated elements of the queue.
  display();

  // Return 0 to indicate successful execution of the program.
  return 0;
}

// The enQueue function adds an element to the rear of the queue.
void enQueue(int value) {
  // Check if the queue is full.
  if (rear == SIZE - 1)
    printf("\nQueue is Full!!");
  else {
    // If the queue is empty, set the front index to 0.
    if (front == -1)
      front = 0;

    // Increment the rear index and add the new element to the queue.
    rear++;
    items[rear] = value;

    // Print a message indicating that the element was inserted.
    printf("\nInserted -> %d", value);
  }
}

// The deQueue function removes the first element from the front of the queue.
void deQueue() {
  // Check if the queue is empty.
  if (front == -1)
    printf("\nQueue is Empty!!");
  else {
    // Print the first element of the queue, which will be removed.
    printf("\nDeleted : %d", items[front]);

    // Increment the front index to remove the first element.
    front++;

    // If the queue is now empty, reset the front and rear indices to -1.
    if (front > rear)
      front = rear = -1;
  }
}

// The display function prints the elements of the queue.
void display() {
  // Check if the queue is empty.
  if (rear == -1)
    printf("\nQueue is Empty!!!");
  else {
    // Iterate through the elements of the queue and print them.
    int i;
    printf("\nQueue elements are:\n");
    for (i = front; i <= rear; i++)
      printf("%d  ", items[i]);
  }
  printf("\n");
}
