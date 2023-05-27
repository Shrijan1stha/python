from functools import reduce

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result

print(factorial(5))


# 5 factorial using reduce function
result = reduce(lambda x, y: x * y, range(1, 6))
print(result)


### Using recursion

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

# 5 * factorial(4)  5 * 24 = 120
# 3 * factorial(3)  4 * 6 = 24
# 3 * factorial(2)  3 * 2 = 6
# 2 * factorial(1)  2 * 1 = 2
# 1 * factorial(0)  1 * 1 = 1


n = int(input("Enter the number: "))
print(factorial(n))