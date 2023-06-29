# Write a program to accept a number and count number of even, odd, zero digits within that number.

num = int(input("enter a number"))
even=0
odd=0
zero=0
while(num>0):
    digit = num % 10
    if(digit!=0 and digit%2==0):
        even+=1
    elif(digit!=0 and digit%2!=0):
        odd+=1;
    else:
        zero+=1
    num //=10

print("number of even number=",even)
print("number of odd number=",odd)
print("number of zero =",zero)
