# a program for a simple calculator

first_value= int(input("Enter the first number: "))
operator = input("Enter the operator: ")
second_value = int(input("Enter the second number: "))

if operator == "+":
    result = first_value + second_value
    print(result)

elif operator == "-":
    result = first_value - second_value
    print(result)

elif operator == "*":
    result = first_value * second_value
    print(result)

elif operator == "/":
    result = first_value / second_value
    print(result)
    
else:
    print("Invalid operator")


