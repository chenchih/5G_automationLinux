"""Calculates the duration between two datetime strings.
start_str: The start datetime string in the format "YYYYMMDD_HH:MM:SS".
end_str: The end datetime string in the format "YYYYMMDD_HH:MM:SS".
"""
from datetime import datetime, timedelta
def calculate_duration(start_str, end_str):

    try:
        start_dt = datetime.strptime(start_str, "%Y%m%d_%H:%M:%S")
        end_dt = datetime.strptime(end_str, "%Y%m%d_%H:%M:%S")
        duration = end_dt - start_dt

        days = duration.days
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        result = ""
        if days > 0:
            result += f"{days} days "
        if days > 0 or hours > 0:
            result += f"{hours} hrs "
        result += f"{minutes} min"
        
        converhrs=days * 24 + hours
        
        # convert time to hours alternative
        '''
        total_seconds = int(duration.total_seconds())

        days = total_seconds // (24 * 3600)
        remaining_seconds = total_seconds % (24 * 3600)
        hours = remaining_seconds // 3600
        remaining_seconds %= 3600
        minutes = remaining_seconds // 60
        #print(f"Running duration: {days} days, {hours} hours, {minutes} minutes")
        #print(f"Converted hours: {days * 24 + hours} hours") 
        '''
        return result, converhrs
        
    except ValueError:
        return "Invalid date format. Please use YYYYMMDD_HH:MM:SS"
# Example usage
#start_time_str = "20250314_17:16:31"
#end_time_str = "20250317_07:56:19"
print('Welcome to calcuateing time tool: YYMMDD_HH:MMSS ex: 20250317_07:56:19')
start_time_str= input('enter your starting date:')
end_time_str = input('enter your ending date:')

duration_str, total_hrs = calculate_duration(start_time_str, end_time_str)
print(f'Running duration: {duration_str}')
#print(f"Running duration: {days} days, {hours} hours, {minutes} minutes")
print(f"Converted hours: {total_hrs} hours") 


input('Press Enter to close...')