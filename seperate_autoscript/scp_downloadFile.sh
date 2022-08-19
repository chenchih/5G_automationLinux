#!/bin/bash
# check fw


echo 'read -p "please enter ypur option on SCP Method: '
echo '1. download'
echo '2. upload'
echo '========================'



function download(){
echo -n "enter ip and host name(ex: nrgnb@192.188.4.21 ): "
read sshhostname
echo -n "enter your source location: "
read sourcePath
echo -n "enter your destination location(save in local location): "
read destinationPath
scp $sshhostname:$sourcePath $destinationPath
}


function upload(){
echo -n "enter ip and host name(ex: nrgnb@192.188.4.21 ): "
read sshhostname
echo -n "enter your source location:(local files to upload): "
read sourcePath
echo -n "enter your destination location:(upload location) : "
read destinationPath
scp $sshhostname:$sourcePath $destinationPath
}




scp $sshhostname:$sourcePath $destinationPath
#scp nrgnb@192.188.4.21:/home/nrgnb/Desktop/chenchihFile/flow.pcapng .
