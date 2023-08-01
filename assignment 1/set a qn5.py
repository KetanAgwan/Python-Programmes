# Write a program to check whether a input number is palindrome or not.

num = int(input("Enter a number :"))
temp = num
sum1=0

while(num>0):
    digit = num%10
    sum1 = sum1 * 10 + digit
    num //= 10

if sum1 == temp:
    print("the number is pelindrome")
else:
    print("the number is not pelindrome")