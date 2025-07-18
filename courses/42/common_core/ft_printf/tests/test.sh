#!/bin/bash

# Define the Makefile target (e.g., "all" or "re")
MAKE_TARGET="all"

# Compile the code using the Makefile with specific flags and without relinking
PROGRAM="./a.out" make CC=cc CFLAGS="-Wall -Wextra -Werror" LDLIBS="-lftprintf" $MAKE_TARGET

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful."
else
    echo "Compilation failed. Exiting."
    exit 1
fi

# Define test cases for the Mandatory part
MANDATORY_CASES=(
    "$PROGRAM 'Character: %c' A"
    "$PROGRAM 'String: %s' 'Hello, World!'"
    "$PROGRAM 'Pointer: %p' '0x1234567890'"
    "$PROGRAM 'Integer: %d' 42"
    "$PROGRAM 'Unsigned Integer: %u' 42"
    "$PROGRAM 'Hexadecimal (lowercase): %x' 255"
    "$PROGRAM 'Hexadecimal (uppercase): %X' 255"
    "$PROGRAM 'This is a literal %% character.'"
)

# Define test cases for the Bonus part (uncomment these lines to use them)
# BONUS_CASES=(
#     "$PROGRAM 'Character: %c' A"
#     "$PROGRAM 'String: %s' 'Hello, World!'"
#     "$PROGRAM 'Pointer: %p' '0x1234567890'"
#     "$PROGRAM 'Integer (width and zero-padding): %05d' 42"
#     "$PROGRAM 'Integer (left-justified): %-10d' 42"
#     "$PROGRAM 'Unsigned Integer: %u' 42"
#     "$PROGRAM 'Hexadecimal (lowercase): %#x' 255"
#     "$PROGRAM 'Hexadecimal (uppercase): %#X' 255"
#     "$PROGRAM 'Positive Integer with +: %+d' 42"
#     "$PROGRAM 'Positive Integer with space: % d' 42"
#     "$PROGRAM 'This is a literal %% character.'"
# )

# Run the test cases for the Mandatory part
for test_case in "${MANDATORY_CASES[@]}"; do
    echo
    echo "----------------------"
    echo "Running test for Mandatory part: $test_case"
    echo "----------------------"
    result=$(eval $test_case)
    echo "Test result: $result"
    echo
done

# Run the test cases for the Bonus part (uncomment to use)
# for test_case in "${BONUS_CASES[@]}"; do
#     echo
#     echo "----------------------"
#     echo "Running test for Bonus part: $test_case"
#     echo "----------------------"
#     result=$(eval $test_case)
#     echo "Test result: $result"
#     echo
# done

# Clean up
make fclean
