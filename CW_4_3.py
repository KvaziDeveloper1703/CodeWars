"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
"""

def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    time_units = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    ]
    
    parts = []
    
    for name, count in time_units:
        value = seconds // count
        if value:
            seconds -= value * count
            if value > 1:
                parts.append(f"{value} {name}s")
            else:
                parts.append(f"{value} {name}")
    
    if len(parts) > 1:
        return ', '.join(parts[:-1]) + ' and ' + parts[-1]
    else:
        return parts[0]

# Example usage
print(format_duration(62))       # Output: "1 minute and 2 seconds"
print(format_duration(3662))     # Output: "1 hour, 1 minute and 2 seconds"
print(format_duration(0))        # Output: "now"
print(format_duration(31536000)) # Output: "1 year"