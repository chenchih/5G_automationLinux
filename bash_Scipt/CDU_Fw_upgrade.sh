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





