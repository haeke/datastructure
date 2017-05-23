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
