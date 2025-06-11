import os
import glob
from natsort import natsorted

file_pattern = 'elog_gnb_du_layer2*'
file_list = glob.glob(file_pattern)

#using default sorted order not in natural order

'''
['elog_gnb_du_layer2.0', 'elog_gnb_du_layer2.1', 
'elog_gnb_du_layer2.10', 'elog_gnb_du_layer2.11', 
'elog_gnb_du_layer2.20', 'elog_gnb_du_layer2.5', 
'elog_gnb_du_layer2.6']
'''

#check if exist delte it 
#merged_file = 'merged_file.txt'
#if os.path.exists(merged_file):
    #os.remove(merged_file)


#using natsorted wil order natural order
sorted_file_list = natsorted(file_list)  # Sort the file list naturally
#w option will overwrite if exist occur
    
with open('merged_file.txt', 'w') as outfile:
    
    for file in sorted_file_list:
        with open(file, 'r') as infile:
            outfile.write(infile.read())
            outfile.write('\n')