#!/bin/sh

IFS=$'\n'
VARS=`ssh test@192.168.50.83 'echo 1 2; echo 3'`
for A_VAR in $VARS; do
    #echo "Out: $A_VAR"
    newvar=$A_VAR
 
done

echo "exit"
echo $newvar
