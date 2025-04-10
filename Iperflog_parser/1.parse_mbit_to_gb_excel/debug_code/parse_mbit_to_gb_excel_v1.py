import re
from datetime import datetime

def process_log_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if "[SUM]" in line:
                    #gbit
                    match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+\.\d+ Gbits/sec)", line)
                    #mbit
                    #match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d+\.]+ Mbits/sec)", line)
                    if match:
                        date_str = match.group(1)
                        transfer_str = match.group(2)

                        try:
                            date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                            formatted_date = date_obj.strftime("%Y%m%d_%H:%M")

                            outfile.write(f"{formatted_date} {transfer_str}\n")
                        except ValueError:
                            print(f"Warning: Invalid date format in line: '{line}'. Skipping.")

                    else:
                        print(f"Warning: Line with [SUM] did not match regex: '{line}'. Skipping.") 
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_file_path = "input_gbits_Short.txt"  # Replace with your input file path
output_file_path = "output.txt" # Replace with your output file path

process_log_file(input_file_path, output_file_path)