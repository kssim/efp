/*
 * Pratice 13. Determining Compound Interest
 * Output:
 *   What is the principal amount? 2000
 *   What is the rate: 6.3
 *   What is the number of years: 4
 *   What is the number of times the interest is compounded per year? 7
 *   $2000 invested at 6.3% for 7 years.
 *   compounded 4 times per year is $3097.86.
 * Formular:
 *   A = P(1+r/n)^nt
 *
 *   A is the amount at the end of the investment.
 *   n is the number of times the interest is compunded per year.
 *   t is the number of years the amount is invested.
 *   r is the annual rate of interest.
 *   P is the principal amount.
 * Constraint:
 *   - Prompt for the rate as a percentage (like 15, not .15).
 *     Divide the input by 100 in your program.
 *   - Ensure that fractions of a cent are rounded up to the next penny.
 *   - Ensure that the output is formatted as money.
 */

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("What is the principal amount? ")
	principal_str, _ := reader.ReadString('\n')
	fmt.Println("What is the rate? ")
	rate_str, _ := reader.ReadString('\n')
	fmt.Println("What is the number of years? ")
	year_str, _ := reader.ReadString('\n')
	fmt.Println("What is the number of times the interest is compounded per year? ")
	interest_year_str, _ := reader.ReadString('\n')

	principal, _ := strconv.Atoi(strings.TrimSpace(principal_str))
	rate, _ := strconv.ParseFloat(strings.TrimSpace(rate_str), 64)
	year, _ := strconv.Atoi(strings.TrimSpace(year_str))
	interest_year, _ := strconv.Atoi(strings.TrimSpace(interest_year_str))

	interest_value := math.Pow((1 + (rate/100)/float64(year)), float64(interest_year*year))
	investment_value := float64(principal) * interest_value

	print_str := fmt.Sprintf("$%d invested at %.2f%s for %d years.\n", principal, rate, "%", interest_year)
	print_str += fmt.Sprintf("compounded %d times per year is $%.2f.", year, investment_value)

	fmt.Println(print_str)
}
