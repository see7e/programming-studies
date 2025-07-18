#include <cs50.h> // Include CS50 library
#include <stdio.h> // Include standard input/output library

// PROTOTYPES
int get_cents(void); // Declare function prototype to get the amount of change owed
int calculate_quarters(int cents); // Declare function prototype to calculate number of quarters to give as change
int calculate_dimes(int cents); // Declare function prototype to calculate number of dimes to give as change
int calculate_nickels(int cents); // Declare function prototype to calculate number of nickels to give as change
int calculate_pennies(int cents); // Declare function prototype to calculate number of pennies to give as change

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents(); // Call get_cents function to get amount of change owed

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents); // Call calculate_quarters function to get number of quarters to give
    cents = cents - quarters * 25; // Subtract value of quarters given from total change owed

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents); // Call calculate_dimes function to get number of dimes to give
    cents = cents - dimes * 10; // Subtract value of dimes given from total change owed

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents); // Call calculate_nickels function to get number of nickels to give
    cents = cents - nickels * 5; // Subtract value of nickels given from total change owed

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents); // Call calculate_pennies function to get number of pennies to give
    cents = cents - pennies * 1; // Subtract value of pennies given from total change owed

    // Sum coins
    int coins = quarters + dimes + nickels + pennies; // Calculate total number of coins given

    // Print total number of coins to give the customer
    printf("%i\n", coins); // Output total number of coins given
}

int get_cents(void)
{
    // TODO
    int cents = 0; // Initialize cents variable to 0
    do
    {
        // Prompt the user for the amount of money
        cents = get_int("Change owed: "); // Get input from user for amount of change owed
    }
    while (cents < 0); // Keep prompting user until non-negative value is entered

    return cents; // Return the amount of change owed
}

// FILTERS
int calculate_quarters(int cents)
{
    // TODO
    int quarters = cents / 25; // Divide cents by 25 to get number of quarters to give
    return quarters; // Return number of quarters to give
}

int calculate_dimes(int cents)
{
    // TODO
    int dimes = cents / 10; // Divide cents by 10 to get number of dimes to give
    return dimes; // Return number of dimes to give
}

int calculate_nickels(int cents)
{
    // TODO
    int nickels = cents / 5; // Divide cents by 5 to get number of nickels to give
    return nickels; // Return number of nickels to give
}

int calculate_pennies(int cents)
{
    // TODO
    int pennies = cents / 1; // Divide cents by 1
    return pennies; // Return number of pennies to give
}
