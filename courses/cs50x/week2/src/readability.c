#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

// Main function
int main(void)
{
    // Prompt Text:
    string text = get_string("Text: ");

    // Count the number of upper and lowecases
    int i = 0;
    int letters = 0;
    int words = 1;
    int sentences = 0;

    while (text[i] != '\0')
    {
        // uppercase or lowercase lettrs
        if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122))
        {
            letters++;
        }
        // spaces between words
        else if (text[i] == 32)
        {
            words++;
        }
        // sentences (. ! ?)
        else if (text[i] == 46 || text[i] == 33 || text[i] == 63)
        {
            sentences++;
        }
        i++;
    }

    // Grade function
    //printf("letters %i\n", letters);
    //printf("words %i\n", words);
    //printf("sentences %i\n", sentences);

    // Caulculate the floating points
    float L = ((float)letters / (float)words) * 100;
    float S = ((float)sentences / (float)words) * 100;
    float subindex = 0.0588 * L - 0.296 * S - 15.8;

    int index = round(subindex);

    if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}