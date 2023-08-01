# Write a program to accept a binary number and convert it into decimal number.

binary = int(input("enter binery number"))
sum1 = 0
i = 0

while (binary > 0):
    digit = binary % 10
    if(digit == 1):
        sum1+= 2**i
    binary //= 10
    i += 1

print("The decimal number is :",sum1)
