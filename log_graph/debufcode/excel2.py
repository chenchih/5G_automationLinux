import pandas as pd
from openpyxl import Workbook

def excelpandas(filename, save):
    df = pd.read_csv(filename) # if your file is comma separated
    print(df)
    df = pd.read_csv(filename, sep='\t')

    #df.to_excel(save+'.xlsx', 'Sheet1')
    #print(df)


def openexcel(filename):
    wb = Workbook()
    ws = wb.active
    f = open('result.txt', 'r')
    data = f.readlines()
    #check last new line if no add new line
    if '\n' not in data[-1]: 
        data[-1] += '\n'

    spaces = ""
    for i in range(len(data)):
        row = data[i].split(" ")  
        ws.append(row)

    wb.save("testval2.xlsx") 


filename="result.txt"
save=filename.split('.')[0]

excelpandas(filename, save)
#openexcel(filename)