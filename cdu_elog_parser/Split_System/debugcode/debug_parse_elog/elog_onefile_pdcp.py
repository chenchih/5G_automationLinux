import io
import re
result=[]
#will trate string as sequence of character 

def getelement(li, element):
    ind = li.index(element)
    return li[ind+1]
    
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
def main(log_data_string, target):
    filedata = io.StringIO(log_data_string)  # simulate file object
    for line in filedata:
        if target in  line:      
            print(line.strip())             
            parse(line, target)
sample_log = """\
[20221217.194812.548218][info]:[[MTU_Size_Pool_1_2]: 13.524528]
[20221217.194812.548223][info]:[====================================]
[20221217.194812.548238][info]:[PDCP DL- ingress traffic: 239.968109(Mbps), egress traffic: 214.256439(Mbps)]
[20221217.194812.548244][info]:[PDCP UL- ingress traffic: 96.111160(Mbps), egress traffic: 95.896652(Mbps)]
[20221217.194817.576984][info]:[Relay DL- ingress traffic: 240.012161(Mbps), egress traffic: 216.351471(Mbps), pkt: 103906]
[20221217.194817.577017][info]:[========== Mem Pool Usage ==========]
[20221217.194817.577023][info]:[[MTU_Size_Pool_1_2]: 13.962437]
"""
#main_io(sample_log)
# Call your function with variable instead of file
UL = 'PDCP UL'
main(sample_log, UL)