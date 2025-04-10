@echo off
:loop
echo %date% %time% >> iperf3_bidirectional.log
iperf3 -c 192.168.1.150 -P 32 -t 2400 --bidir -b 36M --timestamp --logfile iperf3_bidirectional.log
Rem iperf3 -c 192.168.1.150 -P 16 -t 2400 --bidir -b 72M --timestamp --logfile iperf3_bidirectional.log

echo. >> iperf3_bidirectional.log
echo. >> iperf3_bidirectional.log
echo. >> iperf3_bidirectional.log
rem goto loop

rem D:\iperf3.18_64_script
D:\iperf3.18_64_script\overnight