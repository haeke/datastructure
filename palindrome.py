
"""Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string."""

"""
    solution is O(n^3)
    check to see if each substring is a palindrome or not, we check all the substrings

"""

def ret_substrings(s):
    l = len(s)

    for e in range(l, 0, -1):
        for i in range(l - e + 1):
            #return an object containing the substring from largest to shortest
            yield s[i: i+e]

# Define palindrome.
def palindrome(s):
    #check to see if the substring is the same as the string provided
    return s == s[::-1]

#for the string provided get all the substrings
#compare them to the string provided then return
def question2(a):
    for l in ret_substrings(a):
        if palindrome(l):
            return l

# Simple test case.
print question2("rerrmomsmomfhei") #expect momsmom
print question2("wjir3")
