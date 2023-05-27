# For the given input, print the as it is as otherwise, "Fizz" if the number is multiple ko 3,
# "Buzz" if the number is multiple of 5 and "FizzBuzz" if the number is multiple of both 3 and 5


n = int(input("Enter the number"))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif (n % 3) == 0:
    print("Fizz")
elif (n % 5) ==0:
    print("Buzz")
else:
    print(n)