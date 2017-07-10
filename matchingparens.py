"""
    write a function that checks to see that you have a valid number of parens aka no starting "(" should follow with a  ")"
"""

def matchingparens(string):
    count = 0
    #loop through the string, use the counter to keep track if the input
    for c in string:
        print c
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
    #after checking the string the result should be 0 if there are matching pairs
    if count == 0:
        return True
    else:
        return False

string = "()"

print matchingparens(string)
