// Include the standard input/output library
#include <stdio.h>
// Include the CS50 library for getting input from the user
#include <cs50.h>

// Define the main function
int main(void)
{
    // Initialize a variable called "height" to 0
    int height = 0;

    // Loop until the user inputs a valid height value between 1 and 8
    do
    {
        // Prompt the user for the height of the pyramid
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Initialize a variable called "i" to 1
    int i = 1;
    // Loop through each row of the pyramid until "i" is greater than "height"
    while (i <= height)
    {
        // Initialize a variable called "j" to "height - i"
        int j = height - i;
        // Loop through each column of the row and print spaces until "j" is greater than 0
        while (j > 0)
        {
            printf(" ");
            j--;
        }

        // Initialize a variable called "k" to 1
        int k = 1;
        // Loop through each column of the row and print the "#" character until "k" is greater than "i"
        while (k <= i)
        {
            // If "k" is equal to "i", print two "#" characters with a space in between
            if (k == i)
            {
                printf("#  ");
            }
            // Otherwise, print only one "#" character
            else
            {
                printf("#");
            }
            k++;
        }

        // Initialize a variable called "l" to "i"
        int l = i;
        // Loop through each column of the row and print "#" characters until "l" is greater than 0
        while (l > 0)
        {
            printf("#");
            l--;
        }

        // Move to the next line
        printf("\n");
        // Increment "i" by 1
        i++;
    }

    // End the program and return 0
    return (0);
}
