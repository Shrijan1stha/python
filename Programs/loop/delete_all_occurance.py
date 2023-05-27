# WAP to delete all the occurances of a specified character in a given string.
# S = "All the occurances of a specified character in a given string"
# Input = "a"
#Output = "ll the occurance of a specified chrcter in a given string"


s = "All the occurance of a specified character in a given string"
new_s = ""
char = input("Enter the character to be deleted:")

for i in s:
    if i.lower() == char.lower():
        continue
    new_s = new_s + i
print(new_s)

