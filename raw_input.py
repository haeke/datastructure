"""
    read a line of input from stdin and save it to a variable,
    print the contents of s to stdout
    constraints 1<=s<=500
"""

def read_std():

    s = "How many chickens does it take to cross the road?"

    #find the length of the string
    size = len(s)
    if((size>=1) and (size <= 500)):
        print s

#test case1
read_std()


"""
    given an integer n
    if n is odd printer Weird
    if n is even and in the inclusive range 2 to 5 print Not Weird
    if n is even and in the inclusive range 6 to 20 print Weird
    if n is even and greater than 20 pritn Not Weird

"""

def weird(n):

    if n % 2 == 1:
        print "Weird"
    elif n % 2 == 0 and 2 <= n <= 5:
        print "Not Weird"
    elif n % 2 == 0 and 6 <= n <= 20:
        print "Weird"
    else:
        print "Not Weird"

weird(24)
