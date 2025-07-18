/* FIRST CODE EDITED ***/

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // TODO

    // variables
    int buffer = 0;
    int length = strlen(input);


    //  stopping condition
    if (length == 0)
    {
        return buffer;
    }

    // calculus
    if (input[length - 1] >= '0' && input[length - 1] <= '9')
    {
        buffer = input[length - 1] - '0';   // relative number using ASCII
    }
    input[length - 1] = '\0';   // remove each element at the current iteration

    // hook
    return buffer + 10 * convert(input);
}

//*/

/* CODE PASSED THROUGH CHAT ***
*
In this optimized version, we pass the length of the string as a separate argument to the convert
function, avoiding the need to calculate the length repeatedly inside the function. Additionally, we
avoid unnecessary calculations by removing the need to check for ASCII values. The function now
directly subtracts '0' from the last character of the string to obtain the corresponding digit.
*
Please note that recursive solutions may not always be the most efficient approach, especially for 
large inputs, as they can lead to stack overflow errors. Consider using iterative methods or other
algorithms if you're working with significantly large numbers.*

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input, int length);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input, strlen(input)));
}

int convert(string input, int length)
{
    // Base case: Empty string
    if (length == 0)
    {
        return 0;
    }

    // Recursive case
    int lastDigit = input[length - 1] - '0';
    input[length - 1] = '\0';   // Remove the last character

    int converted = convert(input, length - 1);

    // Calculate the result
    return (converted * 10) + lastDigit;
}

*/