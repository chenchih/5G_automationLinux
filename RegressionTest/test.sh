#!/bin/bash




#RESULTS=$(ssh localhost 'ip a';'ls')
VARS=`ssh test@localhost 'echo 1 2; echo 3'`
tt=""
for A_VAR in $VARS; do
    #echo "Out: $A_VAR"
    newvar=$A_VAR
    tt2[$tt]="$A_VAR";
done
echo $tt" "

