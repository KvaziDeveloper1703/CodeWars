"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the troll's comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""

def vowel_buster(given_comment):
    original_comment=given_comment
    processed_comment=""
    vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
    for character in original_comment:
        if character not in vowels:
            processed_comment=processed_comment+character
            
    return processed_comment

troll_comment = input("Write any inappropriate comment here, please: ")
processed_comment = vowel_buster(troll_comment)
print(processed_comment)