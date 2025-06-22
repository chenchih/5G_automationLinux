'''
- checking logfile 1 or more, 1 will rename merged_file.txt, more will wirte into newfile call merged_file.txt
- move merge_multiply_elogfile.py method3 function into rename_file function
    - include natsorted which will do natural sort 
'''
import os, glob, sys
from natsort import natsorted

def check_file_count_glob(file_pattern):
    # Get matching files using glob
    matching_files = glob.glob(file_pattern)
    #Return the count and the list of matching filenames
    return len(matching_files), matching_files

#logfilename: If no value is provided, the default value (elogfile) or use passed value will overwrite it
def rename_file(file_count, matching_files, logfilename="elogfile"):

    if file_count > 1:
        sorted_file_list = natsorted(matching_files)  # Sort the file list naturally
        
        with open(logfilename, 'w') as outfile:
            for file in sorted_file_list:
                with open(file, 'r') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')
        '''
        #rename multiple file
        for i, file in enumerate(matching_files):
            try:
                new_name = f"{logfilename}_{i}"  # Generate a unique name for each file
                os.rename(file, new_name)  # Rename each file
                print(f"Renamed {file} to {new_name}")
            except Exception as e:
                print(f"Error renaming file {file}: {e}")
            
        print(f"Renamed {file} to {new_name}")    
        '''         
    elif file_count==1:
        print(f'Found only 1 file: {matching_files[0]}')    
        try:
            os.rename(matching_files[0], logfilename)
            #print(f'Renamed {matching_files[0]} to {logfilename}')
        except Exception as e:
            print(f"Error renaming file: {e}")
    
    else:
        print('No log file find, exit code!!!')
        input("Press any key to exit...")
        sys.exit()  # Use sys.exit() for a clean exit

        
# Ensure standalone functionality
if __name__ == "__main__":
    file_pattern = "elog_gnb_du_layer2.*"
    file_count, matching_files = check_file_count_glob(file_pattern)                       
    rename_file(file_count, matching_files)
