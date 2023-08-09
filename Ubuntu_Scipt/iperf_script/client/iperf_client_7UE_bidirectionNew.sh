#!/bin/bash
ul_size="7M" #tdd2 15 p2:12 p1:7
dl_size="80M" #tdd2 36 p2:47 p1:80
duration="30"
length="1300" #1360
name="UDP"
#name="TCP"



#name="TCP"
command_1_UL_UDP="iperf3 -c 192.188.11.22 -b $ul_size -l $length  -i 1  -t $duration -u"
command_1_DL_UDP="iperf3 -c 192.188.11.22 -b $dl_size -l $length  -i 1  -t $duration -p 5202 -u -R"

command_2_UL_UDP="iperf3 -c 192.188.22.22 -b $ul_size -l $length  -i 1  -t $duration -u"
command_2_DL_UDP="iperf3 -c 192.188.22.22 -b $dl_size  -l $length  -i 1  -t $duration -p 5202 -u -R"

command_3_UL_UDP="iperf3 -c 192.188.33.22 -b $ul_size -l $length  -i 1  -t $duration -u "
command_3_DL_UDP="iperf3 -c 192.188.33.22 -b $dl_size  -l $length  -i 1  -t $duration  -p 5202 -u -R"

command_4_UL_UDP="iperf3 -c 192.188.44.22 -b $ul_size -l $length  -i 1  -t $duration -u "
command_4_DL_UDP="iperf3 -c 192.188.44.22 -b $dl_size -l $length  -i 1  -t $duration  -p 5202 -u -R"

command_5_UL_UDP="iperf3 -c 192.188.55.22 -b $ul_size -l $length  -i 1  -t $duration -u "
command_5_DL_UDP="iperf3 -c 192.188.55.22 -b $dl_size  -l $length  -i 1  -t $duration  -p 5202 -u -R"

command_6_UL_UDP="iperf3 -c 192.188.66.22 -b $ul_size -l $length  -i 1  -t $duration -u "
command_6_DL_UDP="iperf3 -c 192.188.66.22 -b $dl_size  -l $length  -i 1  -t $duration  -p 5202 -u -R"

command_7_UL_UDP="iperf3 -c 192.188.77.22 -b $ul_size -l $length  -i 1  -t $duration -u "
command_7_DL_UDP="iperf3 -c 192.188.77.22 -b $dl_size  -l $length  -i 1  -t $duration -p 5202 -u -R "



command_1_TCP="iperf3 -c 192.188.11.22 -l $length  -i 1  -t $duration -P 8 --bidir"
#command_1_DL_TCP="iperf3 -c 192.188.11.22 -l $length  -i 1  -t $duration -p 5202 -P 12 -R"
command_2_TCP="iperf3 -c 192.188.22.22 -l $length  -i 1  -t $duration -P 8 --bidir"
#command_2_DL_TCP="iperf3 -c 192.188.22.22 -l $length  -i 1  -t $duration -p 5202 -P 12 -R"
command_3_TCP="iperf3 -c 192.188.33.22 -l $length  -i 1  -t $duration -P 8 --bidir"
#command_3_DL_TCP="iperf3 -c 192.188.33.22 -l $length  -i 1  -t $duration -p 5202 -P 12 -R"
command_4_TCP="iperf3 -c 192.188.44.22 -l $length  -i 1  -t $duration -P 8 --bidir"
#command_4_DL_TCP="iperf3 -c 192.188.44.22 -l $length  -i 1  -t $duration -p 5202 -P 12 -R"
command_5_TCP="iperf3 -c 192.188.55.22 -l $length  -i 1  -t $duration -P 8 --bidir"
#command_5_DL_TCP="iperf3 -c 192.188.55.22 -l $length  -i 1  -t $duration -p 5202 -P 12 -R"
command_6_TCP="iperf3 -c 192.188.66.22 -l $length  -i 1  -t $duration -P 8 --bidir"
#command_6_DL_TCP="iperf3 -c 192.188.66.22 -l $length  -i 1  -t $duration -p 5202 -P 12 -R"
command_7_TCP="iperf3 -c 192.188.77.22 -l $length  -i 1  -t $duration -P 8 --bidir"
#command_7_DL_TCP="iperf3 -c 192.188.77.22 -l $length  -i 1  -t $duration -p 5202 -P 12 -R"


test123(){
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.11.22 UL $NAME\"; $command_1_UL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.11.22 DL UDP\"; $command_1_DL_UDP; exec bash -i"

}

test1(){
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.77.22 UL UDP \"; $command_7_UL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.77.22 DL UDP\"; $command_7_DL_UDP; exec bash -i"
}



UDP-bidir(){
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.11.22 UL UDP\"; $command_1_UL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.11.22 DL UDP\"; $command_1_DL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.22.22 UL UDP\"; $command_2_UL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.22.22 DL UDP\"; $command_2_DL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.33.22 UL UDP\"; $command_3_UL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.33.22 DL UDP\"; $command_3_DL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.44.22 UL UDP\"; $command_4_UL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.44.22 DL UDP\"; $command_4_DL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.55.22UL UDP\"; $command_5_UL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.55.22 DL UDP\"; $command_5_DL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.66.22 UL UDP\"; $command_6_UL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.66.22 DL UDP\"; $command_6_DL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.77.22 UL UDP \"; $command_7_UL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.77.22 DL UDP\"; $command_7_DL_UDP; exec bash -i"
}

TCP-bidir(){
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.11.22 UL TCP\"; $command_1_TCP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.22.22 UL TCP\"; $command_2_TCP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.33.22 UL TCP\"; $command_3_TCP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.44.22 UL TCP\"; $command_4_TCP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.55.22 UL TCP\";  $command_5_TCP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.66.22 UL TCP\"; $command_6_TCP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.77.22 UL TCP \"; $command_7_TCP; exec bash -i"

}


#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.22.22 UL\"; $command_2_UL; exec bash -i"
#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.22.22 DL\"; $command_2_DL; exec bash -i"

#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.33.22 UL\"; $command_3_UL; exec bash -i"
#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.33.22 DL\"; $command_3_DL; exec bash -i"

#########################main###############
#UDP-bidir
TCP-bidir

#test1
