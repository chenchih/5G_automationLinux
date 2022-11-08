
# Read Text Files with Pandas using read_csv()
  
# importing pandas
import pandas as pd
  
# read text file into pandas DataFrame
#df = pd.read_csv("result.txt", sep=" ")
  
# display DataFrame
#print(df)


df = pd.read_table('result.txt')
df.to_excel('output.xlsx', 'Sheet1')