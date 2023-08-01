# Write python script to check whether a input number is perfect number of not

num = int(input("Enter number :"))
sum1=0

for i in range(1,num):
    if num % i == 0:
        sum1+=i

if sum1 == num :
    print("it is an perfect number")
else:
    print("it is not an perfect number")