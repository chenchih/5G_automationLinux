
import logchecking_rename_merge
from datetime import datetime
import parsefile_layer2_single
import excel_layer2_singleUE
import plot_graph_Excel_single

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

            
def wrap_result(outputdir):
    # Define patterns for the general files you want to move
    general_patterns = ['*.xlsx', '*.xls', '*.xlsm', '*.txt', '*.png']
    
    # Define the specific pattern for elog files
    elog_pattern = 'elog*' 
    elog_subfolder_name = 'elogfile'

    # 1. Create the main output directory if it doesn't already exist
    os.makedirs(outputdir, exist_ok=True)
    print(f"Ensured main output directory '{outputdir}' exists.")

    # 2. Create the elog subfolder within the main output directory
    elog_subfolder_path = os.path.join(outputdir, elog_subfolder_name)
    os.makedirs(elog_subfolder_path, exist_ok=True)
    print(f"Ensured elog subfolder '{elog_subfolder_path}' exists.")

    # 3. Loop through all files in the current directory
    moved_general_files_count = 0
    moved_elog_files_count = 0

    for file in os.listdir():
        # Check if the file starts with 'elog'
        if fnmatch.fnmatch(file, elog_pattern):
            try:
                destination_path = os.path.join(elog_subfolder_path, file)
                os.rename(file, destination_path)
                print(f"Moved '{file}' to '{elog_subfolder_path}/'")
                moved_elog_files_count += 1
            except OSError as e:
                print(f"Error moving '{file}' to elog subfolder: {e}")
        # Check if the file matches any of the general patterns (and isn't an elog file)
        elif any(fnmatch.fnmatch(file, pattern) for pattern in general_patterns):
            try:
                destination_path = os.path.join(outputdir, file)
                os.rename(file, destination_path)
                print(f"Moved '{file}' to '{outputdir}/'")
                moved_general_files_count += 1
            except OSError as e:
                print(f"Error moving '{file}' to main output directory: {e}")

    if moved_general_files_count == 0 and moved_elog_files_count == 0:
        print(f"No matching files found to move to '{outputdir}' or '{elog_subfolder_path}'.")
    else:
        print(f"Successfully moved {moved_general_files_count} general files to '{outputdir}'.")
        print(f"Successfully moved {moved_elog_files_count} 'elog' files to '{elog_subfolder_path}'.")
        
print('#################Script Start !!!#################')

#Step1: checking logfile exist 1 or more, 1 file rename to elogfile , more than 2 will write into new filename elogfile
# Define patterns or parameters
print('\n######Step1: Check single or multiple logfile and rename  #######')
file_pattern = "elog_gnb_du_layer2.*"
log_filename="elog_files"
excelfilename='data_result_singleUE'
#print(listcurrentdir())

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
print('\n######Step2:parsing the log file #######')
# Step2 analsyic the log file and export to text file
elogfileName = log_filename
generated_result_filename = parsefile_layer2_single.main(elogfileName)
print(generated_result_filename)

# Step3 convert txt file to excel 
print('\n######Step3: Convert txt result into Excel for plot graph #######')
listcurrentdir()
remove_excelfile()
#generated_result_filename='result-2025-06-16-18-05-28.txt'
#excelfilename='data_result'
full_excel_path_for_plotting = excelfilename + ".xlsx"

excel_filecreate=excel_layer2_singleUE.main(generated_result_filename, full_excel_path_for_plotting)
if excel_filecreate:
    print(f'Log convert to excel file created')

# Step4 plot graph
full_excel_path_for_plotting='data_result_singleUE.xlsx'
print('\n######Step4: Plot data and save to images #######')
plot_graph_Excel_single.main(full_excel_path_for_plotting)

# Step5 Wrapup result into folder
print('\n######Step5: Wrap up result into Folder#######')
datename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
outfileName = f"{datename}_L2_singleUE_Result" # Using an f-string for clarity  
# Call the function to wrap your results
wrap_result(outfileName)
print('\n#################Script DONE !!!#################')
