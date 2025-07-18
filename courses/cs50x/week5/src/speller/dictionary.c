// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <strings.h>    // strcasecmp()
#include <string.h>    // strcpy()
#include <stdio.h>      // FILE | scanf() | EOF
#include <stdlib.h>     // malloc()

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Get the hash value for the word
    unsigned int index = hash(word);

    // Traverse the linked list at the hash index
    node *cursor = table[index];
    while (cursor != NULL)
    {
        // Compare the word with the current node's word
        if (strcasecmp(word, cursor->word) == 0)
        {
            // Word found in the dictionary
            return true;
        }

        // Move to the next node
        cursor = cursor->next;
    }

    // Word not found in the dictionary
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash
    // Initialize the hash value
    unsigned int hash_value = 0;

    // Calculate the hash value by considering the first three characters
    for (int i = 0; i < 3 && word[i] != '\0'; i++)
    {
        hash_value = (hash_value * 26) + (toupper(word[i]) - 'A');
    }

    // Return the hash value within the range of the hash table size
    // return toupper(word[0]) - 'A';
    return hash_value % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO

    // Open the dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Clear the hash table
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // Buffer to store each word read from the file
    char buffer[LENGTH + 1];

    // Read words from the file until the end is reached
    while (fscanf(file, "%s", buffer) != EOF)
    {
        // Create a new node for the word
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(file);
            return false;
        }

        // Copy the word into the node
        strcpy(new_node->word, buffer);

        // Calculate the hash value
        unsigned int index = hash(new_node->word);

        // Insert the node at the beginning of the linked list at the hash index
        new_node->next = table[index];
        table[index] = new_node;
    }

    // Close the dictionary file
    fclose(file);

    // Dictionary loaded successfully
    return true;
    //return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO

    // Initialize the word count
    unsigned int count = 0;

    // Traverse the hash table
    for (int i = 0; i < N; i++)
    {
        // Traverse the linked list at the current index
        node *cursor = table[i];
        while (cursor != NULL)
        {
            // Move to the next node
            cursor = cursor->next;

            // Increment the word count
            count++;
        }
    }

    // Return the word count
    return count;
    //return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO

    // Traverse the hash table
    for (int i = 0; i < N; i++)
    {
        // Traverse the linked list at the current index
        node *cursor = table[i];
        while (cursor != NULL)
        {
            // Keep track of the next node
            node *temp = cursor->next;

            // Free the current node
            free(cursor);

            // Move to the next node
            cursor = temp;
        }
    }

    // Dictionary unloaded successfully
    return true;
    //return false;
}
