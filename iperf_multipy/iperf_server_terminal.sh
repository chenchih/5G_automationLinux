#!/bin/bash

#gnome-terminal -- bash -c "ls; exec bash"
#echo "ls"

#gnome-terminal --tab -- bash -c "sleep 1s; echo \"Foobar\"; ls; exec bash -i"
#(port11=1000)
#command='iperf -s -p'
#echo $port11
#gnome-terminal --tab -- bash -c "sleep 1s; echo \"iperf port default\"; $command+$port; exec bash -i"
port=1000
ip_=11
for i in {1..7}

do 
#command='iperf -s -p'
command="iperf3 -s -i1 -B 192.188.$ip_.22"
#echo $command
#echo $command $port
#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: $command\"; $command $port; exec bash -i"

gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: $command\"; $command; exec bash -i"

#((port=port+1))
((ip_=ip_+11))
done



