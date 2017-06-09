"""
    generators and list comprehensions

    generated() builds a list of cubes by creating an empty and appending the contents from 1 to n using a counter

    generatedYield() returns a list using the keyword yield that needs to be printed after the function call

    listcomp() both builds a list and prints a list using xrange()

"""

#generate the cubes of n

def cubed(n):
    return n**3

#generator return a list of n items cubed
def generated(n):
    genList = []
    current = 1
    while current < n:
        genList.append(cubed(current))
        current += 1
    return genList

print generated(10)

#create a generated using yield to make the list
def generatedYield(n):
    current = 1
    while current < n:
        yield(cubed(current))
        current += 1

#store the generated object
genobject =  generatedYield(10)

#print the contents of the generated object in one line
print[i for i in genobject]

"""
    if we wanted to use list comprehensions we can use xrange(start to stop)
"""

def listcomp():
    #create the range we want to print this will create a list from 1 to 10
    original = xrange(1,11)

    print "Iterate through the list comprehension"
    for i in xrange(1,11):
        print cubed(i)

    print "Print a list of the list comprehension in one line as a list "
    cubesList = [cubed(x) for x in original]
    print cubesList

listcomp()
