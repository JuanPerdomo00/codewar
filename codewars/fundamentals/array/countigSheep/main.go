package main

import "fmt"

func main() {
	var sheep [10]bool
	sheep[0] = true
	sheep[1] = true
	sheep[2] = true
	sheep[3] = true
	sheep[4] = false
	sheep[5] = true
	sheep[6] = false
	sheep[7] = false
	sheep[8] = false
	sheep[9] = true

	counter := countsheep(sheep[:])

	fmt.Printf("sheep: %d\n", counter)
}

func countsheep(sheep []bool) int {
	counts := 0
	for i := 0; i < len(sheep); i++ {
		if sheep[i] {
			counts++
		}
	}
	return counts
}
