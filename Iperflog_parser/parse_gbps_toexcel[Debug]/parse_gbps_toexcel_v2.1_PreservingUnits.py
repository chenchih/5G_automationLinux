"""
version: v2.1: 
    - preserving the original units from file
    - issue: unit might contain gbit/mbit unit and value wil be inconsistency 

Parses a log file, extracts SUM lines with Mbits/sec or Gbits/sec,
formats data, and writes to an Excel file, preserving the original units.
"""
import re
from datetime import datetime
import openpyxl

def process_log_file_to_excel(input_file, output_excel_file):

    try:
        data =[]
        with open(input_file, 'r') as infile:
            for line in infile:
                if "[SUM]" in line:
                    # Modified regex to capture both Mbits/sec and Gbits/sec
                    match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
                    if match:
                        date_str = match.group(1)
                        transfer_str = match.group(2)
                        unit = match.group(3)

                        try:
                            date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                            formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")

                            # Store the transfer value and the unit
                            data.append([formatted_date, float(transfer_str), unit])
                        except ValueError:
                            print(f"Warning: Invalid data format in line: '{line}'. Skipping.")

        if data:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["Datetime", "Tput", "Units"])  # Header row
            for row in data:
                # Write data rows, preserving the original unit
                sheet.append([row[0], row[1], f"{row[2]}bits"])
            workbook.save(output_excel_file)
            print(f"Data written to {output_excel_file}")
        else:
            print("No SUM lines found in the input file.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
input_file_path = "input_Mbits.txt"
output_excel_file_path = "output.xlsx"

process_log_file_to_excel(input_file_path, output_excel_file_path)