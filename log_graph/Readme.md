## Introduction of parsing log file

I am going to develop a automation script to parse log file of CDU throughput data, then save result into txt file, and finally convert the txt result into excel. SIne we have excel data, we can also plot into line graph. 

> ![flex and split cdu system log stucture](../img/Flex_split_logCompare.PNG)

## 1. Split CDU

### Log FIle 
- L2 Elog (Single UE)
```
230213.174350.881038][info]:[[40;32m>>> DL- ingress traffic: 0.000079(Mbps), egress traffic: 0.000085(Mbps), ReTx: 0.000000(Mbps)[0m]
[20230213.174350.881072][info]:[DL- UE[ 0]: Tput=    0.000079 Mbps, Mcs=  9.0(Sigma= 0.0), RbNum=   6.0, ReTxRatio=   0.0, Layers= 1.0, PdschBler=   0.0, nonWPdschBler=   0.0]
[20230213.174350.881084][info]:[>>> DL- Mcs=  9.0, RbNum=   6.0, Layers= 1.0, PdschBler=   0.0, nonWPdschBler=   0.0, MaxSchedUE=   1.0, SchedUE=   1.0]
[20230213.174350.881091][info]:[[40;33mUL <<<- ingress traffic: 0.004133(Mbps) PDU_Count[3], egress traffic: 0.000059(Mbps) PDU_Count[3], ReRx: 0.000000(Mbps)[0m]
[20230213.174350.881105][info]:[UL- UE[ 0]: Tput= 0.000059 Mbps, avg Mcs=  9.0(Sigma= 0.00), RbNum=  90.0, Layers= 1.0, PuschEffecSinr= 0.00(0.0 dB), PuschSinr= 164.00(18.0 dB), PuschBler=   0.0, nonWPuschBler=   0.0, TA=  31.0, PHR= 38.0 dB, SchCnt=     3, S-BSR= 3, L-BSR= 0]
[20230213.174350.881116][info]:[UL <<<- Mcs=  9.0, RbNum=  90.0, Layers= 1.0, PuschEffecSinr= 0.00(0.0 dB), PuschSinr= 164.00(18.0 dB), PuschBler=   0.0, nonWPuschBler=   0.0, TA=  31.0, PHR= 38.0 dB, S-BSR= 3, L-BSR= 0]
[20230213.174350.881123][info]:[DL CFG NUM= 1001, UL CFG NUM= 3, Slot Indication NUM= 20000, Free RNTI Num= 99]
[20230213.174350.881129][info]:[<<<Cell Up Time>>> : 30 sec, cell_index: 0]
```

- L2 Elog (multiple UE)
```
[20230310.232915.783061][info]:[>>> DL- Mcs= 26.0, RbNum=  99.0, Layers= 4.0, PdschBler=   1.7, nonWPdschBler=   1.7, MaxSchedUE=   1.0, SchedUE=   8.0]
[20230311.012825.882186][info]:[[40;32m>>> DL- ingress traffic: 117.590118(Mbps), egress traffic: 120.919250(Mbps), ReTx: 2.519794(Mbps)[0m]
[20230311.012825.882228][info]:[DL- UE[ 4]: Tput=   14.697621 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum=  71.0, ReTxRatio=   0.7, Layers= 4.0, PdschBler=   0.7, nonWPdschBler=   0.7]
[20230311.012825.882243][info]:[DL- UE[ 6]: Tput=   14.699148 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum=  71.4, ReTxRatio=   1.9, Layers= 4.0, PdschBler=   2.0, nonWPdschBler=   1.9]
[20230311.012825.882257][info]:[DL- UE[ 7]: Tput=   14.699283 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum=  70.7, ReTxRatio=   1.4, Layers= 4.0, PdschBler=   1.4, nonWPdschBler=   1.4]
[20230311.012825.882270][info]:[DL- UE[ 9]: Tput=   14.699161 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum=  71.2, ReTxRatio=   1.3, Layers= 4.0, PdschBler=   1.5, nonWPdschBler=   1.3]
[20230311.012825.882283][info]:[DL- UE[11]: Tput=   14.699255 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum=  71.3, ReTxRatio=   1.9, Layers= 4.0, PdschBler=   2.1, nonWPdschBler=   1.9]
[20230311.012825.882296][info]:[DL- UE[18]: Tput=   14.698253 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum=  71.3, ReTxRatio=   1.5, Layers= 4.0, PdschBler=   1.7, nonWPdschBler=   1.5]
[20230311.012825.882310][info]:[DL- UE[28]: Tput=   14.698245 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum=  71.6, ReTxRatio=   4.2, Layers= 4.0, PdschBler=   4.7, nonWPdschBler=   4.5]
[20230311.012825.882322][info]:[DL- UE[29]: Tput=   14.699161 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum=  71.3, ReTxRatio=   2.2, Layers= 4.0, PdschBler=   2.4, nonWPdschBler=   2.2]
[20230311.012825.882339][info]:[>>> DL- Mcs= 55.0, RbNum=  71.2, Layers= 4.0, PdschBler=   2.1, nonWPdschBler=   1.9, MaxSchedUE=   1.0, SchedUE=   8.0]
[20230311.012825.882348][info]:[[40;33mUL <<<- ingress traffic: 77.519501(Mbps) PDU_Count[8000], egress traffic: 74.335068(Mbps) PDU_Count[7647], ReRx: 2.915803(Mbps)[0m]
[20230311.012825.882366][info]:[UL- UE[ 4]: Tput= 6.112589 Mbps, avg Mcs= 14.4(Sigma= 1.95), RbNum= 264.2, Layers= 1.0, PuschEffecSinr= 154.33(13.2 dB), PuschSinr= 150.86(11.4 dB), PuschBler=   0.0, nonWPuschBler=  19.4, TA=  31.3, PHR=  0.1 dB, SchCnt=  1173, S-BSR= 945, L-BSR= 0]
[20230311.012825.882383][info]:[UL- UE[ 6]: Tput= 9.719428 Mbps, avg Mcs= 20.0(Sigma= 0.00), RbNum= 265.5, Layers= 1.0, PuschEffecSinr= 176.22(24.1 dB), PuschSinr= 173.99(23.0 dB), PuschBler=   0.0, nonWPuschBler=   0.0, TA=  31.0, PHR= 16.0 dB, SchCnt=   957, S-BSR= 957, L-BSR= 0]
[20230311.012825.882399][info]:[UL- UE[ 7]: Tput= 9.629381 Mbps, avg Mcs= 20.0(Sigma= 0.00), RbNum= 263.3, Layers= 1.0, PuschEffecSinr= 173.50(22.8 dB), PuschSinr= 170.76(21.4 dB), PuschBler=   0.0, nonWPuschBler=   4.1, TA=  31.4, PHR= 15.0 dB, SchCnt=   998, S-BSR= 957, L-BSR= 0]
[20230311.012825.882414][info]:[UL- UE[ 9]: Tput= 9.753142 Mbps, avg Mcs= 20.0(Sigma= 0.00), RbNum= 266.2, Layers= 1.0, PuschEffecSinr= 172.40(22.2 dB), PuschSinr= 170.06(21.0 dB), PuschBler=   0.0, nonWPuschBler=   0.5, TA=  31.0, PHR= 17.0 dB, SchCnt=   962, S-BSR= 957, L-BSR= 0]
[20230311.012825.882430][info]:[UL- UE[11]: Tput= 9.856048 Mbps, avg Mcs= 20.0(Sigma= 0.00), RbNum= 268.1, Layers= 1.0, PuschEffecSinr= 177.90(24.9 dB), PuschSinr= 175.44(23.7 dB), PuschBler=   0.0, nonWPuschBler=   7.7, TA=  31.0, PHR= 14.0 dB, SchCnt=  1037, S-BSR= 958, L-BSR= 0]
[20230311.012825.882445][info]:[UL- UE[18]: Tput= 9.773015 Mbps, avg Mcs= 20.0(Sigma= 0.00), RbNum= 266.7, Layers= 1.0, PuschEffecSinr= 173.11(22.6 dB), PuschSinr= 170.88(21.4 dB), PuschBler=   0.0, nonWPuschBler=   0.0, TA=  31.2, PHR= 21.1 dB, SchCnt=   957, S-BSR= 958, L-BSR= 0]
[20230311.012825.882461][info]:[UL- UE[28]: Tput= 9.727610 Mbps, avg Mcs= 20.0(Sigma= 0.00), RbNum= 265.8, Layers= 1.0, PuschEffecSinr= 175.20(23.6 dB), PuschSinr= 172.80(22.4 dB), PuschBler=   0.0, nonWPuschBler=   0.1, TA=  31.1, PHR= 25.0 dB, SchCnt=   958, S-BSR= 957, L-BSR= 0]
[20230311.012825.882475][info]:[UL- UE[29]: Tput= 9.763858 Mbps, avg Mcs= 20.0(Sigma= 0.00), RbNum= 266.7, Layers= 1.0, PuschEffecSinr= 174.33(23.2 dB), PuschSinr= 171.99(22.0 dB), PuschBler=   0.0, nonWPuschBler=   0.0, TA=  31.2, PHR=  9.0 dB, SchCnt=   958, S-BSR= 957, L-BSR= 0]
[20230311.012825.882486][info]:[UL <<<- Mcs= 19.2, RbNum= 265.8, Layers= 1.0, PuschEffecSinr= 171.58(21.8 dB), PuschSinr= 169.16(20.6 dB), PuschBler=   0.0, nonWPuschBler=   4.4, TA=  31.2, PHR= 14.6 dB, S-BSR= 7646, L-BSR= 0]
```

- PDCP (contain ingress and egress)
```
[20221217.194812.548238][info]:[PDCP DL- ingress traffic: 239.968109(Mbps), egress traffic: 214.256439(Mbps)]
[20221217.194812.548244][info]:[PDCP UL- ingress traffic: 96.111160(Mbps), egress traffic: 95.896652(Mbps)]
[20221217.194817.576984][info]:[Relay DL- ingress traffic: 240.012161(Mbps), egress traffic: 216.351471(Mbps), pkt: 103906]
[20221217.194817.577017][info]:[========== Mem Pool Usage ==========]
```

### Analysis parse log  
- datetime and Tput value
```
[20221102.064905.609030][info]:[[40;32m>>> DL- ingress traffic: 555.198792(Mbps), egress traffic: 551.669556(Mbps), ReTx: 0.000000(Mbps)[0m]
```

- datetime, tput, other value such as Mcs, RbNum, and etc
```
[20221102.064905.609113][info]:[DL- UE[ 0]: Tput=  555.198792 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum= 198.4, ReTxRatio=   0.0, Layers= 4.0, PdschBler=   0.0, nonWPdschBler=   0.0]
```
## 2. Flex CDU 

### Log FIle 
- L2 Elog 
```
[20240605.181922.505079][info]:[[40;33mUL <<< ingress[0.000000][0], egress[0.000000][0], ReRx[0.000000][0m]
[20240605.181922.505088][info]:[Up Time=30, DlCfgNum=62, SlotIdcNum=20000]
[20240605.181932.504778][info]:[[40;32m>>> DL ingress[0.000000], egress[0.000000], ReTx[0.000000][0m]
[20240605.181932.504815][info]:[[40;33mUL <<< ingress[0.000000][0], egress[0.000000][0], ReRx[0.000000][0m]
[20240605.181932.504825][info]:[Up Time=40, DlCfgNum=63, SlotIdcNum=20000]
```

### Analysis parse log 
- datetime, tput, other value such as Mcs, RbNum, and etc
```
[20240606.150020.325614][info]:[D-UE[ 1][  1]: Tput= 585.617676, Mcs=28.0, RB=262.6, ReTx=  0.0, L=4.0, Bler=  0.0, A[9490]N[  0]D[ 0]S[  17], Rssi=81]
```


