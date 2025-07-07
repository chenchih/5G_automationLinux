import re
from datetime import datetime
import openpyxl

#filter file contain [sum] substring and print and write into txt file
def parse_sum_line(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if "[SUM]" in line:
                print(line, end='')
                outfile.write(line)  # Write to file  
def parse_matching_str(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, open(output_file, 'w') as outfile:
                            
            for line in infile:
                if "[SUM]" in line:
                    match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM]\[(RX-C|TX-C)\].*?([\d\.]+) (bits|Mbits|Gbits)/sec", line)
                    if match:
                        print(match.group(1))
                        outfile.write(match.group(1)+'\n') #write date time
                        #print(line) #capture result
                    else:
                        print(f"No match found in line: {line.strip()}")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode the file using utf-8 encoding.")
    except FileNotFoundError:
        print(f"Error: file not found: {input_file}")

input_file_path = "iperf3_bidirectional.log"  # Replace with your input file path
output_file_path = "output.txt"  # Replace with your output Excel file path
#parse_sum_line(input_file_path, output_file_path)
parse_matching_str(input_file_path, output_file_path)


