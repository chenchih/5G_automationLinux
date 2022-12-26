import os
import re

result = []
filename="PDCP_result.txt"
def checkfile():
    if os.path.exists("result.txt"):
        print("file exist, delete file")
        os.remove(filename)

def getelement(li, element):
    ind = li.index(element)
    return li[ind+1]
    
def timeparse(data):
    datestr = data.split('[', 1)[1].split(']')[0]
    
    #search = re.findall(r'^\[([\d\.]+).+ingress traffic: ([\d\.]+).+egress traffic: ([\d\.]+).+.', data)
    searchtest=re.search(r'(ingress [^(]+).+(egress [^(]+)',data)
    m3New= searchtest.group(1)+", "+ searchtest.group(2) 
    m3New_1=m3New.replace(", ", ":").strip().split(':')
    
    #print(getelement(m3New_1, 'ingress traffic').strip())
    #print(getelement(m3New, 'ingress traffic'))
    #with list
    result.clear()
    #result.append(m3New)   
    #print(result)
    result.append(datestr)  
    result.append(getelement(m3New_1, 'ingress traffic').strip())    
    result.append(getelement(m3New_1, 'egress traffic').strip())

    #result.append(Tput)
    ###########Print or Write result ###########
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
    with open(filename, "a+") as f:
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
        if cycle % 3 == 0:
            print("")

def listprint_Method2():
    #####method1
    #for i in [result[c:c+2] for c in range(0,len(result)) if c%2 == 0]:
       #print(*i)
       
    #####method1-2 normal for loop

    temp = []
    for c in range(0, len(result)):
        if c % 3 == 0:
            temp.append(result[c:c+2])   
    #for i in temp:
    #    print(*i)        
    #temp is two array
    with open("result.txt", "a+") as f:
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

    with open('result.txt', 'a') as output:
        for index, c in enumerate(result):
            if index % 2 == 0:
                print(*result[index:index + 2], file=output)

    ###Method3
def listprint_Method4():
    results = iter(result)
   
    with open('result.txt', 'a') as output:
        for i in zip(results, results):
            print(*i, file=output)
             #file=output

def writefile():
    checkfile()
    with open(filename, 'a') as f:
        bar="#"*10
        #f.write(("datettime \t Tput  \n").expandtabs(22))
        f.write(("datettime ingress-traffic egress-traffic \n"))

        #f.write("="*50+"\n")

def ULDLprint(target):
    
    with open(elogfile, 'r') as filedata:
        for line in filedata:   
            if target in line:
                # Print the line, if the given string is found in the current line
                timeparse(line)
   
def emptywrite(status):
    with open(filename, "a") as f:
        f.write(f"="*25+status+"="*25+"\n")
###################################    
    # MAIN SCRIPT    
###################################
#elogfile="elog_gnb_cu_pdcp.0.20221121.173906.228825"

def main():
    accepted_strings = {'UL', 'DL', 'both'}
	#elogfile=input("enter elog: ")
    givenString=input("enter UL/DL/both: ")

    if givenString =="both":
        UL = 'PDCP UL'
        DL = 'PDCP DL'
        emptywrite("UL")
        #print(f"="*25+"UL"+"="*25)
        ULDLprint(UL)
        #split line ==
        emptywrite("DL")
        #print(f"="*25+"DL"+"="*25)
        ULDLprint(DL)

    elif givenString not in accepted_strings:
        print("Not found, please reenter correct option")
    else:   
        if givenString=="UL":
            emptywrite("UL")
            givenString='PDCP UL'
        elif givenString=="DL":
            emptywrite("DL")
            givenString='PDCP DL' 
            
        with open(elogfile, 'r') as filedata:
            for line in filedata:        
                if givenString in line:
                     # Print the line, if the given string is found in the current line
                     #print(line.strip())
                     timeparse(line)
                     
elogfile=input("enter elog: ")
while True:
    startscript= input("####press any key, q to exit script#####: ")
    if startscript =="q":
        break
    else:
        main()
