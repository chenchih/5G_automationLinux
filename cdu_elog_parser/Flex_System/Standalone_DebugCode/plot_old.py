import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

def plot_sheet_data(df, datetime_col, y_cols_to_plot, sheet_name_label, output_filename_base):
    if df is None or df.empty:
        print(f"DataFrame for {sheet_name_label} is empty or None. Skipping plot.")
        return

    # Make a copy to avoid SettingWithCopyWarning on the original DataFrame
    df_processed = df.copy()

    # Attempt to convert 'datettime' column.
    # The format in your files appears to be YYYYMMDD.HHMMSS.ffffff
    try:
        df_processed[datetime_col] = pd.to_datetime(df_processed[datetime_col], format='%Y%m%d.%H%M%S.%f')
    except ValueError as e:
        print(f"Error converting '{datetime_col}' to datetime for {sheet_name_label} sheet using specific format: {e}")
        # Fallback to inferring the format if the specific one fails.
        try:
            print(f"Attempting to infer datetime format for {sheet_name_label} sheet...")
            df_processed[datetime_col] = pd.to_datetime(df_processed[datetime_col])
        except Exception as e_infer:
            print(f"Could not parse datetime column '{datetime_col}' for {sheet_name_label} sheet: {e_infer}. Skipping plot.")
            return
    except TypeError as te: # Handles cases where datetime_col might already be datetime objects from Excel read
        if pd.api.types.is_datetime64_any_dtype(df_processed[datetime_col]):
            print(f"'{datetime_col}' for {sheet_name_label} already in datetime format.")
        else:
            print(f"TypeError processing '{datetime_col}' for {sheet_name_label}: {te}. Skipping plot.")
            return


    plt.figure(figsize=(15, 8))
    for col in y_cols_to_plot:
        if col in df_processed.columns:
            # Ensure the column is numeric, converting if necessary and handling potential errors
            df_processed[col] = pd.to_numeric(df_processed[col], errors='coerce')
            # Drop rows where conversion to numeric might have failed (NaNs) for this column for plotting
            plt.plot(df_processed[datetime_col].dropna(), df_processed[col].dropna(), label=col, marker='', linestyle='-')
        else:
            print(f"Warning: Column '{col}' not found in {sheet_name_label} DataFrame. Skipping.")

    plt.title(f'{sheet_name_label} Data Visualization', fontsize=16)
    plt.xlabel('Datetime', fontsize=12)
    plt.ylabel('Values', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True)
    
    # Format the x-axis to display dates nicely
    plt.xticks(rotation=90)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(minticks=20, maxticks=50))
    
    plt.tight_layout() # Adjust layout to prevent labels from overlapping

    plot_filename = f"{output_filename_base}_{sheet_name_label}.png"
    plt.savefig(plot_filename)
    plt.close() # Close the figure to free up memory
    print(f"Plot for {sheet_name_label} saved as {plot_filename}")

# --- Main part of the script ---
def main(excel_file):
    excel_file_path = excel_file+".xlsx" # The name of your Excel file
    df_ul = None
    df_dl = None
    
    if os.path.exists(excel_file_path):
        try:
            # Read the "UL" sheet
            df_ul = pd.read_excel(excel_file_path, sheet_name="UL")
            print(f"Successfully loaded 'UL' sheet from {excel_file_path}")
        except Exception as e:
            print(f"Error loading 'UL' sheet from {excel_file_path}: {e}")
    
        try:
            # Read the "DL" sheet
            df_dl = pd.read_excel(excel_file_path, sheet_name="DL")
            print(f"Successfully loaded 'DL' sheet from {excel_file_path}")
        except Exception as e:
            print(f"Error loading 'DL' sheet from {excel_file_path}: {e}")
    else:
        print(f"Excel file not found: {excel_file_path}")
        print("Please ensure 'result.xlsx' is in the same directory as the script, or provide the full path.")
    
    # Define columns to plot for each sheet
    # For UL sheet
    ul_columns_to_plot = ['UL-Tput', 'UL-MCS']
    # For DL sheet
    dl_columns_to_plot = ['DL-Tput', 'DL-MCS']
    
    # Generate and save plot for UL sheet data
    if df_ul is not None:
        plot_sheet_data(df_ul, 'datettime', ul_columns_to_plot, 'UL', 'excel_timeseries_plot')
    else:
        print("UL DataFrame is not loaded (or failed to load). Skipping UL plot.")
    
    # Generate and save plot for DL sheet data
    if df_dl is not None:
        plot_sheet_data(df_dl, 'datettime', dl_columns_to_plot, 'DL', 'excel_timeseries_plot')
    else:
        print("DL DataFrame is not loaded (or failed to load). Skipping DL plot.")
    
    if df_ul is None and df_dl is None and os.path.exists(excel_file_path):
        print("Both UL and DL DataFrames failed to load. Check sheet names and file content.")

if __name__ == "__main__":
    # Replace these with CLI arguments or other input methods if needed
    excelfilename = input("Please enter the Excel file name (e.g., test): ")

    # Define a tuple of common Excel file extensions
    excel_extensions = ('.xlsx', '.xls', '.xlsm')

    # Check if the entered filename ends with any of the specified extensions
    if excelfilename.lower().endswith(excel_extensions):
        excelfilename=excelfilename.split('.')[0]
    else:
        main(excelfilename)
    