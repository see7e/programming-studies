# TODO
from cs50 import get_int

def main():

    # Prompt the user for the height of the pyramid
    height = 0
    while True:
        height = get_int("Height: ")
        if height >= 1 and height <= 8:
            break

    # Loop through each row of the pyramid
    for i in range(1, height + 1):
        # Print spaces before the pyramid
        print(" " * (height - i), end="")
        # Print the left side of the pyramid
        print("#" * i, end="")
        # Print the gap between the sides
        print("  ", end="")
        # Print the right side of the pyramid
        print("#" * i)

# run main()
if __name__ == "__main__":
    main()