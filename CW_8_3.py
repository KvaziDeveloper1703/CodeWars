"""
You get an array of numbers, return the sum of all of the positives ones.
"""

def sum_of_positives(given_numbers):
    sum = 0
    for number in numbers:
        if number > 0:
            sum = sum + number
    return sum

my_array = [1, -4, 7, 12]
print(sum_of_positives(my_array))