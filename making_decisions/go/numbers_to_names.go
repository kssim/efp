/*
 * Pratice 21. Numbers to names
 * Output:
 *   Please enter the number of the month: 3
 *   The name of the month is March.
 * Constraint:
 *   - Use a switch or case statement for this program.
 *   - Use a single output statement for this program.
 */

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func get_month_str(number_month int) string {
	switch {
	case number_month == 1:
		return "January"
	case number_month == 2:
		return "February"
	case number_month == 3:
		return "March"
	case number_month == 4:
		return "April"
	case number_month == 5:
		return "May"
	case number_month == 6:
		return "June"
	case number_month == 7:
		return "July"
	case number_month == 8:
		return "August"
	case number_month == 9:
		return "September"
	case number_month == 10:
		return "October"
	case number_month == 11:
		return "November"
	case number_month == 12:
		return "December"
	}
	return ""
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Please enter the number of the month: ")
	number_month_str, _ := reader.ReadString('\n')

	number_month, _ := strconv.Atoi(strings.TrimSpace(number_month_str))

	if number_month < 1 || number_month > 12 {
		fmt.Println("Wrong input value, you must input number of the month.")
		return
	}

	fmt.Printf("The name of the month is %s.\n", get_month_str(number_month))
}
