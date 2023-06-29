# Write a program to calculate sum of first and last digit of a number

num = int(input("enter a number"))

last = num % 10
num //= 10
while (num > 0):
    first = num % 10
    num //= 10

print("The sum of first and last digit is :",first+last)