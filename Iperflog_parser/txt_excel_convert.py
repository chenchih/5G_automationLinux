import re
from datetime import datetime
import openpyxl  # You'll need to install this: pip install openpyxl

def process_log_file(input_file):
    """
    Parses the input log file, extracts date and mbps from [SUM] lines,
    and returns the extracted data.
    """
    data =[]
    try:
        with open(input_file, 'r', errors='replace') as infile:
            for line in infile:
                if "[SUM]" in line:
                    match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+) Mbits/sec", line)
                    if match:
                        date_str = match.group(1)
                        mbps_str = match.group(2)

                        try:
                            date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                            formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
                            # Convert mbps_str to integer here:
                            mbps_int = int(mbps_str)  
                            data.append([formatted_date, mbps_int])  # Append the integer
                        except ValueError:
                            print(f"Warning: Invalid date format in line: '{line}'. Skipping.")
                        except ValueError:
                            print(f"Warning: Invalid mbps value in line: '{line}'. Skipping.") # Handle potential mbps conversion error
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return None  # Indicate failure
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None  # Indicate failure
    return data

# ... (rest of your code - write_data_to_txt, write_data_to_excel, etc.)def write_data_to_txt(data, output_file):
    """
    Writes the extracted data to a tab-delimited text file.
    """
    if data:
        try:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write("timedate\tmbps\n")
                for row in data:
                    outfile.write(f"{row[0]}\t {row[1]}\n")
            print(f"Data written to {output_file}")
        except Exception as e:
            print(f"An error occurred while writing to text file: {e}")
    else:
        print("No data to write to text file.")

def write_data_to_excel(data, output_file):
    """
    Writes the extracted data to an Excel file.
    """
    if data:
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["timedate", "mbps"])  # Header row
            for row in data:
                sheet.append(row)
            workbook.save(output_file)
            print(f"Data written to {output_file}")
        except Exception as e:
            print(f"An error occurred while writing to Excel file: {e}")
    else:
        print("No data to write to Excel file.")

# Example usage:
input_file_path = "input_Mbits.txt"
output_file_path = "output"  # Base name, extensions will be added

output_format = "excel"  # or "txt" or "both"

extracted_data = process_log_file(input_file_path)

if extracted_data:  # Only write if data was extracted successfully
    if output_format.lower() == "txt" or output_format.lower() == "both":
        write_data_to_txt(extracted_data, output_file_path + ".txt")
    if output_format.lower() == "excel" or output_format.lower() == "both":
        write_data_to_excel(extracted_data, output_file_path + ".xlsx")
    if output_format.lower() not in ["txt", "excel", "both"]:
        print("Invalid output format specified.")