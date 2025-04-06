'''
This script will read your original logfile (big file), and  and splits it into multiple smaller text files. 
You can specify splitting line of file, default uses 4000000 line, which average file will be 405mb. In some textedior like notepad or notepad++ not able to open more than 2gb file, so you can use this method to split into smaller file. 
'''
import os
from tqdm import tqdm

def reading_logfile(input_file, output_directory, lines_per_file):
    #lines_per_file = 4000000
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
            
        #total_lines = sum(1 for _ in open(input_file, 'r', encoding='utf-8', errors='ignore')) #calculate total lines.
        file_size = os.path.getsize(input_file)
        average_line_length = 100  # Adjust as needed
        estimated_total_lines = file_size // average_line_length
        
        

        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
            lines = []
            file_count = 1
            #with tqdm(total=total_lines, desc="Processing Lines") as pbar:
            with tqdm(total=estimated_total_lines, desc="Processing Lines") as pbar:
            
                for line in infile:
                    lines.append(line)

                    if len(lines) >= lines_per_file:
                        output_file_path = os.path.join(output_directory, f"output_{file_count}.txt")
                        with open(output_file_path, 'w', encoding='utf-8') as outfile:
                            outfile.writelines(lines)
                        lines = []
                        file_count += 1

                    pbar.update(1)

                if lines:
                    output_file_path = os.path.join(output_directory, f"output_{file_count}.txt")
                    with open(output_file_path, 'w', encoding='utf-8') as outfile:
                        outfile.writelines(lines)

        print(f"Log file '{input_file}' split into files in '{output_directory}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_file_path = "iperf3_bidirectional.log"
output_directory = "split_logs"

print('--------------------------------------------------')
input_file_path = input('Enter your filename: ')
filelinesplit= input('Enter split file line enter for default: 4000000: ')



if filelinesplit == '':
    filelinesplit = 4000000  # Assign 4000000 to filelinesplit
    
else:
    try:
        filelinesplit = int(filelinesplit)  # Convert to integer if not empty
    except ValueError:
        print("Invalid input. Using default value.")
        filelinesplit = 4000000


reading_logfile(input_file_path, output_directory, filelinesplit)
print('--------------------------------------------------')