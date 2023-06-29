# Write python script to calculate sum of digits of a given input number.

num = int(input("enter a number :"))
sum1=0
while(num>0):
    digit = num%10
    sum1 = sum1+digit
    num //=10
print("The sum is :",sum1)