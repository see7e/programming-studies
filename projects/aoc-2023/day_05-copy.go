package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

type Map struct {
	DestinationStart int
	SourceStart      int
	RangeLength      int
}

type Category struct {
	Maps   []Map
	Source int
}

type Almanac struct {
	Seeds      []int
	Categories map[string][]Category
}

const defaultAlmanac = `seeds:1,2,3,4,5
seed-to-soil map:
0 0 10
10 5 10
soil-to-fertilizer map:
0 0 10
10 5 10
fertilizer-to-water map:
0 0 10
10 5 10
water-to-light map:
0 0 10
10 5 10
light-to-temperature map:
0 0 10
10 5 10
temperature-to-humidity map:
0 0 10
10 5 10
humidity-to-location map:
0 0 10
10 5 10
`

func findLowestLocation(almanac *Almanac) int {
	var wg sync.WaitGroup
	var mu sync.Mutex
	lowestLocation := -1

	for _, seed := range almanac.Seeds {
		currentLocation := seed

		for _, categories := range almanac.Categories {
			for _, category := range categories {
				wg.Add(1)

				go func(category Category) {
					defer wg.Done()

					for _, m := range category.Maps {
						mu.Lock()
						if currentLocation >= m.DestinationStart && currentLocation < m.DestinationStart+m.RangeLength {
							currentLocation = m.SourceStart + (currentLocation-m.DestinationStart)%m.RangeLength
							break
						}
						mu.Unlock()
					}
				}(category)
			}
		}
	}

	wg.Wait()

	return lowestLocation
}

func loadAlmanac(input string) *Almanac {
	almanac := &Almanac{}
	lines := strings.Split(input, "\n")

	// Parse seed-to-soil map
	for _, line := range lines[7:13] {
		values := strings.Split(line, " ")
		category := Category{
			Maps:   append([]Map{}, Map{DestinationStart: parseInt(values[0]), SourceStart: parseInt(values[1]), RangeLength: parseInt(values[2])}),
			Source: 0,
		}
		almanac.Categories["seed-to-soil"] = append(almanac.Categories["seed-to-soil"], category)
	}

	// Parse soil-to-fertilizer map
	for _, line := range lines[14:20] {
		values := strings.Split(line, " ")
		category := Category{
			Maps:   append([]Map{}, Map{DestinationStart: parseInt(values[0]), SourceStart: parseInt(values[1]), RangeLength: parseInt(values[2])}),
			Source: 1,
		}
		almanac.Categories["soil-to-fertilizer"] = append(almanac.Categories["soil-to-fertilizer"], category)
	}

	// Parse fertilizer-to-water map
	for _, line := range lines[21:27] {
		values := strings.Split(line, " ")
		category := Category{
			Maps:   append([]Map{}, Map{DestinationStart: parseInt(values[0]), SourceStart: parseInt(values[1]), RangeLength: parseInt(values[2])}),
			Source: 2,
		}
		almanac.Categories["fertilizer-to-water"] = append(almanac.Categories["fertilizer-to-water"], category)
	}

	// Parse water-to-light map
	for _, line := range lines[28:34] {
		values := strings.Split(line, " ")
		category := Category{
			Maps:   append([]Map{}, Map{DestinationStart: parseInt(values[0]), SourceStart: parseInt(values[1]), RangeLength: parseInt(values[2])}),
			Source: 3,
		}
		almanac.Categories["water-to-light"] = append(almanac.Categories["water-to-light"], category)
	}

	// Parse light-to-temperature map
	for _, line := range lines[35:41] {
		values := strings.Split(line, " ")
		category := Category{
			Maps:   append([]Map{}, Map{DestinationStart: parseInt(values[0]), SourceStart: parseInt(values[1]), RangeLength: parseInt(values[2])}),
			Source: 4,
		}
		almanac.Categories["light-to-temperature"] = append(almanac.Categories["light-to-temperature"], category)
	}

	// Parse temperature-to-humidity map
	for _, line := range lines[42:48] {
		values := strings.Split(line, " ")
		category := Category{
			Maps:   append([]Map{}, Map{DestinationStart: parseInt(values[0]), SourceStart: parseInt(values[1]), RangeLength: parseInt(values[2])}),
			Source: 5,
		}
		almanac.Categories["temperature-to-humidity"] = append(almanac.Categories["temperature-to-humidity"], category)
	}

	// Parse humidity-to-location map
	for _, line := range lines[49:55] {
		values := strings.Split(line, " ")
		category := Category{
			Maps:   append([]Map{}, Map{DestinationStart: parseInt(values[0]), SourceStart: parseInt(values[1]), RangeLength: parseInt(values[2])}),
			Source: 6,
		}
		almanac.Categories["humidity-to-location"] = append(almanac.Categories["humidity-to-location"], category)
	}


	return almanac
}

func parseInt(str string) int {
	result, err := strconv.Atoi(str)
	if err != nil {
		panic(fmt.Sprintf("Cannot parse string to integer: %s", str))
	}
	return result
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

func main() {
	// Read almanac input from file or use default
	path := "" // Set the path to your input file or leave it empty to use defaultAlmanac
	input := getInput(path)

	// Load almanac
	almanac := loadAlmanac(input)

	// Find lowest location
	lowestLocation := findLowestLocation(almanac)

	// Print lowest location
	fmt.Println(lowestLocation)
}
