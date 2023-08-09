#!/bin/bash

#gnome-terminal -- bash -c "ls; exec bash"
#echo "ls"

#gnome-terminal --tab -- bash -c "sleep 1s; echo \"Foobar\"; ls; exec bash -i"
#(port11=1000)
#command='iperf -s -p'
#echo $port11
#gnome-terminal --tab -- bash -c "sleep 1s; echo \"iperf port default\"; $command+$port; exec bash -i"
#port=1000
ip_=11
ip10=100
ip11=101
ip12=102
for i in {1..9}

do 
#command='iperf -s -p'
command="iperf3 -s -i1 -B 192.188.$ip_.22 -p 5202"

#echo $command
#echo $command $port
#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: $command\"; $command $port; exec bash -i"

gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: $command\"; $command; exec bash -i"

#((port=port+1))
((ip_=ip_+11))
done

command2="iperf3 -s -i1 -B 192.188.$ip10.22 -p 5202"
command3="iperf3 -s -i1 -B 192.188.$ip11.22 -p 5202"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: $command2\"; $command2; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: $command3\"; $command3; exec bash -i"
