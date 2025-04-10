import re
from datetime import datetime
import openpyxl
from tqdm import tqdm
import time

def process_log_file_to_excel_combined(input_file, output_excel_file):

    try:
        data, unit = parse_log_file(input_file)
        if data:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            write_data_to_excel(sheet, data, unit)
            adjust_column_width(sheet)
            with tqdm(total=1, desc="Saving Excel File") as pbar_save:
                workbook.save(output_excel_file)
                pbar_save.update(1)
            print(f"Data written to {output_excel_file}")
            
            # Calculate and print duration
            if data:
                calculate_and_print_duration(data)
                
        else:
            print("No SUM lines found in the input file.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def parse_log_file(input_file):
    """Parses the log file and returns the data and unit."""
    data = []
    unit = None
    with open(input_file, 'r', encoding='utf-8', errors='replace') as infile:
        lines = infile.readlines()
        with tqdm(total=len(lines), desc="Processing Log File") as pbar:
            for line in lines:
                if "[SUM]" in line:
                    #match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
                    match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (bits|Mbits|Gbits)/sec",line)
                    #match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM]\[(RX-C|TX-C)\].*?([\d\.]+) (bits|Mbits|Gbits)/sec", line_str)
                    if match:
                        date_str = match.group(1)
                        transfer_str = match.group(2)
                        unit = match.group(3)
                        if unit is None:
                            unit = unit
                        try:
                            date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                            formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
                            transfer_value = float(transfer_str)
                            #v2.2 convert mbit and bit to gbit                                    
                            if unit == "Mbits":
                                transfer_value /= 1000.0
                            elif unit == "bits":
                                transfer_value /= 1000000000.0    
                            data.append([formatted_date, transfer_value])
                        except ValueError:
                            print(f"Warning: Invalid data format in line: '{line}'. Skipping.")
                pbar.update(1)
    return data, unit
#Writes data to the Excel sheet.
def write_data_to_excel(sheet, data, unit):
    #v2.2, since convert to gbps, so unit will be gbps
    header = ["Datetime", "Tput", "gbps"]
    sheet.append(header)
    with tqdm(total=len(data), desc="Writing to Excel") as pbar:
        for row in data:
            sheet.append([row[0], row[1], "gbps"])
            pbar.update(1)
#Adjusts the first column's width
def adjust_column_width(sheet):
    datetime_column = sheet['A']
    max_length = 0
    for cell in datetime_column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except TypeError:
            pass
    adjusted_width = max_length + 2
    sheet.column_dimensions['A'].width = adjusted_width
    
#Calculates and prints the running duration.
def calculate_and_print_duration(data):
    if not data:
        return

    start_time_str = data[0][0]
    end_time_str = data[-1][0]

    start_time = datetime.strptime(start_time_str, "%Y%m%d_%H:%M:%S")
    end_time = datetime.strptime(end_time_str, "%Y%m%d_%H:%M:%S")

    duration = end_time - start_time
    total_seconds = int(duration.total_seconds())

    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60

    print(f"Running duration: {days} days, {hours} hours, {minutes} minutes")
    print(f"Converted hours: {days * 24 + hours} hours")
    
#input_file_path = input('Enter your filename: ')
#output_excel_file_path = "output_combined2.xlsx"
print('\t\t<========================================================================>')

input_file_path= input('Please enter log file name: ')
#output_excel_file_path = (input('save file name: ') +'.xlsx')
output_excel_file_path = (input('save exel file name (enter for default) : ') )

now = datetime.now()
filewithDate=now.strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS

file_content = input_file_path.lower()
if 'mbits' in file_content or 'mbps' in file_content: #add mbps
    filelog='mbitLog'
elif 'gbits' in file_content or 'gbps' in file_content: #add gbps
    filelog='gbitLog'
else: 
    filelog=''

if output_excel_file_path == '':
    output_excel_file_path = f"{filewithDate}_mbit_convert_output_gbit_{filelog}_Result.xlsx"
else:
    output_excel_file_path=output_excel_file_path+'.xlsx'
print('--------------------------------------------------')    
    
try:
    process_log_file_to_excel_combined(input_file_path, output_excel_file_path)
except SystemExit:
    print('\nError: Your log file contains Gbits/sec. This script only captures Mbits/sec log files.')


print('\t\t<========================================================================>')


