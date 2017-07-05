"""
    merge two lists from smallest to largest

"""

"""
    the most optimzed method to merge the list
    O(n) complexity and O(n) space
"""

def merge_lists(my_list, alices_list):
    #allocate enough space for the combined lists
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:
        """
                make sure the lists are not exhausted - if alices list is exhausted or the current element in my list is less than the current elemtn in alices list
        """

        is_mylist_exhausted = current_index_mine >= len(my_list)
        is_aliceslist_exhausted = current_index_alices >= len(alices_list)

        if not is_mylist_exhausted and (is_aliceslist_exhausted or (my_list[current_index_mine] < alices_list[current_index_alices])):

            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1

        #get alices list
        else:
            mergest_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list

"""
    naive implementation of merging a list and then sorting it just in case it is not in order
    O(nlogn) complexity and O(n^2) space
"""
def merge_lists_naive(my_list, a_list):
    sortedlist = []
    sortedlist.extend(my_list)
    sortedlist.extend(a_list)
    sortedlist.sort()
    print sortedlist

"""
    using sorted we combine and sort the list, this is not the most optimized
    O(nlogn) complexity
"""

def merge_list_sorted(my_list, a_list):
    return sorted(mylist + a_list)
