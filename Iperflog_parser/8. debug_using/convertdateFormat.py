from datetime import datetime

def convert_dates_in_file(input_file, output_file):

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = line.strip()  # Remove leading whitespace
                try:
                    date_object = datetime.strptime(line, "%a %b %d %H:%M:%S %Y")
                    formatted_date = date_object.strftime("%Y%m%d_%H:%M:%S")
                    outfile.write(formatted_date + '\n')
                except ValueError:
                    print(f"Warning: Invalid date format in line: '{line}'. Skipping.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_file_path = "datedata.txt"
output_file_path = "output.txt"

convert_dates_in_file(input_file_path, output_file_path)
input('Press Enter to close...')