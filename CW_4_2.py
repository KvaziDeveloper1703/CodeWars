"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""

def snail(array):
    result = []
    while array:
        # Take the first row
        result += array.pop(0)
        if array and array[0]:
            # Take the right column
            for row in array:
                result.append(row.pop())
        if array:
            # Take the bottom row in reverse order
            result += array.pop()[::-1]
        if array and array[0]:
            # Take the left column in reverse order
            for row in array[::-1]:
                result.append(row.pop(0))
    return result

# Example usage
array1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(snail(array1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

array2 = [[1, 2, 3],
          [8, 9, 4],
          [7, 6, 5]]
print(snail(array2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]