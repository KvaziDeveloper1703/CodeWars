"""
Write a program that reverses a string.
"""

def reverse_string(my_string):
    reversed_string = ''
    for i in range(len(my_string) - 1, -1, -1):
        reversed_string = reversed_string + my_string[i]
    return reversed_string

my_string = input("Write your string here, please: ")
print(reverse_string(my_string))