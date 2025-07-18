/* Holding down the button charges the boat
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
*/

package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

// getInput reads the input file based on the part.
func getInput(path string) string {
	if path != "" {
		content, err := os.ReadFile(path)
		if err != nil {
			panic(err)
		}
		return string(content)
	} else {
		return "Time:      7  15   30\nDistance:  9  40  200"
	}
}

func parseLine(line string) []int {
	var numbers []int
	for _, word := range strings.Fields(line) {
		if number, err := strconv.Atoi(word); err == nil {
			numbers = append(numbers, number)
		}
	}
	return numbers
}

func readInputOne(input string) (times []int, distances []int, err error) {
	lines := strings.Split(input, "\n")

	for _, line := range lines {
		if strings.Contains(line, "Time:") {
			times = append(times, parseLine(line)...)
		} else if strings.Contains(line, "Distance:") {
			distances = append(distances, parseLine(line)...)
		}
	}

	if len(times) != len(distances) {
		return nil, nil, fmt.Errorf("time and distance arrays are not the same length")
	}

	return times, distances, nil
}

/* For Part 2 we only need to read the data in a different form:
We need to join the numbers in each line into a single number.

Time:      7  15   30
Distance:  9  40  200

...now instead means this:

Time:      71530
Distance:  940200
*/

func readInputTwo(input string) (time []int, distance []int, err error) {
	for _, line := range strings.Split(input, "\n") {
		if strings.Contains(line, "Time:") {
			timesStr := strings.TrimPrefix(line, "Time:")
			timesStr = strings.ReplaceAll(timesStr, " ", "")
			time = parseLine(timesStr)
		} else if strings.Contains(line, "Distance:") {
			distancesStr := strings.TrimPrefix(line, "Distance:")
			distancesStr = strings.ReplaceAll(distancesStr, " ", "")
			distance = parseLine(distancesStr)
		}
	}

	return time, distance, nil
}

func calculateWins(time []int, distance []int) int {
    totalWays := 1
    races := len(time)

    for race := 0; race < races; race++ {
        success := 0

        // get the time and distance
        currentTime := time[race]
        currentDist := distance[race]
        fmt.Printf("Time: %d, Distance: %d\n", currentTime, currentDist)

        for tries := 1; tries <= currentTime; tries++ {
            passedTime := currentTime - tries
            // fmt.Println(passedTime, tries, currentDist, success)

			// tries also means velocity
			// time * velocity = distance
            if (passedTime * tries) > currentDist {
                success++
            }
        }

        totalWays *= success
    }

    return totalWays
}

func main(){
	// // Part 1
	// startTime := time.Now() // runtime

	// data := getInput("")
	// fmt.Println(data)

	// times, distances,_ := readInputOne(data)
	// fmt.Println(times, distances)
	
	// fmt.Println(calculateWins(times, distances))

	// calibRuntime := time.Since(startTime)
	// fmt.Printf("Calibrate Runtime: %.7f seconds\n", calibRuntime.Seconds())

	// startTime = time.Now() // runtime

	// data = getInput("./src/input_day_06.txt")
	// fmt.Println(data)

	// times, distances,_ = readInputOne(data)
	// fmt.Println(times, distances)
	
	// fmt.Println(calculateWins(times, distances))

	// part1Runtime := time.Since(startTime)
	// fmt.Printf("Part 1 Runtime: %.7f seconds\n", part1Runtime.Seconds())

	// Part 2
	startTime := time.Now() // runtime

	data := getInput("")
	// fmt.Println(data)

	times, distances,_ := readInputTwo(data)
	// fmt.Println(times, distances)

	fmt.Println(calculateWins(times, distances))
	
	calibRuntime := time.Since(startTime)
	fmt.Printf("Calibrate Runtime: %.7f seconds\n", calibRuntime.Seconds())

	
	startTime = time.Now() // runtime

	data = getInput("./src/input_day_06.txt")
	// fmt.Println(data)

	times, distances,_ = readInputTwo(data)
	// fmt.Println(times, distances)

	fmt.Println(calculateWins(times, distances))
	
	part2Runtime := time.Since(startTime)
	fmt.Printf("Part 2 Runtime: %.7f seconds\n", part2Runtime.Seconds())
}