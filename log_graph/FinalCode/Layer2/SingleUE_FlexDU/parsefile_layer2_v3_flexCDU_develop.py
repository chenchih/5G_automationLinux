import os, re
from datetime import datetime
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
        f.write(f"="*25+status+"="*25+"\n")
        #if 'D-UE' in status: 
        if 'D-UE' in status or 'DL' in status: 
            f.write(("datettime \t DL-Tput"+ " "*3+ "DL-RbNum " + "DL-MCS "+"DL-Bler\n").expandtabs(22))
        #elif 'U-UE' in status:
        elif 'U-UE' in status or 'UL' in status:
            f.write(("datettime \t UL-Tput"+ " "*3+ "UL-RbNum " + "UL-MCS "+"UL-Bler\n").expandtabs(22))

def parse_test(data, ULDLstr):    
    #get the time
    datestr = data.split('[', 1)[1].split(']')[0]  
    #search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^]]+)', data)
    #m3New= re.sub(r"[\(\[].*?[\)\]]", "",search.group(2)).replace(',','').strip().split()
    # Modify the regex to exclude 'A[', Matches starting with Tput= but stops before encountering the character 'A'
    search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^A]+)', data)
    m3New = re.sub(r"[\(\[].*?[\)\]]", "", search.group(2)).replace('=', '= ').replace(',', ' ').strip().split()
    #print(m3New)
    #print(getelement(m3New, 'Mcs='))
    result.clear()
    bler="Bler="
    result.append(datestr)
    #comment 
    result.append(getelement(m3New, 'Tput='))
    result.append(getelement(m3New, 'RB= ')) 
    result.append(getelement(m3New, 'Mcs='))
    result.append(getelement(m3New, bler))
    #print(result)

def parse(data, ULDLstr):    
    #get the time
    datestr = data.split('[', 1)[1].split(']')[0]  
    #search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^]]+)', data)
    #m3New= re.sub(r"[\(\[].*?[\)\]]", "",search.group(2)).replace(',','').strip().split()
    search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^A]+)', data)
    m3New = re.sub(r"[\(\[].*?[\)\]]", "", search.group(2)).replace('=', '= ').replace(',', ' ').strip().split()
    result.clear()

    givenString=ULDLstr
    #givenString = input("Please enter your search(Ex: DL- UE or UL- UE):")
    #print(givenString)
    bler="Bler="
    result.append(datestr)    
    #print(getelement(m3New, 'Tput='),' ', getelement(m3New, 'RbNum='), '', getelement(m3New, 'Mcs='))
    
    #comment 
    result.append(getelement(m3New, 'Tput='))
    result.append(getelement(m3New, 'RB='))
    result.append(getelement(m3New, 'Mcs='))
    result.append(getelement(m3New, bler))

    #print(result)
    listprint() #write file =>ok
    #listprint2() #print =>ok
    #listprint_Method2()  # write file =>ok
    #listprint_Method3() #write file =>ok
    #listprint_Method4()
    
#write to file
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
        f.write(f"="*25+status+"="*25+"\n")
  
def listprint2():
    cycle = 0
    for element in result:
        cycle += 1
        #print(element, end="")
        print(element, end=" ")
        if cycle % 6 == 0:
            print("")
            
def ULDLprint(target):
    
    with open(elogfileName, 'r') as filedata:
        for line in filedata:   
            if target in line:
                # Print the line, if the given string is found in the current line
                parse(line, target)
   

def main_backup_test_flex():
    print("update flex CDU")
    #accepted_strings =re.compile(r"([DU]-\ UE(\[\ {0,1}(\d)\])?)|both$")
    accepted_strings = re.compile(r"^(D-UE|U-UE)(\[\d\]|\[ \d\])?$|^both$")
    givenString = input("Please enter your search (Ex: D-UE / U-UE/ U-UE[ 0] / both:):")
    if accepted_strings.match(givenString):
        print("jeeee")

def main():
    #elogfileName= input("Please enter your elog FileName: ")
    #accepted_strings = {'DL- UE', 'UL- UE', 'both', 'UL- UE[ ' }
    #accepted_strings = re.compile(r"([DU]L\-\ UE(\[\ (\d)\])?)|both$")
    #accepted_strings = re.compile(r"([DU]L\-\ UE(\[\ {0,1}(\d)\])?)|both$")
    #accepted_strings = re.compile(r"([DU]L\-\ UE(\[\s*(\d{1,2})\])?)|both$")
    #accepted_strings =re.compile(r"([DU]-\ UE(\[\ {0,1}(\d)\])?)|both$")
    accepted_strings = re.compile(r"^(D-UE|U-UE)(\[\d\]|\[ \d\])?$|^both$")
    givenString = input("Please enter your search (Ex: D-UE / U-UE/ U-UE[ 0] / both:):")

    if accepted_strings.match(givenString):
        if givenString =="both":
            UL = 'U-UE'
            DL = 'D-UE'
            writefile("UL")

            #emptywrite("UL")
            #print(f"="*25+"UL"+"="*25)
            ULDLprint(UL)
            #split line ==
            #emptywrite("DL")
            writefile("DL")
            #print(f"="*25+"DL"+"="*25)
            ULDLprint(DL)
            #ULprint()
            #DLprint()
        else:      
            #emptywrite(givenString)     
            writefile(givenString)
            with open(elogfileName, 'r') as filedata:
                
                for line in filedata:   
                    if givenString in line:
                        
                        # Print the line, if the given string is found in the current line
                        #print(line.strip())
                        parse(line, givenString)
    else:
        print("Not found, please reenter correct option") 

###################################################################################
elogfileName= input("Please enter your elog FileName: ")
while True:
    startscript= input("####press any key, q to exit script#####: ")
    if startscript =="q":
        break
    else:
        main()

   

