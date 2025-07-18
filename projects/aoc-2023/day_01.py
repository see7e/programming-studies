# PART 01
# Read each line from api link
# Check the numbers inside of the line
## if there's only one number, repeat it and parse it to int
## if there's more then two numbers, use the first and the last digit and parse it to int
# Sum all the numbers of the list

# import requests

def get_calibration(part: int = 1) -> str:
    if part == 1:
        # 12, 38, 15, 77
        # produces 142
        return "1abc2\n\
                pqr3stu8vwx\n\
                a1b2c3d4e5f\n\
                treb7uchet"
    elif part == 2:
        # 29, 83, 13, 24, 42, 14, 76
        # produces 281
        return "two1nine\n\
                eightwothree\n\
                abcone2threexyz\n\
                xtwone3four\n\
                4nineeightseven2\n\
                zoneight234\n\
                7pqrstsixteen"

def get_input(part: int = 1) -> str:
    # Tried to get the input automatically from the website, but they dont have a public api
    # input = requests.get('https://adventofcode.com/2023/day/1/input')
    # return input.text
    if part == 1:
        return open('./src/input_day_01.txt', 'r').read()
    elif part == 2:
        return open('./src/input_day_01_02.txt', 'r').read()
    else:
        raise ValueError("Invalid part number")


# Only for Part 02
# Define a dict to store the words and their corresponding digits
WORD_TO_DIGIT = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
# Try to parse the numbers to int in the line, and add to the list
# Try to locate one of the words in the line
## if found, replace the word with the digit and store in the list
## if not found, continue
# Return the list of numbers (only the first and the last one) to be summed in the get_sum function

def parse_written_number(input: str) -> int:
    # Initialize a list to store parsed numbers
    parsed_numbers = []

    # Iterate through each line
    for line in input:
        # Initialize variables to store the current parsed number and actual numbers in the line
        current_number = ""
        numbers_in_line = []

        # Iterate through each character in the line
        for char in line:
            # Try parsing the current char to int
            try:
                temp = int(char) # this is just to provoke the ValueError
                numbers_in_line.append(char)
                current_number = ""
            except ValueError:
                # If the current char is not a number, build the current string letter by letter
                # Update only if the char is alphabetic
                current_number += char if char.isalpha() else ""
                # print("#",current_number)

                # Check if the current string matches any in the WORD_TO_DIGIT
                for key in WORD_TO_DIGIT.keys():
                    if key in current_number:
                        # print(current_number)
                        # Replace the current string with the corresponding digit
                        numbers_in_line.append(WORD_TO_DIGIT[key])
                        current_number = char
                        # current_number = ""

        # Check if numbers_in_line is not empty before trying to access its elements
        if numbers_in_line:
            # print(numbers_in_line)
            # Extract and join the first and last numbers in each line
            parsed_numbers.append(int(numbers_in_line[0] + numbers_in_line[-1]))
    #     print(numbers_in_line)
    # print(parsed_numbers)
    return parsed_numbers


def get_sum(source, part: int = 1) -> int:
    total_sum = 0
    input = source.splitlines()
    # input = get_input().splitlines()

    if part == 1:

        for line in input:
            # Extracting numbers from the line
            numbers = [num for num in line if num.isdigit()]

            # Processing the extracted numbers
            if len(numbers) == 1:
                total_sum += int(numbers[0] + numbers[0])
            elif len(numbers) == 2:
                total_sum += int(numbers[0] + numbers[1])
            elif len(numbers) > 2:
                total_sum += int(numbers[0] + numbers[-1])
    elif part == 2:

        # Call the function to parse the written numbers and sum the result
        total_sum = sum(parse_written_number(input))

    return total_sum

if __name__ == "__main__":
    # PART 01
    # print(get_sum(get_calibration())) # Calibration test
    # print(get_sum(get_input())) # Oficial input

    # PART 02
    # print(get_sum(get_calibration(2), part=2)) # Calibration test
    print(get_sum(get_input(2), part=2)) # Oficial input