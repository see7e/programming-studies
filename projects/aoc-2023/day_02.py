# DAY 02
# Read the line and check if the Game is valid (
    # if any of the dices rolled were more than 12 red cubes, 13 green cubes, and 14 blue cubes
    ## if yes save the number of the game
    ## if not continue
#)

# DICE LIMITS
RED = 12
GREEN = 13
BLUE = 14

def get_calibration() -> str:
    # 1, 2, 5 (8)
    return "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n\
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n\
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n\
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n\
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"


def get_input() -> str:
    return open('./src/input_day_02.txt', 'r').read()


def get_sum(source, part: int = 1) -> int:
    total_sum = 0
    multiplier = 0
    input = source.splitlines()

    for game in input:
        rolls = game.split(':')[1].split(';')
        game_number = int(game.split(':')[0].split('Game ')[1])
        # print(rolls)

        # Check if the game is valid
        red = 0
        green = 0
        blue = 0

        for roll in rolls:
            # print(roll)

            for dice in roll.split(','):
                # print(dice)

                dice_value = int(dice.strip().split(' ')[0])
                # print(dice_value)

                if 'red' in dice:
                    red = dice_value * (dice_value > red) + (dice_value <= red) * red
                if 'green' in dice:
                    green = dice_value * (dice_value > green) + (dice_value <= green) * green
                if 'blue' in dice:
                    blue = dice_value * (dice_value > blue) + (dice_value <= blue) * blue

        # print(f"Game({game_number})>> red::",red, "green::",green, "blue::",blue)

        #########################################
        # PART 02
        # We need to multiply the number of the maximum RGB dices rolled in each game
        multiplier += red * green * blue
        #########################################

        # if any of the dices rolled were more than the limit it's an invalid game
        if red <= RED and green <= GREEN and blue <= BLUE:
            # print(f"Game({game_number}) is valid")
            total_sum += game_number 

    return (part == 1)*total_sum + (part == 2)*multiplier

if __name__ == "__main__":
    # print(get_sum(get_calibration())) # calibration
    # print(get_sum(get_input())) # part 01
    # print(get_sum(get_calibration(), part=2)) # part 02 
    print(get_sum(get_input(), part=2)) # part 02 