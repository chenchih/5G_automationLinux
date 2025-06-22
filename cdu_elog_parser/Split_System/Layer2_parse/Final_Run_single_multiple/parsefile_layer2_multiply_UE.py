import os, re
from datetime import datetime
from tqdm import tqdm  # Import tqdm for progress bar

filename=f"result-{datetime.now():%Y-%m-%d-%H-%M-%S}.txt"
result = []

def checkfile():
    if os.path.exists("result.txt"):
        print("file exist, delete file")
        os.remove("result.txt")

def getelement(li, element):
    ind = li.index(element)
    return li[ind+1]
        
def writefile(status):
    checkfile()
    with open(filename, 'a') as f:
        bar="#"*10
        f.write((f"datettime \t {status}_Tput(ingress) {status}_Tput(egress) {status}_RbNum {status}_MCS {status}_Bler {status}_nonWdBler\n").expandtabs(22))

def new(line):
    if re.search(r'\[(\d+\.\d+\.\d+)\].*?(>>> DL- Mcs=[^]]+)', line):
        parse_bler(line, 'DL')          

def parse(data, ULDLstr):   
    #get tput value
    datestr = data.split('[', 1)[1].split(']')[0]  
    Tputvalue=re.search(r'(ingress [^(]+).+(egress [^(]+)',data)
    m3New= Tputvalue.group(1)+", "+ Tputvalue.group(2) 
    m3New_1=m3New.replace(", ", ":").strip().split(':')
    result.append(datestr)
    result.append(getelement(m3New_1, 'ingress traffic').strip())
    result.append(getelement(m3New_1, 'egress traffic').strip())    

    #listprint2()
    #listprint()
    #result.clear()
    #search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^]]+)', data)
        
def parse_bler(data, ULDLstr): 
    #get bler
    blerresult = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Mcs=[^]]+)', data)
    blerDL= re.sub(r"[\(\[].*?[\)\]]", "",blerresult.group(2)).replace(',','').strip().split()
    
    if ULDLstr in 'DL':
        bler1="PdschBler="
        bler2="nonWPdschBler="
        
    elif ULDLstr in 'UL':
        bler1="PuschBler="
        bler2="nonWPuschBler="
        
    #print(m3New2)
    #print(getelement(blerDL, 'RbNum='))
    result.append(getelement(blerDL, 'RbNum='))
    result.append(getelement(blerDL, 'Mcs='))
    result.append(getelement(blerDL, bler1).strip())
    result.append(getelement(blerDL, bler2).strip())
        
    listprint()
    result.clear()

def listprint():
    #checkfile()
    cycle = 0    
    #    with open("result.txt", "a+") as f:    
    with open(filename, "a") as f:
        for element in result:            
            #print(element+ " ")
            f.write(element+ " ")     
        f.write("\n")
    
        #f.write()
def emptywrite(status):
    with open(filename, "a") as f:
        #f.write(f"hello\n")
        f.write(f"="*25+status+"="*25+"\n")
  
def listprint2():
    cycle = 0
    for element in result:
        cycle += 1
        #print(element, end="")
        print(element, end=" ")
        if cycle % 3 == 0:
            print("")
            
def ULDLprint(target):

    with open(elogfileName, 'r') as filedata:
        for line in filedata:   
            if target in line:
                # Print the line, if the given string is found in the current line
                parse(line, target)
                
#noprogressbar
def main2(elogfileName):
    countUL =0 
    countDL =0
            
##########################
    with open(elogfileName, 'r') as filedata:    
        for line in filedata:                    
            #print(line)
            if "m>>> DL-" in  line:
                if countDL == 0:
                    emptywrite("DL")
                    writefile("DL")
                    countDL+=1
                for nextline in filedata:
                    if re.search(r'\[(\d+\.\d+\.\d+)\].*?(>>> DL- Mcs=[^]]+)', nextline):
                        #print(line, nextline, end='')
                        givenString="DL"
                        #print(line.strip())
                        parse(line, givenString)
                        #print(nextline.strip())
                        parse_bler(nextline, givenString)
                        
                        break # so you can start looking for the first match again
                        
    with open(elogfileName, 'r') as filedata:    
        for line in filedata:                    
            #print(line)
            if "mUL <<<-" in  line: 
                if countUL == 0:
                    emptywrite("UL")
                    writefile("UL")
                    countUL+=1
                for nextline in filedata:
                    #if re.search(r'\[(\d+\.\d+\.\d+)\] .*?(>>> DL- Mcs=[^]]+)', nextline):
                        #if re.search(r'\[(\d+\.\d+\.\d+)\]', nextline):
                    if re.search(r'\[(\d+\.\d+\.\d+)\].*?(UL <<<- Mcs=[^]]+)', nextline):
                        #print(line, nextline, end='')
                        givenString="UL"
                        #print(line.strip())
                        parse(line, givenString)
                        #print(nextline.strip())
                        parse_bler(nextline, givenString)
                        
                        break # so you can start looking for the first match again


def main(elogfileName):
    countUL =0 
    countDL =0
            
##########################
    # Read the file content once into a list of lines for efficient multiple passes
    try:
        with open(elogfileName, 'r') as f_read:
            all_lines = f_read.readlines()
        total_lines = len(all_lines)
    except FileNotFoundError:
        print(f"Error: Elog file '{elogfileName}' not found. Please check the name.")
        return # Exit main if file doesn't exist
    except Exception as e:
        print(f"An error occurred while reading '{elogfileName}': {e}")
        return
        
    #with open(elogfileName, 'r') as filedata: 
        # --- DL Parsing pass with TQDM ---
    print("\nStarting DL data parsing...")
    #for line in filedata:   
    for i, line in enumerate(tqdm(all_lines, total=total_lines, desc="Processing DL", unit=" lines")):        
        #print(line)
        if "m>>> DL-" in  line:  
            if countDL == 0:
                emptywrite("DL")
                writefile("DL")
                countDL+=1
                
            #for nextline in filedata:    
            for j in range(i + 1, total_lines): # Start looking from the line after current
                nextline = all_lines[j]    
                
                if re.search(r'\[(\d+\.\d+\.\d+)\].*?(>>> DL- Mcs=[^]]+)', nextline):
                    #print(line, nextline, end='')
                    givenString="DL"
                    #print(line.strip())
                    parse(line, givenString)
                    #print(nextline.strip())
                    parse_bler(nextline, givenString)
                    
                    break # so you can start looking for the first match again
    # --- UL Parsing pass with TQDM ---
    #print("\nStarting UL data parsing...")               
    #with open(elogfileName, 'r') as filedata:    
    for i, line in enumerate(tqdm(all_lines, total=total_lines, desc="Processing UL", unit=" lines")):
    #for line in filedata:                    
        #print(line)
        
        if "mUL <<<-" in  line: 
            if countUL == 0:
                emptywrite("UL")
                writefile("UL")
                countUL+=1
            for j in range(i + 1, total_lines):   
                nextline = all_lines[j]            
            #for nextline in filedata:
                #if re.search(r'\[(\d+\.\d+\.\d+)\] .*?(>>> DL- Mcs=[^]]+)', nextline):
                    #if re.search(r'\[(\d+\.\d+\.\d+)\]', nextline):
                if re.search(r'\[(\d+\.\d+\.\d+)\].*?(UL <<<- Mcs=[^]]+)', nextline):
                    #print(line, nextline, end='')
                    givenString="UL"
                    #print(line.strip())
                    parse(line, givenString)
                    #print(nextline.strip())
                    parse_bler(nextline, givenString)
                    
                    break # so you can start looking for the first match again
    
    return filename
    

###################################################################################
if __name__ == "__main__":
    try:
        elogfileName= input("Please enter your elog FileName: ")
        if elogfileName:
            main(elogfileName)
            #main2(elogfileName)
        else:
            print("No elog file name provided. Exiting.")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user (Ctrl+C). Exiting gracefully.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Exiting.")
       

'''
startscript= input("####press any key, q to exit script#####: ")
main()

while True:
    startscript= input("####press any key, q to exit script#####: ")
    if startscript =="q":
        break
    else:
        
        main()
'''
   

