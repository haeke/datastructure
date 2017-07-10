"""
    write a function to change the letters of all the consonants in a string [ keep the vowels the same]
"""

def encodeconsonants(string):

    result = ''

    #keep a reference of the vowels
    vowels = ['a','e','i','o','u']

    #loop through the string
    for i in string:
        # z should be replaced with b
        if i == 'z':
            result += 'b'
            break
        #if letter is not a vowel or a space
        elif i not in vowels and i != ' ':
            #convert each letter to its character code
            newcode = ord(i) + 1
            #check to make sure new letter is not a vowel
            if chr(newcode) in vowels:
                newcode += 1

            #get new letter and add to new string
            result += chr(newcode)
        #otherwise character is a vowel or space
        else:
            result += i
    return result

print encodeconsonants('this is a test please work')
