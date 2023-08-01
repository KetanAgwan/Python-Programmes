# Write a program to calculate X^y 

x = int(input("enter value of x :"))
y = int(input("enter value of y :"))
sum1 = 1

# print("answer :",x**y)

while(y>0):
    sum1 *= x
    y-=1

print("The answer is :",sum1)