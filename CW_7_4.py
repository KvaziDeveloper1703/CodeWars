"""
In this assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
"""

def highest_and_lowest(given_numbers):
    array_of_numbers=given_numbers.split()
    array_of_int_numbers=[]
    for number in array_of_numbers:
        array_of_int_numbers.append(int(number))

    maximum=max(array_of_int_numbers)
    minimum=min(array_of_int_numbers)

    return str(maximum) + " " + str(minimum)

my_string_of_numbers = input("Write your string of numbers here, please: ")
print(highest_and_lowest(my_string_of_numbers))

