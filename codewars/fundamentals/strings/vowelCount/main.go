package main

import (
	"fmt"
	"strings"
)

func main() {
	var str string = "abracadabra"
	var str2 string = "holacomoestasmellamojuan"
	var ok int = GetCount(str)
	var ok2 int = GetCount(str2)
	fmt.Printf("\nThe voices of:%v are:%d\n", str, ok)
	fmt.Printf("\nThe voices of:%v are:%d\n", str2, ok2)
}

func GetCount(str string) (count int) {
	voice := "aeiou"
	for _, char := range str {
		if strings.ContainsRune(voice, char) {
			count++
		}

	}
	return count
}
