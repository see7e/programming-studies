/*
Set of userfull functions used in different projects

- innerJoin: returns common elements between a[] and b[].
- contains: checks if a number is in an array.
- getInput: reads the input file based on the part.
- strToIntArray: convert a string to an array of integers.
*/

package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// returns common elements between a[] and b[].
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

// checks if a number is in an array.
func contains(arr []int, num int) bool {
	for _, val := range arr {
		if val == num {
			return true
		}
	}
	return false
}

// getInput reads the input file based on the part.
func getInput(path string) string {
	if path != "" {
		content, err := os.ReadFile(path)
		if err != nil {
			panic(err)
		}
	return string(content)
	}
	return ""
}

// convert a string to an array of integers.
func strToIntArray(str string) []int {
	// Split the string into individual numbers
	seedsSlice := strings.Fields(str)

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
// A variation of the above function (i need to check the time complexity of both)
func parseLine(line string) []int {
	var numbers []int
	for _, word := range strings.Split(line, " ") {
		if number, err := strconv.Atoi(word); err == nil {
			numbers = append(numbers, number)
		}
	}
	return numbers
}


func main() {
	// Usage
}