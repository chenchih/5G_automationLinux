# Parse log working directory 

## Description

Process multiple log files in a directory, extracts SUM lines, converts transfer rates to Gbits/sec,
formats data, and writes to separate sheets in an Excel file.

This code user don't have to enter the logfile, it will parse all the logfile or txt file in current workign directory. 

## output
It will check current working directory for file contain `.txt` and `.log` and parse, but if content contain [RX-C] [TX-C] which is bidirectional log then will skip this logfile

![parse_excelshee_output](..\..\img\parse_excelsheet_output.png)
## version update
- v1: parse unit gbit and mbit
	- run working directory file that contain log or txt file will read the file and parse data
    - if unit is M then will convert unit to G, ex: 1000 then it will change to 1 
    - remove the unit
    - NOT SUPPORT bidirectional 
    - [Issue 001]: 0.00 bit not able to filter
- v2: Capture 0.00 bit  
	- fix issue: adding 0.00 bit also able to parse
	- [Isssue 002]: two digit and space for date will not be capture
- v3: ignore log contain tx or RX 
	- if log contain tx or tx then ignore that file(bidirectional)
- v4: capture date with space and digit 
	- fix issue: Capture space with two digit for date `add \\s+\\d{1,2}`


### check current directory for log and txt file 
```
def process_log_files_to_excel(directory_path, output_excel_file):
workbook = openpyxl.Workbook()
file_list = [f for f in os.listdir(directory_path) if f.endswith((".txt", ".log"))]  # Get .txt and .log files
# Delete the default sheet if it exists
if "Sheet" in workbook.sheetnames:
	del workbook["Sheet"]
if not file_list:
    print(f"No .txt or .log files found in directory: {directory_path}")
		return
```

### parse and capture string
- v1
```
with open(input_file_path, 'r') as infile:
	for line in lines:
		if "[SUM]" in line:
		# Modified regex to capture bits/sec, Mbits/sec, and Gbits/sec
		match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (bits|Mbits|Gbits)/sec",line)
		if match:
			date_str = match.group(1)
			transfer_str = match.group(2)
			unit = match.group(3)
```
- v4
```
with open(input_file_path, 'r') as infile:
	for line in lines:
		if "[SUM][RX-C]" in line or "[SUM][TX-C]" in line:
			print(f"\nSkipping {filename}: Contains RX/TX data.")
			rx_tx_found = True
			break  # Skip to the next file
		if "[SUM]" in line:
			# Modified regex to capture bits/sec, Mbits/sec, and Gbits/sec
			match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (bits|Mbits|Gbits)/sec",line)
```


### convert unit 
```
# Convert to Gbits/sec
transfer_value = float(transfer_str)
	if unit == "Mbits":
		transfer_value /= 1000.0  # Convert Mbits to Gbits
    elif unit == "bits":
		transfer_value /= 1000000000.0 # Convert bits to Gbits
    sheet.append([formatted_date, transfer_value, 'gbps'])
```