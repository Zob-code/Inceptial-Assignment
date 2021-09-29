# create mapping objects of state of abbreviations

states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'India' : 'IND',
    'New York' : 'NY'
}

# create a basic set of states and some cities in them

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'MUM' : 'Mumbai'
}

# add more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some of the cities
print('-' *10)
print("NY state has:", cities['NY'])
print("OR state has:", cities['OR'])

# print out some states
print("-"*10)
print("Florida's Abbreviation is : ", states['Florida'])
print("India's Abbreviation is : ", states['India'])

# do it by using the state then cities dict
print("-"*10)
print("Florida's Abbreviation is : ", cities[states['Florida']])
print("India's Abbreviation is : ", cities[states['India']])

# print every state abbreviation
print("-"*10)
for state, abbrev in list(states.items):
    print(f"{state} is abbrreviated {abbrev}.")

# print every cities abbreviation
print("-"*10)
for abbrev, cities in list(cities.items):
    print(f"{abbrev} is abbrreviated {cities}.")

# now do both at the same time
print("-"*10)
for state, abbrev in list (states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-"*10)
state = states.get('Texas')

if not state:
    print("Sorry no Texas")

# get a city with a deafult value
city = cities.get('TX','does not exist')
print(f"The city for the state 'TX' is {city}")
