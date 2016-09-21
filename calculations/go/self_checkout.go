/*
 * Pratice 10. Self-Checkout
 * Output:
 *   Enter the price of item 1: 25
 *   Enter the quantity of item 1: 2
 *   Enter the price of item 2: 10
 *   Enter the quantity of item 2: 1
 *   Enter the price of item 3: 4
 *   Enter the quantity of item 3: 1
 *   Subtotal: $64.00
 *   Tax: $3.52
 *   Total: $67.52
 * Constraint:
 *   - Keep the input, processing, and output parts of your program separate.
 *     Collect the input, then do the math operations and string building,
 *     and then print out the output.
 *   - Be sure you explicitly convert input to numerical data before doing
 *     any calculations.
 */

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type item struct {
	price int
	count int
}

func main() {
	var item_list [3]item

	reader := bufio.NewReader(os.Stdin)

	for i := 0; i < 3; i++ {
		fmt.Printf("Enter the price of item %d: ", i+1)
		price_str, _ := reader.ReadString('\n')
		item_list[i].price, _ = strconv.Atoi(strings.TrimSpace(price_str))

		fmt.Printf("Enter the quantity of item %d: ", i+1)
		count_str, _ := reader.ReadString('\n')
		item_list[i].count, _ = strconv.Atoi(strings.TrimSpace(count_str))
	}

	subtotal := 0
	tax_rate := 5.5

	for _, item := range item_list {
		subtotal += (item.price * item.count)
	}

	tax := float64(subtotal) * tax_rate / 100
	total := float64(subtotal) + tax

	print_str := fmt.Sprintf("Subtotal: $%d\n", subtotal)
	print_str += fmt.Sprintf("Tax: $%.2f\n", tax)
	print_str += fmt.Sprintf("Total: $%.2f", total)

	fmt.Println(print_str)
}
