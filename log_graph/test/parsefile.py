givenString = "DL- ingress traffic"
result = []
def timeparse(data):
    datestr = data.split('[', 1)[1].split(']')[0]
    Tput = data.split(" DL- ingress traffic:", 1)[1].split(',')[0].split('(')[0].strip()
    result.append(datestr)
    #save to list
    result.append(Tput)
    # without saving to list can print instead
    print(datestr, Tput)
    #return datestr
    #writefile(datestr,Tput)
    writefile2()
def writefile2():
    with open("result.txt", "w") as f:
        for i in result:
            f.write(i + " " + "\n")
            
def writefile(time,tput):
    print("====")
    print(time, tput)
    with open("result.txt", "w") as f:
        for i in result:
            f.write(time +" "+tput +"\n")


with open('elog', 'r') as filedata:
    for line in filedata:   
        if givenString in line:

             # Print the line, if the given string is found in the current line
             #print(line)
             timeparse(line)
#print list value
print ("="*30)
#print(result)
#####method1
#for i in [result[c:c+2] for c in range(0,len(result)) if c%2 == 0]:
   #print(*i)
   
#####method1-2 normal for loop

temp = []
for c in range(0, len(result)):
    if c % 2 == 0:
        temp.append(result[c:c+2])


"""
for i in temp:
    print(*i)
    
#temp is two array
with open("result.txt", "a+") as f:
    for file in temp:
        #file = file.strip()
        my_str = ' '.join(file)
        #print(type(my_str))
        f.write(my_str + "\n")
"""



###Method2
#for index, c in enumerate(result):
#    if index % 2 == 0:
 #       print(*result[index:index + 2])

###Method3

#results = iter(result)
#for i in zip(results, results):
#    print(*i)

print("end")