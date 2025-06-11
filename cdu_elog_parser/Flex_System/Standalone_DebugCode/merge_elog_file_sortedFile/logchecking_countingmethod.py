import os
import glob

filename = ""
####Method1################################
'''Easy to understand. Directly counts files matching the pattern.
Less efficient for large directories with many files'''
def check_file_count_listcomprehension (file_pattern):
    file_count = len([file for file in os.listdir() if file.startswith(file_pattern)])
    return file_count
    
#this is original way from above 
def check_file_count_original (file_pattern): 
    finding_count = 0
    for file in os.listdir():  #Loop through each file in the directory
        if file.startswith(file_pattern): #Check if the file matches the pattern
            finding_count += 1
    return finding_count  # Return the total count    
    
def check_file_count_withsum(file_pattern):
    return sum(1 for file in os.listdir() if file.startswith(file_pattern))
def check_file_count(file_pattern):
    return len(glob.glob(file_pattern))
    
def check(filelen):    
    if  filelen > 1:
        return f'contain {filelen} file, filename: {matching_files}'
    elif filelen ==1:
       return 'contain only 1 file'    
    else:
         return 'No log file find'  
        
#using search with
file_pattern ="elog_gnb_du_layer2.0"
filelen=check_file_count_original(file_pattern)
print('using startwith:', check(filelen))

# using glob 
file_pattern = "elog_gnb_du_layer2.*"
matching_files = glob.glob(file_pattern)
filelen=len(matching_files)
print(f'using glob: {check(filelen)}')

file_pattern_1 ="elog_gnb_du_layer2.0"
file_pattern_2 ="elog_gnb_du_layer2*"
print(f'using startwith exist log: {check_file_count_withsum(file_pattern_1)}')
print(f'using glob check exist log: {check_file_count(file_pattern_2)}')