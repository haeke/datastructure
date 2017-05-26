"""
print a dicitonary containing a list of some states in the USA in alphabetical order

"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['North America']['USA'].append('Arkansas')
locations['North America']['USA'].append('New Jersey')
locations['North America']['USA'].append('New York')

locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

usa_sorted = sorted(locations['North America']['USA'])
print('List of States in USA')
for state in usa_sorted:
    print state

asia_cities = []

print('Asian cities: ')
for countries, cities in locations['Asia'].iteritems():
    city_country = cities[0] + " - " + countries
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print city

"""
    Example of printing a list with indicies in two different ways
    first - create a counter and print the counter and list
    second - use the enumerate to print indicies and list
"""

cities = ['Chicago', 'New York City', 'Los Angeles', 'Sacramento']

# bad way -  create a counter then print the counter and list
i = 0
for city in cities:
    print(i, city)
    i += 1

# better way - using enumerate - we can list the indicies and content of the list
for i, city in enumerate(cities):
    print(i, city)

"""
    COMBINE TWO LISTS - using zip function
    print two lists as a pair - in this example print the two list of x and y coordinates
    first- get the length one of the lists, create a range then iterate through both lists
    second -
"""

x_list = [1,2,3]
y_list = [4,5,6]

#bad way
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x,y)

#better way - use the zip function to combine the lists
for x, y in zip(x_list, y_list):
    print(x,y)

"""
    swap values using the tuple function

"""
x = 10
y = 12
print('before: x = %d, y = %d' % (x,y))
#a bad way
tmp = y
y = x
x = tmp
print('After: x = %d, y = %d' % (x,y))
#a better way
x, y = y, x
print('altered: x = %d, y = %d' % (x,y))

"""
    default dictionary values using the get() function
"""

ages = {
    'Mary': 41,
    'Jonathon': 31,
}

#bad way
if 'Ed' in ages:
    age = ages['Ed']
else:
    age = 'Unknown'

print('Ed is %s years old' % age)

#better way using the get methods
age = ages.get('Ed', 'Unknown')
#first parameter if found second if not found
print('Ed is %s years old' % age)

"""
    for else in loops - search for a value in a list, return True or False

"""

needle = 'd'
haystack = ['a','b','c','e']

#loop through looking for the letter in the list
found = False
for letter in haystack:
    if needle == letter:
        print('Found')
        found = True
        break
    if not found:
        print('not found')

#use the else statement to avoid creating a boolean for found
for letter in haystack:
    if needle == letter:
        print('Found')
        break
else:
    print('not found')


"""
    read a file and output the contents

"""

#bad way - open the text file, print until you get to a return to next line
f = open('sometest.txt')
text = f.read()
for line in text.split('\n'):
    print(line)
f.close()


#better way - loops over the file object remove the read statement
f = open('sometest.txt')
for line in f:
    print(line)
f.close()

#best way? make use of context with 'with' statement  - this will take care of opening and closing the file
with open('sometest.txt') as f:
    print line in f:
        print(line)

"""
    using try and except
    finally - use finally for debugging - if there is an error the finally statement will still run before outputting the error message/program crash
"""

#change data type of a string to an integer
print('convert')
try:
    print(int('x'))
except:
    print('conversion failed')

# check if no exception occured with an else statement
print('convert this')
try:
    print(int('3'))
except:
    print('conversion failed')
else:
    print('conversion successful')
finally:
    print('Done with checking')
