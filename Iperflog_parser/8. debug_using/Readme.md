# Debug For Coding 

## Description of Code
All of these feature implement into the code already, just in case wants to debug specific code, might be useful

### 1. ConvertdateFormat
This code will read `datedata.txt` this file, and convert the datetime from Day MM Date HH:MM:SS YY and convert into YYMMDD_HHMMDD
```
input_file_path = "datedata.txt"
output_file_path = "output.txt"
```

**Output:**

![conver_Datetime_format](../img/debugCode/convertdateFormat.png)

### 2. reading_parseLogFile

This script is use to reading the parsing or filter result. This is useful if you want to see which string is been capture, and it's useful for debugging code. 

- `parse_sum_line()`: Filter and capture `[SUM]` and print it out the result. This is just liek using find `[SUM]` in the log file, but instead capture the result. 
- `parse_matching_str()`: Filter `[SUM][RX-C]` and `[SUM][TX-C]` for bidirectional log file. It capture the datetime and print it. 

**Output:**

![reading_parseresult](../img/debugCode/parseResult.png)

### 3. timeduration_calculate
This code is to calculates the duration between two datetime strings. If you want to caculate the datetime of duration, you can use this code, will help you caculate date and time(convert day to hours)

User enter start and end time:
```
start_time_str= input('enter your starting date:')
end_time_str = input('enter your ending date:')
```
**Output:**

![timeduration_calc](../img/debugCode/timeduration_calc.png)