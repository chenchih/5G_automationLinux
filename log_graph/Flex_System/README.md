#Description of code

## LogParse(Complete)
This is a full code, which will parse the logfile with extract result which include txt file, excel, and png file. 

- How to Run the code: `main_importmodule.py`
- Output: [output for parse log with flex system](#img/output.png)
- Step and code order: You can run individual code, or just run the `main_importmodule.py` which will import all the code at once. 
	- Step1: `main_importmodule.py` and `logchecking_rename_merge.py`: Check logfile in working directory contain 'elog_gnb_du_layer2.0'. It will rename elog file, in case you have multiple elog will write into one file and name `elog_files`  
	- Step2: : `parsefile_layer2_v3_flexCDU_dev.py`: parse log file and filter UL and DL tput value and save result into txt file
	- Step3: `convert_excel_layer2_flexCDU_dev.py`: convert txt file result into excel file
	- Step4: `plot.py`: plot the excel file result into line graph
	- Step5: `main_importmodule.py`: wrap up all result into folder
	
## Code explaination

### Read elog file and filter tput value

- Filter UL TPUT data
```
import re 
with open('elog_gnb_du_layer2.0', 'r') as filedata:
    for line in filedata:   
        if 'U-UE' in line:
            search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^A]+)', line)
            print(search.group(2))   
```
- User enter filter type UL DL or both
Select the traffic string you want to parse, UL DL or both traffic. 
```
accepted_strings = re.compile(r"^(D-UE|U-UE)(\[\d\]|\[ \d\])?$|^both$")
givenString = input("Please enter your search (Ex: D-UE / U-UE/ U-UE[ 0] / both:):")
if accepted_strings.match(givenString):
        if givenString =="both":
            UL = 'U-UE'
            DL = 'D-UE'
            writefile("UL")
            ULDLprint(UL)
            writefile("DL")
            ULDLprint(DL)
        else:        
            writefile(givenString)
            with open(elogfileName, 'r') as filedata:
                for line in filedata:   
                    if givenString in line:
						# Print the line, if the given string is found in the current line
                        #print(line.strip())
                        parse(line, givenString)
else:
    print("Not found, please reenter correct option") 		
```

### analysic the related string 

- parse the data:
```
datestr = data.split('[', 1)[1].split(']')[0]  
search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^A]+)', data)
m3New = re.sub(r"[\(\[].*?[\)\]]", "", search.group(2)).replace('=', '= ').replace(',', ' ').strip().split()
result.clear()
```
- save the value into list 
```
givenString=ULDLstr
bler="Bler="
result.append(datestr)    
result.append(getelement(m3New, 'Tput='))
result.append(getelement(m3New, 'RB='))
result.append(getelement(m3New, 'Mcs='))
result.append(getelement(m3New, bler))
listprint() 
```

- write into file
```
def listprint():
    #checkfile()
    cycle = 0        
    with open(filename, "a") as f:
        for element in result:            
            f.write(element+ " ")     
        f.write("\n")
```


