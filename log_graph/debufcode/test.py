
import re

def getelement(li, element):
    ind = li.index(element)
    return li[ind+1]

string = "[20221018.165317.401606][info]:[DL- UE[ 0]: Tput= 0.000091 Mbps, Mcs= 9.0(Sigma= 0.0), RbNum= 1.4, ReTxRatio= 33.3, Layers= 1.0, PdschBler= 0.0, nonWPdschBler= 33.3]"
datestr = string.split('[', 1)[1].split(']')[0]

m3 = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Mcs=+)*?(Tput=[^]]+)', string)
#print(m3.group(3))
m3New= re.sub("[\(\[].*?[\)\]]", "",m3.group(3)).replace(',','').strip().split()

#print(m3New)
#print(datestr)
#m3New=m3New.split()
#print(m3New)
#print('-'*20)
print(getelement(m3New, 'Tput='),' ', getelement(m3New, 'RbNum='), '', getelement(m3New, 'Mcs='))
