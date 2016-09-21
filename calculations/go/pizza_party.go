/*
 * Pratice 8. Pizza Party
 * Output:
 *   How many people? 22
 *   How many pizzas do you have? 3
 *   22 people with 3 pizzas
 *   Each person gets 1 pieces of pizza.
 *   There are 2 leftover pieces.
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
	fmt.Println("How many people? ")
	people_num_str, _ := reader.ReadString('\n')
	fmt.Println("How many pizzas do you have? ")
	pizzas_num_str, _ := reader.ReadString('\n')

	people_num, _ := strconv.Atoi(strings.TrimSpace(people_num_str))
	pizzas_num, _ := strconv.Atoi(strings.TrimSpace(pizzas_num_str))

	pizza_pieces_num := (pizzas_num * 8)
	print_str := fmt.Sprintf("%d people with %d pizzas\n", people_num, pizzas_num)
	print_str += fmt.Sprintf("Each person gets %d pieces of pizza.\n", (pizza_pieces_num / people_num))
	print_str += fmt.Sprintf("There are %d leftover pieces.", pizza_pieces_num%people_num)

	fmt.Println(print_str)
}
