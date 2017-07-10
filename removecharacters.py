"""
    write a function to return a string with all the characters from an array using a hash table makes it easier to compare the characters against the word we want to check it against
"""

def removecharacters(word, characters):
    #create an empty hashtable to store characters
    hashtable = {}
    #populate the hash table with the word
    for c in word:
        hashtable[c] = True

    #loop through the steing and check if the charcter exists in the hash table, if it does we do not add it
    result = ''
    for c in characters:
        if c not in hashtable:
            result += c

    return result

print removecharacters(["r","w","e"], "hello everybody")
