/*
 * Pratice 9. Pain Calculator
 * Output:
 *   You will need to purchase 2 liters of paint
 *   to cover 10 square meter.
 * Formula :
 *   1 liter covers 9 square meter
 * Constraint:
 *   - Use a constant to hold the conversion rate.
 *   - Ensure that you round up to the next whole number.
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
	fmt.Println("What is the length of the room in feet? ")
	room_length_str, _ := reader.ReadString('\n')
	fmt.Println("What is the width of the room in feet? ")
	width_length_str, _ := reader.ReadString('\n')

	cover_meter := 9
	room_length, _ := strconv.Atoi(strings.TrimSpace(room_length_str))
	width_length, _ := strconv.Atoi(strings.TrimSpace(width_length_str))

	room_square_meter := room_length * width_length

	var required_liter int
	if room_square_meter%cover_meter != 0 {
		required_liter = room_square_meter/cover_meter + 1
	} else {
		required_liter = room_square_meter / cover_meter
	}

	fmt.Printf("You will need to purchase %d liters of paint to cover %d square meter.", required_liter, room_square_meter)
}
