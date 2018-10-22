package main

import "fmt"

// Spec: The scope of an identifier denoting a const, type, var or func (but not method!) declared
//   at the top level is the *package block*.
var AnywhereInThePackage string

func main() {
	// Spec: The scope of a constant or variable identifier declared inside a function begins at the end
	//   of the ConstSpec/VarSpec/ShortVarDecl and ends at the end of the *innermost* containing block.
	var AnywhereInMain string

	for i := 0; i < 1; i++ {
		var OnlyInThisBlock string
		AnywhereInThePackage = "foo"
		AnywhereInMain = "bar"
		OnlyInThisBlock = "qux"

		fmt.Println(AnywhereInThePackage, AnywhereInMain)
		fmt.Println(OnlyInThisBlock)
	}

	fmt.Println(AnywhereInThePackage, AnywhereInMain)
	// fmt.Println(OnlyInThisBlock) // Undefined

	// See channelScope.go to use channels to pass values out of a loop contained within a goroutine.
}
