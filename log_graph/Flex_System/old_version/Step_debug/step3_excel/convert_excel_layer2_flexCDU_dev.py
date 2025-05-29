
'''
file reference: excel_layer2_sheet_v1.py
this is the final code

'''

import pandas as pd

# Global variables for UL and DL lists
ULlist = []
DLlist = []

def parse_file(filename):
    """Parse the input file and organize data into a dictionary."""
    lists = {}
    current_key = None
    with open(filename, 'r') as myfile:
        readline = myfile.read().splitlines()
        for line in readline:
            if "=" in line:
                current_key = line.strip("=")
                lists[current_key] = []
            else:
                assert current_key is not None  # Data should not appear before a header
                lists[current_key].append(line)
    return lists

def process_UL(lists):
    """Process UL data."""
    for i in lists["UL"]:
        ULlist.append(i.split())

def process_DL(lists):
    """Process DL data."""
    for i in lists["DL"]:
        DLlist.append(i.split())

def write_excel(excelfilename):
    """Improved version of writing data to an Excel file."""
    required_ul_columns = {'UL-Tput', 'UL-RbNum', 'UL-MCS', 'UL-Bler'}
    required_dl_columns = {'DL-Tput', 'DL-RbNum', 'DL-MCS', 'DL-Bler'}

    try:
        # Process UL DataFrame
        df1 = pd.DataFrame(ULlist)
        df1 = df1.rename(columns=df1.iloc[0]).drop(df1.index[0])
        missing_ul_columns = required_ul_columns - set(df1.columns)
        if missing_ul_columns:
            raise KeyError(f"Missing UL columns: {', '.join(missing_ul_columns)}")
        for col in required_ul_columns:
            df1[col] = df1[col].astype(float)

        # Process DL DataFrame
        df2 = pd.DataFrame(DLlist)
        df2 = df2.rename(columns=df2.iloc[0]).drop(df2.index[0])
        missing_dl_columns = required_dl_columns - set(df2.columns)
        if missing_dl_columns:
            raise KeyError(f"Missing DL columns: {', '.join(missing_dl_columns)}")
        for col in required_dl_columns:
            df2[col] = df2[col].astype(float)

        # Write to Excel
        with pd.ExcelWriter(excelfilename + '.xlsx', engine='xlsxwriter') as writer:
            df1.style.set_properties(**{'text-align': 'center'}).to_excel(writer, 'UL', index=False)
            worksheet = writer.sheets['UL']
            worksheet.set_column(0, 0, 25)
            worksheet.set_column(1, len(df1.columns) - 1, 15)

            df2.style.set_properties(**{'text-align': 'center'}).to_excel(writer, 'DL', index=False)
            worksheet = writer.sheets['DL']
            worksheet.set_column(0, 0, 25)
            worksheet.set_column(1, len(df2.columns) - 1, 15)

    except KeyError as e:
        print(f"KeyError: {e}. Please check the input file for missing headers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

        
def main(log_filename, excelfilename):
    """Main function to process data and write to Excel."""
    lists = parse_file(log_filename)
    if "UL" in lists:
        process_UL(lists)
    if "DL" in lists:
        process_DL(lists)
    write_excel(excelfilename)

# Ensure script can be imported or run standalone
if __name__ == "__main__":
    # Replace these with CLI arguments or other input methods if needed
    log_filename = input("Please enter your text file name (e.g., test.txt): ")
    excelfilename = input("Please enter the Excel file name (e.g., test): ")
    main(log_filename, excelfilename)