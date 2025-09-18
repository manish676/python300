from functools import  reduce
# [ Expression for item in iterable of condition]

# Create a list of suares

seuares = [x**2 for x in range(10)]
# print(seuares)

# Filter Even Numbers
even = [x for x in range(100) if x % 2 != 0]
# print(even)

# lambda Arguments: expression

addd = lambda x, y: x + y
# print(addd(3,5))


# map() = Applies a functions to each item in an iterable
numbers = [1,2,3,4,5]
# sequares = map(lambda x: x**2, numbers)
# print(list(sequares))


# filter() = Filters items based on a condition
envenList = filter(lambda x: x % 2 == 0, numbers)
print(list(envenList))

# reduce() = Reduces an iterable to a single value
product = reduce(lambda x,y: x * y, numbers)
print(product)