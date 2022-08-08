#!/bin/bash
host=192.188.4.21
#hostIP=127.0.0.1
#echo -n "Please Enter your Host IP"
#read host
#host_=ssh -o StrictHostKeyChecking=no  nrgnb@$host
#sshcommand="ssh -o StrictHostKeyChecking=no  alpha@$hostIP"
sshcommand="ssh -o StrictHostKeyChecking=no nrgnb@$host"
echo $sshcommand
#open terminal to ssh host
for i in {1..7}
do
gnome-terminal --tab -- bash -c "sleep 1s; echo \"SSH to host\"; $sshcommand; exec bash -i"

done
