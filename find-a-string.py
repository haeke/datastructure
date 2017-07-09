
#

def count_substring(string, sub_string):
    #make sure string isn't smaller than one but not greater than 200
    total = 0
    #make sure it is in lower case
    string = string.lower()
    if( 1 <= len(string) <= 200):
        for i in range(0, len(string) - len(sub_string) + 1):
            if string[i:i+len(sub_string)] == sub_string:
                total += 1

        return total
    else:
        return None


print count_substring("Edwined", "ed")
