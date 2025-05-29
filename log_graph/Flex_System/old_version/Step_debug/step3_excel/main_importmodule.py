'''
main scipt for Flexram log analysic, will import serveral module or file
- logchecking_rename.py: Step1 check logfile and rename or write into new logfile. 
'''
import convert_excel_layer2_flexCDU_dev
import os,fnmatch

def listcurrentdir():
    # Define patterns to exclude
    exclude_patterns = ['*.py', '__pycache__']
    # List files in the current directory
    listfiles = os.listdir()
    # Filter files that do not match the exclude patterns
    listfiles = [file for file in os.listdir() if os.path.isfile(file)]  # Filter regular files
    
    #method1
    matching_files = []
    for file in listfiles:
        if not any(fnmatch.fnmatch(file, pattern) for pattern in exclude_patterns):
            matching_files.append(file)  # Add to matching_files if not excluded
    ''' method2 shorter code using list comprehension 
    matching_files = [
        file for file in listfiles 
        if not any(fnmatch.fnmatch(file, pattern) for pattern in exclude_patterns)
    ]
    '''
    #matching_files = [file for file in listfiles if not fnmatch.fnmatch(file, filelist)]
    return (f"=====List File current directory:=====\n{chr(10).join(matching_files)}\n"+ "="*40)

def remove_excelfile():
    excel_extensions = ('.xlsx', '.xls', '.xlsm')
    for file in os.listdir():
        if any(fnmatch.fnmatch(file, pattern) for pattern in patterns):
        #if file.endswith(excel_extensions):
            print(f"Deleting {file}")
            os.remove(file)  # Remove the file
    #return any(fnmatch(file, pattern) for file in os.listdir(directory) for pattern in patterns)


# Define patterns or parameters

file_pattern = "elog_gnb_du_layer2.*"
#log_filename="elog_files"
log_filename="result-2024-11-21-14-07-26_SHORT.txt"
excelfilename='data_result'

print("Step1:", listcurrentdir())

#Step1: checking logfile exist 1 or more, 1 file rename to elogfile , more than 2 will write into new filename elogfile
#file_count, matching_files = logchecking_rename_merge.check_file_count_glob(file_pattern)
#logchecking_rename_merge.rename_file(file_count, matching_files, logfilename=log_filename)

# Step2 analsyic the log file and export to text file

#elogfileName = log_filename
#parsefile_layer2_v3_flexCDU_dev.main(elogfileName)

# Step3 convert txt file to excel 
#listcurrentdir()
#remove_excelfile()
convert_excel_layer2_flexCDU_dev.main(log_filename, excelfilename)


