#!/bin/bash
expect -c "
spawn telnet 192.168.$1.1
expect \"login as:\"
sleep 1
send \"admin\r\"
expect \"password:\"
sleep 1
send \"admin\r\"
expect \"#\"
sleep 1
send \"ifconfig wwan0 | grep inet\r\"
expect \"#\"
sleep 1
send \"exit\r\"
interact
"
date
