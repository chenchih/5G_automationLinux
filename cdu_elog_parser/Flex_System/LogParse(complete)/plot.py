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

    fig, ax1 = plt.subplots(figsize=(15, 8))
    ax2 = ax1.twinx() # Create a second y-axis that shares the same x-axis
    #plt.figure(figsize=(15, 8))

 # Lists to hold Line2D objects for combined legend later
    lines = []
    labels = []

    for col in y_cols_to_plot:
        if col in df_processed.columns:
            df_processed[col] = pd.to_numeric(df_processed[col], errors='coerce')
            plot_df = df_processed[[datetime_col, col]].dropna() # Ensure both columns are non-NaN for plotting

            if not plot_df.empty: # Only plot if there's valid data
                if 'Tput' in col: # Assuming Tput columns contain 'Tput' in their name (e.g., 'UL-Tput', 'DL-Tput')
                    line, = ax1.plot(plot_df[datetime_col], plot_df[col], label=col, marker='', linestyle='-')
                    lines.append(line)
                    labels.append(col)
                elif 'MCS' in col: # Assuming MCS columns contain 'MCS' in their name (e.g., 'UL-MCS', 'DL-MCS')
                    line, = ax2.plot(plot_df[datetime_col], plot_df[col], label=col, marker='', linestyle='--', color='tomato') # Choose a distinct color like 'red' or 'orange'
                    lines.append(line)
                    labels.append(col)
                else:
                    print(f"Warning: Column '{col}' type not recognized for plotting. Skipping.")
            else:
                print(f"Warning: Column '{col}' in sheet '{sheet_name_label}' has no valid data after cleaning. Skipping.")
        else:
            print(f"Warning: Column '{col}' not found in {sheet_name_label} DataFrame. Skipping.")

    ax1.set_title(f'{sheet_name_label} Data Visualization', fontsize=16) # Title should be on ax1
    ax1.set_xlabel('Datetime', fontsize=12, labelpad=20) # Apply xlabel directly to ax1
    ax1.set_ylabel('Tput', fontsize=12, labelpad=20)     # Apply ylabel directly to ax1
    
    # Your legend line which was already updated for ax1:
    # ax1.legend(lines, labels, fontsize=10, loc='upper left') 
    
    ax1.grid(True) # Grid for the primary axis (ax1)

    ax2.set_ylabel('MCS', fontsize=12, color='red') # Set label for the right y-axis
    ax2.tick_params(axis='y', labelcolor='red') # Make tick labels match the line color

    # Set MCS y-axis limits (adjust based on typical MCS ranges, e.g., 0 to 31)
    # This assumes there's at least one 'MCS' column in y_cols_to_plot
    mcs_cols_in_df = [col for col in y_cols_to_plot if 'MCS' in col and col in df_processed.columns]
    if mcs_cols_in_df and not df_processed[mcs_cols_in_df[0]].dropna().empty:
        max_mcs_val = df_processed[mcs_cols_in_df[0]].max() # Get max from the first found MCS column
        ax2.set_ylim(0, max(max_mcs_val * 1.1, 15)) # Set upper limit with 10% buffer, minimum of 15 (adjust as needed for your MCS scale)
    else:
        ax2.set_ylim(0, 35) # Fallback default if no MCS data (e.g., 0-35 is common for MCS index)
    
    # Format the x-axis to display dates nicely, applying directly to ax1
    ax1.tick_params(axis='x', rotation=90, pad=10) # Use tick_params for x-axis rotation on ax1
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S')) # Apply formatter directly to ax1's x-axis
    ax1.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=20, maxticks=50)) # Apply locator directly to ax1's x-axis
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
    