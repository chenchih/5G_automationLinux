#!/bin/bash
SSHUSR="test"
SSHHOST="localhost"

sshcmdarr() {
	cmdarr=($(ssh "$SSHUSR"@"$SSHHOST" "$1"))
	printf "%s %s\n" "Output of remote command :" "$1"
	for (( i=0;i<${#cmdarr[@]};i++ ))
	do
			echo "${cmdarr[$i]}"
	done
}

tt=sshcmdarr "ls"
tt2=sshcmdarr "pwd"
#sshcmdarr "ls ; pwd"
echo $tt
echo $tt2
