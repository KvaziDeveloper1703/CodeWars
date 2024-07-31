"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
"""

def rgb(r, g, b):
    # Helper function to clamp the value and convert to hexadecimal
    def clamp_and_convert(value):
        # Clamp the value to be within the valid range of 0 to 255
        value = max(0, min(255, value))
        # Convert to hexadecimal and ensure it is two digits long
        hex_value = hex(value)[2:]  # Convert to hex and remove the '0x' prefix
        if len(hex_value) == 1:
            hex_value = '0' + hex_value  # Pad with leading zero if necessary
        return hex_value.upper()

    # Convert each component and concatenate the results
    return clamp_and_convert(r) + clamp_and_convert(g) + clamp_and_convert(b)

# Test cases
print(rgb(255, 255, 255))  # Output: "FFFFFF"