"""
    write a method that takes in a list and function with a conditional statement and returns a new list where every element in the original list passes the conditional statement ( returns True)

"""

def filter(arr, fn):

    result = []

    #pass the element to the function and check if the result comes back true
    for i in arr:
        check = fn(i)
        if check:
            result.append(i)

    return result

#in practice
isPositive = lambda x: x > 0
#this will return a list of the postive values in the array passed
print filter([-2,4,5,6,8,10], isPositive)
