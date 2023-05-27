# Criteria to be a closure
# 1. There should be a nested function.
# 2. Inner function must refer parameter from outer function.
# 3. Outer function must return the inner function.


def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func


result = outer_func("Hello World")
print(result())


