package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	fmt.Println("A random number is", rand.Intn(10))
	fmt.Println("\nAnd my favorite number is the empty set :P")
}

func init() {
	rand.Seed(time.Now().UTC().UnixNano())
	fmt.Println("\nSeeding...")
}
