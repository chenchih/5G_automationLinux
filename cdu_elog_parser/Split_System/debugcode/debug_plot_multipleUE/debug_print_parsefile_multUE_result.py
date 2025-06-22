import re
#elogfileName="elog.txt"
elogfileName=input('enter logfile name: ')
#DL
with open(elogfileName, 'r') as filedata:    
    for line in filedata:                    
        #print(line)
        if "m>>> DL-" in  line:
        #if "mUL <<<-" in  line:
            #print(line.strip())
            
            for nextline in filedata:
                #print(re.search(r'\[(\d+\.\d+\.\d+)\].*?(UL <<<- Mcs=[^]]+)', nextline))
          
                if re.search(r'\[(\d+\.\d+\.\d+)\].*?(>>> DL- Mcs=[^]]+)', nextline):
                #if re.search(r'\[(\d+\.\d+\.\d+)\].*?(UL <<<- Mcs=[^]]+)', nextline):
                    #print(line, nextline, end='')
                    print(line.strip())
                    print(nextline.strip())

                    break # so you can start looking for the first match again
            
                    
