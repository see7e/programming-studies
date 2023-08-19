// Optimized implementation of Bubble sort
#include <stdbool.h>
#include <stdio.h>

// Function prototypes
void swap(int* xp, int* yp);
void bubbleSort(int arr[], int n);
void printArray(int arr[], int size);

// Driver program to test above functions
int main()
{
    int arr[] = { 64, 34, 25, 12, 22, 11, 90 };  // Sample array

    int n = sizeof(arr) / sizeof(arr[0]);  // Calculate the size of the array
    bubbleSort(arr, n);  // Call the bubbleSort function to sort the array
    printf("Sorted array: \n");
    printArray(arr, n);  // Print the sorted array
    return 0;
}

void swap(int* xp, int* yp)
{
    int temp = *xp;  // Temporary variable to store the value of *xp
    
    *xp = *yp;  // Assign the value of *yp to *xp
    *yp = temp;  // Assign the value of temp to *yp
}
 
// An optimized version of Bubble Sort
void bubbleSort(int arr[], int n)
{
    int i, j;
    bool swapped;

    for (i = 0; i < n - 1; i++) {  // Iterate over the array from the beginning
        swapped = false;  // Initialize swapped flag as false
        for (j = 0; j < n - i - 1; j++) {  // Iterate over the unsorted part of the array
            if (arr[j] > arr[j + 1]) {  // If current element is greater than the next element
                swap(&arr[j], &arr[j + 1]);  // Swap the elements using the swap function
                swapped = true;  // Set swapped flag to true
            }
        }
 
        // If no two elements were swapped by inner loop, then break
        if (swapped == false)  // If no swaps occurred in the inner loop, the array is already sorted
            break;  // Break out of the outer loop
    }
}
 
// Function to print an array
void printArray(int arr[], int size)
{
    int i;

    for (i = 0; i < size; i++)  // Iterate over the array
        printf("%d ", arr[i]);  // Print each element
}