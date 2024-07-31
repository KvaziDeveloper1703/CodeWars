"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
"""

def format_time(seconds):
    # Calculate hours, minutes, and seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    # Format with leading zeros
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Test cases
print(format_time(0))       # Output: 00:00:00