"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
"""

def pig_it(text):
    # Split the text into words
    words = text.split()
    
    # Initialize a list to hold the transformed words
    transformed_words = []
    
    for word in words:
        # Check if the word is punctuation
        if word.isalpha():
            # Move the first letter to the end and add "ay"
            transformed_word = word[1:] + word[0] + "ay"
        else:
            # Leave punctuation marks untouched
            transformed_word = word
        # Add the transformed word to the list
        transformed_words.append(transformed_word)
    
    # Join the transformed words back into a single string
    return ' '.join(transformed_words)

# Test cases
print(pig_it('Pig latin is cool'))  # Output: igPay atinlay siay oolcay
print(pig_it('Hello world !'))      # Output: elloHay orldway !