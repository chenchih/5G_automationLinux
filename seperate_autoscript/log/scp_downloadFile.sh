#!/bin/bash
#v1: inial release user enter full log path
#v2: hotcode log file location, user enter logfile
# check fw
#echo -n "enter ip and host name(ex: nrgnb@192.188.4.21 ): "
#read sshhostname
sshhostname="nrgnb@192.188.4.21"
loglocation="/var/gnb/log/collect/"
#echo -n "enter your source location: "
echo -n "enter your logfile name: "
read sourcePath
echo -n "enter your destination location: "
read destinationPath

#echo $sshhostname:$loglocation$sourcePath $destinationPath
scp $sshhostname:$loglocation$sourcePath $destinationPath

#scp $sshhostname:$sourcePath $destinationPath
#scp nrgnb@192.188.4.21:/home/nrgnb/Desktop/chenchihFile/flow.pcapng .
