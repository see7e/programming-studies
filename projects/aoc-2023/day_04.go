package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
)

// Card struct represents the data for each card
type Card struct {
	Number          string
	WinningNumbers  []int
	Numbers         []int
	Score           int
}

// Calibration deck
const calibInput = `
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
`

// innerJoin returns common elements between a and b.
func innerJoin(a []int, b []int) (c []int) {
	for _, i := range a {
		for _, j := range b {
			if i == j {
				c = append(c, i)
			}
		}
	}
	return
}

// contains checks if a number is in an array.
func contains(arr []int, num int) bool {
	for _, val := range arr {
		if val == num {
			return true
		}
	}
	return false
}

// cardAsNumber converts the card struct to a unique number.
func cardAsNumber(c Card) int {
	// You can use a unique calculation based on the card details to generate a number
	// For simplicity, let's use a hash-like approach here
	return len(c.WinningNumbers)*1000 + len(c.Numbers)*100 + c.Score*10
}

// getInput reads the input file based on the part.
func getInput(part int) string {
	if part != 0 {
		content, err := os.ReadFile("./src/input_day_04.txt")
		if err != nil {
			log.Fatal(err)
		}
		return string(content)
	}
	// Example scratchcards for calibration
	return calibInput
}

// parseInput converts the input string into a slice of cards.
func parseInput(input string) []Card {
	var cards []Card
	lines := strings.Split(input, "\n")

	for _, line := range lines {
		if len(line) == 0 {
			continue
		}

		// Extracting card details
		parts := strings.Split(line, ": ")
		card := Card{Score: 1, Number: parts[0]}

		// Parsing winning numbers
		winningNumbers := strings.Fields(parts[1][:strings.Index(parts[1], "|")])
		for _, numStr := range winningNumbers {
			num, err := strconv.Atoi(numStr)
			if err != nil {
				log.Fatal(err)
			}
			card.WinningNumbers = append(card.WinningNumbers, num)
		}

		// Parsing player's numbers
		playerNumbers := strings.Fields(parts[1][strings.Index(parts[1], "|")+1:])
		for _, numStr := range playerNumbers {
			num, err := strconv.Atoi(numStr)
			if err != nil {
				log.Fatal(err)
			}
			card.Numbers = append(card.Numbers, num)
		}

		cards = append(cards, card)
	}

	return cards
}

// getScore calculates the score based on the scratchcards, based on the puzzle part.
func getScore(cards []Card, part int) int {
	totalScore := 0

	if part == 1 {
		for _, card := range cards {
			score := 0
			for _, number := range card.Numbers {
				if contains(card.WinningNumbers, number) {
					if score == 0 {
						score = 1
					} else {
						score *= 2
					}
				}
			}
			card.Score = score
			totalScore += score
		}
	} else { // part == 2
		for index, card := range cards {
			common := innerJoin(card.WinningNumbers, card.Numbers)
			commonLen := len(common)

			
			for countFound := index + commonLen; countFound > index; countFound-- {
				cards[countFound].Score += cards[index].Score
			}

			totalScore += cards[index].Score
		}
	}
	
	return totalScore
}

func main() {
	// Part 1
	// Calibrate
	startTime := time.Now()

	calibInput := getInput(0)
	calibCards := parseInput(calibInput)
	calibScore := getScore(calibCards, 1)

	calibRuntime := time.Since(startTime)
	fmt.Printf("Calibrate Score: %d\n", calibScore)
	fmt.Printf("Calibrate Runtime: %.7f seconds\n", calibRuntime.Seconds())

	// Official
	startTime = time.Now()
	
	officialInput := getInput(1)
	officialCards := parseInput(officialInput)
	officialScore := getScore(officialCards, 1)

	officialRuntime := time.Since(startTime)
	fmt.Printf("Official Score: %d\n", officialScore)
	fmt.Printf("Official Runtime: %.7f seconds\n", officialRuntime.Seconds())

	// Part 2
	// Calibrate
	startTime_2 := time.Now()

	calibInput_2 := getInput(0)
	calibCards_2 := parseInput(calibInput_2)
	calibScore_2 := getScore(calibCards_2, 2)
	
	calibRuntime_2 := time.Since(startTime_2)
	fmt.Printf("Calibrate Score: %d\n", calibScore_2)
	fmt.Printf("Calibrate Runtime: %.7f seconds\n", calibRuntime_2.Seconds())

	// Official
	startTime_2 = time.Now()

	officialInput_2 := getInput(2)
	officialCards_2 := parseInput(officialInput_2)
	officialScore_2 := getScore(officialCards_2, 2)
	
	officialRuntime_2 := time.Since(startTime_2)
	fmt.Printf("Official Score: %d\n", officialScore_2)
	fmt.Printf("Official Runtime: %.7f seconds\n", officialRuntime_2.Seconds())
}

