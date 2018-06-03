package main

// Stacking Defers

import "fmt"

func main() {
	fmt.Println("counting")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}

	fmt.Println("done.")
}

// Defer

// import "fmt"

// func main() {
// 	defer fmt.Println("world.")

// 	fmt.Print("Hello ")
// }

// Switch without a condition.

// import (
// 	"fmt"
// 	"time"
// )

// func main() {
// 	t := time.Now()
// 	msg := ""
// 	switch {
// 	case t.Hour() < 12:
// 		msg = "...mornin'..."
// 	case t.Hour() < 17:
// 		msg = "Afternoon."
// 	default:
// 		msg = "Evn'n!"
// 	}
// 	fmt.Println(msg)
// }

// Switch Evaluation Order

// import (
// 	"fmt"
// 	"time"
// )

// func main() {
// 	fmt.Println("When's Saturday?")
// 	today := time.Now().Weekday()
// 	switch time.Saturday {
// 	case today + 0:
// 		fmt.Println("Today. :D")
// 	case today + 1:
// 		fmt.Println("Tomorrow. :)")
// 	case today + 2:
// 		fmt.Println("In two days. : /")
// 	default:
// 		fmt.Println("Far, far away. :(")
// 	}
// }

// switch

// import (
// 	"fmt"
// 	"runtime"
// )

// func main() {
// 	fmt.Print("Go runs on ")
// 	switch os := runtime.GOOS; os {
// 	case "darwin":
// 		fmt.Println("OS X.")
// 	case "linux":
// 		fmt.Println("Linux.")
// 	default:
// 		fmt.Printf("%s.\n", os)
// 	}
// }

// import "fmt"

// func sqrt(x float64) float64 {
// 	i := 0
// 	z := 1.0
// 	for i < 10 {
// 		if z*z == x {
// 			fmt.Println("Precise.")
// 			fmt.Printf("i: %v\n", i)
// 			return z
// 		}
// 		fmt.Println(z)
// 		z -= (z*z - x) / (2 * z)
// 		i++
// 	}
// 	fmt.Printf("i: %v\n", i)
// 	return z
// }

// func main() {
// 	fmt.Println(sqrt(256))
// }

// If and else

// import (
// 	"fmt"
// 	"math"
// )

// func pow(x, n, lim float64) float64 {
// 	if v := math.Pow(x, n); v < lim {
// 		return v
// 	} else {
// 		fmt.Printf("%g >= %g\n", v, lim)
// 	}
// 	return lim
// }

// func main() {
// 	fmt.Println(
// 		pow(3, 2, 10),
// 		pow(3, 3, 20),
// 	)
// }

// Short if

// import (
// 	"fmt"
// 	"math"
// )

// func pow(x, n, lim float64) float64 {
// 	if v := math.Pow(x, n); v < lim {
// 		return v
// 	}
// 	return lim
// }

// func main() {
// 	fmt.Println(
// 		pow(3, 2, 10),
// 		pow(3, 3, 20),
// 	)
// }

// If

// import (
// 	"fmt"
// 	"math"
// )

// func sqrt(x float64) string {
// 	if x < 0 {
// 		return sqrt(-x) + "i"
// 	}
// 	return fmt.Sprint(math.Sqrt(x))
// }

// func main() {
// 	fmt.Println(sqrt(2), sqrt(-4))
// }

// While type for loop

// import "fmt"

// func main() {
// 	sum := 1
// 	for sum < 1000 {
// 		sum += sum
// 	}
// 	fmt.Println(sum)
// }

// for Continued

// import "fmt"

// func main() {
// 	sum := 1
// 	i := 0
// 	for sum < 1000 {
// 		sum += sum
// 		i++
// 	}
// 	fmt.Println(sum)
// 	fmt.Printf("Loop runs: %d\n", i)
// }

// For

// import "fmt"

// func main() {
// 	sum := 0
// 	for i := 0; i < 10; i++ {
// 		sum += 1
// 	}
// 	fmt.Println(sum)
// }
