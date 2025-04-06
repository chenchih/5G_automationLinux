# parse_mbit_to_excel


## Description
This code is similar to `parse_mbit_to_gb_excel.py`, the only different is it will parse only the mbit log file, without convert data unit. In `parse_mbit_to_gb_excel.py` you will realize I will convert mbit log file to gbit, however if you want to get only the mbit you can use this code. Essentialy this code is just to parse the mbit value without convert to gbit. 

Please NOTED, this code ONLY SUPPORT mbit log file, iso in case if you use other than mbit then will throw msg and exit code. 

## Output
If you enter the logfile contain gbit will show Error telling you this code only can capture mbit logfile 
![reading_parseresult](../../img/parse_mbit_gbit/2_parse_mbit_excel_output.png)

## Code Version explanation

- v1.0: inital release
- v1.1: change outpust default file or user enter for much flexible.
- v1.2: change cpature matching string `\d{2}` to `\s+\d{1,2}` which will capture single or multiple date. 

### Capture matching string
```
match = re.match(r"(\w{3} \w{3} \d{2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM]\[(RX-C|TX-C)\].*?([\d\.]+) (M|G)bits/sec", line)
    if match:
        date_str = match.group(1)
        rx_tx = match.group(2)
        transfer_str = match.group(3)
        unit = match.group(4) #

```
![reading_parseresult_regularexpression](../../img/parse_mbit_gbit/2_parse_mbit_excel_output_reg.png)

### convert datetime from log to date format
```
try:
	date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
	formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
	transfer_value = float(transfer_str)
	data.append([formatted_date, transfer_value]) # Do not convert
except ValueError:
    print(f"Warning: Invalid data format in line: '{line}'. Skipping.")
```

### write into excel
```
def write_data_to_excel(sheet, data, unit):
    """Writes data to the Excel sheet."""
    header = ["Datetime", "Tput", "mbps"] # Always mbps
    sheet.append(header)
        for row in data:
            sheet.append([row[0], row[1], "mbps"])
            pbar.update(1)
```
### adjust width for datetime
```
#Adjusts the first column's width.
def adjust_column_width(sheet):
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

### set default output file 
```
if output_excel_file_path == '':
    output_excel_file_path = f"{filewithDate}_output_mbit_Result.xlsx"
else:
    output_excel_file_path=output_excel_file_path+'.xlsx'
```

## Summary
If you want to capture Mbit log and write into excel without convert to gbps unit, then you can use this code. In Mbit it will only get Mbit unit, so will not have issue that contain different unit type like `gb`, `mb` or `bit`. 
