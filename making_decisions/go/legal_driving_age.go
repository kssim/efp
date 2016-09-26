/*
 * Pratice 16. Legal driving age
 * Output:
 *   What is your age? 13
 *   You are not old enough to legally drive.
 *   Or
 *   What is your age? 25
 *   You are old enough to legally drive.
 * Standard:
 *   20 years old.
 * Constraint:
 *   - Use a single output statement.
 *   - Use a ternary operator to write this program.
 *     If your language doesn't support a ternary operator,
 *     use a regular 'if/else' statement, and still use a single output
 *     statement to display the message.
 */

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("What is your age?  ")
	age_str, _ := reader.ReadString('\n')

	age, _ := strconv.Atoi(strings.TrimSpace(age_str))

	var print_str string
	if age >= 20 {
		print_str = "You are old enough to legally drive"
	} else {
		print_str = "You are not old enough to legally drive"
	}

	fmt.Println(print_str)
}
