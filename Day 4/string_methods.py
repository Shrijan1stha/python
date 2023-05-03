m = "hello world"
print(m.capitalize())  # Result => Hello world
print(m.title())  # Result => Hello World
print(m.upper())  # Result => HELLO WORLD
print(m.lower())  # Result => hello world

result = m.split()  # Result => ["hello", "world"]. Splits from space
print(result)

result = m.split('e')  # Splits from 'e'. Result ["h", "llo world"]
print(result)

result = m.split('o')  # Splits from 'o'. Result ["hell", " w", "rld"].
print(result)


message = ["Hello", "World"]
" ".join(message)  # This joins the list with a space (" ") and returns "Hello World"
"+".join(message)  # Result 'Hello+World'


m = "Hello World"
result = m.find("Wo")  # 'Wo' in the string is at 6th position. Result => 6
print(result)

result = m.find("Wooo")  # 'Wooo' is not present in the list. Result => -1
print(result)


m.replace("World", 'world')  # Replace 'World' in the string to 'world'.
print(result)  # Result => "Hello world"