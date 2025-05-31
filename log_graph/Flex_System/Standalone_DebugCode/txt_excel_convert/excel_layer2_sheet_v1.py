'''
Note: 
- Remove the condition UL, DL, and both for checking is it either one. No matter contain UL or DL throughput Data will write into excel with both sheet data. 
- adding try and exception to check code 
- add name orginal write_excel() to write_excel_old() and add a new write_excel(), which is improvement version

'''
import pandas as pd
import re



ULlist= []
DLlist= []

def UL():
    for i in lists["UL"]:
        #remove multiply space reg (don't need it)
        #pattern = re.compile(r'\s+')
        #sentence = re.sub(pattern, ' ', i)        
        #i=i.rstrip().split(' ')
        #i=i.split(' ')

        i=i.split()
        ULlist.append(i)

def DL():
    for i in lists["DL"]:
        #remove multiply space reg (don't need it)
        #pattern = re.compile(r'\s+')
        #sentence = re.sub(pattern, ' ', i)
        
        i=i.split()
        DLlist.append(i)
        
def writeExcel_old():
#writing into excel sheet    
    try:
        #uplink
        df1 = pd.DataFrame(ULlist)
        df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
        df1['UL-Tput'] = df1['UL-Tput'].astype(float)
        df1['UL-RbNum'] = df1['UL-RbNum'].astype(float)
        df1['UL-MCS'] = df1['UL-MCS'].astype(float)
        df1['UL-Bler'] = df1['UL-Bler'].astype(float)    
            
        #downlink 
        df2 = pd.DataFrame(DLlist)
        df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
        df2['DL-Tput'] = df2['DL-Tput'].astype(float)
        df2['DL-RbNum'] = df2['DL-RbNum'].astype(float)
        df2['DL-MCS'] = df2['DL-MCS'].astype(float)
        df2['DL-Bler'] = df2['DL-Bler'].astype(float)
    
        #with pd.ExcelWriter('out.xlsx', engine='xlsxwriter') as writer:
        with pd.ExcelWriter(excelfilename+'.xlsx', engine='xlsxwriter') as writer:
    
            df1=df1.style.set_properties(**{'text-align': 'center'})
            df2=df2.style.set_properties(**{'text-align': 'center'})
            #multiply option
            #df1=df1.style.set_properties(**{'text-align': 'center',
            #'color':'red', 
            #'font-size':'1.0rem',
            #'font-weight': 'bold',
            #'background-color': 'yellow' })
        
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
    except KeyError as e:
        print(f"KeyError: {e}. Please check the input file for missing headers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")   

def writeExcel():
#writing into excel sheet    
    required_ul_columns = {'UL-Tput', 'UL-RbNum', 'UL-MCS', 'UL-Bler'}
    required_dl_columns = {'DL-Tput', 'DL-RbNum', 'DL-MCS', 'DL-Bler'}
    try:
        #uplink
        df1 = pd.DataFrame(ULlist)
        df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
        # Validate UL columns
        missing_ul_columns = required_ul_columns - set(df1.columns)
        if missing_ul_columns:
            raise KeyError(f"Missing UL columns: {', '.join(missing_ul_columns)}")
        # Convert UL columns to float
        for col in required_ul_columns:
            df1[col] = df1[col].astype(float)
        
        # Downlink
        df2 = pd.DataFrame(DLlist)
        df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])

        # Validate DL columns
        missing_dl_columns = required_dl_columns - set(df2.columns)
        if missing_dl_columns:
            raise KeyError(f"Missing DL columns: {', '.join(missing_dl_columns)}")

        # Convert DL columns to float
        for col in required_dl_columns:
            df2[col] = df2[col].astype(float)
        
        
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
    except KeyError as e:
        print(f"KeyError: {e}")
        print("Please check the input file for missing or incorrect headers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")    


resultfilename=input("please enter your txt file name(Ex: test.txt) : ")
excelfilename=input("please enter saving excel file name(Ex: test): ")


lists = {}
current_key = None
#with open ('test.txt', 'r')as myfile:  
with open (resultfilename, 'r')as myfile:  
    readline=myfile.read().splitlines()
    
    for line in readline:
        #print(line)
        if "=" in line:
            current_key = line.strip("=")
           
            lists[current_key] = []
        else:
            assert current_key is not None # there shouldn't be data before a header
            
            lists[current_key].append(line)
            
#check textfile contain Ul or DL
types=""
if "DL" in lists and "UL" in lists:
    DL()
    UL()
    writeExcel()
else:
     types="NOt Exist"