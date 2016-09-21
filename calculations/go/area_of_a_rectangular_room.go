/*
 * Pratice 7. Area of a Rectangular Room
 * Output:
 *   What is the length of the room in feet? 30
 *   What is the width of the room in feet? 20
 *   You entered dimensions of 30 feet by 20 feet.
 *   The area is 600 square feet
 *   55.741824 square meters
 * Formula:
 *   m^2 = f^2 x 0.09290304
 * Constraint:
 *   - Keep the calculations separate from the output.
 *   - Use a constant to hold the conversion factor.
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
	room_width_str, _ := reader.ReadString('\n')

	conversion_factor := 0.09290304
	room_length, _ := strconv.ParseFloat(strings.TrimSpace(room_length_str), 64)
	room_width, _ := strconv.ParseFloat(strings.TrimSpace(room_width_str), 64)
	square_feet := room_length * room_width

	print_str := fmt.Sprintf("You entered dimensions of %g feet by %g feet\n", room_length, room_width)
	print_str += fmt.Sprintf("The area is %g square feet\n", square_feet)
	print_str += fmt.Sprintf("%g square meters", (square_feet * conversion_factor))

	fmt.Println(print_str)
}
