"""
    hacker rank list comprehension

    this program gets the range of a cubic that is not larger than an integer provided

    constaints: 0<=x and 0<=y and 0<=z where it is not equal to n

"""

def comprehensions(x, y, z, n):
    xlist = range(x + 1)
    ylist = range(y + 1)
    zlist = range(z + 1)

    completelist = [[x,y,z] for x in xlist for y in ylist for z in zlist if x+y+z != n]

    print completelist

comprehensions(1,1,1,2)
print('Next set')
comprehensions(2,3,4,7)
