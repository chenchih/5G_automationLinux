#!/bin/bash
# check fw
echo "=========upload file to server SCP====================="

echo -n "enter ip and host name(ex: nrgnb@192.188.4.21 ): "
read sshhostname


echo -n "enter your local file name (source): "
read sourcePath
echo -n "enter your destination(upload location full path)Ex: /home/nrgnb/Downloads/: "
read destinationPath
#echo $sourcePath $sshhostname:$destinationPath 
scp $sourcePath $sshhostname:$destinationPath
#download
#scp nrgnb@192.188.4.21:/home/nrgnb/Desktop/chenchihFile/flow.pcapng .
#uploadfile
#scp l1app-0809 nrgnb@192.188.4.21:/home/nrgnb/Downloads/


