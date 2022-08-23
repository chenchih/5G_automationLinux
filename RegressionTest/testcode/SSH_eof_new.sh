#!/bin/sh

eval $(
ssh -T test@localhost 'bash -s' <<'EOF' 
RESULTS1=$(pwd) 
RESULTS2=$(ls) 
#xtest="x *"
#echo "xtest='$xtest'"
echo "RESULTS1='$RESULTS1'"
echo "RESULTS2='$RESULTS2'"
EOF
)
echo "main"
echo "$RESULTS1"
echo "========="
#echo "xtest='$xtest'"
echo "$RESULTS2"
