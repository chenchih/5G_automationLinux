from datetime import datetime, timedelta

def convert_dates_in_file(input_file, output_file):
    """
    Reads dates from an input text file, converts them to YYYYMMDD_HH:MM:SS format,
    subtracts 4 minutes and 10 seconds from the original time,
    and writes the converted dates to an output text file.

    Args:
        input_file: Path to the input text file.
        output_file: Path to the output text file.
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = line.strip()  # Remove leading/trailing whitespace
                try:
                    date_object = datetime.strptime(line, "%a %b %d %H:%M:%S %Y")

                    # Subtract 4 minutes and 10 seconds
                    time_delta = timedelta(minutes=4, seconds=10)
                    adjusted_date = date_object - time_delta

                    formatted_date = adjusted_date.strftime("%Y%m%d_%H:%M:%S")

                    outfile.write(formatted_date + '\n')
                except ValueError:
                    print(f"Warning: Invalid date format in line: '{line}'. Skipping.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
input_file_path = "datedata.txt"  # Replace with your input file path
output_file_path = "output.txt" # Replace with your output file path

convert_dates_in_file(input_file_path, output_file_path)