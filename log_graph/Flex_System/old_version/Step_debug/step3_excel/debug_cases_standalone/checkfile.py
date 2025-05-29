import os,glob,fnmatch
from fnmatch import fnmatch 


def list_direcrtory():
	print('=====list file======')
	for file in os.listdir():
		print(file)
	print('=====end================')


#using os and fnmatch          
def checking_file_1(file):
	# Filter files that are regular files and match the patterns
	matching_files = [
    file for file in os.listdir() 
    if os.path.isfile(file) and any(fnmatch.fnmatch(file, pattern) for pattern in patterns)
	]
	#print(matching_files)
	return matching_files

#using glob or endwith
def checking_file_2(file):
	matching_files = [file for pattern in patterns for file in glob.glob(pattern)]
	#matching_files = [file for file in os.listdir() if file.endswith('.html')]
	return matching_files

#os and fnmatch
def check_excel_files(): #has_excel_files(directory=".")
    """Check if the directory contains any Excel files."""
    excel_extensions = ('.xlsx', '.xls', '.xlsm')
    #with any
    return any(fnmatch(file, pattern) for file in os.listdir(directory) for pattern in patterns)
    '''
    #without any
    found = False
    for file in os.listdir(directory):
        for pattern in patterns:
            if fnmatch(file, pattern):
                found = True
                break  # Stop checking other patterns for this file
        if found:
            break  # Stop checking other files
    return found
    '''
def remove_file_endwith():
    filetype='.html'
	for file in os.listdir():
        #if file.endswith((".xls", ".xlsx")):
		if file.endswith(filetype):
			os.remove(file)  
            #return True  
    #return False
    
def remove_file_pattern():
    patterns = ['*.xlsx', '*.xls', '*.xlsm']
    # Loop through all files in the current directory
    for file in os.listdir():
        if any(fnmatch.fnmatch(file, pattern) for pattern in patterns):
            print(f"Deleting {file}")
            #os.remove(file)  # Remove the file


#=========================================================================
patterns = ['*.html','.txt']
result=checking_file_1(patterns)
print(result)

result= checking_file_2(patterns)
print(result)


matching_files = [file for file in os.listdir() if file.endswith('.html')]
print(matching_files)

#remove_file_endwith('.html')
remove_file_pattern()
list_direcrtory()


# Usage
if check_excel_files():
#if has_excel_files():
    print("Excel files found in the directory.")
else:
    print("No Excel files found.")
	

#check if file or directory exist, return bool
os.path.isfile('filename.txt')
os.path.isdir('foldername')