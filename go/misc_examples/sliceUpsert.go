package main

import "fmt"

func upsert(s string, slice []string) []string {
	for _, v := range slice {
		if v == s {
			return slice
		}
	}
	return append(slice, s)
}

func main() {
	endpoints := []string{"10.0.0.1", "10.0.0.2"}
	fmt.Println(endpoints)

	old := "10.0.0.2"
	new := "10.0.0.3"

	endpoints = upsert(old, endpoints)
	fmt.Println(endpoints)

	endpoints = upsert(new, endpoints)
	fmt.Println(endpoints)
}
