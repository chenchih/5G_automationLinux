#!/bin/bash

#v.0.0 inital version
#v0.1 add ssh parmater, and iperf server
#v0.2 add append file

host=localhost
CPEhost=localhost
cduservice='cd /'

function pinghost(){
#host=192.168.50.83

ping -c 1 -t 1 $host > /dev/null
if [ $? -eq 0 ]; then
    #echo "ping success";
    #ping client SIDE
    ping -c 1 -t 1 $CPEhost > /dev/null 
    if [ $? -eq 0 ]; then
    #echo "ping success";
    : #do nothing
    else
    	echo "ping ClientPc fail";
    	echo
    	exit
    fi
else
    echo "ping CDU Host fail";
    echo
    exit
fi

}



function patternCheck(){
ssh test@$host -- bash<<'EOF'
configlocation='/home/test/Desktop/5GScript/confChange.txt'
pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "========================================"
echo "Your current Pattern is:"$pattern
echo "========================================"
EOF
}


function P1(){
ssh test@$host -- bash<<'EOF'
scriptlocation='/home/test/Desktop/5GScript'
configlocation='/home/test/Desktop/5GScript/confChange.txt'
resultlocation='/home/test/Desktop/5GScript/'

pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "========================================"
#echo "Your current Pattern is:"$pattern 
if [ "$pattern" == "P1" ]; then 
	echo "Pattern Already P1"
	cd $resultlocation
	echo "Your current Pattern is:"$pattern > resultPattern.txt
else
	echo "change Pattern to P1...."
	#####stop##########
	cd $scriptlocation
	echo "Stop CDU service, please wait 30 second!!!"
	./hello.sh	
	sleep 10
	cd $resultlocation
	echo "Stop CDU Services PASS" >>resultPattern.txt
	####################
	sed -i "/TddConfigCommon.PatternType = /c\TddConfigCommon.PatternType = P1" $configlocation
	pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
	echo "Your current Pattern is:"$pattern >>resultPattern.txt 
	#####start##########
	cd $scriptlocation
	echo "Start CDU service, please wait 30 second!!!"
	./hello.sh
	sleep 10
	cd $resultlocation
	echo "Start CDU Services PASS" >>resultPattern.txt
	####################
fi
echo "========================================"
EOF
}


function TDD2(){
ssh test@$host -- bash<<'EOF'
scriptlocation='/home/test/Desktop/5GScript'
configlocation='/home/test/Desktop/5GScript/confChange.txt'
resultlocation='/home/test/Desktop/5GScript/'

pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "========================================"
#echo "Your current Pattern is:"$pattern 
if [ "$pattern" == "TDD2" ]; then 
	echo "Pattern Already TDD2"
	cd $resultlocation
	echo "Your current Pattern is:"$pattern >resultPattern.txt
else
	echo "change Pattern to TDD2...."
	#####stop##########
	cd $scriptlocation
	echo "Stop CDU service, please wait 30 second!!!"
	./hello.sh	
	sleep 10
	cd $resultlocation
	echo "Stop CDU Services PASS" >>resultPattern.txt
	####################
	sed -i "/TddConfigCommon.PatternType = /c\TddConfigCommon.PatternType = TDD2" $configlocation
	pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
	echo "Your current Pattern is:"$pattern >>resultPattern.txt 
	#####start##########
	cd $scriptlocation
	echo "Start CDU service, please wait 30 second!!!"
	./hello.sh
	sleep 10
	cd $resultlocation
	echo "Start CDU Services PASS" >>resultPattern.txt
	####################
fi
echo "========================================"
EOF
}

function cduresult_merge(){
ssh test@$host "cat /home/test/Desktop/5GScript/resultPattern.txt" >> /home/test/Desktop/5GScript/testresult.txt
}





function menu() {
while :
do
echo "#########"Test v0.2"###############"
echo "1  Pattern:TDD2 IPERF3"
echo "2  Pattern: P1"
echo "3  check current pattern"
echo "4 test"
echo "q) Exit"
echo "###########################"
read -p "Please enter your Options: " option

if [ "$option" == "1" ]; then 
TDD2
cduresult_merge
echo "Start Iperf Server"
iperf_serverLocal
read -p "please enter to continue ... "
clear

elif [ "$option" == "2" ]; then
#echo "p1"
#P1
P1
cduresult_merge
echo "Start Iperf Server"
iperf_serverLocal
read -p "please enter to continue ... "
clear

elif [ "$option" == "3" ]; then
patternCheck
read -p "please enter to continue ... "
clear

elif [ "$option" == "4" ]; then
P1___test
read -p "please enter to continue ... "
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

function iperf_serverLocal(){
gnome-terminal -- bash -c  "iperf -s 2>&1 | tee 123.log "
}

echo $(date) RegressionTest >testresult.txt
pinghost
echo "ALl HOST PinG PASS" >>testresult.txt
menu




