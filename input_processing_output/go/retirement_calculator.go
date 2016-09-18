/*
 * Pratice 6. Retirement Calculator
 * Output:
 *   What is your current age? 27
 *   At what age would you like to retire? 70
 *   You have 43 years left until you can retire.
 *   It's 2016, so you can retire in 2059.
 * Constraint:
 *   - Agian, be sure to convert the input to numerical data
 *     before doing any math.
 *   - Don't hard-code the current year into your program.
 *     Get it from the system time via your programming language.
 */

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("What is your current age? ")
	current_age_str, _ := reader.ReadString('\n')
	fmt.Println("At what age would you like to retire? ")
	retire_age_str, _ := reader.ReadString('\n')

	current_age, _ := strconv.Atoi(strings.TrimSpace(current_age_str))
	retire_age, _ := strconv.Atoi(strings.TrimSpace(retire_age_str))

	if current_age >= retire_age {
		fmt.Println("You must input retire age lagger than current age.")
		return
	}

	left_year := retire_age - current_age

	t := time.Now()
	current_year := t.Year()

	print_str := fmt.Sprintf("You have %d years left until you can retire.", left_year)
	print_str += "\n"
	print_str += fmt.Sprintf("It's %d, so you can retire in %d.", current_year, current_year+left_year)

	fmt.Println(print_str)
}
