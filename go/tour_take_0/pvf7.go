package main

import "fmt"

func nakedSplit(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return x, y
}

func main() {
	fmt.Println(nakedSplit(17))
	fmt.Println(split(17))
}
