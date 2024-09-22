## Description of code


### convert into excel
After above method it's timet to convert it to excel, and I am also going to show you many different ways to establish it.

#### Method 1: openpyxl 
- import relate libary
```
import openpyxl, string
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
```
- write into excel
```
f = open(result, 'r+')  # open text
#########if load excel file ########################
excel = openpyxl.Workbook()
sheet = excel.worksheets
line = f.readline();  # read text
sheet2=excel.create_sheet("Mysheet1", 1) 
new=[]
while line:
    list123 = line.split()  # convert        
    if "=" in line:
        pass   
        elif "-" not in line and "#" not in line:   		
            if count <=2:
                if list123[1] == 'Tput':
                    sheet[0].append(list123)  # write into excel
                else:
                    list123[1] = float(list123[1])
                    sheet[0].append(list123)  # write into excel         
        line = f.readline()  # read next line
		excel.save(excelfilename+".xlsx")
```
#### Method2: openpyxl
- import libary
```
import openpyxl
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
```
- write into excel
```
    wb = openpyxl.Workbook()
    sheet = wb.worksheets[0]
 
    with open(src, "r") as src:
        # First line is column headings
        line = next(src).split()
        sheet.append(line)
        for column in range(1, len(line)+1):
            
            sheet.cell(1, column).font = Font(size=14, bold=True)
            sheet.column_dimensions[get_column_letter(column)].width = 25
 
        # Copy remaining rows converting number strings to numbers.
        for line in src:
            te=[convert_cell(text) for text in line.split()]
            if "---" not in line:  # check if the line does not contain "---"
                sheet.append([convert_cell(text) for text in line.split()])
```

#### Method3: pandas
- import libary
```
import pandas as pd
import re
```
- create excel to ignore specail character
Check if file contain - to ignore character
> `df = pd.read_csv(file, sep=" ", names=column_names, comment="-"`

If you have multiply to check use this, and use this: 
>`df = pd.read_csv(file, sep=" ", names=column_names, comment=resultchar)`

```
def checkchar(x):
    char11=""
    for line in file:
        if '-' in line:
            char11="-"
            break
        elif '#' in line:
            char11="+"
            break 
        else:
            break
    return char11    
```
- Full code 
```
with open("result.txt", "r") as file:
    column_names = next(file).split()
    resultchar=checkchar(file)    
   
    if resultchar == "":
        df = pd.read_csv(file, sep=" ", names=column_names)
    else:
        df = pd.read_csv(file, sep=" ", names=column_names, comment=resultchar)
        #df = pd.read_csv(file, sep=" ", names=column_names, comment="-"
    df.to_excel("test.xlsx", index=False)
writer = pd.ExcelWriter("test.xlsx", engine="xlsxwriter", )
df.to_excel(writer, sheet_name="Data", index=False)
sheet = writer.sheets["Data"]

# Set column widths (option)
sheet.set_column(0, len(column_names)-1, 25)
 
#st header's header (option)
header_format = writer.book.add_format({'bold':True, 'font_size':14})
for index, name in enumerate(column_names):
    sheet.write(0, index, name, header_format)
```

