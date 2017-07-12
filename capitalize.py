"""
    write a function that capitalizes the first letter of everyword
    the word provided is a string

    solved using split, join and capitalize built ins

"""

def capitalizes(word):
    word = ' '.join(words.capitalize() for words in word.split(' '))
    return word

print capitalizes('some words')

print capitalizes('this i s another test these are wor d s')
