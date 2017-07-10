"""
    return the first character that is unique given a string
"""
def norepeat(word):
    # use a hash table for comparing`
    hashtable = {}

    #store each character in the hash table with the frequency of times ir occurs
    for c in word:
        if c not in hashtable:
            hashtable[c] = 1
        else:
            hashtable[c] += 1

    #loop through the string, return the first occurance of 1
    for c in word:
        if hashtable[c] == 1:
            return c

    return False


print norepeat("racecarse")
