'''
version: v2.3.1 [Final]
    - adding parsing, write excel, adjust excel prcocess into function
Parses, transforms, and writes data to Excel with detailed progress bars.
'''
import re
from datetime import datetime
import openpyxl
from tqdm import tqdm

def process_log_file_to_excel_combined(input_file, output_excel_file):

    try:
        data, unit = parse_log_file(input_file)
        if data:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            write_data_to_excel(sheet, data, unit)
            adjust_column_width(sheet)
            workbook.save(output_excel_file)
            print(f"Data written to {output_excel_file}")
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
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
        with tqdm(total=len(lines), desc="Processing Log File") as pbar:
            for line in lines:
                if "[SUM]" in line:
                    match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
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
                            if unit == "M":
                                transfer_value /= 1000.0
                            data.append([formatted_date, transfer_value])
                        except ValueError:
                            print(f"Warning: Invalid data format in line: '{line}'. Skipping.")
                pbar.update(1)
    return data, unit

def write_data_to_excel(sheet, data, unit):
    """Writes data to the Excel sheet."""
    if unit == "G":
        header = ["Datetime", "Tput", "gbps"]
    else:
        header = ["Datetime", "Tput", "mbps"]
    sheet.append(header)
    with tqdm(total=len(data), desc="Writing to Excel") as pbar:
        for row in data:
            sheet.append([row[0], row[1], header[2]])
            pbar.update(1)

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

# Example usage:
input_file_path = "input_Mbits.txt"
output_excel_file_path = "output_combined.xlsx"

process_log_file_to_excel_combined(input_file_path, output_excel_file_path)