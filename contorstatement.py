# A Python program that checks for room temperature

temperature = 26
if temperature > 25:
    print("It is too hot")
else :
    print("It is too cold")


# A program that returns the largest number
first = 98
second = 33
third = 56

if first > second and first > third:
    print(first,"is the largest number")
elif second > first and second > third:
    print(second,"is the largest number")
else:
    print(third,"is the largest number")

# Program to check a number and return whether the number is even or odd
number = 10
if number == 0:
    print(number, "is neutral")
elif number % 2 == 0:
    print(number,"is even")
else:
    print(number,"is odd")
