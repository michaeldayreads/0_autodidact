// mutating maps

package main

import "fmt"

func main() {
	m := make(map[string]int)

	m["Answer"] = 42
	fmt.Printf("Value: %v\n", m["Answer"])

	m["Answer"] = 48
	fmt.Printf("Value: %v\n", m["Answer"])

	delete(m, "Answer")
	fmt.Printf("Value: %v\n", m["Answer"])

	v, ok := m["Answer"]
	fmt.Printf("Value: %v Present? %v\n", v, ok)
}
