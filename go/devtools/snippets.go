package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fmt.Println("Paused for research; Type findings to have them included in log and press enter to continue:")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
}
