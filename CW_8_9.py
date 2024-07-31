"""
Write a program that recieves an integer and a string as an input and returnes the string repeated as many times as the integer says.
https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
"""

def repeat_the_string(given_number, given_string):
    return given_string * given_number

my_number = int(input("Write your number here, please: "))
my_string = input("Write your string here, please: ")

repeated_string = repeat_the_string(my_number, my_string)
print(repeated_string)