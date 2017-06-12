"""
    find the second largest number given an array and a number containing the amount of items contained

    sort the list that you're provided then output the second to last item in the list
    we need to take the length of the array
"""

#if you do not count duplicates
def secondlargestnodupes(n, A):
    secondlargest = sorted(A)
    #print secondlargest
    print secondlargest[(len(secondlargest)-2)]

def secondlargest(n,A):
    #empty list to hold
    list = []
    #get the largest item in the list
    largest = max(A)
    #loop through the list
    for i in range(len(A)):
        #as long as the largest is not in the list the max will be second largest
        #this also handles duplicates of the largest value
        if largest != A[i]:
            list.append(A[i])
    #get the maximum of the new list
    maxi = max(list)
    print maxi


n = 5
A = [2,3,5,7,7,6,7,8,31,30,31,9,5,3,8,5]
secondlargestnodupes(n, A)
secondlargest(n,A)
