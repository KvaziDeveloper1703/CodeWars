"""
Write me a program on Python that takes a number and makes it negative if it is not negative yet.
"""

def make_negative(number):
    return -abs(number)

my_number = input("Enter your number here, please: ")
print(make_negative(my_number))