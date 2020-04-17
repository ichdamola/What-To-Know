package main

import "fmt"

func main () {
	// MAIN TYPES
	// string
	// bool
	// int 
	// int int8 int16 int32 ont64
	// uint uint8 uint16 uint32 uint64 uintptr
	// byte - alias for uint8
	// rune - alias for int32
	// float32 float64
	// complex64 complex128
	var name string = "Nick Cannon"
	var weight int = 50
	fmt.Println(weight)
	fmt.Println(name)
	
	//bool 
	var isKind = true
	fmt.Println(isKind)
	
	//this variable declaration method 
	//can only be used in a function.
	// Shorthand
	age := 23
	
	//shorter way
	gender, size := "male", 2.3
	fmt.Println(size, gender)
	fmt.Println(age)
	
	// Checking var type
	var color = "Yellow"
	fmt.Printf("%T", color)
	
}
