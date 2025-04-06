# Debug For Coding 

## Description of Code
These two codes all can parse the logfile and write the  result into text file. In case if you don't want to display in Excel, and want to use text file, you can run this code. 

- `parser_result_txt`: write the result into a text file
- `parser_txt_excel_convert`: write the result into a text, or Excel or both file. 

### parser_result_txt

**Description:**
Parses the input log file, extracts date and units from `[SUM]` lines, and writes the results to the output file.
Dynamically sets the header based on the units found in the file, and perserve the log unit, which mean bit will become bit,  gbit will become gbit and so on

**output:**
This support both mbit or gbit log file, so you can enter both mbit logfile or gbit logfile, it will work. 

![txt_parsing_output](../img/parser_result_txt_output.png)

#### Code Explanation
- Parse log file
```
if "[SUM]" in line:
	match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (bits|Mbits|Gbits)/sec", line)
        if match:
            date_str = match.group(1)
            transfer_str  = match.group(2)
            current_unit = match.group(3)  # Get the unit (M or G)
```

- Convert datetime format
```
date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
data.append([formatted_date, transfer_str, current_unit])
```
- Write capture result into txt file
```
if data:
	header = "timedate\tTput\tUnit\n" 
	with open(output_file, 'w', encoding='utf-8') as outfile:
        #outfile.write("timedate\tmbps\n")
        outfile.write(header)
            for row in data:
                outfile.write(f"{row[0]}\t {row[1]}\t {row[2]}\n")
	print(f"Data written to {output_file}")
```

- main code, default save file name, or user enter perfer filename
```
input_file_path= input('Please enter log file name: ')
output_file_path = (input('save exel file name (enter for default) : ') )
if output_file_path == '':
    output_file_path = f"output_txtfile.txt"
else:
    output_file_path=output_file_path+'.txt'
process_log_file(input_file_path, output_file_path)
```
### parser_txt_excel_convert
**Description:**
This code allow you to capture and write into different file type, txt,excel or both. If you enter neither txt or excel, or both it will display error telling wrong type. 
It also support both type mbit or gbit log file. 

- adding adjusting time column 
- log file other mbit will throw error and exit 
- add `\\s+\\d{1,2}` to matching
- allow user to add output file ext type, exel txt or both
- support both mbit and gbit

**output:**
![txt_parsing_output](../img/parser_txt_excel_convert_output.png)

#### Code explanation

- capture result and write into txt file
```
def write_data_to_txt(data, output_file):
    if data:
        try:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write("timedate\tTPUT\tunits\n")
                for row in data:
                    outfile.write(f"{row[0]}\t {row[1]}\t {row[2]}\n")
            print(f"Data written to {output_file}")
        except Exception as e:
            print(f"An error occurred while writing to text file: {e}")
    else:
        print("No data to write to text file.")
```
- capture result and write into excel file
```    
def write_data_to_excel(data, output_file):
    if data:
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["timedate", "TPUT","Unit"])  # Header row
            
            for row in data:
                sheet.append(row)
            adjust_column_width(sheet)
            workbook.save(output_file)
            print(f"Data written to {output_file}")
        except Exception as e:
            print(f"An error occurred while writing to Excel file: {e}")
    else:
        print("No data
```