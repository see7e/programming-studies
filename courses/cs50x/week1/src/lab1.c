#include <stdio.io> // Including the standard input/output library
#include <cs50.io>  // Including the CS50 library for user input

int main(void) // Main function, which starts the program
{
    // Start population
    int start; // Declaring an integer variable called "start"

    start = 0; // Assigning the value of 0 to the "start" variable
    do // Starting a do-while loop
    {
        start = get_int("Start population size: "); // Prompting the user to enter the start population size and storing the input in the "start" variable
    }
    while (start < 9); // Loop will repeat as long as the start population is less than 9

    // Ending population
    int end; // Declaring an integer variable called "end"

    end = 0; // Assigning the value of 0 to the "end" variable
    do // Starting a do-while loop
    {
        end = get_int("End population size: "); // Prompting the user to enter the end population size and storing the input in the "end" variable
    }
    while (end < start); // Loop will repeat as long as the end population is less than the start population

    // Years to the goal
    int years; // Declaring an integer variable called "years"

    years = 0; // Assigning the value of 0 to the "years" variable
    while (start < end) // Starting a while loop, which will continue as long as the start population is less than the end population
    {
        start += (start / 3)-(start / 4);
        years++; // Incrementing the years variable by 1
    }
    printf("Years: %i\n", years); // Printing the final output, which displays the number of years it will take to reach the end population size
}
