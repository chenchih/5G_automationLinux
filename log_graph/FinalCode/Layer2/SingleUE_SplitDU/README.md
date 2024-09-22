## Description of code

### Part 1 parsing DATA from a file and write into text file 

#### Filter DL or UL
```
accepted_strings = re.compile(r"([DU]L\-\ UE(\[\s*(\d{1,2})\])?)|both$")
givenString = input("Please enter your search (Ex: DL- UE / UL- UE / UL- UE[ 0] / both:):")
```
So this is an option to parse either option is available:
> allow to parse `UL- UE` for UL 
> allow to parse `UL- UE[ 0]` for UL specfic ID with space
> allow to parse `UL- UE[10]` for UL specfic ID without space
> allow parse `DL- UE` for DL and ID same as above
> allow parse `both`

Let me show you example:
```
import re
accepted_strings = re.compile(r"([DU]L\-\ UE(\[\s*(\d{1,2})\])?)|both$")
#accepted_strings = re.compile(r"([DU]L\-\ UE(\[\ {0,1}(\d)\])?)|both$")
print (accepted_strings.match("DL- UE"))
print (accepted_strings.match("UL- UE"))
print (accepted_strings.match("UL- UE[ 0]"))
print (accepted_strings.match("UL- UE[10]"))
print (accepted_strings.match("UL- UE[ 10]"))
```
> `output:`
>>　<re.Match object; span=(0, 6), match='DL- UE'>
>>　<re.Match object; span=(0, 6), match='UL- UE'>
>>　<re.Match object; span=(0, 10), match='UL- UE[ 0]'>
>>　<re.Match object; span=(0, 10), match='UL- UE[10]'>
>>　<re.Match object; span=(0, 11), match='UL- UE[ 10]'>

what if I change to 
> `accepted_strings = re.compile(r"([DU]L\-\ UE(\[\ {0,1}(\d)\])?)|both$")`
> `output:`
>>　<re.Match object; span=(0, 6), match='DL- UE'>
>>　<re.Match object; span=(0, 6), match='UL- UE'>
>>　<re.Match object; span=(0, 10), match='UL- UE[ 0]'>
>>　<re.Match object; span=(0, 10), match='UL- UE[10]'>
>>　<re.Match object; span=(0, 11), match='UL- UE[ 10]'>

The last two item is not able to find the ID. So in order to fliter the ID we need to use the first patter

#### get the timedate and the value
The best way is to use regular expression 

- Example1: get the ingress TPUT only
The best way is to use regualr expression, i will show with regular expression and without
```
#regular expression
data= "[20230213.174340.880897][info]:[[40;32m>>> DL- ingress traffic: 0.000364(Mbps), egress traffic: 0.000527(Mbps), ReTx: 0.000111(Mbps)[0m]"
datestr = data.split('[', 1)[1].split(']')[0]
Tput = data.split(" DL- ingress traffic:", 1)[1].split(',')[0].split('(')[0].strip()
print(Tput) 

#without regualr expression
subString = data.split("Tput= ", 1)[1]
TPUT=subString.split(',')[0]
TPUT=TPUT.split(' ')[0]
TPUT
```
> `output:` 
>> `0.000364 `
`NOTE:` This example only parse DL ingress traffic, if you wants UL then change to `3mUL <<<- ingress traffic`

- Example2: get all relate value, timedate, tput, mcs, r, bler, and etc
```
data= "[20230213.174340.880929][info]:[DL- UE[ 0]: Tput=    0.000364 Mbps, Mcs=  9.0(Sigma= 0.0), RbNum=   4.2, ReTxRatio=  11.1, Layers= 1.0, PdschBler=   0.0, nonWPdschBler=  11.1]"
datestr = data.split('[', 1)[1].split(']')[0]  
search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^]]+)', data)
m3New= re.sub("[\(\[].*?[\)\]]", "",search.group(2)).replace(',','').strip().split()
print(datestr)
print(m3New)
```
> `output:`
>> `20230213.174340.880929`
>> `['Tput=', '0.000364', 'Mbps', 'Mcs=', '9.0', 'RbNum=', '4.2', 'ReTxRatio=', '11.1', 'Layers=', '1.0', 'PdschBler=', '0.0', 'nonWPdschBler=', '11.1']`

#### save the value into list 
- getelement: this function will get the next string, which is pretty useful
I wants to save the Tput value into list, the next value next to `Tput=` string. 
Since in above I already split all the string, now I just need to get the TPUT's next string which is the value and save to list. 

```
def getelement(li, element):
    ind = li.index(element)
    return li[ind+1]
```

- bler1 and bler2 name
Due to DL and UL's bler name is different so I check it 
```
    bler1=""
    bler2=""
    if givenString in 'DL- UE' or 'DL- UE' in givenString :
        bler1="PdschBler="
        bler2="nonWPdschBler="
    elif givenString in 'UL- UE' or 'UL- UE' in givenString :
        bler1="PuschBler="
        bler2="nonWPuschBler="
    else: 
        print("givenString Not found string")
```

- save to list 
```
#save the date into list
result.append(datestr)    
#save the TPUT value into list
result.append(getelement(m3New, 'Tput='))

```

#### write or print the value from list 
In this example I mention many ways to establish this methond, you can choose which one you much perefer. 
Please Mark off the `#` if you decide to use which one.

`NOTE` I will only put some function in `parsefile_layer2_v2.py`, but you wants to see all method please go to `timedate_tputONLY `> `parse.py` file to check.

```
listprint() #write file =>ok
#listprint2() #print =>ok
#listprint_Method2()  # write file =>ok
#listprint_Method3() #write file =>ok
#listprint_Method4()
```
- listprint() 
This method is basic method of wrtting list into file
```
with open(filename, "a") as f:
    for element in result:            
		f.write(element+ " ")           
        f.write("\n")
```

- listprint2() 
This methond will only print out element from list, for debuging you can use this.
`Note` if you can the `%2` on how many column you have. For `parse.py` will only be 2 column, but for single_UE will be `6` column. 
```
for element in result:
	cycle += 1
		print(element, end=" ")
        if cycle % 2 == 0:
            print(" ")
```

- listprint_Method2()
In this method is also write into file same as above but use differently. You can select below which you like
one with for loop, and the other one is list comp method

```
#####method1
    for i in [result[c:c+2] for c in range(0,len(result)) if c%2 == 0]:
       print(*i)
       
#####method1-2 normal for loop
    temp = []
    for c in range(0, len(result)):
        if c % 2 == 0:
            temp.append(result[c:c+2])   
    #for i in temp:
    #    print(*i)        
    #temp is two array
    with open("result.txt", "a+") as f:
        for file in temp:
            #file = file.strip()
            my_str = ' '.join(file)
            f.write(my_str + "\n")     
```

- listprint_Method3() 
This method use enumerate method
```
def listprint_Method3():
    #for index, c in enumerate(result):
    #    if index % 2 == 0:
    #        print(*result[index:index + 2])
    with open('result.txt', 'a') as output:
        for index, c in enumerate(result):
            if index % 2 == 0:
                print(*result[index:index + 2], file=output)
```
- listprint_Method4()
This method use `zip` method
```
def listprint_Method4():
    results = iter(result)
   
    with open('result.txt', 'a') as output:
        for i in zip(results, results):
            print(*i, file=output)
             #file=output
```


### Part 2 convert into excel
After above method it's timet to convert it to excel, and I am also going to show you many different ways to establish it.

#### openpyxl 
- import relate libary
```
import openpyxl, string
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
```
- write into excel
```
while line:
    list123 = line.split()  # convert        
    if "=" in line:
        pass            
        else:         
            if list123[1] == 'Tput':
                sheet[0].append(list123)  # write into excel
            elif list123[1] == 'DL-Tput':
                sheet[0].append(list123)  # write into excel
            elif list123[1] == 'UL-Tput':
                sheet[0].append(list123)  # write into excel                                          
            else:
                list123[1] = float(list123[1])
                list123[2] = float(list123[2])
                list123[3] = float(list123[3])
                list123[4] = float(list123[4])
                list123[5] = float(list123[5])
                sheet[0].append(list123)  # write into excel
```
- edit the font or size (it's an option) 
```
#excel cell's font
sheet[0]['A1'] .font = Font(size = 14, bold = True)               
#adjust the column width 
i = get_column_letter(column)         
sheet[0].column_dimensions[i].width = 25                  
# read next line
line = f.readline() 
excel.save(excelfilename+'.xlsx')
```

#### pandas
- import libary
```
import pandas as pd
import re
```
- create excel 
```
#sheet1
df1 = pd.DataFrame(ULlist)
df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
df1['UL-Tput'] = df1['UL-Tput'].astype(float)
#sheet2
df2 = pd.DataFrame(DLlist)
df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
df2['DL-Tput'] = df2['DL-Tput'].astype(float)

```
- edit cell font and rename worksheet
```
with pd.ExcelWriter(excelfilename+'.xlsx', engine='xlsxwriter') as writer:
    df1=df1.style.set_properties(**{'text-align': 'center'})
    df2=df2.style.set_properties(**{'text-align': 'center'})
	
	
	df1.to_excel(writer, 'UL', index=False)
    worksheet = writer.sheets['UL']   
    worksheet.set_column(0, 1, 25)   
	df2.to_excel(writer, 'DL', index=False)
	worksheet = writer.sheets['DL'] 
	worksheet.set_column(0, 1, 25)   
```