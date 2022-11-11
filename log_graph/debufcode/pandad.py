
# Read Text Files with Pandas using read_csv()
  
# importing pandas 
# ok
'''
import pandas as pd


df = pd.read_csv('result.txt') # if your file is comma separated
df = pd.read_csv('result.txt', sep=' ')
df.to_excel('output.xlsx', 'Sheet1')
#print(df)
'''






#ok 

from openpyxl import Workbook
wb = Workbook()
ws = wb.active


f = open('result1.txt', 'r')

data = f.readlines()
#check last new line if no add new line
if '\n' not in data[-1]: 
    data[-1] += '\n'

spaces = ""
for i in range(len(data)):
    data[0]=data[0].replace('  ', '')
    data[1]=data[1].replace('  ', '')
    row=data[i].split(" ")
    #print(data[0])
    
    
    ws.append(row)

wb.save("testval2.xlsx") 
