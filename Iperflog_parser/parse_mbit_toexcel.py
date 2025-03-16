'''
Will parse mbit, gbit value, and write into excel
Parses a log file, extracts SUM lines, formats data, and writes to an Excel file.
Includes Mbits/sec and GBytes parsing.
'''
import re
from datetime import datetime
import openpyxl

def process_log_file_to_excel(input_file, output_excel_file):
    try:
        data = []
        with open(input_file, 'r') as infile:
            for line in infile:
                if "[SUM]" in line:
                    match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+\.\d+) GBytes.*?(\d+) Mbits/sec", line)
                    if match:
                        date_str = match.group(1)
                        transfer_str = match.group(2)
                        bitrate_str = match.group(3)
                        #print(match.groups())
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
            workbook.save(output_excel_file)
            print(f"Data written to {output_excel_file}")
        else:
            print("No SUM lines found in the input file.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
input_file_path = "input_Mbits.txt"  # Replace with your input file path
output_excel_file_path = "input_Mbits_output.xlsx"  # Replace with your output Excel file path

process_log_file_to_excel(input_file_path, output_excel_file_path)