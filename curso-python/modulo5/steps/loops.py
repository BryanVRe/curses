planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line


#numbers

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)


#STRINGS
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='') 

#El de toda la vida
for i in range(5):
    print("Doing important work. i =", i)

#----

squares = [n**2 for n in range(10)]
print(squares)

#without comprehesion

squares = []
for n in range(10):
    squares.append(n**2)
print(squares)

#if
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)

#---- count negatives

def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

#with comprehesion

def count_negatives(nums):
    return len([num for num in nums if num < 0])

#more easy

def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])