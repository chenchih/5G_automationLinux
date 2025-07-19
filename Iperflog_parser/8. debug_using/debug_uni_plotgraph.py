import re
from datetime import datetime
import time
import openpyxl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def process_log_file_to_excel_combined(input_file, output_excel_file):
    data, unit = parse_log_file(input_file)
    if data:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        write_data_to_excel(sheet, data, unit)
        adjust_column_width(sheet)
        workbook.save(output_excel_file)
        print(f"Data written to {output_excel_file}")
        # Plotting the data
        #plot_data(data)
        output_image_file = 'throughput_plot.png' # Or .jpg, .pdf, .svg
        plot_data(data, output_image_file)

def write_data_to_excel(sheet, data, unit):
    header = ["Datetime", "Tput", "gbps"]
    sheet.append(header)
    for row in data:
        sheet.append([row[0], row[1], "gbps"])
    
#Adjusts the first column's width
def adjust_column_width(sheet):
    datetime_column = sheet['A']
    max_length = 0
    for cell in datetime_column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except TypeError:
            pass
    adjusted_width = max_length + 2
    sheet.column_dimensions['A'].width = adjusted_width
    
def parse_log_file(input_file):
    """Parses the log file and returns the data and unit."""
    data = []
    unit = None

    max_results = 10  # Change to 20 if you want more                     
    count = 0    
    with open(input_file, 'r') as infile:
        for line in infile:
            match = re.match(r"(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4}) \[SUM\].*?([\d\.]+) (bits|Mbits|Gbits)/sec",line)
            if match:
                date_str = match.group(1)#datetime
                transfer_str = match.group(2)#tput value
                unit = match.group(3)#unit 
                if unit is None:
                    unit = unit
                    # Increment the appropriate counter                
                date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
                formatted_date = date_obj.strftime("%Y%m%d_%H:%M:%S")
                transfer_value = float(transfer_str)                                  
                if unit == "Mbits":
                    transfer_value /= 1000.0
                elif unit == "bits":
                    transfer_value /= 1000000000.0    
                
                #print(formatted_date, transfer_value, unit)
                data.append([formatted_date, transfer_value])
    return data, unit

def parse_log_file_rx_tx(input_file_path):
    pass
    
    
def plot_data(data, output_image_file):
    """Plots the throughput data over time with specified formatting."""
    if not data:
        print("No data to plot.")
        return

    dates = [datetime.strptime(row[0], "%Y%m%d_%H:%M:%S") for row in data]
    throughput_values = [row[1] for row in data]

    fig, ax = plt.subplots(figsize=(12, 6)) # Create figure and axes objects
    ax.plot(dates, throughput_values, marker='o', linestyle='-', markersize=4)

    ax.set_title('Throughput Over Time')
    #ax.set_xlabel('Time')
    ax.set_xlabel('Time', labelpad=25) # Adjust labelpad value as needed
    ax.set_ylabel('Throughput (Gbps)')
    ax.grid(True)

    # --- X-axis Time Formatting ---
    # Set major locator and formatter for dates
    # You can uncomment and choose one of the following locators:
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5, maxticks=50)) # Adjust tick density
    #ax.xaxis.set_major_locator(mdates.SecondLocator(interval=30)) # Minute Intervals, every 30 minutes
    # ax.xaxis.set_major_locator(mdates.HourLocator(interval=1)) # Hourly Intervals, show a tick every hour
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y%m%d_%H:%M:%S')) # Multi-line format

    # Increase tick label size and rotate
    plt.setp(ax.get_xticklabels(), rotation=90, ha='right', fontsize=12)
    plt.setp(ax.get_yticklabels(), fontsize=12)
    ax.tick_params(axis='x', pad=10)     
    plt.tight_layout()
    
    # Save the figure instead of showing it
    try:
        plt.savefig(output_image_file, dpi=300, bbox_inches='tight') # dpi for resolution
        print(f"Plot saved to {output_image_file}")
    except Exception as e:
        print(f"Error saving plot to {output_image_file}: {e}")
        
    plt.show()
    plt.close(fig) # Close the plot to free up memory
  
###########################################
input_file= input("Please enter your elog FileName: ")
output_excel_file_path = 'output.xlsx'
try:
    process_log_file_to_excel_combined(input_file, output_excel_file_path)
    
except SystemExit:
    print('\nError: Your log file contains Gbits/sec. This script only captures Mbits/sec log files.')
