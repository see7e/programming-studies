package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const defaultAlmanac = `seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4`

// starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.
// list of maps which describe how to convert numbers from a source category into numbers in a destination category.
// seed-to-soil map (the seed is the source, the soil is the destination)
// 50(SOIL-destination range start) 98(SEED-source range start) 2(RANGE length:: 98 and 99)
// Any source numbers that aren't mapped correspond to the same destination number.
//So, seed number 10 corresponds to soil number 10.

/*seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51 */

// we need to find the location number. In this example, the corresponding types are:
// Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
// Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
// Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
// Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
// So, the lowest location number in this example is 35.

type seed struct {
	seed        int
	soil        int
	fertilizer  int
	water       int
	light       int
	temperature int
	humidity    int
	location    int
}

// getInput reads the input file based on the part.
func getInput(path string) string {
	if path != "" {
		content, err := os.ReadFile(path)
		if err != nil {
			panic(err)
		}
		return string(content)
	} else {
		return defaultAlmanac
	}
}

func seeds(almanac string) []int {
	// return the list of seeds in the firt line of the input
	seeds := strings.Split(almanac, "\n")[0]

	// remove the "seeds: " prefix
	seeds = strings.TrimPrefix(seeds, "seeds: ")

	// Split the string into individual numbers
	seedsSlice := strings.Fields(seeds)

	// Convert the string numbers to integers and store them in an array
	var numbersArray []int
	for _, numStr := range seedsSlice {
		num, err := strconv.Atoi(numStr)
		if err != nil {
			fmt.Println("Error converting string to integer:", err)
			return nil
		}
		numbersArray = append(numbersArray, num)
	}

	return numbersArray
}

// Seed to Soil:

// Soil to Fertilizer:
// Fertilizer to Water:
// Water to Light:
// Light to Temperature:
// Temperature to Humidity:
// Humidity to Location:


func main() {
	// Usage
	almanac := getInput("")
}