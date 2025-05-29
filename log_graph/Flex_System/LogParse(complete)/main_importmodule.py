'''
main scipt for Flexram log analysic, will import serveral module or file
- logchecking_rename.py: Step1 check logfile and rename or write into new logfile. 
'''
import logchecking_rename_merge
import parsefile_layer2_v3_flexCDU_dev
import convert_excel_layer2_flexCDU_dev
import plot
import os,fnmatch,sys

def listcurrentdir():
    # Define patterns to exclude
    exclude_patterns = ['*.py', '__pycache__']
    # List files in the current directory
    listfiles = os.listdir()
    # Filter files that do not match the exclude patterns
    listfiles = [file for file in os.listdir() if os.path.isfile(file)]  # Filter regular files
    
    
    matching_files = []
    for file in listfiles:
        if not any(fnmatch.fnmatch(file, pattern) for pattern in exclude_patterns):
            matching_files.append(file)  # Add to matching_files if not excluded
    ''' list comprehension 
    matching_files = [
        file for file in listfiles 
        if not any(fnmatch.fnmatch(file, pattern) for pattern in exclude_patterns)
    ]
    '''
    
    #matching_files = [file for file in listfiles if not fnmatch.fnmatch(file, filelist)]
    return (f"=====List File current directory:=====\n{chr(10).join(matching_files)}\n"+ "="*40)

def remove_excelfile():
    patterns = ['*.xlsx', '*.xls', '*.xlsm']
    # Loop through all files in the current directory
    for file in os.listdir():
        if any(fnmatch.fnmatch(file, pattern) for pattern in patterns):
            print(f"Deleting {file}")
            os.remove(file)  # Remove the file


#Step1: checking logfile exist 1 or more, 1 file rename to elogfile , more than 2 will write into new filename elogfile
# Define patterns or parameters

print('######Step1:#######')
file_pattern = "elog_gnb_du_layer2.*"
log_filename="elog_files"
excelfilename='data_result'
print(listcurrentdir())

file_count, matching_files = logchecking_rename_merge.check_file_count_glob(file_pattern)
logchecking_rename_merge.rename_file(file_count, matching_files, logfilename=log_filename)

print('######Step2:#######')
# Step2 analsyic the log file and export to text file
elogfileName = log_filename
generated_result_filename = parsefile_layer2_v3_flexCDU_dev.main(elogfileName)


# Step3 convert txt file to excel 
print('######Step3:#######')
print(listcurrentdir())
remove_excelfile()
print('Generate result into excel File')
convert_excel_layer2_flexCDU_dev.main(generated_result_filename, excelfilename)

# Step4 plot graph
print('######Step4:#######')
plot.main(excelfilename)