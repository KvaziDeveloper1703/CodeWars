"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
"""

def next_bigger(n):
    digits = list(str(n))
    length = len(digits)

    # Step 1: Find the pivot, the point (from right) where the digits start to decrease
    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return -1  # No pivot found, meaning the number is the largest possible with its digits

    # Step 2: Find the smallest digit on right side of pivot that is larger than pivot
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            break

    # Step 3: Swap the pivot with the found digit
    digits[i], digits[j] = digits[j], digits[i]

    # Step 4: Sort the digits to the right of the pivot in ascending order
    digits = digits[:i + 1] + sorted(digits[i + 1:])

    return int("".join(digits))

# Example usage
print(next_bigger(12))    # Output: 21
print(next_bigger(513))   # Output: 531
print(next_bigger(2017))  # Output: 2071