""" Holding down the button charges the boat
releasing the button allows the boat to move.
Boats move faster if their button was held longer,
but time spent holding the button counts against the total race time.

You can only hold the button at the start of the race, and boats don't move until the button is released.

Time:      7  15   30
Distance:  9  40  200

The first race lasts 7 milliseconds. The distance in this race is 9 millimeters.
The second race lasts 15 milliseconds. The distance in this race is 40 millimeters.
The third race lasts 30 milliseconds. The distance in this race is 200 millimeters.

The boat has a starting speed of zero millimeters per millisecond. For each
whole millisecond you spend at the beginning of the race holding down the button,
the boat's speed increases by one millimeter per millisecond.

To see how much margin of error you have, determine the number of ways you can
beat the record in each race; in this example, if you multiply these values
together, you get 288 (
    4 	:: the number of chances to win a race
    * 8
    * 9
)

velocity = distance / time
"""

import time
# Taking into consideration that there's only two lines, we need to relate the columns of the two rows
# and call the ways_to_win function to calculate the number of ways to win
def read_input(input_str: str):
    # split the input into lines
    lines = input_str.splitlines()
    times = lines[0].split('Time:')
    times = list(map(lambda x: int(x.strip()), times[1].split()))

    # The same with distances
    distances = lines[1].split('Distance:')
    distances = list(map(lambda x: int(x.strip()), distances[1].split()))

    # Return the dict with the related values of time and distance
    return dict(zip(times, distances))


# calculate the number of ways to beat the record
def ways_to_win(data: dict) -> int:
    total_ways = 1
    races = len(data)
    for race in range(races):
        success = 0
          
        # get the time and distance
        time = list(data.keys())[race]
        dist = list(data.values())[race]
        # print(f"Time: {time}, Distance: {dist}")

        for tries in range(1, time):
            passedtime = time - tries
            # print(passedtime, tries, dist, success)
            if (passedtime * tries) > dist:
                success += 1
        total_ways *= success
    return total_ways


if __name__ == "__main__":
    start = time.time()
    input_data = "Time:      7  15   30\nDistance:  9  40  200"

    # read the input
    data = read_input(input_data)
    
    # calculate the number of ways to win
    result = ways_to_win(data)
    print(result)
    # give the runtime with 7 decimals
    print(f"Runtime: {time.time() - start:.7f}")