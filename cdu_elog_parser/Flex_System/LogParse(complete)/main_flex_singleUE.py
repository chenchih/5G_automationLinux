'''
main scipt for Flexram log analysic, will import serveral module or file
- logchecking_rename.py: Step1 check logfile and rename or write into new logfile. 
'''
import logchecking_rename_merge
import parsefile_layer2_v3_flexCDU_dev
import convert_excel_layer2_flexCDU_dev
import plot
import os,fnmatch,sys
from datetime import datetime

def listcurrentdir():
    # Define patterns to exclude
    exclude_patterns = ['*.py', '__pycache__','*.md']
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

def wrap_result(outputdir):
    # Define patterns for the files you want to move
    patterns = ['*.xlsx', '*.xls', '*.xlsm', '*.txt', '*.png']

    # 1. Create the output directory if it doesn't already exist
    # os.makedirs creates all necessary intermediate directories
    # exist_ok=True prevents an error if the directory already exists
    os.makedirs(outputdir, exist_ok=True)
    print(f"Ensured directory '{outputdir}' exists.")

    # 2. Loop through all files in the current directory
    moved_files_count = 0
    for file in os.listdir():
        # Check if the file matches any of the defined patterns
        if any(fnmatch.fnmatch(file, pattern) for pattern in patterns):
            try:
                # Construct the full path for the destination
                destination_path = os.path.join(outputdir, file)
                # Move the file
                os.rename(file, destination_path)
                print(f"Moved '{file}' to '{outputdir}/'")
                moved_files_count += 1
            except OSError as e:
                print(f"Error moving '{file}': {e}")

    if moved_files_count == 0:
        print(f"No matching files found to move to '{outputdir}'.")
    else:
        print(f"Successfully moved {moved_files_count} files to '{outputdir}'.")
        
#Step1: checking logfile exist 1 or more, 1 file rename to elogfile , more than 2 will write into new filename elogfile
# Define patterns or parameters

print('######Step1: Check single or multiple logfile and rename  #######')
file_pattern = "elog_gnb_du_layer2.*"
log_filename="elog_files"
excelfilename='flex_singleUE_data_result'

file_count, matching_files=logchecking_rename_merge.check_file_count_glob(log_filename)
if matching_files: # Check if the list is not empty
    print("elog_files exist. Attempting to delete it...")
    for file_path in matching_files:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Successfully deleted file: {file_path}")
            print("========================================")

file_count, matching_files = logchecking_rename_merge.check_file_count_glob(file_pattern)
logchecking_rename_merge.rename_file(file_count, matching_files, logfilename=log_filename)
print(listcurrentdir())

# Step2 analsyic the log file and export to text file
print('\n######Step2: parsing the log file #######')
elogfileName = log_filename
generated_result_filename = parsefile_layer2_v3_flexCDU_dev.main(elogfileName)


# Step3 convert txt file to excel 
print('\n######Step3: Convert txt result into Excel for plot graph #######')
print(listcurrentdir())
remove_excelfile()
print('Generate result into excel File')
convert_excel_layer2_flexCDU_dev.main(generated_result_filename, excelfilename)

# Step4 plot graph
print('\n######Step4: Plot data and save to images #######')
plot.main(excelfilename)

# Step5 Wrap up result into folder
print('\n######Step5: Wrap up result into Folder#######')
datename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
outfileName = f"{datename}_L2_Flex_singleUE_Result" # Using an f-string for clarity  
# Call the function to wrap your results
wrap_result(outfileName)
print('=======Script End=======')
input('Press Enter to close...')
