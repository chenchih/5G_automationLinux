 #!/usr/bin/python
def file_last_line(file_path):
    line = ""
    with open(file_path, "r") as file:
        for line in file:
            pass
    return line.strip()
 
 
def throughput_text(throughput_line):
    throughput = throughput_line.split("                  ")[0]
    throughput=throughput.split(" ")[-2]

    #print(throughput)
    rounded_throughput = round(float(throughput))
    
    state = "pass" if rounded_throughput < 100 else "Fail"
    return (
       f"####Test4:Iperf Result: {state}, Throughput:{rounded_throughput}.0 Mbps ####\n"
        f"{'='*20}Iperf3 Result{'='*20}\n"
        f"{throughput_line}\n"
        f"{'='*50}\n"
        f"Iperf Throughput:{throughput}GBytes,rounded=>{rounded_throughput}.0 Gbps. Result PASS\n"
    )
 
 
def main():
    last_line = file_last_line("iperf3.txt")
    #print(last_line)
    
    text = throughput_text(last_line)
    with open("testresult.txt", "a+") as file:
        file.write(text)
 
 
if __name__ == "__main__":
    main()
