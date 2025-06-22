import pandas as pd
import re
from tqdm import tqdm  # Import tqdm for progress bar

lists = {}
ULlist= []
DLlist= []

def UL():
    for i in tqdm(lists["UL"], desc="Processing UL lines", unit="line", dynamic_ncols=True): #->implement progress bar
    #for i in lists["UL"]:
        #remove multiply space reg (don't need it)
        #pattern = re.compile(r'\s+')
        #sentence = re.sub(pattern, ' ', i)        
        #i=i.rstrip().split(' ')
        #i=i.split(' ')
        i=i.split()
        ULlist.append(i)

    
def DL():
    for i in tqdm(lists["DL"], desc="Processing DL lines", unit="line", dynamic_ncols=True): #->implement progress bar
    #for i in lists["DL"]:
        #remove multiply space reg (don't need it)
        #pattern = re.compile(r'\s+')
        #sentence = re.sub(pattern, ' ', i)
        i=i.split()
        DLlist.append(i)

def writeExcel(result, excelFile):
#writing into excel sheet
    if result =="UL":
        #uplink
        df1 = pd.DataFrame(ULlist)
        df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
        df1['UL-Tput'] = df1['UL-Tput'].astype(float)
        #df1[TPUTULvalue] = df1[TPUTULvalue].astype(float)
        df1['UL-RbNum'] = df1['UL-RbNum'].astype(float)
        df1['UL-MCS'] = df1['UL-MCS'].astype(float)
        df1['UL-Bler'] = df1['UL-Bler'].astype(float)
        df1['UL-nonWPuschBler'] = df1['UL-nonWPuschBler'].astype(float)
      
    elif result =="DL":
        df2 = pd.DataFrame(DLlist)
        df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])

        df2['DL-Tput'] = df2['DL-Tput'].astype(float)
        df2['DL-RbNum'] = df2['DL-RbNum'].astype(float)
        df2['DL-MCS'] = df2['DL-MCS'].astype(float)
        df2['DL-Bler'] = df2['DL-Bler'].astype(float)
        df2['DL_Bler'] = df2['DL_Bler'].astype(float)
        df2['DL-nonWPdschBler'] = df2['DL-nonWPdschBler'].astype(float)
    
    elif result=="both":   
        #uplink
        df1 = pd.DataFrame(ULlist)
        df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
        #df1[TPUTULvalue] = df1[TPUTULvalue].astype(float)
        df1['UL-Tput'] = df1['UL-Tput'].astype(float)
        df1['UL-RbNum'] = df1['UL-RbNum'].astype(float)
        df1['UL-MCS'] = df1['UL-MCS'].astype(float)
        df1['UL-Bler'] = df1['UL-Bler'].astype(float)
        df1['UL-nonWPuschBler'] = df1['UL-nonWPuschBler'].astype(float)

        #downlink 
        df2 = pd.DataFrame(DLlist)
        df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
        df2['DL-Tput'] = df2['DL-Tput'].astype(float)
        df2['DL-RbNum'] = df2['DL-RbNum'].astype(float)
        df2['DL-MCS'] = df2['DL-MCS'].astype(float)
        df2['DL-Bler'] = df2['DL-Bler'].astype(float)
        df2['DL-nonWPdschBler'] = df2['DL-nonWPdschBler'].astype(float)
  
    #with pd.ExcelWriter('out.xlsx', engine='xlsxwriter') as writer:
    #with pd.ExcelWriter(excelFile+'.xlsx', engine='xlsxwriter') as writer:
    with pd.ExcelWriter(excelFile, engine='xlsxwriter') as writer:
        if result == "both":

            df1=df1.style.set_properties(**{'text-align': 'center'})
            df2=df2.style.set_properties(**{'text-align': 'center'})
                #multiply option
                #df1=df1.style.set_properties(**{'text-align': 'center',
                #'color':'red', 
                #'font-size':'1.0rem',
                #'font-weight': 'bold',
                #'background-color': 'yellow' })

            df1.to_excel(writer, 'UL', index=False)
            worksheet = writer.sheets['UL']   
            worksheet.set_column(0, 1, 25)   
            worksheet.set_column(1, 4, 15) 
            worksheet.set_column(4, 5, 20) 
            #worksheet.set_column(3, 5, 15)     
               
            df2.to_excel(writer, 'DL', index=False)
            #worksheet.set_column(1, 0, 20)
            worksheet = writer.sheets['DL'] 
            worksheet.set_column(0, 1, 25)   
            worksheet.set_column(1, 4, 15) 
            worksheet.set_column(4, 5, 20) 
            #worksheet.set_column(0, 2, 20)   
           # worksheet.set_column(3, 6, 15) 

def main(resultfilename,excelfilename):
    
    current_key = None
    readline = [] # Initialize here to ensure it's always defined   ->implement progress bar
    # Progress bar for reading and initial parsing of the text file
    try:  #->implement progress bar
        #with open ('test.txt', 'r')as myfile:  
        with open (resultfilename, 'r')as myfile:  
            readline=myfile.read().splitlines() 
        with tqdm(total=len(readline), desc=f"Parsing '{resultfilename}'", unit="line", dynamic_ncols=True) as pbar_file_read: # ->implement progress bar
            for line in readline:
                #print(line)
                if "=" in line:
                    current_key = line.strip("=")            
                    lists[current_key] = []
                else:
                    assert current_key is not None # there shouldn't be data before a header              
                    lists[current_key].append(line)  
                pbar_file_read.update(1) #->implement progress bar
        tqdm.write(f"Finished parsing '{resultfilename}'.") # Use tqdm.write for this message
    except FileNotFoundError: #->implement progress bar
        print(f"Error: Input file '{resultfilename}' not found.")
        return 'error' # Indicate failure
    except Exception as e:#->implement progress bar
        print(f"An error occurred during file parsing: {e}")
        return 'error'
        
    #check textfile contain Ul or DL
    types=""
    if "DL" in lists and "UL" in lists:
        #print("both UL and DL exist")
        types="both"
        DL()
        UL()
        tqdm.write(f"Writing data to Excel file: '{excelfilename}'...")
        writeExcel(types, excelfilename)
        tqdm.write(f"Excel file '{excelfilename}' created successfully for both UL and DL data.")
            
    elif "UL" in lists:
        #print("UL exist")
        types="UL"     
        UL()    
        tqdm.write(f"Writing UL data to Excel file: '{excelfilename}'...")        
        writeExcel(types, excelfilename)
        tqdm.write("Successfully processed UL data and wrote to Excel.") # ->implement progress bar
        
    elif "DL" in lists:
        #print("DL exist")
        types="DL"
        #print("UL exist")
        #types="UL"      
        DL()  
        tqdm.write(f"Writing DL data to Excel file: '{excelfilename}'...")  
        writeExcel(types, excelfilename) 
        tqdm.write("Successfully processed DL data and wrote to Excel.") # ->implement progress bar        
    else:
        #print("Neither exist")
        types="Not Exist"
        tqdm.write("Neither UL nor DL data sections found in the file.") # ->implement progress bar
    
    return 'ok'
###################################################################################
if __name__ == "__main__":
    '''
    resultfilename=input("please enter your txt file name(Ex: test.txt) : ")
    #resultfilename="111.txt"
    excelfilename=input("please enter saving excel file name(Ex: test): ")
    if resultfilename and excelfilename:
        main(resultfilename,excelfilename)        
    else:
        print('Something went wrong with your input)')
    '''
    
    try:
        resultfilename=input("please enter your txt file name(Ex: test.txt) : ")
        excel_file_input=input("please enter saving excel file name(Ex: test): ")
        
        if not excel_file_input.lower().endswith(('.xlsx', '.xls', '.xlsm')):
            excel_file_input  = excel_file_input + ".xlsx"
            #print(excel_file_input)
        else:
            excel_file_input  = excel_file_input   # If it already has extension, use as is
            print(excel_file_input)
        
        print(f"Attempting to process: {excel_file_input}")
        main(resultfilename, excel_file_input) # Call main with the correctly formatted path
  
    except KeyboardInterrupt:
        print("\nOperation cancelled by user (Ctrl+C). Exiting gracefully.")
    except Exception as e:
        print(f"\nAn unexpected error occurred in the main execution block: {e}")
        print("Exiting.")