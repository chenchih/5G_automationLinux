import os, re
from datetime import datetime
elogfileName= input("Please enter your elog FileName:")
givenString = input("Please enter your search(Ex: DL- UE or UL- UE or UL- UE[ 0]:):")

filename=f"result-{datetime.now():%Y-%m-%d %H-%M-%S}.txt"
elog_parse="elogResult.txt"
result = []

def checkfile():
    if os.path.exists(filename):
        print("file exist, delete file")
        os.remove(filename)
def getelement(li, element):
    ind = li.index(element)
    return li[ind+1]
def parse(data):    
    #get the time
    datestr = data.split('[', 1)[1].split(']')[0]
    #split from tput
    search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^]]+)', data)
    m3New= re.sub("[\(\[].*?[\)\]]", "",search.group(2)).replace(',','').strip().split() 
    result.clear()
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
    #listprint() #write file =>ok
    #listprint2() #print =>ok
    listprint_Method2()  # write file =>ok
    #listprint_Method3() #write file =>ok
    #listprint_Method4()
    
def timeparse(data):
    datestr = data.split('[', 1)[1].split(']')[0]
    Tput = data.split(" DL- ingress traffic:", 1)[1].split(',')[0].split('(')[0].strip()
    #with list
    result.clear()
    result.append(datestr)    
    result.append(Tput)
   
    #print(result)
    #listprint() #write file =>ok
    #listprint2() #print =>ok
    listprint_Method2()  # write file =>ok
    #listprint_Method3() #write file =>ok
    #listprint_Method4()
    
#write to file
def listprint():
    #checkfile()
    cycle = 0    
    #    with open("result.txt", "a+") as f:
    with open(filename, "a") as f:
        
        cycle += 1
        for element in result:            
            #print(element+ " ")
            f.write(element+ " ")           
        f.write("\n")
        #f.write()

#print
def listprint2():
    cycle = 0
    
    for element in result:
        cycle += 1
        #print(element, end="")

        print(element, end=" ")
        if cycle % 6 == 0:
            print("")

def listprint_Method2():
#####method1
    #for i in [result[c:c+2] for c in range(0,len(result)) if c%2 == 0]:
       #print(*i) 
#####method1-2 normal for loop
    temp = []
    for c in range(0, len(result)):
        if c % 6 == 0:
            temp.append(result[c:c+6])   
    #for i in temp:
    #    print(*i)        
    #temp is two array
    with open(filename, "a+") as f:
        for file in temp:
            #file = file.strip()
            my_str = ' '.join(file)
            #print(type(my_str))
            f.write(my_str + "\n")

def listprint_Method3():
    ###Method2
    #for index, c in enumerate(result):
    #    if index % 2 == 0:
    #        print(*result[index:index + 2])

    with open(filename, 'a') as output:
        for index, c in enumerate(result):
            if index % 2 == 0:
                print(*result[index:index + 2], file=output)

def listprint_Method4():
    results = iter(result)
    with open(filename, 'a') as output:
        for i in zip(results, results):
            print(*i, file=output)
             #file=output

def writefile():
    checkfile()
    with open(filename, 'a') as f:
        bar="#"*10
        f.write(("datettime \t Tput"+ " "*3+ "RbNum " + "MCS "+"Bler " +"nonWdBler\n").expandtabs(22))

def saveresult(elogresult):   
    with open(elog_parse, 'a+') as f:
        f.write(elogresult.strip()+"\n" )

###################################    
    # MAIN SCRIPT    
###################################
#filename="result.txt"

writefile()
with open(elogfileName, 'r') as filedata:
    for line in filedata:   
        if givenString in line:
             parse(line)          
#print list value
print ("="*30)
