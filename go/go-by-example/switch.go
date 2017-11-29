package main

import (
	. "fmt"
	. "time"
)

func main() {

	i := 2
	Print("Write ", i, " as ")
	switch i {
	case 1:
		Println("one")
	case 2:
		Println("two")
	case 3:
		Println("three")
	}

	switch Now().Weekday() {
	case Saturday, Sunday:
		Println("It's the weekend")
	default:
		Println("It's a weekday")
	}

	t := Now()
	switch { // no expression is an alterante form of if/else
	case t.Hour() < 12:
		Println("It's before noon")
	default:
		Println("It's after noon")
	}

	// a type switch
	// NOTE: all types implement the empty interface
	// this is an introduction to delayed type checking
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			Println("bool")
		case int:
			Println("int")
		default:
			Printf("Unknown type %T\n", t)
		}
	}
	whatAmI(true)
	whatAmI(1)
	whatAmI("hey")
}
