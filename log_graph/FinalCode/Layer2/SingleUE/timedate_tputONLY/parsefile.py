import os
givenString = "DL- ingress traffic"
#givenString = "DL- UE"
result = []
filename="result.txt"

def checkfile():
    if os.path.exists("result.txt"):
        print("file exist, delete file")
        os.remove("result.txt")
       
def timeparse(data):
    #parse the date and time
    datestr = data.split('[', 1)[1].split(']')[0]
    Tput = data.split(" DL- ingress traffic:", 1)[1].split(',')[0].split('(')[0].strip()
    '''   
    with open("result.txt", "a+") as f:
    #with open("result.txt", "w") as f:
        for i in result:
            f.write(datestr +" "+Tput +"\n") 
'''
    #list
    result.clear()
    result.append(datestr)    
    result.append(Tput)
    listprint() #write file =>ok
    listprint2() #print =>ok
    #listprint_Method2()  # write file =>ok
    #listprint_Method3() #write file =>ok
    #listprint_Method4()
    
#write to file
def listprint():
    #checkfile()
    cycle = 0    
    with open(filename, "a") as f:
        cycle += 1
        for element in result:            
            #print(element+ " ")
            f.write(element+ " ")           
        f.write("\n")
#print
def listprint2():
    
    cycle = 0
    for element in result:
        cycle += 1
        print(element, end=" ")
        #print ('='*30)
        if cycle % 2 == 0:
            print(" ")

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
            f.write(my_str + "\n")          

def listprint_Method3():
    #for index, c in enumerate(result):
    #    if index % 2 == 0:
    #        print(*result[index:index + 2])
    with open('result.txt', 'a') as output:
        for index, c in enumerate(result):
            if index % 2 == 0:
                print(*result[index:index + 2], file=output)

def listprint_Method4():
    results = iter(result)
   
    with open('result.txt', 'a') as output:
        for i in zip(results, results):
            print(*i, file=output)
             #file=output

def writefile():
    checkfile()
    with open(filename, 'a') as f:
        f.write(("datettime \t Tput  \n").expandtabs(22))
        f.write("="*30+ "\n")

###################################    
    # MAIN SCRIPT    
###################################
elogfile=input("Please enter your elog file:")
writefile()
print ('datetime \t \t tput')
print ('='*30)
with open(elogfile, 'r') as filedata:
    for line in filedata:   
        if givenString in line:
             # Print the line, if the given string is found in the current line
             #print(line.strip())
             timeparse(line)
#print list value
print ("="*30)
#print(result)
