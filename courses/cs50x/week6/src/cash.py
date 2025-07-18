# TODO
from cs50 import get_float


def get_cents():
    cents = 0
    while True:
        # Prompt the user for the amount of money
        dollars = get_float("Change owed: ")
        try:
            cents = int(dollars * 100)
            if cents >= 0:
                break
        except ValueError:
            continue
    return cents


def calculate_quarters(cents):
    quarters = cents // 25
    return quarters


def calculate_dimes(cents):
    dimes = cents // 10
    return dimes


def calculate_nickels(cents):
    nickels = cents // 5
    return nickels


def calculate_pennies(cents):
    pennies = cents // 1
    return pennies


def main():
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents -= quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents -= dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents -= nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents -= pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(coins)


if __name__ == "__main__":
    main()
