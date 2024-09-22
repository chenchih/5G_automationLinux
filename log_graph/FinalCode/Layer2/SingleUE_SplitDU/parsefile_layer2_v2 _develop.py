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
    m3New= re.sub("[\(\[].*?[\)\]]", "",search.group(2)).replace(',','').strip().split()
    result.clear()
    givenString=ULDLstr
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
    result.append(getelement(m3New, 'Tput='))
    result.append(getelement(m3New, 'RbNum='))
    result.append(getelement(m3New, 'Mcs='))
    result.append(getelement(m3New, bler1))
    result.append(getelement(m3New, bler2))

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
    with open(filename, "a") as f:
        for element in result:            
            #print(element+ " ")
            f.write(element+ " ")     
        f.write("\n")
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
def main():
    #elogfileName= input("Please enter your elog FileName: ")
    #accepted_strings = re.compile(r"([DU]L\-\ UE(\[\ {0,1}(\d)\])?)|both$")
    accepted_strings = re.compile(r"([DU]L\-\ UE(\[\s*(\d{1,2})\])?)|both$")
    givenString = input("Please enter your search (Ex: DL- UE / UL- UE / UL- UE[ 0] / both:):")

    
    if accepted_strings.match(givenString):
        
        if givenString =="both":
            UL = 'UL- UE'
            DL = 'DL- UE'
            writefile("UL")
            ULDLprint(UL)
            writefile("DL")
            ULDLprint(DL)
        else:         
            writefile(givenString)
            with open(elogfileName, 'r') as filedata:
                for line in filedata:   
                    if givenString in line:
                         parse(line, givenString)
    else:
        print("Not found, please reenter correct option") 
elogfileName= input("Please enter your elog FileName: ")
while True:
    startscript= input("####press any key, q to exit script#####: ")
    if startscript =="q":
        break
    else:
        
        main()

   

