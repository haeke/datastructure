"""
        given an array and a number S - determine if any two numbers within the array sum to S

        approach - loop through the array, add each element to a hash table, then check if the number minus the current element exists in the hash table we are looping
"""

def sumstos(numbers, number):
    hashtable = {}

    #check each element in the numbers array
    for i in range(0, len(numbers)):
        #calculate S minus current element
        sumMinusElement = number - numbers[i]
        #check if the number is in the table
        if sumMinusElement in hashtable:
            return True

        #add the current number to the hash table
        hashtable[numbers[i]] = True
    return False

numbers = [1,3,4,6,7]
number = 4

print sumstos(numbers,number)
