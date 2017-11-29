package main

import . "fmt"

func main() {

	if 7%2 == 0 {
		Println("7 is even")
	} else {
		Println("7 is odd")
	}

	if 8%4 == 0 {
		Println("8 is divisible by 4")
	}

	if num := 9; num < 0 {
		Println(num, "is negative")
	} else if num < 10 {
		Println(num, "has 1 digit")
	} else {
		Println(num, "has multiple digits")
	}
}
