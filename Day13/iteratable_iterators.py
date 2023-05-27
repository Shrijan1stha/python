# Iterators are those objects which can be iterated / looped through.
# Iterable are those objects which can be converted to iterators.

# list, tuples, dictionary , set are the examples of iterables

a = [1, 2, 3]
iter_a = a.__iter__()
iter_a = iter(a)
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))