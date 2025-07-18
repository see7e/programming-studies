// Day 07: Cammel cards

/* your goal is to order them based on the strength of each hand. A hand consists
of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative
strength of each card follows this order, where A is the highest and 2 is the lowest


TYPES: Every hand is exactly one type. From strongest to weakest, they are:
- Five of a kind: AAAAA
- Four of a kind: AA8AA
- Full house: 23332
- Three of a kind: TTT98
- Two pair: 23432
- One pair: A23A4
- High card: 23456

ORDER: 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger
because its first card is stronger. Similarly, 77888 and 77788 are both a full
house, but 77888 is stronger because its third card is stronger (and both hands
have the same first and second card).

BID: Multiply the bid of the hand by its rank (order)
765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5 = 6440

*/

package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)


const defaultPlay = `32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483`

type Play struct {
	Hand string
	Bid int
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

/* Helper function */
func countChars(str string) map[rune]int {
	charCount := make(map[rune]int)

	for _, char := range str {
		charCount[char]++
	}
	// fmt.Println(str,charCount)
	return charCount
}

// ********************************************************* THIS IS ALMOST GOOD
// func getRank(plays []Play) []Play {
// 	sort.Slice(plays, func(i, j int) bool {
// 		// Calculate ranks dynamically based on hand characteristics
// 		rankI := calculateRank(countChars(plays[i].Hand))
// 		rankJ := calculateRank(countChars(plays[j].Hand))

// 		fmt.Println(plays[i].Hand, rankI)
// 		fmt.Println(plays[j].Hand, rankJ)
// 		// Compare ranks for sorting
// 		return rankI > rankJ
// 	})

// 	// Assign ranks based on the sorted order
// 	for i := range plays {
// 		plays[i].Rank = i + 1
// 	}

// 	return plays
// }

// func calculateRank(counts map[rune]int) int {
// 	// Power of each card (descending order)
// 	cardsPower := map[rune]int{
// 		'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8,
// 		'8': 7, '7': 6,'6': 5, '5': 4, '4': 3, '3': 2, '2': 1,
// 	}

// 	// Sort characters by power in descending order
// 	sortedChars := make([]rune, 0, len(counts))
// 	for char := range counts {
// 		sortedChars = append(sortedChars, char)
// 	}
// 	sort.Slice(sortedChars, func(i, j int) bool {
// 		return cardsPower[sortedChars[i]] > cardsPower[sortedChars[j]]
// 	})

// 	// Create a string representing the sorted hand
// 	sortedHand := ""
// 	for _, char := range sortedChars {
// 		sortedHand += strings.Repeat(string(char), counts[char])
// 	}

// 	// For simplicity, let's use the sum of character powers as a criteria
// 	sum := 0
// 	for _, char := range sortedHand {
// 		sum += cardsPower[char]
// 	}

// 	return sum
// }
// ********************************************************* THIS IS ALMOST GOOD
func getRank(plays []Play) []Play {
	sort.Slice(plays, func(i, j int) bool {
		// Calculate ranks dynamically based on hand characteristics
		rankI := calculateRank(countChars(plays[i].Hand))
		rankJ := calculateRank(countChars(plays[j].Hand))

		fmt.Println(plays[i].Hand, rankI)
		fmt.Println(plays[j].Hand, rankJ)

		// Compare ranks for sorting
		return rankI < rankJ
	})

	fmt.Println("--------------------")
	fmt.Println("1st sorted plays:", plays)
	fmt.Println("--------------------")

	// Assign ranks based on the sorted order
	for i := 0; i < len(plays); i++ {
		plays[i].Rank = i + 1
	}

	return plays
}

func calculateRank(counts map[rune]int) (hash int) {
	// Power of each card (descending order)
	cardsPower := map[rune]int{
		'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8,
		'8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1,
	}
	// fmt.Println(counts)

	// Sort characters by power in descending order
	// sortedChars := make([]rune, 0, len(counts))
	sortedChars := make([]int, 0, len(counts))
	set := handType(counts)
	for char, count := range counts {
		// sortedChars = append(sortedChars, char)
		charPower := cardsPower[char]
		// charValue := int(char)
		// fmt.Println("char:", char, "count:", count, "charPower:", charPower, "set:", set)
		sortedChars = append(sortedChars, charPower*count)
		// fmt.Println("sortedChars:", sortedChars)
	}
	// sort.Slice(sortedChars, func(i, j int) bool {
	// 	return sortedChars[i] > sortedChars[j]
	// })

	// sort.Slice(sortedChars, func(i, j int) bool {
	// 	return cardsPower[sortedChars[i]] > cardsPower[sortedChars[j]]
	// })
		
	// fmt.Println(sortedChars)
	
	// Sum the values of the cards
	for _, char := range sortedChars {
		hash += char * set
	}
	// fmt.Println("hash:", hash)

	// // Create a unique key for the combination of cards
	// key := ""
	// for _, char := range sortedChars {
	// 	key += string(char) + strconv.Itoa(counts[char])
	// }

	// // Hash the key using a simple hash function
	// hashValue := 0
	// for _, char := range key {
	// 	hashValue = (hashValue * 31) + int(char)
	// }
	return hash
}

func handType(rankCount map[rune]int) int {
	// fmt.Println(rankCount)
	// Determine the hand type and calculate its rank
	switch {
		// Five of a kind: AAAAA
		case len(rankCount) == 1:
			return 7
		// Four of a kind: AA8AA
		case len(rankCount) == 2 && contains(rankCount, 4):
			return 6
		// Full house: 23332
		case len(rankCount) == 2 && contains(rankCount, 3) && contains(rankCount, 2):
			return 5
		// Three of a kind: TTT98
		case len(rankCount) == 3 && contains(rankCount, 3):
			return 4
		// Two pair: 23432
		case len(rankCount) == 3 && contains(rankCount, 2):
			return 3
		// One pair: A23A4
		case len(rankCount) == 4 && contains(rankCount, 2):
			return 2
		// High card: 23456
		case len(rankCount) == 5:
			return 1
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

func main() {
	input := getInput("")
	plays := parseInput(input)
	plays = getRank(plays)
	// plays = resolveTie(plays)

	// Print the result
	for _, play := range plays {
		fmt.Printf("Hand: %s, Bid: %d, Rank: %d\n", play.Hand, play.Bid, play.Rank)
	}
}