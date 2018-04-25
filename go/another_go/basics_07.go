package main

import "fmt"

func naked_return(sum int) (x, y int) {
    // this is a naked return
    x = sum * 4 / 9
    y = sum - x
    return
}

func optional_named_return(sum int) (x, y int) {
    // this is the same as above, but now we are 
    // optionally naming the return values
    x = sum * 4 / 9
    y = sum - x
    return x, y
}

func names_required(sum int) (int, int) {
    // in this instance, we have to declare
    // and explicitly return the values
    // failing to declare => `undefined <foo>`
    x := sum * 4 / 9
    y := sum - x
    // failing to return => `not enough arguments to return`
    return x, y
}

func main() {
    fmt.Println(naked_return(17))
    fmt.Println(optional_named_return(17))
    fmt.Println(names_required(17))
}
