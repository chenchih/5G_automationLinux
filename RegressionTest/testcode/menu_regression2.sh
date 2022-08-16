#!/bin/bash

function patternCheck(){
#clear
pattern=`grep -r "TddConfigCommon.PatternType" confChange.txt | awk '{printf $3}'`
echo "Your current Pattern is:"$pattern
}

function P1(){
pattern=`grep -r "TddConfigCommon.PatternType" confChange.txt | awk '{printf $3}'`

if [ "$pattern" == "P1" ]; then 
echo "Pattern Already P1"

else
sed -i "/TddConfigCommon.PatternType = /c\TddConfigCommon.PatternType = P1" confChange.txt
fi
}


function TDD2(){
pattern=`grep -r "TddConfigCommon.PatternType" confChange.txt | awk '{printf $3}'`

if [ "$pattern" == "TDD2" ]; then 
echo "Pattern Already TDD2"

else
sed -i "/TddConfigCommon.PatternType = /c\TddConfigCommon.PatternType = TDD2" confChange.txt

fi
}



function menu() {
while :
do
echo "#########"Test v0"###############"
echo "1  Pattern:TDD2 IPERF3"
echo "2  Pattern: P1"
echo "3  check current pattern"
echo "q) Exit"
echo "###########################"
read -p "Please enter your Options: " option

if [ "$option" == "1" ]; then 
#echo "TDD2"
TDD2
read -p "please enter to continue"
clear

elif [ "$option" == "2" ]; then
#echo "p1"
P1
read -p "please enter to continue"
clear

elif [ "$option" == "3" ]; then
patternCheck
read -p "please enter to continue"
clear

elif [ "$option" == "q" ]; then
read -p "please enter to exit"
exit
clear 

else
echo -e "no options found, please enter to retry"
#break
fi
done	

}

clear

menu



