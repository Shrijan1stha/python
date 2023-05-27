# Recursion occurs when a function definition has the same function call.


c = 0
def message():
    global c
    c += 1
    if c == 10:
        return
    print("Hello World")
    message()


message()
