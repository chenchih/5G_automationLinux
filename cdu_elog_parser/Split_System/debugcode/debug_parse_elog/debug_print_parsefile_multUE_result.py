#limit the number of results printed
import re
def readall(elogfileName):    
    with open(elogfileName, 'r') as filedata:    
        for line in filedata:   
        #print(line)
            if "m>>> DL-" in  line:  
            #if "mUL <<<-" in  line:
                #print(line.strip())
                for nextline in filedata:
                        #print(re.search(r'\[(\d+\.\d+\.\d+)\].*?(UL <<<- Mcs=[^]]+)', nextline))
                        if re.search(r'\[(\d+\.\d+\.\d+)\].*?(>>> DL- Mcs=[^]]+)', nextline):
                            #print(line, nextline, end='')
                            print(line.strip())
                            print(nextline.strip()) #so you can start looking for the first match again

def readMmatch_single(elogfileName):
    max_results = 10  # Change to 20 if you want more                     
    count = 0         
    with open(elogfileName, 'r') as filedata:
        for line in filedata:
            if "UL- UE" in line:
                match = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^]]+)', line)
                if match:
                    print(line.strip())
                    print('-' * 80)  # for visual separation
                    count += 1
                    if count >= max_results:
                        print(f"Displayed first {max_results} results. Stopping.")
                        break
                        
def readMmatch(elogfileName):                         
    max_results = 10  # Change to 20 if you want more                     
    count = 0         
    with open(elogfileName, 'r') as filedata:
        for line in filedata:
            if "m>>> DL-" in line:
                for nextline in filedata:
                    match = re.search(r'\[(\d+\.\d+\.\d+)\].*?(>>> DL- Mcs=[^]]+)', nextline)
                    if match:
                        print(line.strip())
                        print(nextline.strip())
                        print('-' * 80)  # for visual separation
                        count += 1
                        if count >= max_results:
                            print(f"Displayed first {max_results} results. Stopping.")
                            break
                if count >= max_results:
                    break
                    
#elogfileName="elog.txt"               
elogfileName= input("Please enter your elog FileName: ")
#readall(elogfileName)
#readMmatch(elogfileName)
readMmatch_single(elogfileName)