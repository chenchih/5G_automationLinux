## Description of code


### Select parsing Traffic
Select the traffic string you want to parse, UL DL or both traffic. 
- > `accepted_strings = re.compile(r"^(D-UE|U-UE)(\[\d\]|\[ \d\])?$|^both$")`
- > `givenString = input("Please enter your search (Ex: D-UE / U-UE/ U-UE[ 0] / both:):")`

So this is an option to parse either option is available:
> allow to parse `U-UE[ 0]` for UL 
> allow to parse `U-UE[ 0]` for UL specfic ID with space
> allow to parse `U-UE[ 0]` for UL specfic ID without space
> allow parse `D-UE` for DL
> allow parse `both`

```
accepted_strings = re.compile(r"^(D-UE|U-UE)(\[\d\]|\[ \d\])?$|^both$")
givenString = input("Please enter your search (Ex: D-UE / U-UE/ U-UE[ 0] / both:):")
if accepted_strings.match(givenString):
        if givenString =="both":
            UL = 'U-UE'
            DL = 'D-UE'
            writefile("UL")
            ULDLprint(UL)
            writefile("DL")
            ULDLprint(DL)
        else:        
            writefile(givenString)
            with open(elogfileName, 'r') as filedata:
                for line in filedata:   
                    if givenString in line:
                        
# Print the line, if the given string is found in the current line
                        #print(line.strip())
                        parse(line, givenString)
    else:
        print("Not found, please reenter correct option") 		
```

### analysic the related string 

- parse the data:
```
datestr = data.split('[', 1)[1].split(']')[0]  
search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^A]+)', data)
m3New = re.sub(r"[\(\[].*?[\)\]]", "", search.group(2)).replace('=', '= ').replace(',', ' ').strip().split()
result.clear()
```
- save the value into list 
```
givenString=ULDLstr
bler="Bler="
result.append(datestr)    
result.append(getelement(m3New, 'Tput='))
result.append(getelement(m3New, 'RB='))
result.append(getelement(m3New, 'Mcs='))
result.append(getelement(m3New, bler))
listprint() 
```

- write into file
```
def listprint():
    #checkfile()
    cycle = 0        
    with open(filename, "a") as f:
        for element in result:            
            f.write(element+ " ")     
        f.write("\n")
```


