"""
version: v2.3 [Final]
    - progress par to each function
Parses, transforms, and writes data to Excel with detailed progress bars.
"""

import re
from datetime import datetime
import openpyxl
from tqdm import tqdm

def process_log_file_to_excel(input_file, output_excel_file):

    try:
        data = []
        unit = None

        # 1. Parsing Stage
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
            with tqdm(total=len(lines), desc="Parsing Log Lines") as pbar_parse:
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
                    pbar_parse.update(1)

        if data:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            if unit == "G":
                header = ["Datetime", "Tput", "gbps"]
            else:
                header = ["Datetime", "Tput", "mbps"]
            sheet.append(header)

            # 2. Writing to Excel Stage
            with tqdm(total=len(data), desc="Writing Data to Excel") as pbar_write:
                for row in data:
                    sheet.append([row[0], row[1], header[2]])
                    pbar_write.update(1)

            # 3. Adjusting Column Width Stage
            with tqdm(total=1, desc="Adjusting Column Width") as pbar_adjust:
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
                pbar_adjust.update(1) #This stage only happens once.

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