''' update
- v3: add flex cdu parsing just
    - orignial is use for split cdu 
- adding process bar when parsing the log data
    - no adding this will not see what's going on in background
- checkfile(): remove files matching the pattern 'result-*' 
    - original will remove fixed file with result.txt
'''
import os, re, glob
from datetime import datetime
from tqdm import tqdm  # Import tqdm for progress bar

# Define filename for results
filename = f"result-{datetime.now():%Y-%m-%d-%H-%M-%S}.txt"
result = []

#will remove result.txt
def checkfile_old():
    if os.path.exists("result.txt"):
        print("File exists, deleting file...")
        s.remove("result.txt")
        
# Delete all files matching the pattern 'result-*'        
def checkfile():
    for file in glob.glob("result-*"):
        print(f"Deleting file: {file}...")
        os.remove(file)


def getelement(li, element):
    ind = li.index(element)
    return li[ind + 1]

def writefile(status):
    #checkfile()
    with open(filename, 'a') as f:
        f.write("=" * 25 + status + "=" * 25 + "\n")
        if 'D-UE' in status or 'DL' in status: 
            f.write(("datettime \t DL-Tput" + " " * 3 + "DL-RbNum " + "DL-MCS " + "DL-Bler\n").expandtabs(22))
        elif 'U-UE' in status or 'UL' in status:
            f.write(("datettime \t UL-Tput" + " " * 3 + "UL-RbNum " + "UL-MCS " + "UL-Bler\n").expandtabs(22))

def parse(data, ULDLstr):    
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
    listprint() 

def listprint():
    with open(filename, "a") as f:
        f.write(" ".join(result) + "\n")

def ULDLprint(target):
    try:
        with open(elogfileName, 'r') as filedata:
            lines = filedata.readlines()
            total_lines = len(lines)
            #qprint(f"Total lines to process: {total_lines}")  # Debugging output
            for line in tqdm(lines, total=total_lines, desc=f"Processing {target}"):
                if target in line:
                    parse(line, target)
    except Exception as e:
        print(f"An error occurred: {e}")
        
#without process         
def ULDLprint_original(target):
    with open(elogfileName, 'r') as filedata:
        for line in filedata:   
            if target in line:
                # Print the line, if the given string is found in the current line
                parse(line, target)
   
def main():
    global elogfileName
    elogfileName = input("Please enter your elog FileName: ")
    accepted_strings = re.compile(r"^(D-UE|U-UE)(\[\d\]|\[ \d\])?$|^both$")
    givenString = input("Please enter your search (Ex: D-UE / U-UE/ U-UE[ 0] / both:): ")

    if accepted_strings.match(givenString):
        if givenString == "both":
            writefile("UL")
            ULDLprint('U-UE')
            writefile("DL")
            ULDLprint('D-UE')
        else:        
            writefile(givenString)
            ULDLprint(givenString)
    else:
        print("Not found, please reenter correct option") 

# Main script execution
#while True:
startscript = input("####press any key, q to exit script#####: ")
if startscript == "q":
    #break
    exit
else:
    main()