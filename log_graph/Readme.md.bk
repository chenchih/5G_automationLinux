## Intro
I am going to develop drawing a graph when reading data.
 

## checklist version 
- [x] init
- [x] anlaysic data get datetime and tput value
- [x] anlaysic data more value
- [ ] draw graph

## Step Manual Test 
1. Please put your log file in this file
2. run the code : py parsefile.py
output: will be like this: datetime tput => 20221018.234547.824204 0.656478


## Code description:
### Example1 read elog and parse time and tput value

#### Step: 
1. The code will fist search on the keyword
2. If keyword match it will start to spit the datetime, and TPUT value. 
3. It will save to list and print it. (You don't have to save in list)


#### 2. file or log file
- declare empty list and keyword you wants to filter or search
```
givenString = "DL- ingress traffic" #search word in a file
result = [] #empty list to store result
```
- read log file 
with open('elog', 'r') as filedata:
    for line in filedata:   
        if givenString in line:

             # Print the line, if the given string is found in the current line
             #print(line)
			 
             timeparse(line)

#### 3.parse file and get datetime and tput
Ｉwants to get the date and TPUT value, so I will use `spit` and `strip` method. 
 
> method 1:
`spit`: Spit what I wants
`strip`: after spit, remove the empty space if there are

```
datestr = data.split('[', 1)[1].split(']')[0]
Tput = data.split(" DL- ingress traffic:", 1)[1].split(',')[0].split('(')[0].strip()
```
>Note: There are two option you can print or save to list and print list 
```
#save data to list
result.append(datestr)
result.append(Tput)

# print 
print(datestr, Tput) 
```
> method 2: regular expression get the date data only
I only show how to get date information
```
import re
s = "list[20221013.162853.788442]"
m = re.search(r"\[([0-9.]+)\]", s)
print(m.group(1) ) #20221013.162853.788442
```

#### 4-1.print two column datetime and tput result from list
There are many different method you can accomplish it, I just wants to print two column, the time and Tput. 
I have store all my date into list, so if I just use print list, it will have all bunch of data, so I wish to have newline after date and tput, or two colummn. 

- print
```
	cycle = 0
    for element in result:
        cycle += 1
        #print(element, end="")
        print(element, end=" ")
        if cycle % 2 == 0:
            print("")
```
- write
```
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

```

#### 4-2 List Comprehensions Or For loop 
```
for i in [result[c:c+2] for c in range(0,len(result)) if c%2 == 0]:
    print(*i) 
```
If you're not familar with it, you can use a normal `for loop` as below:
```
temp = []
for c in range(0, len(result)):
    if c % 2 == 0:
        temp.append(result[c:c+2])

for i in temp:
    print(*i)
```

#### 4-3 using enumerate
```
#results = ['A', 'B', 'C', 'D']
for index, c in enumerate(result):
    if index % 2 == 0:
        print(*results[index:index + 2])
```

#### 4-4 using Zip
```
#results = iter(["A", "B", "C", "D"])
results = iter(result)
for i in zip(results, results):
    print(*i)
```

### Example2 parse more value (TBD)