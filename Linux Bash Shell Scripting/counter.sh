#!/bin/bash
declare -i counter 
counter=10
	while [ $counter -gt 0 ]; do
		echo "This step $counter"
		counter=counter-1
	done
exit 0
