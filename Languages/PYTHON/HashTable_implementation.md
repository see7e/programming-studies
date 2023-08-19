---
title: Python - Hash Table - Implementation
tags: studies, programação
use: Documentation
languages: Python
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Code File #](#code-file-)
- [Explanation](#explanation)
  - [Creating the Hash Table:](#creating-the-hash-table)
  - [Checking for Prime Numbers:](#checking-for-prime-numbers)
  - [Finding a Prime Number:](#finding-a-prime-number)
  - [Hashing Function:](#hashing-function)
  - [Inserting Data into the Hash Table:](#inserting-data-into-the-hash-table)
  - [Removing Data from the Hash Table:](#removing-data-from-the-hash-table)
  - [Putting Items in the Hash Table:](#putting-items-in-the-hash-table)
  - [Printing the Hash Table:](#printing-the-hash-table)
  - [Removing an Item from the Hash Table:](#removing-an-item-from-the-hash-table)
  - [Printing the Updated Hash Table:](#printing-the-updated-hash-table)
- [Found in Programiz](#found-in-programiz)

</details>

---

# Code File [#](hash_table.py)

There are a couple of issues with the [given code](#found-in-programiz):

-   Incorrect initialization of `hashTable`: The line `hashTable = [[],] * 10` creates a list with a single empty list object, and then replicates that object 10 times. As a result, modifying one element of the list will affect all other elements since they are references to the same object. To fix this, you can use a list comprehension to create separate empty lists: `hashTable = [[] for _ in range(10)]`.
    
-   Incorrect prime number checking: The `checkPrime()` function checks for prime numbers, but it has a bug in the range of the `for` loop. It should include the upper limit (`n//2 + 1`) instead of excluding it. The correct line should be: `for i in range(2, n//2 + 1):`
    
-   Inefficient prime number calculation: The `getPrime()` function is used to find a prime number for the hash table capacity. It starts with `n` and increments by 2 until a prime number is found. However, this method is inefficient for larger numbers. An alternative approach is to use a more efficient prime number generation algorithm like the Sieve of Eratosthenes.
    
-   Incorrect removal of data: The `removeData()` function sets the value at the computed index to 0, which is not a valid representation for an empty slot in the hash table. To remove an element, you should use the `del` statement or assign `None` to the element at the index. For example: `del hashTable[index]` or `hashTable[index] = None`.


# Explanation
> ChatGPT powered

##  Creating the Hash Table:

```python
hashTable = [[] for _ in range(10)]
```

We are creating something called a hash table. It's like a special box with compartments inside it. Here, we are making 10 compartments. We use empty lists to represent each compartment.

## Checking for Prime Numbers:

```python
def checkPrime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False

    return True
```

A prime number is a special number that is only divisible by 1 and itself. We need to check if a number is prime or not. We go through a loop from 2 to half of the number. If the number is divisible by any of those smaller numbers, then it's not prime. Otherwise, it is prime.

## Finding a Prime Number:

```python
def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n
```

We need to find a special prime number to determine the size of our hash table. We start with a number (let's say 10). If it's even, we add 1 to make it odd. Then, we keep increasing the number by 2 until we find a prime number.

## Hashing Function:

```python
def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity
```

A hashing function is like a magic formula that tells us in which compartment of the hash table an item should go. Here, we find a prime number (let's say 10) using the `getPrime()` function. Then, we use the magic formula `%` (which means "remainder") to find the compartment for our item. We take the item's number and divide it by the prime number (10), and we put the item in the compartment corresponding to the remainder.

## Inserting Data into the Hash Table:

```python
def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]
```

Now, we can put items into our hash table. We need a key (a number) and some data (anything you want to store). We use the `hashFunction()` to find the compartment where the item should go. Then, we put the item in that compartment.

## Removing Data from the Hash Table:

```python
def removeData(key):
    index = hashFunction(key)
    del hashTable[index]
```

Sometimes, we want to remove an item from the hash table. We use the `hashFunction()` again to find the compartment where the item is. Then, we take out the item from that compartment and remove it completely.

## Putting Items in the Hash Table:

```python
insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")
```

Let's put some items in our hash table. We have different fruits, and each fruit has a unique number. We call the `insertData()` function and give it the number of the fruit and the fruit's name. The function will find the right compartment and put the fruit there.

## Printing the Hash Table:

```python
print(hashTable)
```

Now, let's see what our hash table looks like. We print it out to see all the compartments and what's inside them.

## Removing an Item from the Hash Table:

```python
removeData(123)
```

Uh-oh! We made a mistake and put the wrong fruit in the hash table. We wanted to remove the fruit with the number 123. We call the `removeData()` function and give it the number of the fruit we want to remove. The function will find the compartment and take out the fruit completely.

## Printing the Updated Hash Table:

```python
print(hashTable)
```

Let's check our hash table again after removing the fruit. We print it out to see the updated compartments and what's inside them.

That's it! Now you understand how a hash table works and how to put items in it and remove them.

# Found in [Programiz](https://www.programiz.com/dsa/hash-table#python-code)

```python
# Python program to demonstrate working of HashTable 

hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1


def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)

removeData(123)

print(hashTable)
```