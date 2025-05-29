''' update
- v3: add flex cdu parsing just
    - orignial is use for split cdu 
- adding process bar when parsing the log data
    - no adding this will not see what's going on in background
- checkfile(): remove files matching the pattern 'result-*' 
    - original will remove fixed file with result.txt

- user no need to input, will capture both as default, chnage main() code cleaner
'''
import os, sys, re, glob
from datetime import datetime
from tqdm import tqdm  # Import tqdm for progress bar

#parse the result and store into list
result = []

def getelement(li, element):
    ind = li.index(element)
    return li[ind + 1]
    
#write UL/DL and header into txt file
def writefile(status, filename):
    #checkfile()
    with open(filename, 'a') as f:
        f.write("=" * 25 + status + "=" * 25 + "\n")
        if 'D-UE' in status or 'DL' in status: 
            f.write(("datettime \t DL-Tput" + " " * 3 + "DL-RbNum " + "DL-MCS " + "DL-Bler\n").expandtabs(22))
        elif 'U-UE' in status or 'UL' in status:
            f.write(("datettime \t UL-Tput" + " " * 3 + "UL-RbNum " + "UL-MCS " + "UL-Bler\n").expandtabs(22))

def parse(data, ULDLstr,filename):    
    # Get the time
    datestr = data.split('[', 1)[1].split(']')[0]  
    search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^A]+)', data)
    m3New = re.sub(r"[\(\[].*?[\)\]]", "", search.group(2)).replace('=', '= ').replace(',', ' ').strip().split()
    result.clear()
    bler = "Bler="
    result.append(datestr)    
    result.append(getelement(m3New, 'Tput='))
    result.append(getelement(m3New, 'RB='))
    result.append(getelement(m3New, 'Mcs='))
    result.append(getelement(m3New, bler))
    listprint(filename) 
    
#write data into file
def listprint(filename):
    with open(filename, "a") as f:
        f.write(" ".join(result) + "\n")
        
#progress bar:open elog file and parse the realted string parameter 
def ULDLprint(target, elogfileName,filename):
    try:
        with open(elogfileName, 'r') as filedata:
            lines = filedata.readlines()
            total_lines = len(lines)
            #qprint(f"Total lines to process: {total_lines}")  # Debugging output
            for line in tqdm(lines, total=total_lines, desc=f"Processing {target}"):
                if target in line:
                    parse(line, target,filename)
    except Exception as e:
        print(f"An error occurred: {e}")
        
#without process: open elog file and parse the realted string parameter       
def ULDLprint_original(target, elogfileName,filename):
    with open(elogfileName, 'r') as filedata:
        for line in filedata:   
            if target in line:
                # Print the line, if the given string is found in the current line
                parse(line, target, filename)
   
def main(elogfileName='elog_gnb_du_layer2.0'):
    #result filename
    filename = f"result-{datetime.now():%Y-%m-%d-%H-%M-%S}.txt"
    #elogfileName=logfilename
    #elogfileName = 'elog_gnb_du_layer2.0'
    print(elogfileName)
    
    # Check if the log file not exist exit 
    if not os.path.isfile(elogfileName): 
        print('elog_files not exist, please check your file again')
        input("Press any key to exit...")  # Prompt the user to press a key
        sys.exit()  # Use sys.exit() for a clean exit

    givenString='both'
    if givenString=='both':
        modes = [("UL", 'U-UE'), ("DL", 'D-UE')]
        for mode, string in modes:
            writefile(mode,filename) #write UL and DL into file
            ULDLprint(string, elogfileName,filename) #
    return filename

if __name__ == "__main__":
    main(elogfileName='elog_gnb_du_layer2.0')