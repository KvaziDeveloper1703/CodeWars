"""
Write a program that takes in a string of one or more words, and returns the same string, 
but with all words that have five or more letters reversed.
https://www.codewars.com/kata/5264d2b162488dc400000001
"""

def spin_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    return ' '.join(words)

my_sentence = input("Write your sencence here, please: ")
processed_sentence = spin_words(my_sentence)
print(processed_sentence)