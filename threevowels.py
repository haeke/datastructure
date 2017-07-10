"""
    you're given a string, convert it into seperate words then check to see if the word contains 3 vowels in it ( we use the re library to check for an occurance of aeiou in a word)
"""

import re

def threevowels(word):
    #split the string into an array of words
    arr = word.split(' ') #split by space
    print arr
    count = 0
    #use a regular expression to see if the word contains 3 vowels
    for item in arr:
        if re.search(r'[aeiou]{3,}', item) != None:
            count += 1

    return count



word = "Thisis a taiest tester sometimes y"

print threevowels(word)
