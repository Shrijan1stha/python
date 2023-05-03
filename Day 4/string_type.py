# String in Python are of immutable type.
# We can create an empty string using str() built-in function using empty single or double quotes.

example = ""  # Empty string using double quotes
print(example)

example = ''  # Empty string using single quotes
print(example)

example = str()  # Empty string
print(example)

example = "Hello World"  # Its a valid string.
# example = 'Hello World"  # Invalid String.
# example = "Hello World'  # Invalid String.


# Escape Sequences
# Escape Sequences / Characters are the strings in python which supresses the usual meaning of a character
# and gives a new meaning.

example = 'I\'m learning python'  # Here \' is an escape character.
print(example)

example = "Path to my file is E:\\Python"  # Here \\ is an escape character.
print(example)

example = "Hello\nWorld"  # Here \n is a new-line escape character.
print(example)

example = "Hello\tWorld"  # Here \t is an escape character for a tab.
print(example)

example = "Hello\bWorld"  # Here \b is an escape character for a backspace.


# Triple quotes strings
example = '''
Example1
'''
print(example)  # Example with triple single quotes

example = """
Example2
Example
"""
print(example)  # Example with triple double quotes

example = """
I'm learning python
"""
print(example)  # We don't need to use escape characters for songle/double quote in triple quoted string.

"""
Function to calculate difference. We can treat this as a multiline commment
"""
def diff(a, b):
    return a - b


# Indexing and Slicing in string
# String indexing and slicing is similar to list slicing and indexing.

message = "Hello World"
print(message[3])  # This gives 'l'
print(message[6])  # This gives 'w'. Space is also condisered as a character
print(message[-2])  # Negative indexing is also possible. It gives 't'.


print(message[1: 7])  # Result => 'ello W'.
print(message[1: 7: 2])  # Result => 'el '.
print(message[1: -3])  # Result => 'ello Wo'.
print(message[-7: -3])  # Result => 'o  Wo'.
print(message[-3: -7])  # Result => ''


# String doesn't support item assignment because it is immutable.
message = "Hello"
# message[1] = "E"  # This is not possible
