"""
    calculate the sum of nested arrays
    iterate through the entire list, if a nested array is found
    loop through the elements
"""

def sumsnested(numbers):
    result = 0
    #loop through the length of the array
    for i in range(0, len(numbers)):

        #check that the element is a nested array, then sum the elements`
        if type(numbers[i]) is not int:
            result += sumsnested(numbers[i])
        else:
            result += numbers[i]

    return result

numbers = [1,3,5,7,[4,5,[6]]]

print sumsnested(numbers)
