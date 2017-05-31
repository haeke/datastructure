### Question 1 main function and helper functions.
"""Given two strings s and t, determine whether some anagram of t is a
substring of s. For example: if s = "udacity" and t = "ad", then the
function returns True. Your function definition should look like:
question1(s, t) and return a boolean True or False."""
"""
    complexity is O(n^2)
    To solve this problem, I created lists of the two strings that were given,
    we sort them alphabetically then compare them to see if they are the same.
"""

def isanagram(s1, s2):

    # create lists of the strings so they can be sorted then compared
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    #return comparison ( will get true or false)
    #complexity of comparison is O(n)
    return s1 == s2

# Main function.
def question1(t, s):

    # get the lengh of both strings
    t_len = len(t)
    s_len = len(s)

    # Setting the range to be the string we want to compare
    #complexity of for in iteration is O(n)
    for i in range(s_len - t_len):
        # Call helper function which checks for t in s.
        if isanagram(s[i:i+t_len], t):
            return True
    return False

# first test
print question1("ud", "udacity")

print question1("", "check this")
# True
