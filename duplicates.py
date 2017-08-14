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
        # check if it is a directory if true put it into the stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)
        #if it is a file
        else:
            #get its contents
            with open(current_path) as file:
                file_contents = file.read()
            #get its last edited time
            current_last_edited_time = os.path.getmtime(current_path)
            #if we have seen it before
            if file_contents in files_seen_already:
                existing_last_edited_time, existing_path = files_seen_already[file_contents]
                if current_last_edited_time > existing_last_edited_time:
                    #currrent file is a duplicate
                    duplicate.append((current_path, existing_path))
                else:
                    #old file is dupe - delete it
                    duplicates.append((existing_path, current_path))
                    # update files_seen_already to have the new file's info
                    files_seen_already[file_contents] = (current_last_edited_time, current_path)
            else:
                #if its a new file - add it to files_seen_already and record path and last edited time.
                files_seen_already[file_contents] = (current_last_edited_time, current_path)

    return duplicates
