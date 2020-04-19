package main

import "fmt"


func greetings(name string) string {
	return "Hello " + name
}

func main () {
	fmt.Println(greetings("Brad"))
	
}
