# Iperf Log parser and convert result

This is an aumtiomation on parse or filter iperf3 log file and write the Throughput into excel or txt file. 

The Iperf3 log might look like this in file:

- Filename: `input_Gbits.txt` use for run throughput log
	- > `Thu Mar 13 10:04:38 2025 [SUM]   7.01-8.01   sec   283 MBytes  2.37 Gbits/sec  `
- Filename: `input_Mbits.txt` use for stability test log
	- > `Mon Mar 10 18:47:06 2025 [SUM]   0.00-10.00  sec  2.76 GBytes  2368 Mbits/sec`

As you can above log, I will get the Datetime, Throgput value `2.37 Gbits/sec` or `2368 Mbits/sec`

## Updated record 
- 2025.3.16: inital 


## Python File explanation 

- `parse_gbps_toexcel.py`: used to parse log file (support gbit) and export mbit anf gbit unit to excel file
	- v3.1: wrap each function(parser, adjust column width, progress bar..etc) into function
	- v3.0: adding progress loading bar
	- v2.2: using correct unit type by covert mbps unit o gbit unit 
	- v2.1: unit type use according file
	- v2.0: unit type hoted coded
- `allFile_excelsheet.py`: parse all log file in directory and write into excel sheet name as filename. 
	- use for multiple file parser(throughput)
- `Date_convert\convertdateFormat.py`: Convert datetime `Mon Mar 10 18:47:06 2025` to correct format.
- `parser_result_txt.py`: use to parse log file and export to txt file. 
- `debug_code_test.py`: use for debug code
- `parse_mbit_toexcel.py`: used to parse log file(support mbit and gbit) and export excel file
- `txt_excel_convert.py`: used to parse log file (support mbit) can export txt ot excel

Please use `parse_gbps_toexcel.py` or `allFile_excelsheet.py` these two log will export to excel file. 

| FileName | Mbit | Gbit |excel|txt|Remark|
| :-- | :--: |:--:|:--:|:--:| :--|
|parse_gbps_toexcel.py | V  | V | V | X |*major|
|allFile_excelsheet.py| V  | V | V | X |*major|
|convertdateFormat.py| X  | X | X | X |minor|
|parser_result_txt.py| V  | V | X | V |minor|
|txt_excel_convert.py| V  | X| V  | V |minor|
|parse_mbit_toexcel.py| V  | V | V | X |minor|
|debug_code_test.py| V  | V | X | X |Debug Use|

## Code Explantion on function
- parser regular expression:

```
re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
#get the Mbit or Gbit
```

- Dynamically set the header with `gbps` or `mbps` based on the unit found in the file.
```
#regular expression matching:
match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (M|G)bits/sec", line)
....
current_unit = match.group(3)  # Get the unit (M or G)

# Set the unit if it's the first time we encounter it
if unit is None:
    unit = current_unit

# Dynamically set the header
if unit == "G":
    header = ["Datetime", "Tput", "gbps"]
else:
   header = ["Datetime", "Tput", "mbps"]
sheet.append(header)

for row in data:
    sheet.append([row[0], row[1], header[2]])  # Write data rows with the correct unit

```

- Adjust the width of first column
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

- Write file into excel and delete default worksheet 

```
#file: allFile_excelsheet.py
# Delete the default sheet if it exists
if "Sheet" in workbook.sheetnames:
	del workbook["Sheet"]
```
