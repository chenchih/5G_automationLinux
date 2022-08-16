#!/bin/bash
host=localhost

function patternCheck(){
ssh test@$host<<'EOF'
configlocation='/home/test/Desktop/5GScript/confChange.txt'
pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "========================================"
echo "Your current Pattern is:"$pattern
echo "========================================"
EOF
}

function P1___test(){
ssh test@$host<<'EOF'
configlocation='/home/test/Desktop/5GScript/confChange.txt'
pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "========================================"
echo "Your current Pattern is:"$pattern
echo "change Pattern to P1...."
sed -i "/TddConfigCommon.PatternType = /c\TddConfigCommon.PatternType = P1" $configlocation
echo "Your current Pattern is:"$pattern
echo  
echo "========================================"
EOF
}


function P1(){
ssh test@$host<<'EOF'
configlocation='/home/test/Desktop/5GScript/confChange.txt'
pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "========================================"
#echo "Your current Pattern is:"$pattern 
if [ "$pattern" == "P1" ]; then 
echo "Pattern Already P1"
echo "Your current Pattern is:"$pattern 

else
echo "change Pattern to P1...."
sed -i "/TddConfigCommon.PatternType = /c\TddConfigCommon.PatternType = P1" $configlocation
pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "Your current Pattern is:"$pattern 
fi
echo "========================================"
EOF
}




function TDD2(){
ssh test@$host<<'EOF'
configlocation='/home/test/Desktop/5GScript/confChange.txt'
pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "========================================"
#echo "Your current Pattern is:"$pattern 
if [ "$pattern" == "TDD2" ]; then 
echo "Pattern Already TDD2"
echo "Your current Pattern is:"$pattern 

else
echo "change Pattern to TDD2...."
sed -i "/TddConfigCommon.PatternType = /c\TddConfigCommon.PatternType = TDD2" $configlocation
pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "Your current Pattern is:"$pattern 
fi
echo "========================================"
EOF
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
TDD2
read -p "please enter to continue"
clear

elif [ "$option" == "2" ]; then
#echo "p1"
#P1
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



