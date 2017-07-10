"""
    find the majority element that appears more than n / 2 times
    using the majority vote algorithm to solve this problem
    start with a candidate element that is empty and count that is set to 0.
    for each element in the array we check it against the candidate element
    if the candidate element is blank or the count is 0, set the current element to be the candidate element and set the count to 1. if the current element equals the candidate element, increase the count by 1. if the current element does not equal the candidate element, decrease the count by 1.

"""

import math

def majorityelement(number):
    candidate = None
    count = 0

    # case 1 - if candidate is None or count is 0 setcandidate to the current element
    # case 2 - if the candidate matches cuirrent element we increase the count
    # case 3 - if candidate does nto match current element, decrease the count by 1
    for i in range(0, len(number)):
        if candidate is None or count == 0:
            candidate = number[i]
            count = 1
        elif number[i] == candidate:
            count += 1
        else:
            count -= 1
    #once we have a majority element we check to make sure it occurs more than n / 2 times
    count = 0
    for element in number:
        if element == candidate:
            count += 1

    if count > math.floor(len(number) / 2):
        return candidate
    else:
        return None

number = [1,2,2,2,2,4]
print majorityelement(number)
