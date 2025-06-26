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
################################################################################          
def getelement(li, element):
    ind = li.index(element)
    return li[ind+1]
 
def parse_ingress_egress(data, ULDLstr):   
    #get tput value
    datestr = data.split('[', 1)[1].split(']')[0]  
    Tputvalue=re.search(r'(ingress [^(]+).+(egress [^(]+)',data)
    m3New= Tputvalue.group(1)+", "+ Tputvalue.group(2) 
    m3New_1=m3New.replace(", ", ":").strip().split(':') #split tput and value together
    print(m3New_1)
    #result.append(datestr)
    #result.append(getelement(m3New_1, 'ingress traffic').strip())
    #result.append(getelement(m3New_1, 'egress traffic').strip())  
    #print(result)

def parse_single(target, data):
    #get the time
    datestr = data.split('[', 1)[1].split(']')[0]
    #split from tput
    search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^]]+)', data)
    
    #remove () and comma after value
    m3New= re.sub(r"[\(\[].*?[\)\]]", "",search.group(2)).replace(',','').strip().split()
    bler1=""
    bler2=""
    if target in 'DL- UE' or 'DL- UE' in target :
        bler1="PdschBler="
        bler2="nonWPdschBler="
    elif target in 'UL- UE' or 'UL- UE' in target :
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
    print(result)
  
def parse_UID(target, log_data_string):
    filedata = io.StringIO(log_data_string)  # simulate file object
    for line in filedata:
        if target in  line:      
            print(line.strip())   
            parse_single(target,  line)

def main_case1(log_data_string):
    UL = 'UL- UE'
    DL = 'DL- UE'
    target=UL
    #target=DL
    filedata = io.StringIO(log_data_string)  # simulate file object
    for line in filedata:
        if target in  line:      
            print(line.strip())   
            parse_single(target,  line)
            
def main_case1_2(sample_log):
    accepted_strings = re.compile(r"([DU]L\-\ UE(\[\s*(\d{1,2})\])?)|both$")
    givenString = input("Please enter your search special UE ID (Ex: DL- UE / UL- UE / UL- UE[ 0] ):")
    if accepted_strings.match(givenString):
        #print('matched')
        parse_UID(givenString, sample_log)
        
def main_case1_3(sample_log):
    givenString = "DL- ingress traffic"
    filedata = io.StringIO(sample_log)  # simulate file object
    for line in filedata:
        if givenString in line:
            datestr = line.split('[', 1)[1].split(']')[0]
            Tput = line.split(" DL- ingress traffic:", 1)[1].split(',')[0].split('(')[0].strip()
            print(datestr, '', Tput)
            #parse_ingress_egress(line, givenString)


############################################################
           
sample_log = """\
[20230607.155337.836828][info]:[[40;32m>>> DL- ingress traffic: 0.000027(Mbps), egress traffic: 0.000291(Mbps), ReTx: 0.000069(Mbps)[0m]
[20230607.155337.836848][info]:[DL- UE[ 1]: Tput=    0.000027 Mbps, Mcs=  9.0(Sigma= 0.0), RbNum=   1.0, ReTxRatio=   0.0, Layers= 1.0, PdschBler=   0.0, nonWPdschBler=   0.0]
[20230607.155337.836861][info]:[>>> DL- Mcs=  9.0, RbNum=   1.0, Layers= 1.0, PdschBler=   0.0, nonWPdschBler=   0.0, MaxSchedUE=   1.0, SchedUE=   1.0]
[20230607.155337.836872][info]:[[40;33mUL <<<- ingress traffic: 0.003726(Mbps) PDU_Count[4], egress traffic: 0.001274(Mbps) PDU_Count[3], ReRx: 0.000000(Mbps)[0m]
[20230607.155337.836887][info]:[UL- UE[ 1]: Tput= 0.001274 Mbps, avg Mcs=  4.0(Sigma= 0.00), RbNum= 134.0, Layers= 1.0, PuschEffecSinr= 0.00(0.0 dB), PuschSinr= 166.25(19.1 dB), PuschBler=   0.0, nonWPuschBler=   0.0, TA=  31.0, PHR= 31.0 dB, SchCnt=     4, S-BSR= 4, L-BSR= 0]
[20230607.155337.836906][info]:[UL <<<- Mcs=  4.0, RbNum= 134.0, Layers= 1.0, PuschEffecSinr= 0.00(0.0 dB), PuschSinr= 166.25(19.1 dB), PuschBler=   0.0, nonWPuschBler=   0.0, TA=  31.0, PHR= 31.0 dB, S-BSR= 4, L-BSR= 0]
[20230607.155337.836918][info]:[DL CFG NUM= 1007, UL CFG NUM= 4, Slot Indication NUM= 20000, Free RNTI Num= 99]
"""

#main_case1(sample_log)
#main_case1_2(sample_log)
#main_case1_3(sample_log)
main_case1_3(sample_log)