#!/bin/bash

echo "What is your favourite color?"
read text1
echo "What is your friend's favourite color?"
read text2
	if test $text1 != $text2; then 
		echo "I guess opposites attract."
	else
		echo "You two think alike!"
	fi
exit 0
