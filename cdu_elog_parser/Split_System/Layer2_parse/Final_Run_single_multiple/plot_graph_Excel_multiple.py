import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def main(excel_file):
    print(f'Excel File Name: {excel_file}')
    # List of sheets to process
    sheets = ['UL', 'DL']
    
    # Calculate the total number of distinct steps for the progress bar
    # 1. Read Excel data
    # 2. Convert datetime column
    # 3. Create figure and plot lines
    # 4. Set ticks and labels
    # 5. Set axis labels and title
    # 6. Adjust layout and save figure
    
    # Let's count 6 major steps per sheet for better granularity
    steps_per_sheet = 6
    total_plotting_steps = len(sheets) * steps_per_sheet

    #excel_file = excel_file+".xlsx" # The name of your Excel file

    # Initialize a single tqdm progress bar for the entire plotting process
    with tqdm(total=total_plotting_steps, desc="Generating Performance Plots", unit="step") as pbar:
        for sheet_name in sheets:
            print(f"Processing sheet: {sheet_name}")
            # --- Step 1: Read the specific sheet from the Excel file ---
            data = pd.read_excel(excel_file, sheet_name=sheet_name)
            pbar.update(1) # Increment progress after reading data

            # Determine column names based on the current sheet
            datetime_col = 'datettime'
            tput_col_ing = f'{sheet_name}_Tput(ingress)'
            tput_col_eng = f'{sheet_name}_Tput(egress)'
            mcs_col = f'{sheet_name}_MCS'
            bler_col = f'{sheet_name}_Bler'

            # --- Step 2: Convert 'datettime' column to datetime objects ---
            data[datetime_col] = pd.to_datetime(data[datetime_col], format='%Y%m%d.%H%M%S.%f')
            pbar.update(1) # Increment progress after datetime conversion

            # Extract relevant columns - ensure datetime is already converted
            datetime_series = data[datetime_col] # Renamed to avoid conflict with `datetime` module
            tput_ingress = data[tput_col_ing]
            tput_engress = data[tput_col_eng]
            mcs = data[mcs_col]
            bler = data[bler_col]
        
            # --- Step 3: Create a new figure and plot lines ---
            # Create a new figure for each sheet, width and height
            plt.figure(figsize=(20, 8), dpi=300) 

            # Plot TWO throughput lines (ingress and egress) 
            plt.plot(datetime_series, tput_ingress, label=f'{sheet_name} Tput(ingress)', color='orange')
            plt.plot(datetime_series, tput_engress, label=f'{sheet_name} Tput(egress)', color='blue')
            plt.plot(datetime_series, mcs, label=f'{sheet_name} MCS', color='red')
            plt.plot(datetime_series, bler, label=f'{sheet_name} Bler', color='green')
            pbar.update(1) # Increment progress after plotting lines

            # --- Step 4: Matplotlib Tick Generation and Formatting ---
            ax = plt.gca() # Get the current axes object for more control
            num_data_points = len(datetime_series)
            desired_num_ticks = 100 

            if num_data_points > desired_num_ticks:
                tick_indices = np.linspace(0, num_data_points - 1, desired_num_ticks, dtype=int)
            else:
                tick_indices = np.arange(num_data_points) # Use all indices if not many points

            # Get the actual datetime values at these indices to use as tick locations
            tick_locations = datetime_series.iloc[tick_indices]
            # Get the actual datetime values at these indices to use as tick labels (formatted)
            tick_labels = datetime_series.iloc[tick_indices].dt.strftime('%Y%m%d.%H:%M:%S.%f') 

            # Set the tick locations and labels
            ax.set_xticks(tick_locations)
            ax.set_xticklabels(tick_labels, rotation=90, ha='right') # Rotate for readability

            # Ensure labels are visible if tick params are used elsewhere
            ax.xaxis.set_tick_params(labelbottom=True) 
            pbar.update(1) # Increment progress after tick formatting

            # --- Step 5: Set Axis Labels, Title, Legend, Grid ---
            ax.set_xlabel('Time', labelpad=10) # Add labelpad for X-axis
            ax.set_ylabel('Value', labelpad=10) # Add labelpad for Y-axis
            ax.set_title(f'{sheet_name} Performance Metrics Over Time') # Use ax.set_title for consistency
        
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            pbar.update(1) # Increment progress after setting labels, legend, grid

            # --- Step 6: Adjust layout and Save the figure ---
            plt.subplots_adjust(left=0.05, right=0.95, bottom=0.3, top=0.95)
            plt.savefig(f'{sheet_name}_performance.png')
            plt.close() # Close the figure to free memory
            pbar.update(1) # Increment progress after saving figure
    print("Plotting complete. Check your directory for UL_performance.png and DL_performance.png")

def main_noprogressbar(excel_file):
    print(excel_file)
    # List of sheets to process
    sheets = ['UL', 'DL']
    #excel_file = excel_file+".xlsx" # The name of your Excel file
    for sheet_name in tqdm(sheets, desc="Drawing Graphs", unit="sheet"): 
    #for sheet_name in sheets:
        print(f"Processing sheet: {sheet_name}")
    
        # Read the specific sheet from the Excel file into a pandas DataFrame
        data = pd.read_excel(excel_file, sheet_name=sheet_name)
    
        # Determine column names based on the current sheet
        datetime_col = 'datettime'
        tput_col_ing = f'{sheet_name}_Tput(ingress)'
        tput_col_eng = f'{sheet_name}_Tput(egress)'
        mcs_col = f'{sheet_name}_MCS'
        bler_col = f'{sheet_name}_Bler'
        #Convert 'datettime' column to datetime objects FIRST ---
        data[datetime_col] = pd.to_datetime(data[datetime_col], format='%Y%m%d.%H%M%S.%f')
        # Extract relevant columns - ensure datetime is already converted
        datetime_series = data[datetime_col] # Renamed to avoid conflict with `datetime` module

        tput_ingress = data[tput_col_ing]
        tput_engress = data[tput_col_eng]
        mcs = data[mcs_col]
        bler = data[bler_col]

        # Create a new figure for each sheet, width and height
        plt.figure(figsize=(20, 8), dpi=300) 

        # Plot TWO throughput lines (ingress and egress) 
        plt.plot(datetime_series, tput_ingress, label=f'{sheet_name} Tput(ingress)', color='orange')
        plt.plot(datetime_series, tput_engress, label=f'{sheet_name} Tput(egress)', color='blue')
        plt.plot(datetime_series, mcs, label=f'{sheet_name} MCS', color='red')
        plt.plot(datetime_series, bler, label=f'{sheet_name} Bler', color='green')
        '''
        # Method1 : 
        
        plt.xlabel('Time', labelpad=10) 
        plt.ylabel('Value', labelpad=10)
        plt.title(f'{sheet_name} Performance Metrics Over Time')

        # Generate numerical indices for tick locations
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
        '''

        #Method2 : this metod overall is better 
        #ax.set_xticks(), ax.set_xticklabels(), ax.xaxis.set_tick_params(), etc.: When you get the Axes object (e.g., ax = plt.gca() or fig, ax = plt.subplots()), 
        #you have direct access to that specific plot's coordinate system and all its sub-elements. 

        # --- Matplotlib Tick Generation and Formatting ---
        ax = plt.gca() #  Get the current axes object for more control
        
        num_data_points = len(datetime_series)
        desired_num_ticks = 100 

        # Ensure there are enough data points for the desired number of ticks
        if num_data_points > desired_num_ticks:
            tick_indices = np.linspace(0, num_data_points - 1, desired_num_ticks, dtype=int)
        else:
            tick_indices = np.arange(num_data_points) # Use all indices if not many points

        # Get the actual datetime values at these indices to use as tick locations
        tick_locations = datetime_series.iloc[tick_indices]
        # Get the actual datetime values at these indices to use as tick labels (formatted)
        tick_labels = datetime_series.iloc[tick_indices].dt.strftime('%Y%m%d.%H:%M:%S.%f') 
        
        # Set the tick locations and labels
        ax.set_xticks(tick_locations)
        ax.set_xticklabels(tick_labels, rotation=90, ha='right') # Rotate for readability

        # Ensure labels are visible if tick params are used elsewhere
        ax.xaxis.set_tick_params(labelbottom=True) 
        
        # --- Set Axis Labels and Pad ---
        ax.set_xlabel('Time', labelpad=10) # Add labelpad for X-axis
        ax.set_ylabel('Value', labelpad=10) # Add labelpad for Y-axis
        ax.set_title(f'{sheet_name} Performance Metrics Over Time') # Use ax.set_title for consistency
        
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        #plt.tight_layout()
        # Adjust layout for rotated labels and save the figure
        plt.subplots_adjust(left=0.05, right=0.95, bottom=0.3, top=0.95)
        
        # Save the figure with a dynamic name based on the sheet
        plt.savefig(f'{sheet_name}_performance.png')
        plt.close()

    print("Plotting complete. Check your directory for UL_performance.png and DL_performance.png")

if __name__ == "__main__":

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
        '''
        # Define a tuple of common Excel file extensions
        excel_extensions = ('.xlsx', '.xls', '.xlsm')

        # Check if the entered filename ends with any of the specified extensions
        main(excel_file_path)    
        if excel_file_input.lower().endswith(excel_extensions):
            excel_file_input=excel_file_input.split('.')[0]
            print(excel_file_input)
        else:
            #main(excel_file_input)
            print(excel_file_input)
        '''
        
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user (Ctrl+C). Exiting gracefully.")
    except Exception as e:
        print(f"\nAn unexpected error occurred in the main execution block: {e}")
        print("Exiting.")