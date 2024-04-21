"""
Write a program that returns the sum of all the multiples of 3 or 5 below the number passed in.

If the number is negative, return 0.
"""

def sum_multiples_of_3_or_5(number):
    if number <= 0:
        return 0
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return sum

my_number = input("Write your number here, please: ")
print(sum_multiples_of_3_or_5(my_number))