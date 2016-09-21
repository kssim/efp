/*
 * Pratice 12. Computing Simple Interest
 * Output:
 *   Enter the principal: 2000
 *   Enter the rate of interest: 5.98
 *   Enter the number of years: 3
 *   After 3 years at 5.98%, the investment will be worth $2358.8.
 * Constraint:
 *   - Prompt for the rate as a percentage (like 20%, not 20).
 *     Divide the input by 100 in your program.
 *   - Ensure that fractions of a cent are rounded up to the next penny.
 *   - Ensure that the output is formatted as money.
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
	fmt.Println("Enter the principal: ")
	principal_str, _ := reader.ReadString('\n')
	fmt.Println("Enter the rate of interest: ")
	interest_rate_str, _ := reader.ReadString('\n')
	fmt.Println("Enter the number of years: ")
	year_str, _ := reader.ReadString('\n')

	principal, _ := strconv.Atoi(strings.TrimSpace(principal_str))
	interest_rate, _ := strconv.ParseFloat(strings.TrimSpace(interest_rate_str), 64)
	year, _ := strconv.Atoi(strings.TrimSpace(year_str))

	if interest_rate <= 0 {
		fmt.Println("You must enter a positive number.")
		os.Exit(1)
	}

	interest := (float64(principal) * interest_rate / 100) * float64(year)

	fmt.Printf("After %d years at %.2f%s, the investment will be worth $%.2f.\n", year, interest_rate, "%", float64(principal)+interest)
}
