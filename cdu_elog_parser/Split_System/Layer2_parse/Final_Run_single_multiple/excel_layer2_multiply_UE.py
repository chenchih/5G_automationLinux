import pandas as pd
import re
from tqdm import tqdm

ULlist= []
DLlist= []
lists = {}

def UL():
    #for i in lists["UL"]:
    for i in tqdm(lists["UL"], desc="Processing UL data lines", unit="line"):
        #remove multiply space reg (don't need it)
        #pattern = re.compile(r'\s+')
        #sentence = re.sub(pattern, ' ', i)        
        #i=i.rstrip().split(' ')
        #i=i.split(' ')
        i=i.split()
        ULlist.append(i)

    
def DL():
    #for i in lists["DL"]:
    for i in tqdm(lists["DL"], desc="Processing DL data lines", unit="line"):
        #remove multiply space reg (don't need it)
        #pattern = re.compile(r'\s+')
        #sentence = re.sub(pattern, ' ', i)
        i=i.split()
        DLlist.append(i)
        

#writing into excel sheet     
def writeExcel(result, excelfilename):
    
    if result =="UL":
        #uplink
        df1 = pd.DataFrame(ULlist)
        df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
        df['UL_Tput(ingress)'] = df1['UL_Tput(ingress)'].astype(float)
        df1['UL_Tput(egress)'] = df1['UL_Tput(egress)'].astype(float)
        df1['UL_RbNum'] = df1['UL_RbNum'].astype(float)
        df1['UL_MCS'] = df1['UL_MCS'].astype(float)
        df1['UL_Bler'] = df1['UL_Bler'].astype(float)
        df1['UL_nonWdBler'] = df1['UL_nonWdBler'].astype(float)
        
    elif result =="DL":
        df2 = pd.DataFrame(DLlist)
        df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
        #df2['ingress-traffic'] = df2['ingress-traffic'].astype(float)
        #df2['egress-traffics'] = df2['egress-traffics'].astype(float)

        df2['DL_Tput(ingress)'] = df2['DL_Tput(ingress)'].astype(float)
        df2['DL_Tput(egress)'] = df2['DL_Tput(egress)'].astype(float)
        df2['DL_RbNum'] = df2['DL_RbNum'].astype(float)
        df2['DL_MCS'] = df2['DL_MCS'].astype(float)
        df2['DL_Bler'] = df2['DL_Bler'].astype(float)
        df2['DL_nonWdBler'] = df2['DL_nonWdBler'].astype(float)
          
        

        #writeexcel(result)
    
    elif result=="both": 
        #uplink
        df1 = pd.DataFrame(ULlist)
        df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])

        #df1['ingress-traffic'] = df1['ingress-traffic'].astype(float)
        #df1['egress-traffics'] = df1['egress-traffics'].astype(float)
        df1['UL_Tput(ingress)'] = df1['UL_Tput(ingress)'].astype(float)
        df1['UL_Tput(egress)'] = df1['UL_Tput(egress)'].astype(float)
        df1['UL_RbNum'] = df1['UL_RbNum'].astype(float)
        df1['UL_MCS'] = df1['UL_MCS'].astype(float)
        df1['UL_Bler'] = df1['UL_Bler'].astype(float)
        df1['UL_nonWdBler'] = df1['UL_nonWdBler'].astype(float)
        
        #downlink 
        df2 = pd.DataFrame(DLlist)
        df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
        df2['DL_Tput(ingress)'] = df2['DL_Tput(ingress)'].astype(float)
        df2['DL_Tput(egress)'] = df2['DL_Tput(egress)'].astype(float)
        df2['DL_RbNum'] = df2['DL_RbNum'].astype(float)
        df2['DL_MCS'] = df2['DL_MCS'].astype(float)
        df2['DL_Bler'] = df2['DL_Bler'].astype(float)
        df2['DL_nonWdBler'] = df2['DL_nonWdBler'].astype(float)

        
    #with pd.ExcelWriter('out.xlsx', engine='xlsxwriter') as writer:
    #with pd.ExcelWriter(excelfilename+'.xlsx', engine='xlsxwriter') as writer:
    with pd.ExcelWriter(excelfilename, engine='xlsxwriter') as writer:
        if result == "both":
            ''' no progress
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
            worksheet.set_column(0, 2, 20)   
            worksheet.set_column(3, 6, 15)     
               
            df2.to_excel(writer, 'DL', index=False)
            #worksheet.set_column(1, 0, 20)
            worksheet = writer.sheets['DL'] 
            worksheet.set_column(0, 2, 20)   
            worksheet.set_column(3, 6, 15) 
            
            '''
            sheets_to_process = [
                {"df": df1, "name": "UL"},
                {"df": df2, "name": "DL"}
            ]
            #progress bar on writting sheet 2 sheet
            for sheet_info in tqdm(sheets_to_process, desc="Writing Excel Sheets", unit="sheet"):
                df_current = sheet_info["df"]
                sheet_name = sheet_info["name"]
            
                df_current=df_current.style.set_properties(**{'text-align': 'center'})
                df_current.to_excel(writer, sheet_name, index=False)
                
                worksheet = writer.sheets[sheet_name]    
                worksheet.set_column(0, 2, 24)    #start col,  end col, width
                worksheet.set_column(3, 6, 15)    
            print(f"Excel file '{excelfilename}' created successfully with UL and DL sheets.")
            
                        
def main(resultfilename, excelfilename):

    current_key = None
    #with open ('test.txt', 'r')as myfile:  
    with open (resultfilename, 'r')as myfile:  
        readline=myfile.read().splitlines()
        
        # Progress bar for categorizing lines from the input text file
        for line in tqdm(readline, desc="Categorizing data", unit="line"):
        #for line in readline:
            if "=" in line:
                current_key = line.strip("=")
            
                lists[current_key] = []
            else:
                assert current_key is not None # there shouldn't be data before a header
                
                lists[current_key].append(line)

    #print("DL" in lists and "UL" in lists)
    #print("UL" in lists)
    #print("DL" in lists)

    #check textfile contain Ul or DL
    types=""
    if "DL" in lists and "UL" in lists:
        #print("both UL and DL exist")
        types="both"
        DL()
        UL()
        writeExcel(types, excelfilename)
        
    elif "UL" in lists:
        #print("UL exist")
        types="UL"     
        UL()    
        writeExcel(types, excelfilename)
    elif "DL" in lists:
        #print("DL exist")
        types="DL"
        #print("UL exist")
        #types="UL"      
        DL()  
        writeExcel(types,excelfilename)    
    else:
        #print("Neither exist")
        types="NOt Exist"
        #writeexcel(result)
        
    return 'ok'

if __name__ == "__main__":

    try:
        resultfilename=input("please enter your txt file name(Ex: test.txt) : ")
        excel_file_input=input("please enter saving excel file name(Ex: test): ")
        
        if not excel_file_input.lower().endswith(('.xlsx', '.xls', '.xlsm')):
            excel_file_input  = excel_file_input + ".xlsx"
            print(excel_file_input)
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