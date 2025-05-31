# Record Diffferent version code

## Parse Elog 

### v1. without progress bar, and user enter Throguhput value
This code will not display progress bar while it's parsing logfile and write result
- **File**: `parsefile_layer2_flexDU_v1.py`
**Output:** 
```
$py parsefile_layer2_flexDU_v1.py
Please enter your elog FileName: elog_gnb_du_layer2.0
####press any key, q to exit script#####:
Please enter your search (Ex: D-UE / U-UE/ U-UE[ 0] / both:):D-UE
####press any key, q to exit script#####: q
PS D:\demoexample\Standalone_DebugCode>
```
### v3: implement progress bar when parsing
- **File**: `parsefile_layer2_v3_flexCDU_userinput.py`: User enter filter TPUT
User can decide to capture UL, DL or both, however if capture UL or DL it will only contain one tput result in a txt file, wither UL or DL. IF choose both will capture both UL and DL result. 

**Output:**
```
py parsefile_layer2_v3_flexCDU.py
####press any key, q to exit script#####:
Please enter your elog FileName: elog_gnb_du_layer2.0
Please enter your search (Ex: D-UE / U-UE/ U-UE[ 0] / both:): D-UE
Processing D-UE: 100%|████████████████████████████████████████████████████████| 90169/90169 [00:01<00:00, 59981.71it/s]
####press any key, q to exit script#####: q
```

- **File** `parsefile_layer2_v3.2_flexCDU.py`: Capture both UL and DL
After investivate the elog, relazie we can capture both UL and DL, if one is not running it will just obtain `0` so overall capture both value will a better choice.

The result will contain ULand DL in one txt file

**Output:**
```
$py parsefile_layer2_v3_flexCDU_dev.py
elog_gnb_du_layer2.0
Processing U-UE: 100%|████████████████████████████████████████████████████████| 90169/90169 [00:01<00:00, 61250.00it/s]
Processing D-UE: 100%|████████████████████████████████████████████████████████| 90169/90169 [00:01<00:00, 59851.37it/s]
PS D:\demoexample\Standalone_DebugCode>
```
## Convert UL and DL Result into excel
- **File**: `excel_layer2_sheet_v2_progress_type_2multipletask.py`

**Output:**
```
$py excel_layer2_sheet_v2_progress_type_2multipletask.py
please enter your txt file name (Ex: test.txt): result-2025-05-30-17-21-48.txt
please enter saving excel file name (Ex: test): test
Processing UL and DL: 100%|███████████████████████████████| 25731/25731 [00:00<00:00, 706024.66it/s]
Writing Excel: 100%|██████████████████████████████████████████████████| 4/4 [00:01<00:00,  2.65it/s]
```

## Test function and debug 
- `debugTest_file_moving.py`: use for implement for file moving to folder
- `debugTest_checkfile_ext.PY`: use for implment checking file extenction type
- `debugTest_readfile.py`: debuging that allow to read elog and capture result

### Check File type

#### check file endswith 
```
matching_files = [file for file in os.listdir() if file.endswith('.html')]
print(matching_files)

```
#### check if file or directory exist, return bool
```
os.path.isfile('filename.txt')
os.path.isdir('foldername')
```

#### check file ext type
```
#using os and fnmatch  
def checking_file_1(file):
	# Filter files that are regular files and match the patterns
	matching_files = [
    file for file in os.listdir() 
    if os.path.isfile(file) and any(fnmatch.fnmatch(file, pattern) for pattern in patterns)
	]
	#print(matching_files)
	return matching_files

#using glob or endwith
def checking_file_2(file):
	matching_files = [file for pattern in patterns for file in glob.glob(pattern)]
	#matching_files = [file for file in os.listdir() if file.endswith('.html')]
	return matching_files

#os and fnmatch
def check_excel_files(): #has_excel_files(directory=".")
	#Check if the directory contains any Excel files.
    excel_extensions = ('.xlsx', '.xls', '.xlsm')
    #with any
    return any(fnmatch(file, pattern) for file in os.listdir(directory) for pattern in patterns)
    '''
    #without any
    found = False
    for file in os.listdir(directory):
        for pattern in patterns:
            if fnmatch(file, pattern):
                found = True
                break  # Stop checking other patterns for this file
        if found:
            break  # Stop checking other files
    return found
    '''
	
patterns = ['*.html','.txt']
result=checking_file_1(patterns)
print(result)

result= checking_file_2(patterns)
print(result)

if check_excel_files():
#if has_excel_files():
    print("Excel files found in the directory.")
else:
    print("No Excel files found.")
	
	

```
#### remove file
```
def remove_file_endwith():
    filetype='.html'
	for file in os.listdir():
        #if file.endswith((".xls", ".xlsx")):
		if file.endswith(filetype):
			os.remove(file)  
            #return True  
    #return False
    
def remove_file_pattern():
    patterns = ['*.xlsx', '*.xls', '*.xlsm']
    # Loop through all files in the current directory
    for file in os.listdir():
        if any(fnmatch.fnmatch(file, pattern) for pattern in patterns):
            print(f"Deleting {file}")
            #os.remove(file)  # Remove the file
#remove_file_endwith('.html')
remove_file_pattern()
list_direcrtory()
```



#### list file pattern 


#### list exclude file pattern

```
# Define patterns to exclude
exclude_patterns = ['*.py', '__pycache__']

matching_files = []
for file in listfiles:
    # Check if the file matches any of the exclude patterns
    exclude = False
    for pattern in exclude_patterns:
        print(f"Checking file '{file}' against pattern '{pattern}'")
        if fnmatch.fnmatch(file, pattern):
            exclude = True
            print(f"File '{file}' matches pattern '{pattern}', excluding.")
            break  # No need to check other patterns, skip this file
    if not exclude:
        matching_files.append(file)  # Add to matching_files if not excluded

```

you can also use this: 
```
# Filter files that do not match the exclude patterns
matching_files = [
    file for file in listfiles 
    if not any(fnmatch.fnmatch(file, pattern) for pattern in exclude_patterns)
]

```