import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Excel file into a pandas DataFrame
data = pd.read_excel('2.xlsx')

# Extract datetime and Tput columns
datetime = data['datetime']
tput = data['Tput']
mcs = data['MCS']
# Convert the datetime column to numeric values using NumPy
x = np.arange(len(datetime))
#plt.figure(figsize=(25, 6.5))
plt.figure(figsize=(15,5), dpi=300)
# Plot the line graph
plt.plot(datetime, tput, label='DL')
plt.plot(datetime, mcs, label='MCS')

plt.xlabel('time')
plt.ylabel('Tput')
plt.title('TPUT')

#tick_interval = 15  # Adjust the interval as per your preference
#plt.xticks(range(0, len(datetime), tick_interval), rotation=90)
plt.xticks( np.linspace(0, len(datetime)-1, 100 ),rotation=90 )


plt.legend()
#adjust the layout 
plt.tight_layout() 
#plt.show()

plt.savefig('tput.png')