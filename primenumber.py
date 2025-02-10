# a program to check whether a number is prime or not
num = int(input("Enter a number: "))
for i in range(2,num):
    if num%i==0:
        print("the number is not a prime number")
        break
else:
    print("the number is a prime number")