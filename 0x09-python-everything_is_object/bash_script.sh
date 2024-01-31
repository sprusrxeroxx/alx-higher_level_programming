#!/bin/bash

# declare an array called array and define 3 vales
array=( [1, 2, 3], 1, [1, 2, 3, 4], [1, 2, 3])
declare -i j=10
for i in "${array[@]}"
do
	echo "$i">$j-answer.txt
done
