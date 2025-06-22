import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def main(excel_file):
    print(f'Excel File Name: {excel_file}')
    # List of sheets to process
    sheets = ['UL', 'DL']
    steps_per_sheet = 12 #6
    total_plotting_steps = len(sheets) * steps_per_sheet
    
    #excel_file = excel_file+".xlsx" # The name of your Excel file
    with tqdm(total=total_plotting_steps, desc="Generating Performance Plots", unit="step") as pbar:
        for sheet_name in sheets:
            #print(f"Processing sheet: {sheet_name}") 
            tqdm.write(f"Processing sheet: {sheet_name}") 
            #tqdm.write(f"Processing sheet: {sheet_name}")
            # Step 1: Read the specific sheet
            # Read the specific sheet from the Excel file into a pandas DataFrame
            data = pd.read_excel(excel_file, sheet_name=sheet_name)
            pbar.update(1) # Increment progress after reading data
            
            
            # Step 2: Convert datetime
            # Determine column names based on the current sheet
            datetime_col = 'datettime'
            tput_col = f'{sheet_name}-Tput'
            mcs_col = f'{sheet_name}-MCS'
            bler_col = f'{sheet_name}-Bler'
            
            #Convert 'datettime' column to datetime objects ---
            data[datetime_col] = pd.to_datetime(data[datetime_col], format='%Y%m%d.%H%M%S.%f')
            pbar.update(1) # Increment progress after datetime conversion
            
            # Step 3: Extract series
            # Extract relevant columns - ensure datetime is already converted
            datetime_series = data[datetime_col] # Renamed to avoid conflict with `datetime` module
            tput = data[tput_col]
            mcs = data[mcs_col]
            bler = data[bler_col]
            pbar.update(1)
            # Step 4: Initialize figure
            # Create a new figure for each sheet, width and height
            plt.figure(figsize=(20, 8), dpi=300) 
            pbar.update(1)
            
            # Step 5–7: Plotting lines
            plt.plot(datetime_series, tput, label=f'{sheet_name} Tput', color='blue'); pbar.update(1)
            plt.plot(datetime_series, mcs, label=f'{sheet_name} MCS', color='red'); pbar.update(1)
            plt.plot(datetime_series, bler, label=f'{sheet_name} Bler', color='green'); pbar.update(1)
            
            
            ''' Method2
            # Get the current axes object
            #ax = plt.gca() # <--- GET AXES OBJECT HERE
            # --- Set Axis Labels and Pad ---
            #ax.set_xlabel('Time', labelpad=10) # Add labelpad for X-axis
            #ax.set_ylabel('Value', labelpad=10) # Add labelpad for Y-axis
            #ax.set_title(f'{sheet_name} Performance Metrics Over Time') # Use ax.set_title for consistency
            '''
            
            # Step 8: Format X ticks
            # 1. Generate numerical indices for tick locations
            num_data_points = len(datetime_series)
            desired_num_ticks = 100 # You specified 100 ticks
            # Calculate the indices where you want ticks to appear
            tick_indices = np.linspace(0, num_data_points - 1, desired_num_ticks, dtype=int)
            # Get the actual datetime values at these indices to use as tick labels
            tick_labels = datetime_series.iloc[tick_indices].dt.strftime('%Y%m%d.%H:%M:%S.%f') 
            
            # Set the tick locations using the actual datetime values for Matplotlib's internal date conversion
            # And set the tick labels using the formatted strings
            plt.xticks(datetime_series.iloc[tick_indices], tick_labels, rotation=90) # Pass datetime values as locations
            
            plt.gca().xaxis.set_tick_params(rotation=90, labelbottom=True) # Ensure labels are drawn
            pbar.update(1) # Increment progress after tick formatting
            
            
            # Step 9–11: Set labels, title, legend, grid
            plt.xlabel('Time', labelpad=10) ; pbar.update(1)
            plt.ylabel('Value', labelpad=10); pbar.update(1)
            plt.title(f'{sheet_name} Performance Metrics Over Time')
        
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            pbar.update(1) # Increment progress after setting labels, legend, grid
            #plt.tight_layout()
            
            # Step 12: Save figure
            plt.subplots_adjust(left=0.05, right=0.95, bottom=0.3, top=0.95)
            #plt.tight_layout(rect=[0.05, 0.2, 0.95, 0.95])
            # Save the figure with a dynamic name based on the sheet
            plt.savefig(f'{sheet_name}_performance.png')
            plt.close()
            pbar.update(1)
  
    print("Plotting complete. Check your directory for UL_performance.png and DL_performance.png")


if __name__ == "__main__":
    '''
    # Define the Excel file name
    #excel_file = 'test.xlsx'
    
    # Replace these with CLI arguments or other input methods if needed
    excel_file = input("Please enter the Excel file name (e.g., test): ")

    # Define a tuple of common Excel file extensions
    excel_extensions = ('.xlsx', '.xls', '.xlsm')

    # Check if the entered filename ends with any of the specified extensions
    if excel_file.lower().endswith(excel_extensions):
        excel_file=excel_file.split('.')[0]
    else:
        main(excel_file)
    '''
    
    try:
        # Replace these with CLI arguments or other input methods if needed
        excel_file_input  = input("Please enter the Excel file name (e.g., test): ")
        
        if not excel_file_input.lower().endswith(('.xlsx', '.xls', '.xlsm')):
            excel_file_path  = excel_file_input + ".xlsx"
            #print(excel_file_path)
        else:
            excel_file_path  = excel_file_input   # If it already has extension, use as is
            #print(excel_file_path)
        
        #print(f"Attempting to process: {excel_file_path}")
        main(excel_file_path) # Call main with the correctly formatted path
    except KeyboardInterrupt:
        print("\nOperation cancelled by user (Ctrl+C). Exiting gracefully.")
    except Exception as e:
        print(f"\nAn unexpected error occurred in the main execution block: {e}")
        print("Exiting.")