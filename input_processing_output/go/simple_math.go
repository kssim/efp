/*
 * Pratice 5. Simple Math
 * Output:
 *   What is the first number? 20
 *   What is the second number? 5
 *   20 + 5 = 25
 *   20 - 5 = 15
 *   20 * 5 = 100
 *   20 / 5 = 4
 * Constraint:
 *   - Values coming from users will be strings. Ensure that you
 *     convert these values to numbers before doing the math.
 *   - Keep the inputs and outputs separate from the numerical
 *     conversions and other processing.
 *   - Generate a single output statement with line breaks in the
 *     appropriate spots.
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
	fmt.Println("What is the first number? ")
	first_num_str, _ := reader.ReadString('\n')
	fmt.Println("What is the second number? ")
	second_num_str, _ := reader.ReadString('\n')

	first_num, _ := strconv.Atoi(strings.TrimSpace(first_num_str))
	second_num, _ := strconv.Atoi(strings.TrimSpace(second_num_str))

	print_str := fmt.Sprintf("%d + %d = %d", first_num, second_num, first_num+second_num)
	print_str += "\n"
	print_str += fmt.Sprintf("%d - %d = %d", first_num, second_num, first_num-second_num)
	print_str += "\n"
	print_str += fmt.Sprintf("%d * %d = %d", first_num, second_num, first_num*second_num)
	print_str += "\n"
	print_str += fmt.Sprintf("%d / %d = %d", first_num, second_num, first_num/second_num)

	fmt.Println(print_str)
}
