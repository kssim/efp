/*
 * Pratice 3. Printing Quotes
 * Output:
 *   What is the quote? Books are a uniquely portable magic.
 *   Who said it? Stephen King
 *   Stephen King says, "Books are a uniquely portable magic."
 * Constraint:
 *   - Use a single output statement to produce this output,
 *     using appropriate string-escaping techniques for quotes.
 *   - If your language supports string interpolation or string
 *     substitution, don't use it for this exercise. Use string
 *     concatenation instead.
 */

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("What is the quote? ")
	quotation, _ := reader.ReadString('\n')
	fmt.Println("Who said it? ")
	author, _ := reader.ReadString('\n')

	var print_str string
	print_str = strings.TrimSpace(author)
	print_str += " says, \""
	print_str += strings.TrimSpace(quotation)
	print_str += "\""

	fmt.Println(print_str)
}
