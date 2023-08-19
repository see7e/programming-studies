# Hash Table Implementation in Python

hashTable = [[] for _ in range(10)]  # Create a list of 10 empty lists to represent the hash table

def checkPrime(n):
	if n == 1 or n == 0:  # Check if n is 1 or 0, which are not prime numbers
		return False

	for i in range(2, n//2 + 1):  # Iterate from 2 to n//2 + 1 to check if n is divisible by any number
		if n % i == 0:  # If n is divisible by i, it is not a prime number
			return False

	return True  # If n is not divisible by any number, it is a prime number

def getPrime(n):
	if n % 2 == 0:  # If n is even, increment it by 1 to start with an odd number
		n = n + 1

	while not checkPrime(n):  # Keep incrementing n by 2 until a prime number is found
		n += 2

	return n  # Return the prime number

def hashFunction(key):
	capacity = getPrime(10)  # Get the prime number for hash table capacity (here, 10)
	return key % capacity  # Return the hash value for the given key

def insertData(key, data):
	index = hashFunction(key)  # Get the index in the hash table for insertion
	hashTable[index] = [key, data]  # Store the key-value pair at the computed index

def removeData(key):
	index = hashFunction(key)  # Get the index in the hash table for removal
	del hashTable[index]  # Remove the element at the computed index

insertData(123, "apple")  # Insert key-value pair into the hash table
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)  # Print the hash table

removeData(123)  # Remove a key-value pair from the hash table

print(hashTable)  # Print the updated hash table
