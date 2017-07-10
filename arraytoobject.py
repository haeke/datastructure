"""
    convert an array of strings to an object
    write a function that will take in a string of user information and create and object
"""

def arraytoobject(string):
    #empty hashtable
    obj = {}

    #split the string at each person
    people = string.split(' ')
    #loop through all people
    for p in people:
        #split information for each person
        info = p.split(',')

        #store this information into the user object / hashtable
        userobject = {
            'email': info[1] or None,
            'age': int(info[2]) if info[2] else None,
            'occupation': info[3] or None
        }

        #store key-value in object of users
        obj[info[0]] = userobject
    return obj

#example information
s = "Edwin,fff@fff.com,56,Coder Murphy,email@email.com,55,Teacher"
#create the object from the string
people = arraytoobject(s)

print people
#test that hashtable works
print people['Edwin']['age']
