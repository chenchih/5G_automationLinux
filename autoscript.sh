#!/bin/bash

#sshhostname=nrgnb@192.188.4.21

function log(){
sshhostname="nrgnb@192.188.4.21"
loglocation="/var/gnb/log/collect/"
#echo -n "enter your source location: "
echo -n "enter your logfile name-Ex(xxxx.tar.gz): "
read sourcePath
echo -n "enter your destination location Ex: . : "
read destinationPath
scp $sshhostname:$loglocation$sourcePath $destinationPath
}

function downloadfile(){
echo "=========Download file to server (SCP)====================="
echo -n "enter ip and host name(ex: nrgnb@192.188.4.21 ): "
read sshhostname
echo -n "enter your source location: "
read sourcePath
echo -n "enter your destination location: "
read destinationPath
scp $sshhostname:$sourcePath $destinationPath
echo "Download Complete!!!"
}


function uploadfile(){
echo "=========upload file to server (SCP)====================="
echo -n "enter ip and host name(ex: nrgnb@192.188.4.21 ): "
read sshhostname
echo -n "enter your local file name (source): "
read sourcePath
echo -n "enter your destination(upload location full path)-Ex: /home/nrgnb/Downloads/: "
read destinationPath
scp $sourcePath $sshhostname:$destinationPath
}


function fwupgrade(){
sshhostname="nrgnb@192.188.4.21"
echo -n "current FW is: "
cat /home/nrgnb/gnbfs/system/etc/buildver

echo -n "Please Enter your FW Name(xxx.img): "
read fwname

#upgrade fw
#cd /home/nrgnb/
imgPath="/home/nrgnb/Downloads/"
systenBIN="/home/nrgnb/gnbfs/system/bin/"
cd $systenBIN

read -p "Enter to start upgrade"
./fw_upgrade scp 127.0.0.1:$imgPath$fwname nrgnb nr@Gnb
#./fw_upgrade scp 127.0.0.1:~/Downloads/$fwname nrgnb nr@Gnb
}


function menu() {
while :
do
echo "#########"AutoScript v0.1"###############"
echo "1  Download Log from CDU"
echo "2  Upload file to CDU"
echo "3  Download file from CDU"
echo "3  CDU FW Upgrade"
echo "q) Exit"
echo "###########################"
read -p "Please enter your Options: " option

if [ "$option" == "1" ]; then 
log
read -p "please enter to continue"
clear

elif [ "$option" == "2" ]; then
downloadfile
read -p "please enter to continue"
clear

elif [ "$option" == "3" ]; then
uploadfile
read -p "please enter to continue"
clear

elif [ "$option" == "4" ]; then
fwupgrade
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



