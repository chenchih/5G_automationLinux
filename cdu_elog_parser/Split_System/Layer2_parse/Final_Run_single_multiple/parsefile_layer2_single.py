import os, re
from datetime import datetime
from tqdm import tqdm  # Import tqdm for progress bar

result_filename=f"result-{datetime.now():%Y-%m-%d-%H-%M-%S}.txt"
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
    with open(result_filename, 'a') as f:
        #bar="#"*10
        f.write(f"="*25+status+"="*25+"\n")
        if 'DL' in status: 
            f.write(("datettime \t DL-Tput"+ " "*3+ "DL-RbNum " + "DL-MCS "+"DL-Bler " +"DL-nonWPdschBler\n").expandtabs(22))
        
        elif  'UL' in status: 
            f.write(("datettime \t UL-Tput"+ " "*3+ "UL-RbNum " + "UL-MCS "+"UL-Bler " +"UL-nonWPuschBler\n").expandtabs(22))

def parse(data, ULDLstr):    
    #get the time
    datestr = data.split('[', 1)[1].split(']')[0]  
    search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^]]+)', data)
    m3New= re.sub(r"[\(\[].*?[\)\]]", "",search.group(2)).replace(',','').strip().split()

    result.clear()

    givenString=ULDLstr
    #givenString = input("Please enter your search(Ex: DL- UE or UL- UE):")
    #print(givenString)
    bler1=""
    bler2=""
    
    if givenString in 'DL- UE' or 'DL- UE' in givenString :
        bler1="PdschBler="
        bler2="nonWPdschBler="
    elif givenString in 'UL- UE' or 'UL- UE' in givenString :
        bler1="PuschBler="
        bler2="nonWPuschBler="
    else: 
        print("givenString Not found string")

    result.append(datestr)    
    #print(getelement(m3New, 'Tput='),' ', getelement(m3New, 'RbNum='), '', getelement(m3New, 'Mcs='))
    
    result.append(getelement(m3New, 'Tput='))
    result.append(getelement(m3New, 'RbNum='))
    result.append(getelement(m3New, 'Mcs='))
    result.append(getelement(m3New, bler1))
    result.append(getelement(m3New, bler2))

    #print(result)
    listprint() #write file =>ok

#write to file
def listprint():
    #checkfile()
    cycle = 0    
    #with open("result.txt", "a+") as f:    
    with open(result_filename, "a") as f:
        for element in result:            
            #print(element+ " ")
            f.write(element+ " ")     
        f.write("\n")

def emptywrite(status):
    with open(result_filename, "a") as f:
        f.write(f"="*25+status+"="*25+"\n")
  
def listprint2():
    cycle = 0
    for element in result:
        cycle += 1
        #print(element, end="")
        print(element, end=" ")
        if cycle % 6 == 0:
            print("")
            
def ULDLprint(target, elogfileName):
    try: #mew add for progress bar
        with open(elogfileName, 'r') as filedata:
            lines = filedata.readlines() #mew add for progress bar
            total_lines = len(lines) #mew add for progress bar
            #for line in filedata:  
            for line in tqdm(lines, total=total_lines, desc=f"Processing {target}"):   #mew add for progress bar     
                if target in line:
                    # Print the line, if the given string is found in the current line
                    parse(line, target)
    except Exception as e: #mew add for progress bar
        print(f"An error occurred: {e}")                
                

def main(elogfile):
    #accepted_strings = {'DL- UE', 'UL- UE', 'both', 'UL- UE[ ' }
    #accepted_strings = re.compile(r"([DU]L\-\ UE(\[\ (\d)\])?)|both$")
    #accepted_strings = re.compile(r"([DU]L\-\ UE(\[\ {0,1}(\d)\])?)|both$")
    
    #accepted_strings = re.compile(r"([DU]L\-\ UE(\[\s*(\d{1,2})\])?)|both$")
    #givenString = input("Please enter your search (Ex: DL- UE / UL- UE / UL- UE[ 0] / both:):")

    UL = 'UL- UE'
    DL = 'DL- UE'
    writefile("UL")
    ULDLprint(UL, elogfile)
    writefile("DL")
    ULDLprint(DL, elogfile)
    return result_filename
    
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
    elogfileName= input("Please enter your elog FileName: ")
    if elogfileName:
        main(elogfileName)


while True:
    startscript= input("####press any key, q to exit script#####: ")
    if startscript =="q":
        break
    else:        
        main()
'''
   

