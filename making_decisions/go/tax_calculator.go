/*
 * Pratice 14. Tex-Calculator
 * Output:
 *   What is the order amount? 10
 *   What is the state? WI
 *   The subtotal is $10.00
 *   The tax is $0.55
 *   The total is $10.55
 *   Or
 *   What is the order amount? 10
 *   What is the state? MN
 *   The subtotal is $10.55
 * Constraint:
 *   - Implement this program using only a simple if state-ment-don't use an 'else' clause.
 *   - Ensure that all money is rounded up to the nearest cent.
 *   - Use a single output statement at the end of the program to display the program result.
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
	fmt.Println("What is the order amount?  ")
	order_amount_str, _ := reader.ReadString('\n')
	fmt.Println("What is the state?  ")
	state, _ := reader.ReadString('\n')

	order_amount, _ := strconv.ParseFloat(strings.TrimSpace(order_amount_str), 64)
	tax_rate := 0.055
	tax := order_amount * tax_rate

	var print_str string
	if strings.ToUpper(strings.TrimSpace(state)) == "WI" {
		print_str = fmt.Sprintf("The subtotal is $%d\nThe tax is $%.2f\nThe total is $%.2f", order_amount, tax, order_amount+tax)
	} else {
		print_str = fmt.Sprintf("The total is $%.2f", order_amount+tax)
	}

	fmt.Println(print_str)
}
