import os
import glob
from natsort import natsorted

def method1():
    # Directory containing the files to merge
    directory = "."
    #directory = "/path/to/files"
    # Output file name
    output_file = "merged.txt"

    # Loop through all files in the directory and append their contents to the output file
    with open(output_file, "w") as outfile:
        for filename in os.listdir(directory):
            if filename.startswith("elog_gnb_du_layer2."):
                with open(os.path.join(directory, filename), "r") as infile:
                    outfile.write(infile.read())


def method2():
    file_pattern = 'elog_gnb_du_layer2*'
    file_list = glob.glob(file_pattern)

    with open('merged_file.txt', 'w') as outfile:
        for file in file_list:
            with open(file, 'r') as infile:
                outfile.write(infile.read())
                
#using natsort wil read file inorder                    
def method3():
    file_pattern = 'elog_gnb_du_layer2*'
    file_list = glob.glob(file_pattern)
    sorted_file_list = natsorted(file_list)  # Sort the file list naturally

    with open('merged_file.txt', 'w') as outfile:
        for file in sorted_file_list:
            with open(file, 'r') as infile:
                outfile.write(infile.read())
                    
                
method3()           
method2()
#method1()