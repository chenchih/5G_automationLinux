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

send \"adb shell atcli at+cfun=0\r\r\"
sleep 1
expect \"OK\"
send \"\r\"
send \"adb shell atcli at+cfun=1\r\"
expect \"OK\"
sleep 1
send \"exit\r\"
interact
"
date
