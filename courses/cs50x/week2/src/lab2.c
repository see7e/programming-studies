#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

// Function prototype
int compute_score(string word);

// Main function
int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int i = 0;
    int score = 0;

    while (word[i] != '\0')
    {
        // uppercase lettrs
        if (word[i] >= 65 && word[i] <= 90)
        {
            score += POINTS[word[i] - 65];
            //printf("%i\n", score);
        }
        //lowercase lettrs
        else if (word[i] >= 97 && word[i] <= 122)
        {
            score += POINTS[word[i] - 97];
            //printf("%i\n", score);
        }
        i++;
    }
    return score;
}
