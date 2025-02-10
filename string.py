# string is a collection of characters
from variables import firstname

text = "Hello World"
course = "MIT"

print(text)
print(course)

# accessing an element in a string
print(text[1])

# Size of a string
print(len(text))
print(len(course))

# Modifying a string
print(text.upper())
print(course.lower())
space = " "

# string concatenation
firstname = "John"
lastname = "Doe"
print("Hello " , firstname + space + lastname)

print(text + " " + course)

