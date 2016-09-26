/*
 * Pratice 17. Blood alcohol calculator
 * Output:
 *   Your BAC is 0.08
 *   It is not legal for you to drive.
 * Formula:
 *   BAC = (A x 5.14/W x r)-.015 x H
 *   A is total alcohol consumed, in ounces(oz).
 *   W is body weight in pounds.
 *   r is the alcohol distribution ratio:
 *       - 0.73 for men
 *       - 0.66 for women
 *   H is number of hours since the last drink.
 * Standard:
 *   BAC = 0.08 under.
 * Constraint:
 *   - Prevent the user from entering non-numeric values.
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
	fmt.Println("What is your weight?  ")
	weight_str, _ := reader.ReadString('\n')
	fmt.Println("What is your gender(m or f)?  ")
	gender, _ := reader.ReadString('\n')
	fmt.Println("How much do you drink alcohol(oz)?  ")
	total_alcohol_str, _ := reader.ReadString('\n')
	fmt.Println("What is number of hours since the last drink?  ")
	last_drink_time_str, _ := reader.ReadString('\n')

	if strings.ToUpper(strings.TrimSpace(gender)) != "M" && strings.ToUpper(strings.TrimSpace(gender)) != "F" {
		fmt.Println("You must input 'M' or 'F'.")
		return
	}

	weight, _ := strconv.ParseFloat(strings.TrimSpace(weight_str), 64)
	total_alcohol, _ := strconv.ParseFloat(strings.TrimSpace(total_alcohol_str), 64)
	last_drink_time, _ := strconv.ParseFloat(strings.TrimSpace(last_drink_time_str), 64)

	male_alcohol_ratio := 0.73
	female_alcohol_ratio := 0.66
	oz_calculation_value := 5.14
	last_drink_time_calculation_value := .015
	legal_standard_bac := 0.08

	var alcohol_ratio float64
	if strings.ToUpper(strings.TrimSpace(gender)) == "M" {
		alcohol_ratio = male_alcohol_ratio
	} else {
		alcohol_ratio = female_alcohol_ratio
	}

	bac_value := (total_alcohol * oz_calculation_value / weight * alcohol_ratio) - (last_drink_time_calculation_value * last_drink_time)

	fmt.Printf("Your BAC is %.2f\n", bac_value)

	if bac_value < legal_standard_bac {
		fmt.Println("It is legal for you to drive.")
	} else {
		fmt.Println("It is not legal for you to drive.")
	}
}
