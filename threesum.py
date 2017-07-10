"""
    given an array and a number S - determine if any three numbers withing the array sum to S

    First we sort the array into ascending order. We can use a built-in sort function which will run in O(nlogn).[1] Then we loop through each element in the array and for each of the elements we maintain two pointers (or indices), one from the (current position + 1) and the second pointer starting from the end of the array. Then we check to see if these 3 elements sum to S. One of 3 things will be true:
        1. If the current element plus the 2 other elements is greater than S, we decrease the pointer at
        the end of the array at 1.
        2. If the current element plus the other 2 elements is less than S, we increase the pointer at the
        beginning by 1.
        3. If the pointers end up meeting, then we know we cannot add 2 elements plus the current
        element to sum to S. We move on to the next element in the array and reset the pointers.
"""

def threesum(arr, num):
    arr = sorted(arr)

    for i in range(0, len(arr) - 2):
        #start two pointers, one from thre current position + 1
        #the other at the end of the array
        ptr_start, ptr_end = i + 1, len(arr) - 1

        while ptr_start < ptr_end:
            add = arr[i] + arrpptr_start] + arr[ptr_end]

            #if we find a sum
            if add == num:
                return True
            #if the sum is < num
            elif add < num:
                ptr_start += 1
            #if the sum is > num
            else:
                ptr_end -= 1
        return False
