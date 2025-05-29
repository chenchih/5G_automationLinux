from tqdm import tqdm
import pandas as pd

# Input file names
resultfilename = input("Please enter your txt file name (Ex: test.txt): ")
excelfilename = input("Please enter saving Excel file name (Ex: test): ")

# Initialize variables
lists = {}
current_key = None

# Step 1: Read and parse the file
with tqdm(desc="Task 1: Reading and Parsing File", total=1, unit="task") as task1_bar:
    with open(resultfilename, 'r') as myfile:
        readline = myfile.read().splitlines()
        for line in readline:
            if "=" in line:
                current_key = line.strip("=")
                lists[current_key] = []
            else:
                assert current_key is not None  # Ensure there's a valid header
                lists[current_key].append(line)
    task1_bar.update(1)  # Mark the task as completed

ULlist = []
DLlist = []

# Step 2: Process UL and DL data
with tqdm(desc="Task 2: Processing UL and DL Data", total=2, unit="task") as task2_bar:
    def process_list(data, target_list):
        for line in data:
            target_list.append(line.split())

    if "DL" in lists and "UL" in lists:
        process_list(lists["DL"], DLlist)
        task2_bar.update(1)  # Mark DL processing as completed

        process_list(lists["UL"], ULlist)
        task2_bar.update(1)  # Mark UL processing as completed
    else:
        print("Data does not contain both UL and DL sections.")
        exit()

# Step 3: Write data to Excel
with tqdm(desc="Task 3: Writing to Excel", total=2, unit="task", leave=True) as task3_bar:

    def process_dataframe(data, sheet_name, writer):
        df = pd.DataFrame(data)
        df.columns = df.iloc[0]  # Use the first row as column names
        df = df.drop(df.index[0])  # Remove the header row from the data

        # Process each column based on its type
        for col in df.columns:
            if df[col].dtype == object:  # Check if column contains strings
                df[col] = df[col].str.strip()  # Clean strings
                df[col] = pd.to_numeric(df[col], errors="ignore")  # Try converting to numeric

        # Write to Excel with formatting
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        task3_bar.update(0.5) 
        # Adjust column widths
        worksheet = writer.sheets[sheet_name]
        worksheet.set_column(0, 0, 25)  # Adjust first column width
        worksheet.set_column(1, len(df.columns) - 1, 15)  # Adjust other columns
        task3_bar.update(0.5) 

    with pd.ExcelWriter(excelfilename + '.xlsx', engine='xlsxwriter') as writer:
        process_dataframe(ULlist, "UL", writer)
        process_dataframe(DLlist, "DL", writer)

