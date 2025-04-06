# parse_mbit_excel
This  code will parse gbit or mbit logfile and capture result into excel File. 


## Description
This script is used to read log file and parse mbit or gbit related keyword. In th elog as you can see the log content contain below different keyword:

```
#input_Gbits.txt
Thu Mar 13 10:04:38 2025 [SUM]   7.01-8.01   sec   283 MBytes  2.37 Gbits/sec

#input_Mbits.txt
Mon Mar 10 18:47:06 2025 [SUM]   0.00-10.00  sec  2.76 GBytes  2368 Mbits/sec
```
You will have realize the keyword to filter is the `[sum]` line, which will display as above. I need to get the time, and the last value either Gbit or Mbits. The Gbit will display in GB and Mbit will display in MB. After capture these string, I will export it to excel file, so that I can draw a graph. 

I have implement many diffent feature, due to some of them have different issue. The reason why I obtain differnt version of code is because so feature might be use in future which I kept as noted. 

Note: This automation will not plot the data in graph, maybe in future. 

## output



#### v2.3.2 Calculate duration start and end time  
- [Improvement]: Print and display more clearner
```
print('\t\t<========================================================================>')

    
if output_excel_file_path == '':
    output_excel_file_path = f"{filewithDate}_mbit_convert_output_gbit_Result.xlsx"
else:
    output_excel_file_path=output_excel_file_path+'.xlsx'
print('--------------------------------------------------')    
    
try:
    process_log_file_to_excel_combined(input_file_path, output_excel_file_path)
except SystemExit:
    print('\nError: Your log file contains Gbits/sec. This script only captures Mbits/sec log files.')


print('\t\t<========================================================================>')
```
- [fixed issue 2.3.0]: the unit name is in mbps. Basically it reads the matching unit, and didn't adjust the unit. 
	- ex: `2.368 mbps` , you can see it convert to gb but unit not change. 
	- using gbit log file will not matter because unit is gbps
- Adding Feature: Adding timedate time, which will calculate how long this test is been run, the duration. 
 
#### v2.3.1: Wrap up feature into function

- [Improvement]: Implement user to enter log filename
```
input_file_path= input('Please enter log file name: ')
output_excel_file_path = (input('save file name: ') +'.xlsx')
```
- [Improvement]: wrap up each feature into function for easier to manage 
```
#main feature contain parse, write excel feature
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

#parse the data
def parse_log_file(input_file):
	with open(input_file, 'r') as infile:
        lines = infile.readlines()
        with tqdm(total=len(lines), desc="Processing Log File") as pbar:
			for line in lines:
                if "[SUM]" in line:
			.......
	return data, unit

#write into excel and save
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
#adjust column width
def adjust_column_width(sheet):
	...
```

#### v2.3.0: Adding progress bar to show parsing log file, and  write to excel
- [New Feature]: Adding progress bar: Parses, transforms, and writes data to Excel with detailed progress bars
Adding progress bar while parsing data, writting the excel
```
from tqdm import tqdm
# 1. Parsing Stage
with tqdm(total=len(lines), desc="Parsing Log Lines") as pbar_parse:
	lines = infile.readlines() 
	with tqdm(total=len(lines), desc="Parsing Log Lines") as pbar_parse:
		for line in lines:
            if "[SUM]" in line:
		....
			pbar_parse.update(1)

	#create excel
        if data:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
			....

            # 2. Writing to Excel Stage
            with tqdm(total=len(data), desc="Writing Data to Excel") as pbar_write:
                for row in data:
                    sheet.append([row[0], row[1], header[2]])
                    pbar_write.update(1)

			# 3. Adjusting Column Width Stage
            with tqdm(total=1, desc="Adjusting Column Width") as pbar_adjust:
                datetime_column = sheet['A']
                max_length = 0
				...
				adjusted_width = max_length + 2
                sheet.column_dimensions['A'].width = adjusted_width
                pbar_adjust.update(1) 
				workbook.save(output_excel_file)
```
- [Improvement] Adjust the datetime column width
```
	# Adjust datetime column width
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
            
    workbook.save(output_excel_file)
    print(f"Data written to {output_excel_file}")
```

- [Issue]: The mbit logfile unit type will not be updated correctly, the mbit unit will display incorrect type 
You can see below code if unit `unit = match.group(3)` is mbit log will be `M`, however  we convert `mb` to `gb` but unit is not been convert. It will display like this : `2.368 mbps` the data type is incorrect. gbit log file will not have problem, because the value is gbit data unit. 
	```
	unit = match.group(3) #match the log line for unit, for mbit file uses  unit as M                       
							
	if unit == "G":
			header = ["Datetime", "Tput", "gbps"]
		else:
			header = ["Datetime", "Tput", "mbps"]
	```


#### v2.2: convert tput value to gb if value exsit mb type
- [Fix Issue 001]: convert tput consistency value, by check mbit unit convert to gbit type
Convert gbit log if contain mbit then convert it into gbps by divide to 1000. If some throughput didn't reach gb it will show `850 Mbits/se`, so make all value consistency to future flot
```
# Convert to Gbits/sec
transfer_value = float(transfer_str)
if unit == "M":
    transfer_value /= 1000.0  # Convert Mbits to Gbits
    data.append([formatted_date, transfer_value])
```
	- output:
	```
	#original gbits v2.0
	20250313_10:08:37	850	gbps
	# convert the value to gbps
	20250313_10:08:37	0.85	gbps
	```
	
#### v2.1: Preserve unit from log file without changing it
- [Fix Issue 002] Preserving Units according to log file, use according to the log unit. Previous Issue, gbit log might contain mbit, so need to manual check unit.  
```
 # Store the transfer value and the unit
 data.append([formatted_date, float(transfer_str), unit])
```
	- output:



#### v2.0 

- [Improvement]: LogFile will check Mbit or gbit rather assign correct log file content contain mbit or gbit.
In previous version you need to specify the correct logfile to parse correct string for specific data. in this version no matter gbit or mbit  both can help parse the `[SUM]` string. 
```	
#Parses a log file, extracts SUM lines, formats data, and writes to an Excel file.
if "[SUM]" in line:
	match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
	if match:
		date_str = match.group(1) #datetime
		transfer_str = match.group(2) #tput value
		current_unit = match.group(3)  # unit, Get the unit (M or G)	              
```
- [Issue: 002 FIX]: Dynamically sets the header for unit type(ex: mbps or gbps)
in previous version use fixed unit, so no matter mbit, or gbit always show gbps. This version solve this issue by checking unit. 
```
# Dynamically set the header
if unit == "G":
    header = ["Datetime", "Tput", "gbps"]
else:
	header = ["Datetime", "Tput", "mbps"]
sheet.append(header)
	
for row in data:
    sheet.append([row[0], row[1], header[2]])  # Write data rows with the correct unit
```

- [implement] implement write result into excel 
```
workbook = openpyxl.Workbook()
sheet = workbook.active
#write header into excel
#Gbit 
sheet.append(["Datetime", "Tput", "Gbits"])  
#Mbits
sheet.append(["Datetime", "Tput", "Mbits"]) 


for row in data:
	sheet.append([row[0], row[1], header[2]])  # Write data rows with the correct unit
workbook.save(output_excel_file)
print(f"Data written to {output_excel_file}")
```

- [output]:


#### v1: inital release
-  [New Feature] Parses a log file, extracts SUM lines with Mbits/sec or Gbit/sec, as individual parser 
The regular expression here search for datatime, and tput value, in this part it seatch for Gbit, if you want to search for Mbit, please change the string. In next version will make a better method to solve this problem. 
```
if "[SUM]" in line:
	#for gbit
	match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+) Gbits/sec", line)
	#for mbit
	match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+) Mbits/sec", line)

	if match:
		date_str = match.group(1) #get datetime
		transfer_str = match.group(2) #get tput value		
		
	else:
        print(f"Warning: Line with [SUM] did not match regex: '{line}'. Skipping.") # This line is added	
		
```

- [New Feature] Format the datetime into customize format YYMMDD_HHMMSS
```
#convert datetime to YYMMFF_HHMMSS
date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")  # Include seconds
data.append([formatted_date, float(transfer_str)])  # Store data as list	
```


- [output]:

- [Issue: 001]: The tput value is inconsistency data type, some value ub gbit will show mb(when tpt not reach will show mb)
- [Issue: 002]: The unit type is been hoted code to mbps on the last column which value is gbps, but unit show mbps. 
```
 #ex
 20250313_10:08:36	1.95 gbps
 20250313_10:08:37	850	gbps
```


### parse_mbit_excel_mbps
In above script is able to convert mbits log file from mb to gb, however in this script will obtain orginal mbits. 

> Note: This only support using Mbit log file `input_Mbits.txt`

