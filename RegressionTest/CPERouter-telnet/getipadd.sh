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
send \" killall appmgrd\r\"
expect \"#\"
sleep 1
send \" killall adpmgr\r\"
expect \"#\"
sleep 1
send \" adb shell atcli at+cfun=0\r\"
expect \"#\"
sleep 1
send \"exit\r\"
interact
"
date
