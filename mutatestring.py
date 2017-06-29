"""
    Task -

    Read a given string, change the character at a given index and then print the modified string.

    Input Format
    The first line contains a string, .
    The next line contains an integer , denoting the index location and a character  separated by a space.

    Output Format
    Using any of the methods explained above, replace the character at index  with character .

"""

def mutate_string(string, position, character):
    string = string[:int(position)] + character + string[(int(position)+1):]
    return string


print mutate_string('abracadabra', 5, 'k')
