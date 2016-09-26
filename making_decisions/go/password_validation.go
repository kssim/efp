/*
 * Pratice 15. Password validation
 * Output:
 *   What is the username: kssim
 *   What is the password: 12345
 *   I don't know you.
 *   Or
 *   What is the username: kssim
 *   What is the password: abc$123
 *   Welcome!
 * Constraint:
 *   - Use an 'if/else' statement for this problem.
 *   - Make sure the program is case sensitive.
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
	fmt.Println("What is the username?  ")
	username, _ := reader.ReadString('\n')
	fmt.Println("What is the password?  ")
	password, _ := reader.ReadString('\n')

	if strings.TrimSpace(username) == "kssim" && strings.TrimSpace(password) == "abc$123" {
		fmt.Println("Welcome!")
	} else {
		fmt.Println("I don't know you.")
	}
}
