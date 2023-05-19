# Max-Heap data structure in Python

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # Calculate the left child index
    r = 2 * i + 2  # Calculate the right child index

    if l < n and arr[largest] < arr[l]:  # Compare left child with the current largest
        largest = l

    if r < n and arr[largest] < arr[r]:  # Compare right child with the current largest
        largest = r

    if largest != i:  # If the largest is not the current node, swap and recursively heapify
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)  # If the array is empty, simply append the new element
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)  # Heapify the array from the bottom up

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]  # Swap the element to be deleted with the last element

    array.remove(num)  # Remove the element from the array
    size -= 1  # Decrement the size of the array

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)  # Heapify the array after deletion

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
