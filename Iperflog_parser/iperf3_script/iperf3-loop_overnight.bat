@echo off
:loop
echo %date% %time% >> iperf3_F.log
iperf3 -c 192.168.1.150 -i 1 -f m -w 2m -P 32 -t 0 -R --timestamp --logfile iperf3_F.log
echo. >> iperf3_F.log
echo. >> iperf3_F.log
echo. >> iperf3_F.log
goto loop

rem D:\iperf3.18_64_script
D:\iperf3.18_64_script\overnight