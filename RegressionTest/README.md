## Version
- v0.1 inital version 

## Description 
This is an automation script to edit CDU server by SSH 

### Step:
1. SSH to CDU server ssh username@host 
2. Change your confgiure file to pattern TDD2 P1 P2 etc
3. apply the configure file 
4. start yoru services
5. run Iperf server in 5GC server(local PC)
6. run Iperf client

## How to run
Under ubuntu server run the script `./menu_regression.sh`

## Special Note

### parser string using SED and awk
####  1. Parse or get the last parameter
> Example: `TddConfigCommon.PatternType = TDD2` 
> Parse last string TDD2 command: 
>> `pattern=`grep -r "TddConfigCommon.PatternType" confChange.txt | awk '{printf $3}'``

###  2. Replace the last parameter 
> comamnd: 
>> 'sed -i "/TddConfigCommon.PatternType = /c\TddConfigCommon.PatternType = TDD2" confChange.txt'

### SSH remote 
ssh connect inaxtie mode add 'bash -s'
> ssh -T test@localhost 'bash -s' <<'EOF'

####  sshpass (please install sshpass package)
>　$ sshpass -p "My_Server_Password" ssh ubuntu@18.118.208.79
or
>  ssh and send command: `sshpass -p mypassword ssh username@10.0.0.9 touch foo`
> sshpass -ffilename_with_password_in_it ssh user@server uname -a


#### ssh with variable 

- EOF method: assign multiply variable
```
host=192.168.50.83
ssh -T test@192.168.50.83 <<'EOF'
var1=$(ls)
var2=$(pwd)
echo -e $var1'\n'$var2

```
- only one single variable 
> end comamnd `VARS=`ssh test@192.168.50.83 'echo 1 2; echo 3'``

```
IFS=$'\n'
VARS=`ssh test@192.168.50.83 'echo 1 2; echo 3'`
for A_VAR in $VARS; do
    #echo "Out: $A_VAR"
    newvar=$A_VAR
```

#### Iperf command 

- run iperf and export to a file
```
run and dump into logfile in same time:
#!/bin/bash
(
  iperf -c 127.0.0.1 -t 10 -i 1 >> iperf.log
) 2>&1 | tee -a file.log

```
- parse only Bandwith
>iperf -c localhost -i 1 -t 10 | grep -i --color Gbits/sec
> iperf -c localhost -i 1 -t 10  | grep -Po '[0-9.]*(?= Gbits/sec)'

#### multiply termianl 
- run terminal with export log file 
> gnome-terminal -- bash -c  "iperf -s 2>&1 | tee 123.log "
- run terminal tab with multiply command 
> gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: $command\"; $command; >> testLLog111.txt ;exec bash -i " 

