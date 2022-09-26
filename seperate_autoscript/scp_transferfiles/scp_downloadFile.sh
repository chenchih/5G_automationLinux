#!/bin/bash
# check fw
sshhostname="nrgnb@192.188.4.21"
#echo -n "enter ip and host name(ex: nrgnb@192.188.4.21 ): "
#read sshhostname

echo -n "enter your source location: "
read sourcePath
#echo -n "enter your destination location: "
#read destinationPath
#destinationPath="/home/alpha/Desktop/file/script/scp_transferfiles"
destinationPath=$(pwd)
#scp $sshhostname:$sourcePath $destinationPath
sshpass -p 'nr@Gnb' scp $sshhostname:$sourcePath $destinationPath



#scp nrgnb@192.188.4.21:/home/nrgnb/Desktop/chenchihFile/flow.pcapng .
