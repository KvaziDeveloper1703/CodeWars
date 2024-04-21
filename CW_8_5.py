"""
Write a program that takes a boolean value and return a "Yes" string for True, or a "No" string for False.
"""

def bool_to_word(given_boolean):
    if given_boolean == True:
        return "Yes"
    else:
        return "No"

my_boolean = input("Write True or False here, please: ")
print(bool_to_word(given_boolean))