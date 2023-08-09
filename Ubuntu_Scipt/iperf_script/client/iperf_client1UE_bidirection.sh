#!/bin/bash
ul_size="110M"  # p2 80 p1 45 tdd2 110
dl_size="260M"  #p2 340  p1 600 tdd2 260
duration="30"
length="1300" #1360
name="UDP"
#name="TCP"

#tcp

command_1_TCP="iperf3 -c 192.188.44.22 --i 1 -M $length -t $duration -P 12 --bidir"
#command_1_UL_TCP="iperf3 -c 192.188.11.22 -l $length  -i 1  -t $duration -P 8"


# UDPcommand_1_UL_UDP="iperf3 -c 192.188.11.22 -l 1360  -i 1  -t $duration -p 10"

command_1_DL_UDP="iperf3 -c 192.188.44.22 -b $dl_size -l $length  -i 1  -t $duration -u -R -p 5202"
command_1_UL_UDP="iperf3 -c 192.188.44.22 -b $ul_size -l $length  -i 1  -t $duration -u"


#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.22.22 UL\"; $command_2_UL; exec bash -i"
#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.22.22 DL\"; $command_2_DL; exec bash -i"

#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.33.22 UL\"; $command_3_UL; exec bash -i"
#gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.33.22 DL\"; $command_3_DL; exec bash -i"



function TCPDLUL(){
#TCP bidiretion
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.11.22 bidirection_TCP \"; $command_1_TCP; exec bash -i"

}



function UDPDLUL(){
#UDP -UL
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.11.22 DL_UDP \"; $command_1_DL_UDP; exec bash -i"
gnome-terminal --tab -- bash -c "sleep 1s; echo \"command: 192.188.11.22 UL_UDP \"; $command_1_UL_UDP; exec bash -i"
}




#########################main###############
#TCPDLUL
UDPDLUL
