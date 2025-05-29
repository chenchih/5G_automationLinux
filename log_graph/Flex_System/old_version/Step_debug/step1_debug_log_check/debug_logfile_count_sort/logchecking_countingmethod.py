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
    
    
####Method2################################
'''
Memory-efficient, Faster for large directories as it doesn't require storing unnecessary data.
'''    
def check_file_count_withsum(file_pattern):
    return sum(1 for file in os.listdir() if file.startswith(file_pattern))
    
####Method3##################################    
'''
Supports advanced wildcard patterns (*, ?, etc.), making it more versatile.
Convenient for matching complex patterns. 
Less efficient for large directories with many files
'''    
def check_file_count(file_pattern):
    return len(glob.glob(file_pattern))


# Define the file pattern to search for
#file_pattern = "result-*.txt"
file_pattern = "elog_gnb_du_layer2.0*"
file_pattern_file_startwith = "elog_gnb_du_layer2.0"


# Get the list of matching files (debug used)
#matching_files = glob.glob(file_pattern)
#filelen=len(matching_files)



filelen=check_file_count_glob(file_pattern) 
#filelen=check_file_count_withsum(file_pattern_file_startwith) 
#filelen=check_file_count_withsum(file_pattern_file_startwith) 
#filelen=check_file_count_original(file_pattern_file_startwith) 


if  filelen > 1:
        print(f'contain {filelen} file, filename: {matching_files}')
elif filelen ==1:
    print('contain only 1 file')
    
else:
    print('No log file find')

