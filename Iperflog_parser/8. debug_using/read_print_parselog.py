import re
from datetime import datetime
import time
def undirectional_maxtpt(elogfileName):
    max_results = 10  # Change to 20 if you want more                     
    count = 0         
    with open(elogfileName, 'r') as filedata:        
        lines = filedata.readlines()
        for line in lines:
            if "[SUM]" in line:
                #print(line.strip())
                match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (bits|Mbits|Gbits)/sec",line) 
                if match:
                    date_str = match.group(1)
                    transfer_str = match.group(2)
                    unit = match.group(3)
                    print(date_str, transfer_str, unit)
                    #print(line.strip())

                    date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                    formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
                    transfer_value = float(transfer_str)                                  
                    if unit == "Mbits":
                        transfer_value /= 1000.0
                    elif unit == "bits":
                        transfer_value /= 1000000000.0    
                    print(formatted_date, transfer_str, unit)
                    
                    print('-' * 80)  # for visual separation
                    count += 1
                    if count >= max_results:
                        print(f"Displayed first {max_results} results. Stopping.")
                        break

def bidirectional(elogfileName):
    max_results = 10  # Change to 20 if you want more                     
    count = 0    
  
    with open(elogfileName, 'r') as filedata:        
        lines = filedata.readlines()
        for line in lines:
            match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM]\[(RX-C|TX-C)\].*?([\d\.]+) (bits|Mbits|Gbits)/sec", line)
            if match:
                date_str = match.group(1)#datetime
                rx_tx = match.group(2)#TX-C and RX-C
                transfer_str = match.group(3)#tput value
                unit = match.group(4)#unit 
                
                # Increment the appropriate counter
  

                print(date_str, rx_tx, transfer_str, unit)
                
                date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
                transfer_value = float(transfer_str)                                  
                if unit == "Mbits":
                    transfer_value /= 1000.0
                elif unit == "bits":
                    transfer_value /= 1000000000.0    
                
                print(formatted_date, transfer_str, unit)
                print('-' * 80)  # for visual separation
                count += 1
                if count >= max_results:
               
                    print(f"Displayed first {max_results} results. Stopping.")
                    break

logfile= input("Please enter your elog FileName: ")
#undirectional_maxtpt(logfile)   
bidirectional(logfile)    

