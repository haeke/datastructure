"""
    return the mean median and mode of an array

    python has a builtin to sum an array and get the length of the array
    python has a builtin to sort and array then we can get midpoint of the array by dividing the length by 2
    using a hashtable to store the elements we can count which number repeats and keep the largest count 

"""

def meanmedianmode(arr):
    #sum the array and then divide by the number of elements in the array
    mean = sum(arr) / float(len(arr))

    #sort the array then get the point of the array that is half the size
    arr = sorted(arr)
    #get the element that is half the arrays size
    median = arr[int(len(arr) / 2)]

    #to get the mode, store all the elements into a hash table and keep a count and also always maintain the largest count
    mode = None
    hashtable = {}
    for i in arr:
        if i in hashtable:
            hashtable[i] += 1
        else:
            hashtable[i] = 1
        if mode is None or hashtable[i] > mode:
            mode = i
    return { 'mean': mean, 'median': median, 'mode': mode }

arr = [1,3,5,6,8,10,10]

print meanmedianmode(arr)
