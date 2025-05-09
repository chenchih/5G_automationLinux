import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_from_excel_simple_adjusted(excel_file):
    """Reads an Excel file and plots 'Datetime' vs 'Tput' from each sheet with adjusted axes."""
    try:
        all_sheets_data = pd.read_excel(excel_file, sheet_name=None)
        for sheet_name, df in all_sheets_data.items():
            if 'Datetime' in df.columns and 'Tput' in df.columns:
                # Ensure 'Datetime' is treated as string for direct display
                datetime_col = df['Datetime']
                tput_col = pd.to_numeric(df['Tput'], errors='coerce') # Convert Tput to numeric, handle errors

                plt.figure(figsize=(12, 5), dpi=150)  # Adjust figure size if needed
                plt.plot(datetime_col, tput_col, label='Tput')
                plt.xlabel('Time')
                plt.ylabel('Throughput (gbps)')
                plt.title(f'Throughput - {sheet_name}')
                plt.legend()
                plt.grid(True)

                # Set y-axis limits
                plt.ylim(0, 4)

                # Display full datetime on x-axis
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                plt.savefig(f"tput_adjusted_{sheet_name}.png")
                plt.close()
                print(f"Adjusted plot for {sheet_name} saved.")
            else:
                print(f"Warning: Sheet '{sheet_name}' missing 'Datetime' or 'Tput' columns.")
    except FileNotFoundError:
        print(f"Error: Excel file '{excel_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    excel_file = "all_log_txt_output.xlsx"  # Assuming your Excel file is named this
    plot_from_excel_simple_adjusted(excel_file)
    print("Adjusted plotting complete.")