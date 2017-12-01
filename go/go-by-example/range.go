package main

import "fmt"

func main() {

	nums := []int{2, 3, 4}
	sum := 0

	// range over slice or array
	// we use the blank identifier as we do not use the index in this case
	for _, num := range nums {
		sum += num
	}

	fmt.Println("sum:", sum)

	// range over maps
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}

	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}

	for k := range kvs {
		fmt.Println("key:", k)
	}

	// i: starting byte index c: unicode *rune*
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}
