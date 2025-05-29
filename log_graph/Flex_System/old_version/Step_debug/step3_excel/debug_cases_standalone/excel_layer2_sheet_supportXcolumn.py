from tqdm import tqdm
import pandas as pd
import re

resultfilename = input("Please enter your txt file name (Ex: test.txt): ")
excelfilename = input("Please enter saving Excel file name (Ex: test): ")

lists = {}
current_key = None

with open(resultfilename, 'r') as myfile:
    readline = myfile.read().splitlines()
    for line in readline:
        if "=" in line:
            current_key = line.strip("=")
            lists[current_key] = []
        else:
            assert current_key is not None  # Ensure there's a valid header
            lists[current_key].append(line)

ULlist = []
DLlist = []

def UL():
    for i in lists["UL"]:
        ULlist.append(i.split())

def DL():
    for i in lists["DL"]:
        DLlist.append(i.split())
def process_dataframe(data, sheet_name, writer):
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]  # Use the first row as column names
    df = df.drop(df.index[0])  # Remove the header row from the data

    # Process each column based on its type
    for col in df.columns:
        if df[col].dtype == object:  # Check if column contains strings
            df[col] = df[col].str.strip()  # Clean strings
            # Try converting to numeric, if applicable
            df[col] = pd.to_numeric(df[col], errors="ignore")

    # Write to Excel with formatting
    df.style.set_properties(**{'text-align': 'center'}).to_excel(writer, sheet_name, index=False)

    # Adjust column widths
    worksheet = writer.sheets[sheet_name]
    worksheet.set_column(0, 0, 25)  # Adjust first column width
    worksheet.set_column(1, len(df.columns) - 1, 15)  # Adjust other columns

def writeExcel():
    with pd.ExcelWriter(excelfilename + '.xlsx', engine='xlsxwriter') as writer:
        process_dataframe(ULlist, "UL", writer)
        process_dataframe(DLlist, "DL", writer)

# Check if input file contains both UL and DL data
if "DL" in lists and "UL" in lists:
    DL()
    UL()
    writeExcel()
else:
    print("Data does not contain both UL and DL sections.")