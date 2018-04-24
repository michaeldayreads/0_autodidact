package main

import "fmt"

func main() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)

	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)

	var a1 [2]int
	b := [3]string{"It", "Seems", "Funky"}
	var c [2]string
	c[0] = "It's"
	c[1] = "not!"

	fmt.Println(a1)
	fmt.Println(b)
	fmt.Println(c)
}
