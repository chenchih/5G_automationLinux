import re
elogfileName="elog_gnb_du_layer2.1.20230310.232915.782975"

#DL
with open(elogfileName, 'r') as filedata:    
    for line in filedata:                    
        #print(line)
        #if "m>>> DL-" in  line:
        if "mUL <<<-" in  line:
            #print(line.strip())
            
            for nextline in filedata:
                print(re.search(r'\[(\d+\.\d+\.\d+)\].*?(UL <<<- Mcs=[^]]+)', nextline))
            '''
                #if re.search(r'\[(\d+\.\d+\.\d+)\].*?(>>> DL- Mcs=[^]]+)', nextline):
                if re.search(r'\[(\d+\.\d+\.\d+)\].*?(UL <<<- Mcs=[^]]+)', nextline):
                    #print(line, nextline, end='')
                    print(line.strip())
                    print(nextline.strip())

                    break # so you can start looking for the first match again
            '''
                    
