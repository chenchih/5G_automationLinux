## Code Description
### Part 1 parsing DATA from a file and write into text file 

### Part 1 Filter DL or UL

- Search related string 
There are two layer of string need to search:
Step1: Find the file contain `m>>> DL-` string `"m>>> DL-`
Step2: Find contain average Tput and relate string `\[(\d+\.\d+\.\d+)\].*?(>>> DL- Mcs=[^]]+)`

```
with open(elogfileName, 'r') as filedata:    
    for line in filedata:                     
        if "m>>> DL-" in  line:
            for nextline in filedata:
                if re.search(r'\[(\d+\.\d+\.\d+)\].*?(>>> DL- Mcs=[^]]+)', nextline):
                    parse_bler(nextline, givenString)
```

Below is an example of the log
```
# Step 1: get the Tput value ingress and egress
[20230311.012825.882186][info]:[[40;32m>>> DL- ingress traffic: 117.590118(Mbps), egress traffic: 120.919250(Mbps), ReTx: 2.519794(Mbps)[0m]
# Step2 get the average value 
[20230311.012825.882339][info]:[>>> DL- Mcs= 55.0, RbNum=  71.2, Layers= 4.0, PdschBler=   2.1, nonWPdschBler=   1.9, MaxSchedUE=   1.0, SchedUE=   8.0]
```
> I wants:
>> ` DL- ingress traffic: 117.590118(Mbps), egress traffic: 120.919250(Mbps)`
>> `20230311.012825.882339 DL- Mcs= 55.0RbNum=  71.2, PdschBler=   2.1, nonWPdschBler=   1.9`

- get parse (Step 1 value)
In this step you parse the datetime, ingress and egress tput and save into list 
```
datestr = data.split('[', 1)[1].split(']')[0]  
Tputvalue=re.search(r'(ingress [^(]+).+(egress [^(]+)',data)
m3New= Tputvalue.group(1)+", "+ Tputvalue.group(2) 
m3New_1=m3New.replace(", ", ":").strip().split(':')
result.append(datestr)
result.append(getelement(m3New_1, 'ingress traffic').strip())
result.append(getelement(m3New_1, 'egress traffic').strip())  
```


- get parse_bler (Step 2 value)
In this step will get all the related average value
```
if ULDLstr in 'DL':
bler1="PdschBler="
bler2="nonWPdschBler="
        
elif ULDLstr in 'UL':
	bler1="PuschBler="
    bler2="nonWPuschBler="        
result.append(getelement(blerDL, 'RbNum='))
result.append(getelement(blerDL, 'Mcs='))
result.append(getelement(blerDL, bler1).strip())
result.append(getelement(blerDL, bler2).strip())
listprint()
result.clear() #clear list 
```

### Part 2 Excel

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
df['UL_Tput(ingress)'] = df1['UL_Tput(ingress)'].astype(float)
df1['UL_Tput(egress)'] = df1['UL_Tput(egress)'].astype(float)

```
- edit cell font and rnemae worksheet
```
with pd.ExcelWriter(excelfilename+'.xlsx', engine='xlsxwriter') as writer:
    df1=df1.style.set_properties(**{'text-align': 'center'})
	df1.to_excel(writer, 'UL', index=False)
    worksheet = writer.sheets['UL']   
    worksheet.set_column(0, 1, 25)   

```
