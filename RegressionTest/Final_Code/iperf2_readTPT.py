 #!/usr/bin/python
result=""
last_line=""
TPT=""
with open('file.log', 'r') as f:
    last_line = f.readlines()
    last_line=last_line[-1].strip()
print("="*30)     
TPT= last_line.split('  ')[-1]
value= int(round(float(TPT[:4])))
print("Orginal Throuhgput value:", TPT)
print("after Round Value: :", value)

if value< 100:
    print("Iperf result: pass")
    result="Iperf Result: pass"
else:
    print("Iperf result: Fail")
    result="Iperf Result: Fail"

with open("result.txt", "a+") as f:
    # here, position is already at the end
    f.write(f"Iperf Throughput:{TPT},=>{value}. Result PASS\n")


