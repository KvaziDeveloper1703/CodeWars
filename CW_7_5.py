"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
"""

def descending_order(given_number):
    given_number_as_a_string = str(given_number)
    sorted_digits = sorted(given_number_as_a_string, reverse=True)
    highest_number = int(''.join(sorted_digits))
    return highest_number

my_number = input("Write your number here, please: ")
print(descending_order(my_number))