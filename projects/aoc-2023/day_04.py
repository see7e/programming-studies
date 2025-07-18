# DAY 04
import pandas as pd
import time

CALIB_DECK = "\
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n\
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n\
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n\
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n\
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n\
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

# PART 1
## winning numbers | numbers that you have
## lookup the numbers that you have in the winning numbers
## count the numbers found in each card
## for each card found multiply the score by two
### (1 found = 1 point, 2 found = 2 points, 3 found = 8 points)
## sum the scores of each card

# PART 2
## we now only care about the count of the numbers found in each card
## for each card with numbers found, we add the count, plus the card iteself
## if a card has two numbers found, we add 1 (the card) + 2 (the count) = 3



def get_input(part: int = None) -> str:
    if part:
        return open('./src/input_day_04.txt', 'r').read()
    else:
        return CALIB_DECK
    

def parse_input(input: str) -> pd.DataFrame:
    data = []
    cards = input.splitlines()

    for card in cards:
        card = card.split(':')

        card_number = card[0].split('Card ')[1].strip()
        winning_numbers = [int(x) for x in card[1].split('|')[0].strip().split() if x.isdigit()]
        numbers = [int(x) for x in card[1].split('|')[1].strip().split() if x.isdigit()]

        data.append({
            'card': card_number,
            'winning_numbers': winning_numbers,
            'numbers': numbers,
        })
        
        # print(f"Card {card_number} - {winning_numbers} - {numbers}")

    df = pd.DataFrame(data)
    return df


def get_score(df: pd.DataFrame) -> int:
    df['score'] = 0

    for index, row in df.iterrows():
        # print(index)

        score = 0
        winning_numbers = row['winning_numbers']
        numbers = row['numbers']
        # print(f"Card {row['card']} - {winning_numbers} - {numbers}")

        for number in numbers:
            if number in winning_numbers:
                score = 1 if score == 0 else score * 2
                # print(f"Card {row['card']} - {number} - {score}")
        df.loc[index, 'score'] = score
        # print("------")
    return df['score'].sum()


if __name__ == '__main__':
    # Part 1
    ## Calibrate    
    start_time = time.time()
    df_cards = parse_input(get_input())
    # print(df_cards.to_string(index='card'))
    print(f"Score: {get_score(df_cards)}")
    print("--- Part 1: Calibration:: %.7f seconds ---" % (time.time() - start_time))

    # Official
    start_time = time.time()
    df_cards = parse_input(get_input(1))
    print(f"Score: {get_score(df_cards)}")
    print("--- Part 1: Official:: %.7f seconds ---" % (time.time() - start_time))

    # # Part 2
    # ## Calibrate
    # df_cards = parse_input(get_input())
    # print(len(df_cards.index))
    # print(df_cards.to_string(index='card'))
