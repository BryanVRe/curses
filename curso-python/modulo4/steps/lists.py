primes = [2, 3, 5, 7]
print(primes)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

print(hands)

my_favourite_things = [32, 'raindrops on roses', help]


#INDEXINg

print(planets[0])

print(planets[1])

print(planets[-1])

print(planets[-2])

#Slicing

print(planets[0:3])
print(planets[0:3])

print(planets[3:])

# All the planets except the first and last
print(planets[1:-1])

# The last 3 planets
planets[-3:]

#CHARGING

planets[3] = 'Malacandra'
print(planets)

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

#FUNCTIONS in a list

print(len(planets))

print(sorted(planets))

primes = [2, 3, 5, 7]
print(sum(primes))

print(max(primes)) #we can also use it with MIN

#List Methods

# Pluto is a planet darn it!
planets.append('Pluto')

print(planets)

print(planets.pop())

#SEARCHHHH

print
#(planets.index('Earth'))

# Is Earth a planet?
print("Earth" in planets)