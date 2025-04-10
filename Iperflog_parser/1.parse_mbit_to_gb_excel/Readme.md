# parse_mbit_excel

Parses a log file, extracts all SUM lines, formats the date and transfer data, and writes the results to an output file.

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

## Output
![reading_parseresult_gbit](img/parse_mbit_gbit/v3.1.PNG)


## Code Version explanation

| version | Type | Status |Description|
| :--: | :-- |:--:|:--:|:--|
|1|**Release**|-|inital release user have to enter correct input log|
||Issue-001|BUG|only able to capture one ddata type(mbit and bit not been capture)|
||Issue-004|BUG|Will not capture date with one digit|
||Target-001|	To DO|	code need to manual change mbit or gbit when parse log file|
||Target-002|	To DO|	Adding Header |
|2|**Release**|-|Parse result and write into excel|
||-|New Feature|Write Result to excel|
||Issue-001|Improvement/BUG|can capture mbit data in gbit log|
||Issue-002|BUG|mbit log the unit show incorrrect|
||Issue-003|BUG|Value is inconsistecy some are gbit some are gbit|
||Target-001|Improvement|code need to manual change mbit or gbit when parse log file|
||Target-002|Improvement|Adding Header|
||Target-003|To-Do|Excel timedate column width need to be adjust|
|2.1|**Release**|-|preserving the original units from log file, formats data, and writes to an Excel file|
||Issue-002|Resolve|mbit log the unit show incorrrect|
||Issue-003|BUG|Value is inconsistecy some are gbit some are gbit|
||Issue-001|BUG|only able to capture one ddata type(mbit and bit not been capture)|
|2.2|Release|-| convert value to consitency and add progress bar|
||Issue-001	|Resolve|only able to capture one ddata type(mbit and bit not been capture)|
||Issue-002|Resolve|mbit log the unit show incorrrect|
||Issue-003|Resolve|Value is inconsistecy some are gbit some are gbit|
||-	|New Feature|	Implement progress bar|
||Target-003|	Improvement	|Excel timedate column width need to be adjust|
|2.3|Release|-|wrap up feature in to function, for better readable and manage|
||Target-004|	Improvement	|Implement user to enter their logfile, and save filename|
|3|**Release**|-|Fixing date with space and one or two date|
||Issue-004|	*Resolve*	|New Feature	calculate test start and end time |
||-|New Feature	|implment default output file, or user enter file name|
||-|New Feature	|calculate test start and end time |

<a name="toc"></a>
### Version List 
- [V3: Create default output filename contain datetime and logfile if contain mbit or gbit related str](#v3)
	- [[Fix Issue-004] Capture date with space for single date](#v3_fix003)
	- [[NEW] Set default output save file ](#v3_fix003_New)
- [V2.3: wrap up each feature into individual function](#v2.3)
	- [[Improvement] wrap up each feature into individual function](#v2.3_wrap_feature_function)
	- [[Improvement] Implement user to enter log filename](#2.3_user_enter_logfile)
- [v2.2 convert tput value to consistency type](#v2.2)
	- [[Fix Issue-001] parsing log file and cpature Mbit and Gbit](#v2.2_fixissue-001)
	- [[Fix Issue-003] convert tput value to gbit](#v2.2_fixissue-003)
	- [[Improvement Target-003] Adust column width](#v2.2_improvement_target-003)
	- [[Improvement Target-004] adding progress bar](#v2.2_improvement_target-004)
	- [ISSUE and Summary](#v2.2_summary)
- [V2.1](#v2.1):
	- [[NEW]Write result into excel](#v2.1_writeExcel)
	- [ISSUE and Summary](#v2.1_issue_summary) 
- [v2: parse logfile and write result to excel](#v2)
	- /ISSUE-001] parsing log file and capture Mbit and Gbit](#v2_issue001)
	- [[Target-002 improvement ] Dynamically sets the header for unit type(ex: mbps or gbps)](#v2_target002)
	- [New] Write result into excel(#v2_writeexcel)
	- ISSUE and Summary(#v2_summary)
- [V1 : inital parse logfile and write result to txt](#v1)
	- [[NEW] parsing log file and capture](#v1_new_parse)
	- [[NEW] convert the datetime format](#v1_convertdatetime)
	- [ISSUE and Summary](#v1_issuesumamry)

<a name="v3"></a>
### v3 Create default output filename contain datetime and logfile if contain mbit or gbit related str [🔝](toc)

In this version I just clean up the code, like user enter log file, save output file with default name, and fix issue-004. 


- Feature in v3:
	- Fixe issue-004
	- Implement default output excel filename
	
	
![v3.0_parse_mbit_gbit](../img/v3.PNG)

<a name="v3_fix003"></a>
#### [Fix Issue-004] Capture date with space for single date[👈](#v3)

If your date contain one date like Apr 1, then using previous regular expression argument `\d{2}` will not work. It only can capture date with two digit like Apr 11, however in our logfile it contain two type of date Apr 1, and Mar 31. In order to capture both string, need to add `\s+\d{1,2}` to fix this issue

```
if "[SUM]" in line:
match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (bits|Mbits|Gbits)/sec",line)
    if match:
        date_str = match.group(1)
        transfer_str = match.group(2)
        unit = match.group(3)
	.....
```
![v3_regularExpression](../img/v3_reg.PNG)


- `\s+`: one or more whitespace characters`
- `\d{2}`: specifically looks for exactly two digits.
- `\d{1,2}`: is more flexible and looks for either one or two digits.


<a name="v3_fix003_New"></a>
#### [NEW] Set default output save file  [👈](#v3)
This code generates a default output Excel filename based on the current date and time. It also checks the content of the input log file to determine if it contains 'mbits' or 'gbits' and includes this information in the filename.

- add default output save file
```
now = datetime.now()
filewithDate=now.strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS

file_content = input_file_path.lower()
if 'mbits' in file_content or 'mbps' in file_content: #add mbps
    filelog='mbitLog'
elif 'gbits' in file_content or 'gbps' in file_content: #add gbps
    filelog='gbitLog'
else: 
    filelog=''

if output_excel_file_path == '':
    output_excel_file_path = f"{filewithDate}_mbit_convert_output_gbit_{filelog}_Result.xlsx"
else:
    output_excel_file_path=output_excel_file_path+'.xlsx'

```
![v3.1_parse_mbit_gbit](../img/v3_outputfile.PNG)

<a name="v2.3"></a>
### v2.3 wrap up each feature into individual function  [🔝](toc)
In this version I just wrap up each feature into function which will be easier to manage or read. 

- Feature in v2.3:
	- wrap each feature into individual function
	- Implement user to add their logfile and save result name

![v2_parse_mbit_gbit](../img/v2.3.PNG)

<a name="v2.3_wrap_feature_function"></a>
#### [Improvement] wrap feature to function [👈](#v2.3)
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
<a name="v2.3_user_enter_logfile"></a>
#### [Improvement] Implement user to enter log filename [👈](#v2.3)
```
input_file_path= input('Please enter log file name: ')
output_excel_file_path = (input('save file name: ') +'.xlsx')

process_log_file_to_excel_combined(input_file_path, output_excel_file_path)
```

<a name="v2.2"></a>
### v2.2 convert tput value to consistency type  [🔝](toc)
In 2.1 the unit I use perserve the logfile's unit, however it seem like it's not a great method. As you can see if it didn't reaches gbit, it will display mbit or even bit. If lof is so big it hard to realize mbit is hidden inside. THe best solution is to convert all the tput value into gbit. This mean if it occur mbit or bit, then it will convert it into gbit. This all the unit will be consistency, and this will be easier in future if you need to plot to graph.P  Please refer below picture for what I mean, you can see the Mbit is burry in, you need to filter out. 
![v2.1_parse_mbit_gbit](../img/v2.1_solution.PNG)

**output:** Below is the output for v2.2 version.	
![v2_parse_mbit_gbit](../img/v2.2.PNG)


- Feature in v2.2:
	- convert tput to gbit, all value will be consistency unit
	- Adjusts the datetime column width. 
	- Able to capture bit 
	- Adding porgress bar to show it process something
<a name="v2.2_fixissue-001"></a>
#### [Fix Issue-001] parsing log file and cpature Mbit and Gbit [👈](#v2.2)
```
if "[SUM]" in line:
	#v2.2
	match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (bits|Mbits|Gbits)/sec",line)
    if match:
		date_str = match.group(1)
        transfer_str = match.group(2)
        unit = match.group(3)
		........
```

Resolve Issue-001, by adding `(bits|Mbits|Gbits)/sec` can capture bit or gbit or mbit

![v2_parse_mbit_gbit](../img/v2.3_reg.PNG)

<a name="v2.2_fixissue-003"></a>
#### [Fix Issue-003] convert tput value to gbit[👈](#v2.2)
This is a better solution instead of using perserve logfile unit, I check if unit are mbit or bit, then convert the tput to gbit. 

Convert gbit log if contain mbit then convert it into gbps by divide to 1000. If some throughput didn't reach gb it will show `850 Mbits/se`, so make all value consistency to future flot

```
v2.2 convert mbit and bit to gbit                                    
if unit == "Mbits":
	transfer_value /= 1000.0
elif unit == "bits":
	transfer_value /= 1000000000.0    
```

**output:**
```
#original gbits v2.0
20250313_10:08:37	850	gbps
# convert the value to gbps
20250313_10:08:37	0.85	gbps
```

<a name="v2.2_improvement_target-003"></a>
#### [Improvement Target-003] Adust column width [👈](#v2.2)
I adjust the width of the first column which store the datetime.
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
```
<a name="v2.2_improvement_target-004"></a>
#### [Improvement Target-004] adding progress bar [👈](#v2.2)
If you load a big file, running the scrip it will not show anything, it will only show outfile after it finshed write into file. But during these period nothing is showing, to solve this issue I added a progress bar to show user that it's process something.

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
<a name="v2.2_summary"></a>
#### ISSUE and Summary [👈](#v2.2)

- [Known issue]
	- [Resolve] ~~Issue-001:~~: It can parse both gbit and mbit, but bit not able capture
	- [Resolve] ~~Issue-003~~: Value is inconsistecy some are gbit some are gbit tput value like (850 mbit, and 1.95 gbit)
	![v2.2_parse_mbit_gbit_resolve](../img/v2.2_resolve.PNG)

- [Improvement]
	- Target-003: Excel timedate column width need to be adjust width
	- Target-004: Adding progress bar
	![v2.2_parse_mbit_gbit](../img/v2.2_target.PNG)
	

<a name="v2.1"></a>
### v2.1 [🔝](toc)
Preserving Units according to log file, use according to the log unit. Previous Issue, gbit log might contain mbit, so need to manual check unit. The solution for the unit column perserve the same unit from the logfile. In v2.0 we use fixed unit Gbit or Mbit like below:
````
#fixed
sheet.append([row[0], row[1], "Gbits"])  # Write data rows with Gbit
sheet.append([row[0], row[1], "Mbits"])  # Write data Mbit

#use the log file correct unit, this version will use this one
sheet.append([row[0], row[1], header[2]])  # Write data rows with the correct unit, using log unit
````
- Feature in v2.1:
	- remove checking unit, write static header 
	- use the logfile unit without 


**output:** Below is the output for v2.1 version. 
![v2.1_parse_mbit_gbit](../img/v2.1_output.PNG)




<a name="v2.1_writeExcel"></a>
#### [NEW]Write result into excel [👈](#v2.1)
Modify the sheet for unit, perserve the unit from logfile. Remove check mbit or gbit before write into header
```
#original and remove these
if unit == "G":
    header = ["Datetime", "Tput", "gbps"]
else:
    header = ["Datetime", "Tput", "mbps"]
sheet.append(header) 
	
for row in data:
		#sheet.append([row[0], row[1], header[2]])  # Write data rows with the correct unit, using log unit
		sheet.append([row[0], row[1], "Gbits"])  # Write data rows
		#sheet.append([row[0], row[1], "Gbits"])  # Write data rows
		
# new version, static header and perserve unit from logfile 
sheet.append(["Datetime", "Tput", "Units"])  # Header row
	for row in data:
        # Write data rows, preserving the original unit
        sheet.append([row[0], row[1], f"{row[2]}bits"])
    workbook.save(output_excel_file)
```

**output:**   
```
#mbits
20250310_19:24:46	2373	Mbits	
#gbits
20250313_10:05:16	2.37	Gbits
```
<a name="v2.1_issue_summary"></a>
#### ISSUE and Summary[👈](#v2.1)
- [Known issue]
	- [Resolve] ~~Issue-002~~: mbit log the unit show incorrrect
	![v2.1_resolve_parse_mbit_gbit](../img/v2.1_resolve.PNG)
	- Issue-001: It can parse both gbit and mbit, but bit not able capture
	- Issue-003: Value is inconsistecy some are gbit some are gbit tput value like (850 mbit, and 1.95 gbit)
	- Issue-004: The date contain one digit will not be able to capture, so you can see April 2, the 2 is not been capture	
- [To-DO]
	- Target-003: Excel timedate column width need to be adjust width
	- Target-004: Adding progress bar
	
	

<a name="v2"></a>	
### v2 parse logfile and write result to excel [🔝](toc)

Parses a log file, extracts SUM lines, formats data, and writes to an Excel file. 

**output:** Below is the output for v2 version. 

![v2_parse_mbit_gbit](../img/v2_output.PNG)

- Feature in v2.0:
	- Write result into excel file
	- adding header by checing unit type
	- capture both Mbit and Gbit 
	
<a name="v2_issue001"></a>	
#### [Improvment/ISSUE-001] parsing log file and capture Mbit and Gbit [👈](#v2)
In previous version you need to specify the correct logfile to parse correct string for specific data. In this version no matter gbit or mbit  both can help parse the `[SUM]` string.
Note: This issue not fully fix just can capture both Mbit or Gbit, due to  I had realize bit is not been capture so this is not fully fix. 

To parse Mbit and gbit you have to change the regular express mathing argument like `(M|G)bits/sec` picture show as below: 

> - Fix: (M|G)bits=>capture both M or G its

![v2_parse_mbit_gbit](../img/v2_regImprove.PNG)

```
if "[SUM]" in line:
	#v2.0
	match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
		if match:
			date_str = match.group(1)
            transfer_str = match.group(2)
			#v2.0
            current_unit = match.group(3)  # Get the unit (M or G)
```
<a name="v2_target002"></a>	
#### [Target-002 improvement ] Dynamically sets the header for unit type(ex: mbps or gbps)[👈](#v2)
in previous version use fixed unit, so no matter mbit, or gbit always show gbps. This version solve this issue by checking unit. 
```
# Dynamically set the header
if unit == "G":
    header = ["Datetime", "Tput", "gbps"]
else:
	header = ["Datetime", "Tput", "mbps"]
```

<a name="v2_writeexcel"></a>	
#### [New] Write result into excel [👈](#v2)
```
import openpyxl
.....
if data:
	workbook = openpyxl.Workbook()
    sheet = workbook.active
	#Dynamically set the header
	
	sheet.append(header)
    for row in data:
		#sheet.append([row[0], row[1], header[2]])  # Write data rows with the correct unit, using log unit
		sheet.append([row[0], row[1], "Gbits"])  # Write data rows
		#sheet.append([row[0], row[1], "Gbits"])  # Write data rows
		
	workbook.save(output_excel_file) #save excel 
```

<a name="v2_summary"></a>	
####  ISSUE and Summary [👈](#v2)
In this v2 version I have implment write into excel instead of using txt.

- [issue]
	- Issue-001: It can parse both gbit and mbit, but bit not able capture
	- Issue-002: mbit log the unit show incorrrect
	- Issue-003: Value is inconsistecy some are gbit some are gbit tput value like (850 mbit, and 1.95 gbit)
	```
	 20250313_10:08:36	1.95	gbps
	20250313_10:08:37	850	gbps
	```
	- Issue-004: The date contain one digit will not be able to capture, so you can see April 2, the 2 is not been capture	
	![v2_parse_mbit_gbit](../img/v2_issue.PNG)


- [Improvement]
	- Target-001: No need to idential change the matching argument, it can capture Gbit and Mbit, solution as below using `(M|G)bits/sec`
	```
	match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)                     
	```
	![v2_parse_mbit_gbit](../img/v2_regImprove.PNG)
	
	- Target-002: Header is been implement in Excel file
	```
	#sheet.append([row[0], row[1], header[2]])  # Write data rows with the correct unit, using log unit
    sheet.append([row[0], row[1], "Gbits"])  # Write data rows with Gbit
    #sheet.append([row[0], row[1], "Mbits"])  # Write data Mbit
	```

- [To-DO]
	- Target-003: Excel timedate column width need to be adjust width


<a name="v1"></a>
### v1 inital parse logfile and write result to txt  [🔝](toc)
Parses a log file, extracts SUM lines, formats data, and writes to an Txt  file. You have to manually add the logfile and matching argument, and write result into txt file. . Overall it's not efficiently, and flexiblity. In future version will fixe many issue, and improve some feature. Please go to summary section in v1, to see the issue and need to improvement. 

**output:** Below is the output for v1 version. 

![v1_parse_mbit_gbit](../img/v1_output.PNG)

<a name="v1_new_parse"></a>
####  [NEW] parsing log file and capture [👈](#v1)
```
try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if "[SUM]" in line:
				#matcing 
				match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+\.\d+) GBytes", line)
				if match:
                    date_str = match.group(1) #datetime
                     transfer_str = match.group(2) #tput value
					.....

			#not match will print
            else:
                print(f"Warning: Line with [SUM] did not match regex: '{line}'. Skipping.") 
``` 
- parse gbit and mbit

User have to put the correct logfile, due to the matching argument wlll match the logfile content like Gbytes, and Mbit

```
#matching argument 
#for gbit log
match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+\.\d+) GBytes", line)

input_file_path = "input_Gbits_Short.txt"  # Replace with your input file path
output_file_path = "output.txt" # Replace with your output file 


#parse mbit log
#match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+) Mbits/sec", line)
input_file_path = "input_Mbits_Short.txt"  # Replace with your input file path
output_file_path = "output.txt" # Replace with your output file 
```
<a name="v1_convertdatetime"></a>
#### [NEW] convert the datetime format  [👈](#v1)

It will convert th elog file date format `Wed	Apr	2	15:42:24	2025` to `20250402_15:42:24`. You can manual use the `convertdateFormat.py` under `8. debug_using` which have same effect. 
```
if match:
	date_str = match.group(1) #datetime
	#convert the date format
	date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
	formatted_date = date_obj.strftime("%Y%m%d_%H:%M")
	outfile.write(f"{formatted_date} {transfer_str}\n")
```

output convert format:
```
#original
Wed	Apr	2	15:42:24	2025
Wed	Apr	2	15:42:25	2025
Wed	Apr	2	15:42:26	2025

#convert to specific format 
20250402_15:42:24
20250402_15:42:25
20250402_15:42:26
```
<a name="v1_issuesumamry"></a>
#### ISSUE and Summary  [👈](#v1)

- [ISSUE]: 
	- 001: THe Mbit andf bits is not been capture. When run iperf if not reach Gbit, it might drop to Mbit or bit. In this case if it drop, my reg argument not been capture. 
	- 004: The date contain one digit will not be able to capture, so you can see April 2, the 2 is not been capture	
	
Please refer below picture for more detail, which I had marked the issue part: 
![v1_parse_mbit_gbit](../img/v1_issue.PNG)

- [Improvement]: 
	- **Target-001**: Need to manually add mbit or gbit, you have to add th idential logfile with the same gbit or mbit match argument. This is not flexiblity user have to enter correct logfile, and check the correct matching argument mbit or gbit.
	```
	#gbit
	match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+\.\d+ Gbits/sec)", line)
	input_file_path = "input_gbits_Short.txt"
	#mbit
	match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?(\d+\.\d+ Mbits/sec)", line)
	input_file_path = "input_gbits_Short.txt"
	```
	- **Target-002**: Output txt file, seem like not header is not added 
	```
	20250313_10:04 2.30 Gbits/sec
	20250313_10:04 2.38 Gbits/sec
	20250313_10:04 2.37 Gbits/sec
	20250313_10:04 2.37 Gbits/sec
	```