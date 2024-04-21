"""
In this task, you are asked to square every digit of a number and concatenate them.

For example, an input of 765 will return 493625.
"""

def square_digits(given_number):
    our_number_as_an_integer = given_number
    processed_number = ""
    our_number_as_a_string=str(our_number_as_an_integer)
    for digit_as_a_string in our_number_as_a_string:
        digit_as_an_integer = int(digit_as_a_string) 
        squared_digit = digit_as_an_integer**2
        squared_digit_as_a_string = str(squared_digit)
        processed_number=processed_number+squared_digit_as_a_string
    processed_number_as_an_integer=int(processed_number)
    return processed_number_as_an_integer

my_number = input("Write your number here, please: ")
processed_number = square_digits(my_number)
print(processed_number)