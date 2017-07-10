"""
    given a number of lightbulbs represented by n and n number of people each turning on or off
    write a function that goes through n light bulbs and performs eac hoperation for every person labeled from 1 to n.
"""

def lightbulb(n):
    #create n lightbulbs and set them to off / False
    lightbulbs = [False for i in range(0, n)]

    #each person i labeled from 1 to n sets each Kth lightbulb on or off where k = 2*i, 3*i etv.
    for i in range(1, n +1):
        w = 1
        k = w * i
        while k <= n:
            lightbulbs[k - 1] = not lightbulbs[k - 1]
            w += 1
            k = w * i

    return lightbulbs

print lightbulb(100)
