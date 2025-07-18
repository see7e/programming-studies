#!/bin/bash

# Check if BUFFER_SIZE is defined in the header file (assuming it's ../get_next_line.h)
if grep -q "#define BUFFER_SIZE 42" ../get_next_line.h; then
    # Compile your C code without specifying BUFFER_SIZE
    gcc -Wall -Werror -Wextra ../get_next_line_bonus.c ../get_next_line_utils_bonus.c -o gnl_test
else
    # Compile your C code with the specified BUFFER_SIZE
    gcc -Wall -Werror -Wextra -D BUFFER_SIZE=42 ../get_next_line_bonus.c ../get_next_line_utils_bonus.c -o gnl_test
fi

# Check if compilation was successful
if [ $? -ne 0 ]; then
    echo "Compilation failed. Exiting."
    exit 1
fi

# Define the input file for testing
input_file="./testfile.txt"

# Create a test input file with sample content
echo "This is line 1." > "$input_file"
echo "This is line 2." >> "$input_file"
echo "This is line 3." >> "$input_file"
echo "This is line 4." >> "$input_file"
echo "This is line 5." >> "$input_file"

# Test 1: Read all lines from the input file
echo "Test 1: Reading all lines from the input file"
while IFS= read -r expected_line; do
    # Run your C program and capture its output
    output=$(./gnl_test < "$input_file")

    # Compare the output with the expected line
    if [ "$output" = "$expected_line" ]; then
        echo "Test passed: '$output' == '$expected_line'"
    else
        echo "Test failed: '$output' != '$expected_line'"
    fi
done < "$input_file"

# Test 2: Read from an empty file
echo "Test 2: Reading from an empty file"
empty_file="./emptyfile.txt"
touch "$empty_file"
output=$(./gnl_test < "$empty_file")
if [ -z "$output" ]; then
    echo "Test passed: Empty file returned empty result"
else
    echo "Test failed: Empty file did not return an empty result"
fi
rm "$empty_file"

# Test 3: Read from a file with very large lines
echo "Test 3: Reading from a file with large lines"
large_lines_file="./largelines.txt"
echo "A" > "$large_lines_file"
for i in {1..1000}; do
    echo -n "B" >> "$large_lines_file"
done
output=$(./gnl_test < "$large_lines_file")
expected_line="A$(printf 'B%.0s' {1..999})"
if [ "$output" = "$expected_line" ]; then
    echo "Test passed: Large lines were read correctly"
else
    echo "Test failed: Large lines were not read correctly"
fi
rm "$large_lines_file"

# Clean up by removing the test input file
rm "$input_file"

# Clean up by removing the compiled program
rm gnl_test

# Clean the output files
make fclean
