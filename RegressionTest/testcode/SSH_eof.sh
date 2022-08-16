
#!/bin/sh
varall=""
host=192.168.50.83
ssh -T test@192.168.50.83 <<'EOF'
var1=$(ls)
var2=$(pwd)
echo -e $var1'\n'$var2
#echo $var2
varall=$var1
EOF
echo "exit"
echo $varall
