"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""

def move_zeros(arr):
    # Initialize two lists, one for non-zeros and one for zeros
    non_zeros = []
    zeros = []
    
    # Separate the elements into non-zeros and zeros
    for num in arr:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    
    # Combine the non-zeros followed by the zeros
    return non_zeros + zeros

# Test case
print(move_zeros([1, 0, 1, 2, 0, 1, 3]))  # Output: [1, 1, 2, 1, 3, 0, 0]