import os, re
givenString = "DL- UE"
#givenString = "DL- UE"
result = []
filename="result.txt"

def checkfile():
    if os.path.exists("result.txt"):
        print("file exist, delete file")
        os.remove("result.txt")

def parse(data):       
    datestr = data.split('[', 1)[1].split(']')[0]
    search=re.findall(r"[0-9]*\.[0-9]+", data)
    #print(f"datetime: {datestr} TPUT: {search[2]} MCS: {search[3]} RbNum: {search[4]}, ReTxRatio: {search[5]}")
    #print(search[2])
    
    result.clear()
    result.append(datestr)    
    result.append(search[2])
    result.append(search[3])
    #print(result)
    listprint() #write file =>ok
    #listprint2() #print =>ok
    #listprint_Method2()  # write file =>ok
    #listprint_Method3() #write file =>ok
    #listprint_Method4()
    
def timeparse(data):
    datestr = data.split('[', 1)[1].split(']')[0]
    Tput = data.split(" DL- ingress traffic:", 1)[1].split(',')[0].split('(')[0].strip()

    '''   
    with open("result.txt", "a+") as f:
    #with open("result.txt", "w") as f:
        for i in result:
            f.write(datestr +" "+Tput +"\n") 
'''
    #with list
    result.clear()
    result.append(datestr)    
    result.append(Tput)
   
    print(result)
    #listprint() #write file =>ok
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
        if c % 2 == 0:
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
        f.write(("datettime \t Tput"+ " "*3+ "MCS\n").expandtabs(24))
        f.write("="*50+"\n")

    
###################################    
    # MAIN SCRIPT    
###################################
writefile()
#with open('elog', 'r') as filedata:
#print ("datettime  \t \t Tput  MCS")
#print ("="*50)
with open('elogshort', 'r') as filedata:
    for line in filedata:   
        if givenString in line:

             # Print the line, if the given string is found in the current line
            #print(line.strip())
             #timeparse(line)
             parse(line)
#print list value
print ("="*30)
#print(result)
