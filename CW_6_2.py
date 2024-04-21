"""
Write a program that takes in a string of one or more words, and returns the same string, 
but with all words that have five or more letters reversed.
"""

def spin_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    return ' '.join(words)

my_sentence = input("Write your sencence here, please: ")
print(spin_words(my_sentence))