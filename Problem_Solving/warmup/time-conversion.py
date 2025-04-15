# Problem: Birthday Time Conversion
# https://www.hackerrank.com/challenges/time-conversion/

from datetime import datetime

def timeConversion(s):
    """
    Converts a 12-hour time string (e.g., '07:05:45PM') to 24-hour format.
    
    Parameters:
    time_12h (str): Time in 12-hour format with AM/PM (e.g., '07:05:45PM')
    
    Returns:
    str: Time in 24-hour format (e.g., '19:05:45')
    """
    return datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")

if __name__ == '__main__':
    # Example tests
    print(timeConversion("07:05:45PM"))  # Output: "19:05:45"
    print(timeConversion("12:00:00AM"))  # Output: "00:00:00"
    print(timeConversion("12:00:00PM"))  # Output: "12:00:00"
    print(timeConversion("01:00:00AM"))  # Output: "01:00:00"