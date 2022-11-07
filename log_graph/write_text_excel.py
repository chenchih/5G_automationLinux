from datetime import datetime
import pandas as pd
filename=f"result-{datetime.now():%Y-%m-%d %H-%m-%d}.txt"


#new_list = [["first", "second"], ["third", "four"], ["five", "six"]]
df = pd.DataFrame(new_list)
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()



#with open(filename, 'w') as f:
#    f.write(("datettime  \t put  MCS\n").expandtabs(10))
#    f.write("="*50)
