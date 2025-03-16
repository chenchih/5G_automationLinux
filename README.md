## Intro
This repoistory wil be automation script on 5G system. 
I been using the 5G system which ues Ubuntu as it's OS. 

The purpose of automation is to accelerating work, to work smark and indeed to much more productiv+efficiency

## checklist 
- [x] log_graph (python)
- [x] Ubuntu_Scipt (linux bash script)
- [x]seperate_autoscript
- [x] Iperflog_parser 

## Description:
- log_graph: analyze CDU Log parse the log file, and draw graph 
- Ubuntu Script: Common used linux command without typing command used the code
- Iperflog_parser: filter iperf3 log and export to excel or txt file

## Linux commands:

- SSH automate
```
$ sshpass -p "My_Server_Password" ssh ubuntu@hostIP
or
sshpass -p mypassword ssh username@hostIP touch foo
sshpass -ffilename_with_password_in_it ssh user@server uname -a
```
- `grep -r`: get last string 
```
#Get last string: ex:TddConfigCommon.PatternType = TDD2, get TDD2 
pattern=`grep -r "TddConfigCommon.PatternType" confChange.txt | awk '{printf $3}'`
```

- `SED`: replace TDD2 to other string
```
sed -i "/TddConfigCommon.PatternType = /c\TddConfigCommon.PatternType = TDD2" confChange.txt
```

- run and dump into logfile in same time:
```
#!/bin/bash
(
  iperf -c 127.0.0.1 -t 10 -i 1 >> iperf.log
) 2>&1 | tee -a file.log

```

- open multiply terminal 
```
dump into logfile in same time
gnome-terminal -- bash -c  "iperf -s 2>&1 | tee 123.log "
#many comamnd
#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: $command\"; $command; >> testLLog111.txt ;exec bash -i " 
#gnome-terminal -- bash -c 'sshpass -p 123456 ssh -t '$hostiperf' "iperf3 -c 127.0.0.1 -t 10;exec bash"'
gnome-terminal -- bash -c  "iperf3 -s  2>&1 | tee iperf3.txt"
```

## Code description(old) need to remove:

- `add_virtual.sh`: adding virtual IP when multiple UE connect on Switch 
- `ipadd_test.sh`:
- `scp_downloadFile.sh`: use `scp` to upload and download file, use enter your full path name
- `script_Forma.sh`: It's  just a simple bash format file
- `SSH_multiply_Host.sh`: will automatically run multipy terminal and make ssh connection
- `iperf_server_terminal.sh`: run multipy iperf server in new terminal with increment Ip address

