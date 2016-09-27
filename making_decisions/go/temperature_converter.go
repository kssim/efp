/*
 * Pratice 18. Temperature converter
 * Output:
 *   Press C to convert from Fahrenheit to Celsius.
 *   Press F to convert from Celsius to Fahrenheit.
 *   Your choice: C
 *
 *   Please enter the temperature in Fahrenheit: 32
 *   The temperature in Celsius is 0.
 * Formula:
 *   C = (F - 32) x 5/9
 *   F = (C x 9/5) + 32
 * Constraint:
 *   - Ensure that you allow upper or lowercase values for C and F.
 *   - Use as few output statements as possible and avoid repeating output strings.
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

	fmt.Println("Press C to convert from Fahrenheit to Celsius.")
	fmt.Println("Press F to convert from Celsius to Fahrenheit.")

	fmt.Println("Your choice: ")
	choice, _ := reader.ReadString('\n')
	fmt.Println("Please enter the temperature in Fahrenheit: ")
	temperature_str, _ := reader.ReadString('\n')

	if strings.ToUpper(strings.TrimSpace(choice)) != "C" && strings.ToUpper(strings.TrimSpace(choice)) != "F" {
		fmt.Println("You must input 'C' or 'F'.")
		return
	}

	temperature, _ := strconv.Atoi(strings.TrimSpace(temperature_str))
	convert_value := 32

	convert_temperature := 0
	if strings.ToUpper(strings.TrimSpace(choice)) == "C" {
		convert_temperature = (temperature - convert_value) * (5 / 9)
	} else {
		convert_temperature = (temperature * (9 / 5)) + convert_value
	}

	fmt.Printf("The temperature in Celsius is %d.\n", convert_temperature)
}
