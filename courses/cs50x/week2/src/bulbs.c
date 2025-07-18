#include <cs50.h>
#include <stdio.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // user input
    string txt = get_string("Message: ");

    // loop through each character
    for (int i = 0; txt[i] != '\0'; i++)
    {
        // Transform decimal into bits
        int decimal = txt[i];
        for (int pos = BITS_IN_BYTE - 1; pos >= 0; pos--)
        {
            char bit = (decimal >> pos) & 1;  // extract each bit
            print_bulb(bit);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
