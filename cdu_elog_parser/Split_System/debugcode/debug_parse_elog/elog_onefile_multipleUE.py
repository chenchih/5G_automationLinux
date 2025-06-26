import io
import re
result=[]
#will trate string as sequence of character 
#Output: one character per line.
def main(log_data_string):   
    for line in log_data_string:
        print(line) 

#Treats the string as a file-like object, where each line is separated by \n.
#Output: one full line per iteration
def main_io(log_data_string):   
    iostr=io.StringIO(log_data_string)
    for line in iostr:
        print(line)
        #if "m>>> DL-" in  line:  
            #print('yes')
##################################################           
def getelement(li, element):
    ind = li.index(element)
    return li[ind+1]
    
def parse_bler(data, ULDLstr): 
    #get bler
    blerresult = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Mcs=[^]]+)', data)
    blerDL= re.sub(r"[\(\[].*?[\)\]]", "",blerresult.group(2)).replace(',','').strip().split()
    print(blerDL)

    if ULDLstr in 'DL':
        bler1="PdschBler="
        bler2="nonWPdschBler="
        
    elif ULDLstr in 'UL':
        bler1="PuschBler="
        bler2="nonWPuschBler="
        
    #print(m3New2)
    print(getelement(blerDL, 'RbNum='))
    result.append(getelement(blerDL, 'RbNum='))
    result.append(getelement(blerDL, 'Mcs='))
    result.append(getelement(blerDL, bler1).strip())
    result.append(getelement(blerDL, bler2).strip())
    print(result)    
    #listprint()
    #result.clear() 
  
def parse(data, ULDLstr):   
    #get tput value
    datestr = data.split('[', 1)[1].split(']')[0]  
    Tputvalue=re.search(r'(ingress [^(]+).+(egress [^(]+)',data)
    m3New= Tputvalue.group(1)+", "+ Tputvalue.group(2) 
    m3New_1=m3New.replace(", ", ":").strip().split(':') #split tput and value together
    result.append(datestr)
    result.append(getelement(m3New_1, 'ingress traffic').strip())
    result.append(getelement(m3New_1, 'egress traffic').strip())  
    print(result)
    
def main2_from_string_single(log_data_string):
    countDL = 0
    filedata = io.StringIO(log_data_string)  # simulate file object
    for line in filedata:
        if "m>>> DL-" in  line:      
            print(line.strip())             
            for nextline in filedata:
                if re.search(r'\[(\d+\.\d+\.\d+)\].*?(>>> DL- Mcs=[^]]+)', nextline): 
                    givenString = "DL"
                    print(nextline)
                    parse(line, givenString)
                    parse_bler(nextline, givenString)
                    break
   
sample_log = """\
[20230927.051909.458444][info]:[[40;32m>>> DL- ingress traffic: 248.349854(Mbps), egress traffic: 247.500244(Mbps), ReTx: 1.471227(Mbps)[0m]
[20230927.051859.458431][info]:[DL- UE[ 0]: Tput=    0.000317 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum=   2.0, ReTxRatio=   0.0, Layers= 1.0, PdschBler=   0.0, nonWPdschBler=   0.0]
[20230927.051859.458447][info]:[DL- UE[ 2]: Tput=   57.686012 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum= 194.7, ReTxRatio=   1.6, Layers= 3.9, PdschBler=   0.7, nonWPdschBler=   0.7]
[20230927.051859.458463][info]:[DL- UE[ 4]: Tput=   59.352180 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum= 198.4, ReTxRatio=   2.4, Layers= 3.9, PdschBler=   1.5, nonWPdschBler=   1.6]
[20230927.051859.458478][info]:[DL- UE[ 6]: Tput=   61.132641 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum= 199.3, ReTxRatio=   0.9, Layers= 4.0, PdschBler=   0.0, nonWPdschBler=   0.0]
[20230927.051859.458493][info]:[DL- UE[ 7]: Tput=   60.267414 Mbps, Mcs= 26.0(Sigma= 0.0), RbNum= 198.1, ReTxRatio=   2.8, Layers= 4.0, PdschBler=   1.6, nonWPdschBler=   1.7]
[20230927.051859.458504][info]:[>>> DL- Mcs= 26.0, RbNum= 197.5, Layers= 4.0, PdschBler=   0.9, nonWPdschBler=   1.0, MaxSchedUE=   1.0, SchedUE=   7.0]

"""
#main_io(sample_log)
# Call your function with variable instead of file
main2_from_string(sample_log)