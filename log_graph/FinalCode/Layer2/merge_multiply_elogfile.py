import os


def method1():
    # Directory containing the files to merge
    directory = "."
    directory = "/path/to/files"
    # Output file name
    output_file = "merged.txt"

    # Loop through all files in the directory and append their contents to the output file
    with open(output_file, "w") as outfile:
        for filename in os.listdir(directory):
            if filename.startswith("elog_gnb_du_layer2"):
                with open(os.path.join(directory, filename), "r") as infile:
                    outfile.write(infile.read())
                    
def method2():
    import glob

    file_pattern = 'elog_gnb_du_layer2*'
    file_list = glob.glob(file_pattern)

    with open('merged_file.txt', 'w') as outfile:
        for file in file_list:
            with open(file, 'r') as infile:
                outfile.write(infile.read())

method2()
#method1()