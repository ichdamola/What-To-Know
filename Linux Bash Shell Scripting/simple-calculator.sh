#!/bin/bash
declare -i value1
declare -i value2
declare -i merge

#getting value1 from user
echo "What is your lucky number? "
	read value1
#getting value2 from user
echo "What is your favourite number? "
	read value2
#perform operation on the values

#addition
merge=$value1+$value2
	echo "Aha! your added lucky favourite number is: " $merge

exit 0
