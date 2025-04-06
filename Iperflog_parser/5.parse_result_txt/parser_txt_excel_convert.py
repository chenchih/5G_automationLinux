import re, sys
from datetime import datetime
import openpyxl 

def process_log_file(input_file):

    data =[]
    try:
        with open(input_file, 'r', errors='replace') as infile:
            for line in infile:
                if "[SUM]" in line:
                    #only filter M or G
                    #match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
                    match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (bits|Mbits|Gbits)/sec", line)
                    if match:
                        date_str = match.group(1)
                        TPUT = match.group(2)
                        unit = match.group(3)

                        '''
                        if unit is None:
                            unit = unit
                        elif unit == 'G':      
                            print('Warming Your log file contains Gbits/seclog file which not support. \nThis script only captures Mbits/sec log files, please change log file!!!')                        
                            sys.exit(1) # Exit with an error code
                        '''
                        try:
                            date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                            formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
                            data.append([formatted_date, float(TPUT), unit])  # Append the integer
                        except ValueError:
                            print(f"Warning: Invalid date format in line: '{line}'. Skipping.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return None  # Indicate failure
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None  # Indicate failure
    return data

def write_data_to_txt(data, output_file):
    if data:
        try:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write("timedate\tTPUT\tunits\n")
                for row in data:
                    outfile.write(f"{row[0]}\t {row[1]}\t {row[2]}\n")
            print(f"Data written to {output_file}")
        except Exception as e:
            print(f"An error occurred while writing to text file: {e}")
    else:
        print("No data to write to text file.")
        

    
def write_data_to_excel(data, output_file):
    if data:
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["timedate", "TPUT","Unit"])  # Header row
            
            for row in data:
                sheet.append(row)
            adjust_column_width(sheet)
            workbook.save(output_file)
            print(f"Data written to {output_file}")
        except Exception as e:
            print(f"An error occurred while writing to Excel file: {e}")
    else:
        print("No data to write to Excel file.")

def adjust_column_width(sheet):
    """Adjusts the first column's width."""
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
input_file_path = input('Enter your filename: ')
output_file_path = "output"  # Base name, extensions will be added

output_format = input('Enter output format type (excel, txt, both): ')
#output_format = "excel"  # or "txt" or "both"

extracted_data = process_log_file(input_file_path)


if extracted_data:  # Only write if data was extracted successfully
    if output_format.lower() == "txt" or output_format.lower() == "both":
        write_data_to_txt(extracted_data, output_file_path + ".txt")
    if output_format.lower() == "excel" or output_format.lower() == "both":
        write_data_to_excel(extracted_data, output_file_path + ".xlsx")
    if output_format.lower() not in ["txt", "excel", "both"]:
        print("Invalid output format specified.")
