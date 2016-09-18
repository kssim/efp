/*
 * Pratice 1. Saying Hello
 * Output:
 *   What is your name? Kssim
 *   Hello, Kssim, nice to meet you!
 * Constraint:
 *   - Keep the input, string concatenation, and output separate.
 */

package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Please input your name")
		return
	}

	var user_name = os.Args[1]

	var print_str string
	print_str = "What is your name? "
	print_str += user_name
	print_str += "\n"
	print_str += "Hello, "
	print_str += user_name
	print_str += ", nice to meet you!"

	fmt.Println(print_str)
}
