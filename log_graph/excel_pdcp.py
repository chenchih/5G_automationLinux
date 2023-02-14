lists = {}
current_key = None
with open ('test.txt', 'r')as myfile:  
    readline=myfile.read().splitlines()
    for line in readline:
        #print(line)
        if "=" in line:
            current_key = line.strip("=")
           
            lists[current_key] = []
        else:
            assert current_key is not None # there shouldn't be data before a header
            lists[current_key].append(line)



print("*"*50)
UL =[]

#print("DL" in lists)

for i in lists["UL"]:
    #remove end space
    i=i.rstrip().split(' ')
    #i=i.split(' ')
    #print(i)
    
    UL.append(i)



DL =[]
for i in lists["DL"]:
    #remove end space
    i=i.rstrip().split(' ')
    #i=i.split(' ')
    #print(i)
    
    DL.append(i)


import pandas as pd

#uplink
df1 = pd.DataFrame(UL)
df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])

df1['ingress-traffic'] = df1['ingress-traffic'].astype(float)
df1['egress-traffic'] = df1['egress-traffic'].astype(float)

#downlink 
df2 = pd.DataFrame(DL)
df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
df2['ingress-traffic'] = df2['ingress-traffic'].astype(float)
df2['egress-traffic'] = df2['egress-traffic'].astype(float)

#print(df2)
# To Excel




with pd.ExcelWriter('out.xlsx', engine='xlsxwriter') as writer:
    
    
    df1=df1.style.set_properties(**{'text-align': 'center'})
    df2=df2.style.set_properties(**{'text-align': 'center'})
    #multiply option
    #df1=df1.style.set_properties(**{'text-align': 'center',
    #'color':'red', 
    #'font-size':'1.0rem',
    #'font-weight': 'bold',
    #'background-color': 'yellow' })
    
    
    df1.to_excel(writer, 'sheet1', index=False)
    worksheet = writer.sheets['sheet1']   
    worksheet.set_column(0, 2, 20)   
    
   
    df2.to_excel(writer, 'sheet2', index=False)
    #worksheet.set_column(1, 0, 20)
    worksheet = writer.sheets['sheet2'] 
    worksheet.set_column(0, 2, 20)

