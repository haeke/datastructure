"""
    you're provided a word, remove any repeating letters from it and return the result
"""

def removeadjacent(word):
    #string to hold the result
    result = ''
    count = 0

    while count < len(word):
        #if we are on the last chracter
        if count == len(word) - 1: #starts at 0
            result += word[count]
        #characters are not eqal then add to the result
        elif word[count] != word[count + 1]:
            result += word[count]
        else:
            #don't add the current letter it is repeating
            count += 1 #if they are equal then keep looping
        count += 1

    return result


print removeadjacent("eevcjei3")
