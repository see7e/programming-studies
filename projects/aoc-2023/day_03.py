# DAY 03

# Map the X and Y coordinates of the symbols
SYMBOLS = ['*', '@', '=', '%', '+', '$', '&', '/', '-', '#']

# Define the possible directions (left, right, up, down, diagonals)
## (x-1, y-1) (x, y-1) (x+1, y-1)
## (x-1, y)   (x, y)   (x+1, y)
## (x-1, y+1) (x, y+1) (x+1, y+1)

LEFT, RIGHT = (-1, 0), (1, 0)
UP, DOWN = (0, -1), (0, 1)
UP_LEFT, UP_RIGHT = (-1, -1), (1, -1)
DOWN_LEFT, DOWN_RIGHT = (-1, 1), (1, 1)
DIRECTIONS = [LEFT, RIGHT, UP, DOWN, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]

CALIB_MAP = "\
467..114..\n\
...*......\n\
..35..633.\n\
......#...\n\
617*......\n\
.....+.58.\n\
..592.....\n\
......755.\n\
...$.*....\n\
.664.598.."


def get_input(part: int) -> str:
    if part:
        return open('./src/input_day_03.txt', 'r').read()
    else:
        return CALIB_MAP


def check_symbol_positions(map) -> list:
    symbol_coords = []
    y = 0
    for line in map.splitlines():
        y += 1
        x = 0

        for point in line:
            if not point == '.' and not point.isnumeric():
                symbol_coords.append((x+1, y))
            x += 1
    return symbol_coords


# For Part 2: gears
import pandas as pd

# Must find the numbers that are connected to a gear ('*')
# Then use the function to complete the number (check_adjacent)
# Then multiply the numbers, adding the multiplication to a list
# Finaly sum all the numbers
def find_gears(map) -> list:
    gears = []
    y = 0
    for line in map.splitlines():
        y += 1
        x = 0
        for point in line:
            x += 1
            # Check if point is a gear
            gears.append((x, y)) if point == '*' else None
    return gears


def check_adjacent(line:str, point: str, x: int, y: int, used_points: list) -> int:
    # The point received is already valid and a number
    # Lookup on the left and right for the rest of the number, the numbers can have up to 3 digits,
    # so we need to check 2 points on each side:
    ## if the number was used by a previous iteration, stop
    ## if hits a symbol or a dot ('.'), stop
    ## if hits a number, continue
    # Join the digits in order (left to right) and return the number
    
    # print(f'Checking adjacent points for {point} at ({x}, {y})')
    x_left = x
    left_number = ''
    while x_left > 0:
        x_left -= 1

        left_point = line[x_left-1] # because the line starts with x=1
        if (x_left, y) in used_points:
            return 0
        if left_point.isnumeric():
            left_number = left_point + left_number
            # print(f'Left number: {left_number}')
        else:
            break

    # print(f'Left number: {left_number}')
    final_number = left_number + point
    # print(f'temp final number: {final_number}')

    x_right = x
    right_number = ''
    while x_right < len(line):
        x_right += 1

        right_point = line[x_right-1]
        if (x_right, y) in used_points:
            return 0
        if right_point.isnumeric():
            right_number = right_number + right_point
            # print(f'Right number: {right_number}')
        else:
            break

    # print(f'Right number: {right_number}')
    final_number = final_number + right_number
    # print(f'Final number: {final_number}')

    return int(final_number) * (final_number.isnumeric()) + 0


def check_numbers(map, part: int = 1):
    used_points, valid_numbers = [], []
    if part == 2:
        gears_df = pd.DataFrame(columns=['gear', 'number1', 'number2'])
        gears = find_gears(map)
    else:
        symbol_coords = check_symbol_positions(map)

    y = 0
    for line in map.splitlines():
        y += 1
        x = 0

        for point in line:
            x += 1
            # print((x,y))
            
            # Check if point is a number
            if point.isnumeric():

                # Check if point is valid on each direction for symbol presence
                for dx, dy in DIRECTIONS:
                    if part == 1 and (x + dx, y + dy) in symbol_coords:
                        used_points.append((x, y))
                        number = check_adjacent(line, point, x, y, used_points)
                        valid_numbers.append(number) if number else None
                    if part == 2 and (x + dx, y + dy) in gears:
                        used_points.append((x, y))
                        number = check_adjacent(line, point, x, y, used_points)
                        if number == 0:
                            continue

                        # Check if the DataFrame is not empty before accessing its values
                        if not gears_df.empty and (x + dx, y + dy) in gears_df['gear'].values.tolist():
                            gears_df.loc[gears_df['gear'] == (x + dx, y + dy), 'number2'] = number
                        else:
                            gears_df = pd.concat([gears_df, pd.DataFrame({'gear': [(x + dx, y + dy)], 'number1': [number]})], ignore_index=True)
                        # print(gears_df.to_string())

    return valid_numbers if part == 1 else gears_df


def calculate_gear_ratio(df):
    # check if the gear has 2 numbers
    # if not, return 0
    # if yes, multiply the numbers and return the list of results
    gear_ratios = []

    for _, row in df.iterrows():
        # Check if the gear has two numbers
        if pd.notna(row['number1']) and pd.notna(row['number2']):
            # Calculate the gear ratio and append it to the list
            gear_ratios.append(row['number1'] * row['number2'])

    return gear_ratios


if __name__ == '__main__':
    # # Part 1
    # # Calibration
    # calibration_output = check_numbers(CALIB_MAP)
    # print(f'Calibration output: {calibration_output, sum(calibration_output)}')
    # # Oficial
    # # part_1_output = check_numbers(get_input(1))
    # # print(f'Part 1 output: {part_1_output, sum(part_1_output)}')

    # Part 2
    # Calibration
    # calibration_output = check_numbers(CALIB_MAP, 2)
    # print(f'Calibration output: {calibration_output}:: {sum(calculate_gear_ratio(calibration_output))}')
    # Oficial
    part_2_output = check_numbers(get_input(1), 2)
    print(f'Part 2 output: {sum(calculate_gear_ratio(part_2_output))}')


