x = 'Pluto is a planet'
y = "Pluto is a planet"
print(x == y)

print("Pluto's a planet!")
print('My dog is named "Pluto"')

hello = "hello\nworld"
print(hello)


triplequoted_hello = """hello
world"""
print(triplequoted_hello)
triplequoted_hello == hello

print("hello")
print("world")
print("hello", end='')
print("pluto", end='')

# Indexing
planet = 'Pluto'
planet[0]

# Slicing
planet[-3:]

# How long is this string?
len(planet)

[char+'! ' for char in planet]

#FUNCTIONSSSS

# ALL CAPS
claim = "Pluto is a planet!"
claim.upper()

# all lowercase
claim.lower()

# Searching for the first index of a substring
claim.index('plan')

claim.startswith(planet)

# false because of missing exclamation mark
claim.endswith('planet')

#Lists and Strings

words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')

planet + ', we miss you.'

#change a number to a string

planet + ", you'll always be the " + str(position) + "th planet to me."

"{}, you'll always be the {}th planet to me.".format(planet, position)

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)