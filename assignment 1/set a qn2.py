# Write python script to check whether a input number is Armstrong number or not.

num = int(input("Enter the number :"))
temp = num
sum1 = 0

while(num>0):
    digit = num%10
    sum1 += digit**3
    num //=10

if sum1==temp:
    print("This is an armstrong number")
else:
    print("this is not an armstrong number") 