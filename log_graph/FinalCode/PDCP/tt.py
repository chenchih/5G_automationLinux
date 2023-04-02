lists = {}
current_key = None
with open ('PDCP_result.txt', 'r')as myfile:  
    readline=myfile.read().splitlines()
    
    for line in readline:
        if "=" in line:
            current_key = line.strip("=")   #split = so get UL or DL
                        
            lists[current_key] = []           
            #print(lists)
        else:

            #assert current_key is not None # there shouldn't be data before a header
            #print(lists[current_key])
            
            lists[current_key].append(line)
print("="*50)
print(lists["UL"])
print("="*50)
print(lists["DL"])
