'''
adding progress bar v1 version1
single unified progress bar or aggregated progress bar: 
This approach combines multiple steps or processes into a single progress bar to provide a cohesive and continuous visual representation of the overall task's progress.
'''

from tqdm import tqdm
import pandas as pd
import re

resultfilename = input("Please enter your txt file name(Ex: test.txt): ")
excelfilename = input("Please enter saving excel file name(Ex: test): ")

lists = {}
current_key = None

# Reading file and storing data in lists
with open(resultfilename, 'r') as myfile:
    readline = myfile.read().splitlines()
    
    for line in readline:
        if "=" in line:
            current_key = line.strip("=")
            lists[current_key] = []
        else:
            assert current_key is not None  # there shouldn't be data before a header
            lists[current_key].append(line)

ULlist = []
DLlist = []

# Function to process UL data
def UL():
    for i in lists["UL"]:
        i = i.split()
        ULlist.append(i)

# Function to process DL data
def DL():
    for i in lists["DL"]:
        i = i.split()
        DLlist.append(i)

# Process the data and write to Excel

def writeExcel_process_old():
    total_steps = 4  # Define the number of major steps in this function
    with tqdm(total=total_steps, desc="Writing Excel") as pbar:
        # Processing UL data
        df1 = pd.DataFrame(ULlist)
        df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
        df1['UL-Tput'] = df1['UL-Tput'].astype(float)
        df1['UL-RbNum'] = df1['UL-RbNum'].astype(float)
        df1['UL-MCS'] = df1['UL-MCS'].astype(float)
        df1['UL-Bler'] = df1['UL-Bler'].astype(float)
        pbar.update(1)  # Update progress after processing UL data

        # Processing DL data
        df2 = pd.DataFrame(DLlist)
        df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
        df2['DL-Tput'] = df2['DL-Tput'].astype(float)
        df2['DL-RbNum'] = df2['DL-RbNum'].astype(float)
        df2['DL-MCS'] = df2['DL-MCS'].astype(float)
        df2['DL-Bler'] = df2['DL-Bler'].astype(float)
        pbar.update(1)  # Update progress after processing DL data

        # Writing to Excel
        with pd.ExcelWriter(excelfilename + '.xlsx', engine='xlsxwriter') as writer:
            df1 = df1.style.set_properties(**{'text-align': 'center'})
            df2 = df2.style.set_properties(**{'text-align': 'center'})

            # Get last column indices for formatting
            last_col_index_df1 = [idx for idx, col in enumerate(df1.columns)][-1]
            last_col_index_df2 = [idx for idx, col in enumerate(df2.columns)][-1]

            # Write UL data to Excel
            df1.to_excel(writer, 'UL', index=False)
            worksheet = writer.sheets['UL']
            worksheet.set_column(0, 0, 25)
            worksheet.set_column(1, last_col_index_df1, 15)
            pbar.update(1)  # Update progress after writing UL data to Excel

            # Write DL data to Excel
            df2.to_excel(writer, 'DL', index=False)
            worksheet = writer.sheets['DL']
            worksheet.set_column(0, 0, 25)
            worksheet.set_column(1, last_col_index_df2, 15)
            pbar.update(1)  # Update progress after writing DL data to Excel

#adding new progress bar
def writeExcel():
#writing into excel sheet    
    required_ul_columns = {'UL-Tput', 'UL-RbNum', 'UL-MCS', 'UL-Bler'}
    required_dl_columns = {'DL-Tput', 'DL-RbNum', 'DL-MCS', 'DL-Bler'}
    
    try:
        total_steps = 6  # Define the number of major steps in this function    
        with tqdm(total=total_steps, desc="Writing Excel") as pbar:
        #uplink
            df1 = pd.DataFrame(ULlist)
            df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
            pbar.update(1)  # Step 1: Dataframe creation for UL
            # Validate UL columns
            missing_ul_columns = required_ul_columns - set(df1.columns)
            if missing_ul_columns:
                raise KeyError(f"Missing UL columns: {', '.join(missing_ul_columns)}")
            pbar.update(1)  # Step 2: UL column validation
    
            # Convert UL columns to float
            for col in required_ul_columns:
                df1[col] = df1[col].astype(float)
            pbar.update(1)  # Step 3: UL type conversion
    
            # Downlink
            df2 = pd.DataFrame(DLlist)
            df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
            pbar.update(1)  # Step 4: Dataframe creation for DL
    
            # Validate DL columns
            missing_dl_columns = required_dl_columns - set(df2.columns)
            if missing_dl_columns:
                raise KeyError(f"Missing DL columns: {', '.join(missing_dl_columns)}")
    
            # Convert DL columns to float
            for col in required_dl_columns:
                df2[col] = df2[col].astype(float)
            pbar.update(1)  # Step 5: DL type conversion
            
            # Writing to Excel
            #with pd.ExcelWriter('out.xlsx', engine='xlsxwriter') as writer:
            with pd.ExcelWriter(excelfilename+'.xlsx', engine='xlsxwriter') as writer:
    
                df1=df1.style.set_properties(**{'text-align': 'center'})
                df2=df2.style.set_properties(**{'text-align': 'center'})
                #get the last index of column without fix column
                last_col_index_df1 = [idx for idx, col in enumerate(df1.columns)][-1]
                last_col_index_df2 = [idx for idx, col in enumerate(df1.columns)][-1]
                #below is the traditional way of above with out comprensive 
                #last_col_index = -1
                #for idx, col in enumerate(df1.columns):
                #last_col_index = idx
            
                df1.to_excel(writer, 'UL', index=False)
                worksheet = writer.sheets['UL']   
                worksheet.set_column(0, 0, 25)   
                worksheet.set_column(1, last_col_index_df1, 15)     
                
                df2.to_excel(writer, 'DL', index=False)
                #worksheet.set_column(1, 0, 20)
                worksheet = writer.sheets['DL'] 
                worksheet.set_column(0, 0, 25)   
                worksheet.set_column(1, last_col_index_df2, 15)  
            pbar.update(1)  # Step 6: Excel writing complete
    except KeyError as e:
        print(f"KeyError: {e}")
        print("Please check the input file for missing or incorrect headers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")    
     



#check textfile contain Ul or DL
types=""
if "DL" in lists and "UL" in lists:
    
    DL()
    UL()
    writeExcel()
else:
     types="NOt Exist"

