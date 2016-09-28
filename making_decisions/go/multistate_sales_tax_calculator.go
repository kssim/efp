/*
 * Pratice 20. Multistate sales tax calculator
 * Output:
 *   What is the order amount? 10
 *   What state do you live in? Wisconsin
 *   What county do you live in? Eau Claire
 *   The state tax is $0.55.
 *   The county tax is $0.05.
 *   The total tax is $0.60.
 *   The total is $10.60.
 *   Or
 *   What is the order amount? 10
 *   What state do you live in? Illinois
 *   The total tax is $0.80.
 *   The total is $10.80.
 * Standard:
 *   State
 *   Illinois : 0.08
 *   County (If state is Wisconsin)
 *       - Eau Claire : 0.005
 *       - Dunn : 0.004
 * Constraint:
 *   - Ensure that all money is rounded up to the nearest cent.
 *   - Use a single output statement at the end of the program to display the program results.
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
	fmt.Println("What is the order amount? ")
	amount_str, _ := reader.ReadString('\n')

	fmt.Println("What state do you live in? ")
	state, _ := reader.ReadString('\n')

	amount, _ := strconv.ParseFloat(strings.TrimSpace(amount_str), 64)

	tax := 0.0
	county_tax := 0.0

	if strings.ToUpper(strings.TrimSpace(state)) == "WISCONSIN" {
		fmt.Println("What county do you live in? ")
		county, _ := reader.ReadString('\n')

		if strings.ToUpper(strings.TrimSpace(county)) == "EAU CLAIRE" {
			county_tax = amount * 0.005
		} else if strings.ToUpper(strings.TrimSpace(county)) == "DUMN" {
			county_tax = amount * 0.004
		}

		tax = amount * 0.055
	} else if strings.ToUpper(strings.TrimSpace(state)) == "ILLINOIS" {
		tax = amount * 0.08
	} else {
		tax = 0
	}

	fmt.Printf("The state tax is $%.2f\n", tax)

	if county_tax != 0 {
		fmt.Printf("The county tax is $%.2f\n", county_tax)
	}

	fmt.Printf("The total tax is $%.2f\n", tax+county_tax)
	fmt.Printf("The total is $%.2f\n", amount+tax+county_tax)
}
