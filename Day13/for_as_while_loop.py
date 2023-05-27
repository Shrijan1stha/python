a = [1, 2, 3, 4, 5, 6, 7]
iter_a = iter(a)
while True:
    try:
        value = next(iter_a)
        print(value)
    except StopIteration:
        break

# The aboe code is same as using for loop as below
for i in a:
    print(i)
