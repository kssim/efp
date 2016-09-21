/*
 * Pratice 11. Currency Conversion
 * Output:
 *   How many euros are you exchanging? 81
 *   What is the exchange rate? 134.81
 *   81 euros at an exchange rate of 134.81
 *   109.20 U.S. dollars.
 * Constraint:
 *   - Ensure that fractions of a cent are rounded up to the next penny.
 *   - Use a single output statement.
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
	fmt.Println("How many euros are you exchanging?  ")
	euros_str, _ := reader.ReadString('\n')
	fmt.Println("What is the exchange rate? ")
	exchange_rate_str, _ := reader.ReadString('\n')

	euros, _ := strconv.ParseFloat(strings.TrimSpace(euros_str), 64)
	exchange_rate, _ := strconv.ParseFloat(strings.TrimSpace(exchange_rate_str), 64)

	if euros <= 0 {
		fmt.Println("You must enter a positive number.")
		os.Exit(1)
	}

	dollars := euros * exchange_rate / 100

	print_str := fmt.Sprintf("%.2f euros at an exchange rate of %.2f\n", euros, exchange_rate)
	print_str += fmt.Sprintf("%.2f U.S. dollars.", dollars)

	fmt.Println(print_str)
}
