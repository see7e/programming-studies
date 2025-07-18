package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const ranks = "AKQJT98765432"

const defaultPlay = `32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483`

type Play struct {
	Hand string
	Bid  int
	Rank int
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
		return defaultPlay
	}
}

func parseInput(input string) []Play {
	var plays []Play
	for _, line := range strings.Split(input, "\n") {
		if line != "" {
			// Split line by space
			line := strings.Fields(line)

			hand := line[0]
			bid, err := strconv.Atoi(line[1])
			if err != nil {
				fmt.Println("Error converting string to integer:", err)
				return nil
			}

			play := Play{hand, bid, 0}
			plays = append(plays, play)
		}
	}
	return plays
}

// Define constants for hand types
const (
	HighCardRank int = iota
	OnePairRank
	TwoPairRank
	ThreeOfAKindRank
	FourOfAKindRank
	FullHouseRank
)

func getRank(plays []Play) []Play {
	sort.Slice(plays, func(i, j int) bool {
		// Compare ranks for sorting
		return calculateRank(plays[i]) < calculateRank(plays[j])
	})

	// Assign ranks based on the sorted order
	for i := 0; i < len(plays); i++ {
		plays[i].Rank = i + 1
		// // Check for ties and adjust ranks accordingly
		// if i > 0 && calculateRank(plays[i]) == calculateRank(plays[i-1]) {
		// 	plays[i].Rank = plays[i-1].Rank
		// }
	}

	return plays
}

func calculateRank(play Play) int {
	// Sort characters by their rank in descending order
	sortedChars := make([]rune, len(play.Hand))
	copy(sortedChars, []rune(play.Hand))
	sort.Slice(sortedChars, func(i, j int) bool {
		return strings.IndexRune(ranks, sortedChars[i]) > strings.IndexRune(ranks, sortedChars[j])
	})

	// Count the occurrences of each rank
	rankCount := make(map[rune]int)
	for _, char := range sortedChars {
		rankCount[char]++
	}
	// fmt.Println(play.Hand, rankCount)

	// Determine the hand type and calculate its rank
	switch {
	case len(rankCount) == 1:
		return 8 // FiveOfAKindRank
	case len(rankCount) == 2 && contains(rankCount, 4):
		return 7 // FourOfAKindRank
	case len(rankCount) == 2 && contains(rankCount, 3):
		return 5 //FullHouseRank
	case len(rankCount) == 2 && contains(rankCount, 2):
		return 4 // TwoPairRank
	case len(rankCount) == 3 && contains(rankCount, 3):
		return 3 // ThreeOfAKindRank
	case len(rankCount) == 4:
		return 2 // OnePairRank
	case len(rankCount) == 5:
		return 1 // HighCardRank
	}

	return 0 // Default case
}

func contains(m map[rune]int, target int) bool {
	for _, v := range m {
		if v == target {
			return true
		}
	}
	return false
}

// Resolve ties based on card ranks
func resolveTie(plays []Play) []Play {
	for i := 1; i < len(plays); i++ {
		// Check if tied with the previous play
		if plays[i].Rank == plays[i-1].Rank {
			// Compare the ranks of the cards
			for j := 0; j < len(plays[i].Hand); j++ {
				if plays[i].Hand[j] > plays[i-1].Hand[j] {
					plays[i].Rank = i
					break
				} else if plays[i].Hand[j] < plays[i-1].Hand[j] {
					plays[i].Rank = i + 1
					break
				}
			}
		}
	}
	return plays
}


func main() {
	input := getInput("")
	plays := parseInput(input)

	// Check for ties and resolve them
	plays = getRank(plays)
	// plays = resolveTie(plays)

	// Print the result
	for _, play := range plays {
		fmt.Printf("Hand: %s, Bid: %d, Rank: %d\n", play.Hand, play.Bid, play.Rank)
	}
}

// func main() {
// 	input := getInput("")
// 	plays := parseInput(input)
// 	plays = getRank(plays)

// 	// Print the result
// 	for _, play := range plays {
// 		fmt.Printf("Hand: %s, Bid: %d, Rank: %d\n", play.Hand, play.Bid, play.Rank)
// 	}
// }