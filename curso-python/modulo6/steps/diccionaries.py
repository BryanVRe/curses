numbers = {'one':1, 'two':2, 'three':3}

print(numbers['one'])

numbers['eleven'] = 11
print(numbers)

#dictionary
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial

for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
' '.join(sorted(planet_to_initial.values()))

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))