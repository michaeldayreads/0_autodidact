package main

import (
	"errors"
	"fmt"
)

func sim(i int) (int, error) {
	if i < 10 {
		return -1, errors.New("Not yet...")
	} else {
		return 42, nil
	}
}

func main() {
	i := 0
	var j int
	for {
		j, err := sim(i)
		if err != nil {
			fmt.Println("Unable to use current value of i:", i, err)
			i++
			continue
		} else {
			fmt.Println(j)
			break
		}
	}
	fmt.Println(j)
}
