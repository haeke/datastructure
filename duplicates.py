"""
    write a function that returns a list of all duplicate files. We'll check them by hand before actually deleting them. Since programmatically deleting files can be 'scary'.

    return a list of tuples where -
    the first items is the duplicate file
    the second item is the original file

"""

# use a dictionry to hold files weve already seen
# stack to hold directories and files as we go through them
# list to hold our output tuples
def find_dupe_files(starter):
    files_seen_already = {}
    stack = [starter]

    #track tuples ( dupes and original)
    duplicates = []

    while len(stack):
        current_path = stack.pop()

    return duplicates
