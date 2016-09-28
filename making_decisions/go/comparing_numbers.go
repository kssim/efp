/*
 * Pratice 22. Comparing numbers
 * Output:
 *   Enter the first number: 1
 *   Enter the second number: 51
 *   Enter the third number: 2
 *   The largest number is 51.
 * Constraint:
 *   - Write the algorithm manually.
 *     Don't use a built-in function for finding the largest number in a list.
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
	fmt.Println("Enter the first number: ")
	number_one_str, _ := reader.ReadString('\n')
	fmt.Println("Enter the second number: ")
	number_second_str, _ := reader.ReadString('\n')
	fmt.Println("Enter the third number: ")
	number_third_str, _ := reader.ReadString('\n')

	number_one, _ := strconv.Atoi(strings.TrimSpace(number_one_str))
	number_two, _ := strconv.Atoi(strings.TrimSpace(number_second_str))
	number_three, _ := strconv.Atoi(strings.TrimSpace(number_third_str))

	if number_one == number_two || number_one == number_three || number_two == number_three {
		fmt.Println("You input the same number.")
		return
	}

	var largest_number int
	if number_one > number_two {
		largest_number = number_one
	} else {
		largest_number = number_two
	}

	if largest_number < number_three {
		largest_number = number_three
	}

	fmt.Printf("The largest number is %d.\n", largest_number)
}
