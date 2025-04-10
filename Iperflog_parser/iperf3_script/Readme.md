# Iperf3 script description

My current iperf3 is 3.18, you can use iperf3 -v will show like below
```
iperf 3.18 (cJSON 1.7.15)
CYGWIN_NT-10.0-19045 DESKTOP-G6APJQH 3.5.4-1.x86_64 2024-08-25 16:52 UTC x86_64
Optional features available: CPU affinity setting, authentication, support IPv4 don't fragment, POSIX threads
```

## File Description

- `iperf3-loop_TPT.bat`: Running Throughput both Upload(uplink), and Download(downlink). The log file will be related to Mbit.log file 
```
#DL
iperf3 -c 192.168.1.150 -i 1 -P 48 -R -t 600 --timestamp --logfile DL_dailyTpt.log
#UL
iperf3 -c 192.168.1.150 -i 1 -P 48 -t 600 --timestamp --logfile UL_dailyTpt.log
```

- `iperf3-loop_overnight.bat`: Running stability, or running without stopping. The `-t` is set to 0  been non stop. This log file will be related to Gbit.log file. 

```
# display on terminal 
iperf3 -c 192.168.1.150 -P 32 -t 0 --bidir -b 36M
# save log file
iperf3 -c 192.168.1.150 -P 32 -t 0 --bidir -b 36M --timestamp --logfile iperf3_bidirectional.log
```

- `iperf3-loop_bidirectional.bat`: Run throughput with bidirectional 

```
# display on terminal 
iperf3 -c 192.168.1.150 -P 32 -t 2400 --bidir -b 36M
# save log file
iperf3 -c 192.168.1.150 -P 32 -t 2400 --bidir -b 36M --logfile iperf3_bidirectional.log
```
