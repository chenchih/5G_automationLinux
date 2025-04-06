import re
from datetime import datetime

def process_log_file(input_file, output_file):

    try:
        data = []
        #unit = None  # Initialize unit to None
        with open(input_file, 'r',  errors='replace') as infile:
            for line in infile:
                if "[SUM]" in line:
                    #match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+) (M|G)bits/sec", line)
                    match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (bits|Mbits|Gbits)/sec", line)
                    if match:
                        date_str = match.group(1)
                        transfer_str  = match.group(2)
                        current_unit = match.group(3)  # Get the unit (M or G)
                        #print(current_unit)
                        
                        #convert datetime    
                        try:
                            date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                            formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
                            data.append([formatted_date, transfer_str, current_unit])
                        except ValueError:
                            print(f"Warning: Invalid date format in line: '{line}'. Skipping.")

        if data:
            header = "timedate\tTput\tUnit\n" 
 
            with open(output_file, 'w', encoding='utf-8') as outfile:
                #outfile.write("timedate\tmbps\n")
                outfile.write(header)
                
                for row in data:
                    outfile.write(f"{row[0]}\t {row[1]}\t {row[2]}\n")
                    
            print(f"Data written to {output_file}")
        else:
            print("No [SUM] lines found in the input file.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
        
print('\t\t<========================================================================>')

input_file_path= input('Please enter log file name: ')
output_file_path = (input('save exel file name (enter for default) : ') )
if output_file_path == '':
    output_file_path = f"output_txtfile.txt"
else:
    output_file_path=output_file_path+'.txt'


#input_file_path = "input_Mbits.txt"  # Replace with your input file path
#output_file_path = "output22.txt"  # Replace with your output file path

process_log_file(input_file_path, output_file_path)
print('\t\t<========================================================================>')