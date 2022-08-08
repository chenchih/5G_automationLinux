#!/bin/bash

# check fw
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


echo "========Exit:============="



output:
root@nrgnb:/home/nrgnb/Desktop/Untitled Folder# ./CDU_Fw_upgrade.sh 
Please Enter your FW Name(xxx.img): aero_cdu_5.0.5-015.img 
5.0.5-014.v2
-p Enter to start upgrade
state= Running, firmware upgrade running
install target sequence= 2
state= Success, firmware upgrade success
start system features.
========Exit:=============

