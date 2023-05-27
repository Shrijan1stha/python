"""
Check whether a number is palindrome or not
a = 121
Output = "It is palindrome number"
A = 321
Output = "It is not a palindrome number"
"""
# Treating n as string

# n = input("Enter the number:")
# reverse = n[::-1]
# print("Palindrome") if n == reverse else print("Not Palindrome")


# Treating n as integer

n = int(input("Enter a number:"))
b = n
reverse = 0
while n != 0:
   remainder = n % 10
   reverse = reverse * 10 + remainder
   print(reverse)
   n = n // 10
print("Palindrome") if reverse == b else print("Not Palindrome")
