"""
Return the number of vowels in the given sentence.

We will consider a, e, i, o, u, y as vowels.

The input string will only consist of lower case letters and/or spaces.
"""

def count_vowels(sentence):
    counter=0
    vowels = ["a","e","i","o","u","y"]
    for character in sentence:
        if character in vowels:
            counter=counter+1
    return counter

my_sentence = input("Write your sentence here, please: ")
number_of_vowels_in_a_sentence = count_vowels(my_sentence)
print(number_of_vowels_in_a_sentence)