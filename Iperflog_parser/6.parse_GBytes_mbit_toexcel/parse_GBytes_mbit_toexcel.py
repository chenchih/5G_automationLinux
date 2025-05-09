import re
from datetime import datetime
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def process_log_file_to_excel(input_file, output_excel_file):
    try:
        data = []
        with open(input_file, 'r') as infile:
            for line in infile:
                if "[SUM]" in line:
                    match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+\.\d+) GBytes.*?(\d+) Mbits/sec", line)
                    if match:
                        date_str = match.group(1) #datetime
                        transfer_str = match.group(2) #Gbytes value
                        bitrate_str = match.group(3) #Mbit value

                        try:
                            date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                            formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
                            data.append([formatted_date, float(transfer_str), int(bitrate_str)])
                        except ValueError:
                            print(f"Warning: Invalid date format in line: '{line}'. Skipping.")
                            
                        except AttributeError:
                            print(f"Warning: could not parse bitrate in line: '{line}'. Skipping.")
     
                    
        if data:            
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["Datetime", "GBytes", "Mbits/sec"])  # Header row
            for row in data:
                sheet.append(row)
            adjust_column_width(sheet)
            workbook.save(output_excel_file)
            print(f"Data written to {output_excel_file}")
        else:
            print('Error: Your log file contains Gbits/sec. This script only captures GBytes and Mbits/sec log files.')
            #print("No SUM lines found in the input file. ")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
           
#Adjusts the first column's width.
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


if __name__ == "__main__":        
    # Example usage:
    #input_file_path = "input_Mbits_short.txt"  # Replace with your input file path
    #output_excel_file_path = "input_Mbits_short.xlsx"  # Replace with your output Excel file path

    input_file_path = input('Enter your filename: ')
    output_excel_file_path = (input('save exel file name: ')+'.xlsx' )

    process_log_file_to_excel(input_file_path, output_excel_file_path)
