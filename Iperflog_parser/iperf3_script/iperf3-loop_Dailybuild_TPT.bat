@echo off
echo %date% %time% >> DL_dailyTpt.log
iperf3 -c 192.168.1.150 -i 1 -P 48 -R -t 600 --timestamp --logfile DL_dailyTpt.log

echo %date% %time% >> UL_dailyTpt.log
iperf3 -c 192.168.1.150 -i 1 -P 48 -t 600 --timestamp --logfile UL_dailyTpt.log

D:\iperf3.18_64_script\Throughput