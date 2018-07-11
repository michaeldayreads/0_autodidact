package main

import "fmt"

func mytype(v interface{}) string {
	return fmt.Sprintf("%T", v)
}

func main() {
	s := "A string"
	b := true
	i := 6
	f := 3.14

	fmt.Println(mytype(s))
	fmt.Println(mytype(b))
	fmt.Println(mytype(i))
	fmt.Println(mytype(f))
}
