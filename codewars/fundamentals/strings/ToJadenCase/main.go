package main

// by: jakepy

import (
	"fmt"
	"strings"
)

func ToJadenCase(s string) string { // lol, I didn't know .Title existed, haha ​​anyway it's all about learning
	words := strings.Split(s, " ")
	finallyString := ""
	for i := 0; i < len(words); i++ {
		finallyString += strings.ToUpper(words[i][0:1]) + words[i][1:] + " "
	}
	return finallyString[0 : len(finallyString)-1] // remove the space finally
}

func main() {
	fmt.Println(ToJadenCase("All the rules in this world were made by someone no smarter than you. So make your own.") == "All The Rules In This World Were Made By Someone No Smarter Than You. So Make Your Own.")
}

// All The Rules In This World Were Made By Someone No Smarter Than You. So Make Your Own. -> ouput
// All The Rules In This World Were Made By Someone No Smarter Than You. So Make Your Own. -> Response codewars
