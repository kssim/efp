/*
 * Pratice 2. Counting the Number of Characters
 * Output:
 *   What is the input string? kssim
 *   kssim has 5 characters.
 * Constraints:
 *   - Be sure the output contains the original string.
 *   - Use a single output statement to construct the output.
 *   - Use a built-in function of the programming language to
 *     determine the length of the string.
 */

package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Please input string.")
		return
	}

	var input_str = os.Args[1]

	var print_str string
	print_str = "What is the input string? "
	print_str += input_str
	print_str += "\n"
	print_str += input_str
	print_str += " has "
	print_str += strconv.Itoa(len(input_str))
	print_str += " characters."

	fmt.Println(print_str)
}
