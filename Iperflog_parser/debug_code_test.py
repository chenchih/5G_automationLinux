import re
from datetime import datetime
import openpyxl

def process_log_file_to_excel(input_file, output_excel_file):

    with open(input_file, 'r') as infile:
        for line in infile:
            if "[SUM]" in line:
                #print(line)
                #get GBytes
                #match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+\.\d+) GBytes", line)
                #get Mbits/sec
                #match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+) Mbits/sec", line)
                match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
                print(match.group(3))
                      
# Example usage:
input_file_path = "input_Mbits_short.txt"  # Replace with your input file path
output_excel_file_path = "output.xlsx"  # Replace with your output Excel file path

process_log_file_to_excel(input_file_path, output_excel_file_path)


