/*
 * Pratice 19. BMI Calculator
 * Output:
 *   Your BMI is 19.5.
 *   You are within the ideal weight range.
 *   Or
 *   Your BMI is 32.5.
 *   You are overweight. You should see your doctor.
 * Formula:
 *   bmi = (weight / (height x height)) x 703
 * Standard:
 *   BMI 18.5 ~ 25 is nomal weight.
 * Constraint:
 *   - Ensure your program takes only numeric data.
 *     Don't let the user continue unless the data is valid.
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

	fmt.Println("What is your weight(pound)? ")
	weight_str, _ := reader.ReadString('\n')
	fmt.Println("What is your height(inch)? ")
	height_str, _ := reader.ReadString('\n')

	weight, _ := strconv.ParseFloat(strings.TrimSpace(weight_str), 64)
	height, _ := strconv.ParseFloat(strings.TrimSpace(height_str), 64)

	bmi_convert_value := 703
	bmi_raw_data := weight / (height * height)
	bmi := bmi_raw_data * float64(bmi_convert_value)

	fmt.Printf("Your BMI is %.2f\n", bmi)

	if bmi < 18.5 {
		fmt.Println("You are within the ideal weight range.")
	} else if bmi > 25 {
		fmt.Println("You are overweight. You should see your doctor.")
	} else {
		fmt.Println("You are nomal weight.")
	}
}
