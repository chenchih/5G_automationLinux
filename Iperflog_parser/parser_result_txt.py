import re
from datetime import datetime

def process_log_file(input_file, output_file):
    """   
    Parses the input log file, extracts date and units from [SUM] lines,
    and writes the results to the output file.
    Dynamically sets the header based on the units found in the file.
    """
    try:
        data = []
        unit = None  # Initialize unit to None
        with open(input_file, 'r',  errors='replace') as infile:
            for line in infile:
                if "[SUM]" in line:
                    #match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+) (M|G)bits/sec", line)
                    match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
                    
                    if match:
                        date_str = match.group(1)
                        transfer_str  = match.group(2)
                        current_unit = match.group(3)  # Get the unit (M or G)
                        # Set the unit if it's the first time we encounter it
                        if unit is None:
                            unit = current_unit
                        #convert datetime    
                        try:
                            date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                            formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
                            data.append([formatted_date, transfer_str])
                        except ValueError:
                            print(f"Warning: Invalid date format in line: '{line}'. Skipping.")

        if data:
            if unit == "G":
                header = "timedate\tgbps\n"
            else:
                header = "timedate\tmbps\n"
                
            with open(output_file, 'w', encoding='utf-8') as outfile:
                #outfile.write("timedate\tmbps\n")
                outfile.write(header)
                for row in data:
                    outfile.write(f"{row[0]}\t {row[1]}\n")
            print(f"Data written to {output_file}")
        else:
            print("No [SUM] lines found in the input file.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
input_file_path = "input_Mbits.txt"  # Replace with your input file path
output_file_path = "output22.txt"  # Replace with your output file path

process_log_file(input_file_path, output_file_path)