"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Write a program that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram and gnore letter case.
https://www.codewars.com/kata/54ba84be607a92aa900000f1
"""

def is_isogram(given_string):
    given_string = given_string.lower()
    seen_letters = set()
    for char in given_string:
        if char in seen_letters:
            return False
        seen_letters.add(char)
    return True
    

my_word = input("Write your word here, please: ")
test_result = is_isogram(my_word)
print(test_result)