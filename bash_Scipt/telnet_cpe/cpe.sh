#!/bin/bash

	expect -c "
	spawn telnet 
	expect \"telnet>\"
	send \"open 192.168.$1.1\r\"
	send \"admin\r\"
	expect \"as:\"
	send \"admin\r\"
        expect \"password:\"
	send \"adb shell\r\"
	sleep 1
	expect \"#\"
	send \"atcli at+cfun=0\r\r\"
	sleep 1
	expect \"OK\"
	send \"\r\"
	send \"atcli at+cfun=1\r\"
	expect \"OK\"
	sleep 10
	send \"atcli at+cesqdbm\r\"
        expect \"#\"
        send \"atcli at+cgdcont?\r\"
        expect \"OK\"
	sleep 3
	send \"atcli at+cgpaddr\r\"
        expect \"OK\"
	interact
	"
