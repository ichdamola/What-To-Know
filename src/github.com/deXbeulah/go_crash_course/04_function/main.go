package main

import (
"fmt"
)

func greetings(name string) string {
	return "Hello " + name
}

func getSum(number1, number2 int) int{
	return(number1 + number2)
}

func main () {
	fmt.Println(greetings("Brad"))
	fmt.Println(getSum(4,5))
	
}
