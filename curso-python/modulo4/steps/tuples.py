t = (1, 2, 3)

t = 1, 2, 3 # equivalent to above
print(t)

#They cannot be modified (they are immutable).
#t[0] = 100

x = 0.125
print(x.as_integer_ratio())

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

a = 1
b = 0
a, b = b, a
print(a, b)