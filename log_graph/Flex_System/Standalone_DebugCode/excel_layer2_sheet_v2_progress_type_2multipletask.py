'''
This code is base on excel_layer2_progress_1_version2.py 
implement two progress bars — one for processing UL and DL, and the second for writing Excel 
'''
from tqdm import tqdm
import pandas as pd

resultfilename = input("please enter your txt file name (Ex: test.txt): ")
excelfilename = input("please enter saving excel file name (Ex: test): ")

lists = {}
current_key = None

# Read and process the input file
with open(resultfilename, 'r') as myfile:
    readline = myfile.read().splitlines()
    for line in readline:
        if "=" in line:
            current_key = line.strip("=")
            lists[current_key] = []
        else:
            assert current_key is not None  # Ensure data comes after a header
            lists[current_key].append(line)

ULlist = []
DLlist = []

# Define UL processing function
def UL(pbar):
    for i in tqdm(lists["UL"], desc="Processing UL", leave=False, ncols=100):
        i = i.split()
        ULlist.append(i)
        pbar.update(1)

# Define DL processing function
def DL(pbar):
    for i in tqdm(lists["DL"], desc="Processing DL", leave=False, ncols=100):
        i = i.split()
        DLlist.append(i)
        pbar.update(1)

# Define Excel writing function
def writeExcel():
    # Create dataframes for UL and DL
    df1 = pd.DataFrame(ULlist)
    df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
    df1['UL-Tput'] = df1['UL-Tput'].astype(float)
    df1['UL-RbNum'] = df1['UL-RbNum'].astype(float)
    df1['UL-MCS'] = df1['UL-MCS'].astype(float)
    df1['UL-Bler'] = df1['UL-Bler'].astype(float)

    df2 = pd.DataFrame(DLlist)
    df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
    df2['DL-Tput'] = df2['DL-Tput'].astype(float)
    df2['DL-RbNum'] = df2['DL-RbNum'].astype(float)
    df2['DL-MCS'] = df2['DL-MCS'].astype(float)
    df2['DL-Bler'] = df2['DL-Bler'].astype(float)

    # Prepare steps for writing Excel
    steps = ["Writing UL Sheet", "Setting UL Styles", "Writing DL Sheet", "Setting DL Styles"]
    with tqdm(total=len(steps), desc="Writing Excel", ncols=100) as pbar:
        with pd.ExcelWriter(excelfilename + '.xlsx', engine='xlsxwriter') as writer:
            # Writing UL sheet
            df1.to_excel(writer, sheet_name='UL', index=False)
            pbar.update(1)  # Progress update
            
            # Styling UL sheet
            worksheet = writer.sheets['UL']
            worksheet.set_column(0, 0, 25)
            worksheet.set_column(1, len(df1.columns) - 1, 15)
            pbar.update(1)  # Progress update

            # Writing DL sheet
            df2.to_excel(writer, sheet_name='DL', index=False)
            pbar.update(1)  # Progress update

            # Styling DL sheet
            worksheet = writer.sheets['DL']
            worksheet.set_column(0, 0, 25)
            worksheet.set_column(1, len(df2.columns) - 1, 15)
            pbar.update(1)  # Progress update

# Main process flow
if "DL" in lists and "UL" in lists:
    total_lines = len(lists["UL"]) + len(lists["DL"])
    with tqdm(total=total_lines, desc="Processing UL and DL", ncols=100) as pbar:
        if "UL" in lists:
            UL(pbar)
        if "DL" in lists:
            DL(pbar)
    # Call the writeExcel function with its own progress bar
    writeExcel()
else:
    print("Data for UL or DL not found.")
