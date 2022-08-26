 #!/usr/bin/python
result=""
last_line=""
lastResult_line=""
TPT=""
with open('iperf3.txt', 'r') as f:
    last_line = f.readlines()
    #lastResult_line="".join(last_line[-3:])
    #lastResult_line=lastResult_line.strip()
    last_line=last_line[-1].strip()
    
print("="*30)  
#print(lastResult_line)
#print(last_line)
TPT= last_line.split('                  ')
TPT=TPT[0].split(' ')[-2]
value= int(round(float(TPT)))
print(f"Orginal Throuhgput value: {TPT} Mbps")
print(f"after Round Value: {value}.0 Mbps")

if value< 100:
    print("Iperf result: pass")
    result="Iperf Result: pass"
else:
    print("Iperf result: Fail")
    result="Iperf Result: Fail"
with open("testresult.txt", "a+") as f:
    # here, position is already at the end
    f.write(f"####Test4:{result}, Throughput:{value}.0 Mbps ####\n")
    f.write(f"{'='*20}Iperf3 Result{'='*20}\n")
    f.write(f"{last_line}\n")
    #f.write(f"{lastResult_line}\n")
    f.write(f"{'='*50}\n")
    f.write(f"Iperf Throughput:{TPT}GBytes,rounded=>{value}.0 Mbps. Result PASS\n")


