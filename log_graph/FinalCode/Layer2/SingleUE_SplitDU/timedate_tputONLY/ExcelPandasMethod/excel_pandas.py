import pandas as pd
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
 
#writer.save()
writer.close()