import re 
with open('elog_gnb_du_layer2.0', 'r') as filedata:
    for line in filedata:   
        if 'U-UE' in line:
            search = re.search(r'\[(\d+\.\d+\.\d+)\].*?(Tput=[^A]+)', line)
            print(search.group(2))

            