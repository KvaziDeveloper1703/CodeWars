"""
Write a program that finds the number that appears an odd number of times in a given array of integers.

There will always be only one integer that appears an odd number of times.
"""

def find_odd_occurrence(given_array):
    counts = {}
    for number in given_array:
        if number in counts:
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1
    for number, count in counts.items():
        if count % 2 != 0:
            return number

my_array = [3,1,1,2,2]
print(find_odd_occurrence(my_array))