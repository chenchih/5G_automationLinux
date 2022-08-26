#!/bin/bash

#v.0.0 inital version
#v0.1 add ssh parmater, and iperf server
#v0.2 add append file
#v0.4 iperf3  log migrate
#v0.5 ssh without password

host=localhost
CPEhost=localhost
cduservice='cd /'
resultFile='/home/test/Desktop/5GScript/testresult.txt'
password='123456'
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
sshpass -p $password ssh -T -o StrictHostKeyChecking=no test@localhost -- bash <<'EOF'
#ssh test@$host -- bash<<'EOF'
configlocation='/home/test/Desktop/5GScript/confChange.txt'
pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "========================================"
echo "Your current Pattern is:"$pattern
echo "========================================"
EOF
}


function P1(){
sshpass -p $password ssh -T -o StrictHostKeyChecking=no test@localhost -- bash <<'EOF'
scriptlocation='/home/test/Desktop/5GScript'
configlocation='/home/test/Desktop/5GScript/confChange.txt'
resultlocation='/home/test/Desktop/5GScript/'

pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "===========Login CDU Server============================="
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
	echo "Stop CDU Services ok" >resultPattern.txt
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
	echo "Start CDU Services ok" >>resultPattern.txt
	echo "Exit CDU server"
	####################
fi
echo "===========Exit CDU server=================="
EOF
}


function TDD2(){
#ssh test@$host -- bash<<'EOF'
sshpass -p $password ssh -T -o StrictHostKeyChecking=no test@localhost -- bash <<'EOF'
scriptlocation='/home/test/Desktop/5GScript'
configlocation='/home/test/Desktop/5GScript/confChange.txt'
resultlocation='/home/test/Desktop/5GScript/'

pattern=$(grep -r "TddConfigCommon.PatternType" $configlocation | awk '{printf $3}')
echo "===========Login CDU Server============================="
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
	echo "Stop CDU Services ok" >resultPattern.txt
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
	echo "Start CDU Services ok" >>resultPattern.txt	
	####################
echo "Exit CDU server"
fi
echo "===========Exit CDU server=================="
EOF
}

function checkhost(){
echo "####Test1: Check Host################ " >>$resultFile
pinghost
echo "ALl HOST PinG PASS" >>$resultFile
}

function cduresult_merge(){
#ssh test@$host "cat /home/test/Desktop/5GScript/resultPattern.txt" >> /home/test/Desktop/5GScript/testresult.txt
sshpass -p $password ssh -T -o StrictHostKeyChecking=no test@localhost "cat /home/test/Desktop/5GScript/resultPattern.txt" >> $resultFile
#ssh test@$host "cat /home/test/Desktop/5GScript/resultPattern.txt" >> $resultFile
}

function testiperf(){
#iperf_serverLocal
#echo "Run Iperf Server ok" 
#read -p "please enter to continue ... "
#iperfclient
#read -p "please enter to continue ... "
#ssh test@$host "iperf3 -c 127.0.0.1 -t 10"
gnome-terminal -- bash -c  ssh test@127.0.0.1 "iperf3 -c 127.0.0.1 -t 10"

}

function iperf_serverLocal(){
#kill iperf server
#echo "Kill all IPERF server =>PASS">>$reult_location
#command="iperf3 -s -i1 -B 192.188.11.22"
#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: $command\"; $command; exec bash -i"2>&1 | tee -a iperftest.log
#gnome-terminal -- bash -c  "iperf -s 2>&1 | tee iperf.log "
#gnome-terminal -- bash -c  "iperf3 -s -i1 -B 192.188.11.22 2>&1 | tee iperf.log"
echo "open iperf server ok"
gnome-terminal -- bash -c  "iperf3 -s  2>&1 | tee iperf3.txt"
#gnome-terminal -- bash -c  "$command -s 2>&1 | tee iperf.log "
#killall iperf
}


function iperfclient(){
iperfservercmd='iperf3 -c 127.0.0.1'
#hostiperf='test@127.0.0.1'
#ssh test@$host "iperf3 -c 127.0.0.1 -t 10"

sshpass -p $password ssh -T -o StrictHostKeyChecking=no test@localhost "$iperfservercmd" &>/dev/null
#gnome-terminal -- bash -c 'sshpass -p 123456 ssh -t '$hostiperf' "iperf3 -c 127.0.0.1 -t 10;exec bash"'

echo "run iperf client ok"
}

function reportcollect(){
#merger iperf log to report 
python3 iperf3_readTPT.py
#rename report 
#mv testresult.txt "$(date +"%m-%d-%y-%h-%m-%s")"
mkdir -p result 
mv $resultFile ./result/"$(date +"%Y-%m-%d %H:%M.%S")"
}




function menu() {
while :
do
echo "#########"Test v0.5"###############"
echo "1  Pattern:TDD2 IPERF3"
echo "2  Pattern: P1"
echo "3  check current pattern"
echo "4 test iperf"
echo "q) Exit"
echo "###########################"
read -p "Please enter your Options: " option
clear

checkhost
if [ "$option" == "1" ]; then 
echo -e "\n####Test2: Change Pattern#" 
echo "####Test2: Change Pattern############" >> $resultFile

#merge cdu result
cduresult_merge
echo "cdu ok" 
echo -e "\n####Test3: SetUP Iperf####" 
echo "####Test3: SetUP Iperf####" >> $resultFile
iperf_serverLocal
echo "Run Iperf Server ok" >> $resultFile
#read -p "please enter to continue ... "
iperfclient
sleep 15
echo "Run Iperf Client ok" >> $resultFile
#read -p "please enter to continue ... "
reportcollect

killall iperf3 &>/dev/null
read -p "please enter to continue ... "
clear

elif [ "$option" == "2" ]; then
echo -e "\n####Test2: Change Pattern############ " >> $resultFile
P1
cduresult_merge
echo "####Test3: SetUP Iperf Server######## " >> $resultFile
iperf_serverLocal
echo "Run Iperf Server ok" >> $resultFile
iperfclient
sleep 15
echo "Run Iperf Client ok" >> $resultFile
reportcollect
killall iperf3 &>/dev/null
clear






elif [ "$option" == "3" ]; then
patternCheck
read -p "please enter to continue ... "
clear

elif [ "$option" == "4" ]; then
testiperf
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


###################MAIN SCRIPT ######################
clear
echo "======================RegressionTest-Report=============">$resultFile
echo "Date: "$(date) >>$resultFile
#echo "####Test1: Check Host################ " >>$resultFile
#pinghost
#echo "ALl HOST PinG PASS" >>$resultFile
menu


#####################################################

