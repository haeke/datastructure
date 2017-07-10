"""
    find the overlapping range of numbers from two lists
    we wil loop from the star to of the first range to the end. then we check if each of the number swithin that range are greater than the beginning of range 2 and lesser than the end of range 2.
"""


def overlapping(range1, range2):
    overlap = []
    # check whether each number within range 1
    # is within the numbers in range 2
    for i in range(range1[0], range1[1] + 1):
        if i >= range2[0] and i <= range2[1]:
            overlap.append(i)
    return overlap

range1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
range2 = [17, 18, 19, 20, 21]

print overlapping(range1, range2)
