# Parse log working directory 

## Description

Process multiple log files in a directory, extract SUM lines, convert transfer rates to Gbits/sec,
formats data, and writes to separate sheets in an Excel file.

This code user doesn't have to enter the logfile, it will parse all the logfiles or txt files inthe  current working directory. 

## output
It will check the current working directory for files containing `.txt` and `.log` and parse, but if the content contains [RX-C] [TX-C] which is a bidirectional log then it will skip this logfile

![parse_excelshee_output](../img/parse_excelsheet_output.png)
## version update
- v1: parse unit gbit and mbit
	- Run the current working directory file that contains log or txt file will read the file and parse data
    - If the unit is M then it will convert the unit to G, ex: 1000 then it will change to 1 
    - Remove the unit
    - NOT SUPPORT bidirectional 
    - [Issue 001]: 0.00 bit not able to filter
- v2: Capture 0.00 bit  
	- fix issue: adding 0.00 bit is also able to parse
	- [Isssue 002]: two digit and space for date will not be captured
- v3: ignore log contains tx or RX 
	- if log contains tx or tx then ignore that file(bidirectional)
- v4: capture date with space and digit 
	- fix issue: Capture space with two digit for date `add \\s+\\d{1,2}`
- v5: implment plot graph on all sheet 
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

### parse and capture a string
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

- v5

adjust x axis for datetime with interval (data divide by interval in below 50, which will show how many x axis)
>  `plt.xticks( np.linspace(0, len(datetime_col)-1, 50 ),rotation=90, ha='right' )`	



```
all_sheets_data = pd.read_excel(excel_file, sheet_name=None)
    for sheet_name, df in all_sheets_data.items():
        if 'Datetime' in df.columns and 'Tput' in df.columns:
            # Ensure 'Datetime' is treated as string for direct display
            datetime_col = df['Datetime']
            tput_col = pd.to_numeric(df['Tput'], errors='coerce') # Convert Tput to numeric, handle errors
            plt.figure(figsize=(12, 5), dpi=150) # Adjust figure size if needed
            plt.plot(datetime_col, tput_col, label='Tput')
            plt.xlabel('Time')
            plt.ylabel('Throughput (gbps)')
            plt.title(f'Throughput - {sheet_name}')
            plt.legend()
            plt.grid(True)
            # Set y-axis limits
            plt.ylim(0, 4)
            # Display full datetime on x-axis
            #plt.xticks(rotation=45, ha='right')
            plt.xticks( np.linspace(0, len(datetime_col)-1, 50 ),rotation=90, ha='right' )
            plt.tight_layout()
            plt.savefig(f"tput_adjusted_{sheet_name}.png")
            plt.close()
            print(f"Adjusted plot for {sheet_name} saved.")
        else:
            print(f"Warning: Sheet '{sheet_name}' missing 'Datetime' or 'Tput' co
```
you can also use minute or hour as interval 
```
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce', format='%Y%m%d_%H:%M:%S')
df.dropna(subset=['Datetime', 'Tput'], inplace=True)
fig, ax = plt.subplots(figsize=(12, 5), dpi=150) # Use subplots for date formatting
ax.plot(datetime_col, tput_col, label='Tput')
ax.set_xlabel('Time')
ax.set_ylabel('Throughput (gbps)')
ax.set_title(f'Throughput - {sheet_name}')
ax.legend()
ax.grid(True)
.....
plt.tight_layout()
plt.savefig(f"tput_adjusted_{sheet_name}.png")
plt.close()
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