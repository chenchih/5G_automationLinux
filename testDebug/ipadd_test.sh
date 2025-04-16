#!/bin/bash

ip=10
for loop in {1..3}
do 
command="192.168."$ip".50"
((ip=ip+1))
echo $command
done

