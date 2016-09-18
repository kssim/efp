/*
 * Pratice 4. Mad Lib
 * Output:
 *   Enter a noun: cat
 *   Enter a verb: beleive
 *   Enter an adjective: adorable
 *   Enter an adverb: seriously
 *   Do you beleive your adorable cat seriously?
 * Constraint:
 *   - Use a single output statement for this program.
 *   - If your language supports string interpolation or string
 *     substitution, use it to build up the output.
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
	fmt.Println("Enter a noun: ")
	noun, _ := reader.ReadString('\n')
	fmt.Println("Enter a verb: ")
	verb, _ := reader.ReadString('\n')
	fmt.Println("Enter a adjective: ")
	adjective, _ := reader.ReadString('\n')
	fmt.Println("Enter a adverb: ")
	adverb, _ := reader.ReadString('\n')

	print_str := fmt.Sprintf("Do you %s your %s %s %s?", strings.TrimSpace(verb), strings.TrimSpace(adjective), strings.TrimSpace(noun), strings.TrimSpace(adverb))
	fmt.Println(print_str)
}
