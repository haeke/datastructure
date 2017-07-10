"""
    write a function that takes in a list and function and applies the function to each element in the list and returns a new list
"""

def map(arr, fn):
    result = []

    # apply the function to each element and store the result
    for i in arr:
        applied = fn(i)
        result.append(applied)

    return result

#in practice
square = lambda x: x * x
addzero = lambda x: int(str(x) + '00')

print map([1,2,3,4], square)
print map([1,2,3,4,], addzero)
