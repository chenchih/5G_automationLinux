'''
version: v2.0
Description: 
Parses a log file, extracts SUM lines, formats data, and writes to an Excel file.
Dynamically sets the header and adjusts the datetime column width.
   
Args:
input_file: Path to the input log file.
output_excel_file: Path to the output Excel file.

- [New Feature]
    - implement Parses a log file, extracts SUM lines with Mbits/sec and Gbit
    - foramt the datetime into customize format YYMMDD_HHMMSS

- [Issue]
    - Issue-001: bit not parse
    - issue1-003: The tput value is inconsistency data type, some are in gb some are in mb(when tpt not reach will show mb)
    - issue-002: The unit type is been hoted code to mbps on the last column which value is gbps, but unit show mbps. 
'''
import re
from datetime import datetime
import openpyxl

def process_log_file_to_excel(input_file, output_excel_file):
    try:
        data = []
        unit = None  # Initialize unit to None
        with open(input_file, 'r') as infile:
            for line in infile:
                if "[SUM]" in line:
                    match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
                     
                    if match:
                        date_str = match.group(1)
                        transfer_str = match.group(2)
                        current_unit = match.group(3)  # Get the unit (M or G)
                        
                        # Set the unit if it's the first time we encounter it
                        if unit is None:
                            unit = current_unit
                            
                        try:
                            date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                            formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")  # Include seconds
                            data.append([formatted_date, float(transfer_str)])  # Store data as list
                        except ValueError:
                            print(f"Warning: Invalid date format in line: '{line}'. Skipping.")

        if data:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            #sheet.append(["Datetime", "Tput", "GBytes"])  # Header row
            #sheet.append(["Datetime", "Tput", "Mbits"])  # Header row
            
            # Dynamically set the header
            if unit == "G":
                header = ["Datetime", "Tput", "gbps"]
            else:
                header = ["Datetime", "Tput", "mbps"]
            sheet.append(header)
            
            for row in data:
                #sheet.append([row[0], row[1], header[2]])  # Write data rows with the correct unit
                sheet.append([row[0], row[1], "Gbits"])  # Write data rows
                #sheet.append([row[0], row[1], "Mbits"])  # Write data rows
               
            
            workbook.save(output_excel_file)
            print(f"Data written to {output_excel_file}")
        else:
            print("No SUM lines found in the input file.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
input_file_path = "input_Mbits_Short.txt"  # Replace with your input file path
output_excel_file_path = "input_Mbits.xlsx"  # Replace with your output Excel file path

process_log_file_to_excel(input_file_path, output_excel_file_path)


