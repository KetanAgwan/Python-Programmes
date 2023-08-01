# Write a program which accept an integer value ‘n’ and display all prime numbers till ‘n’.

n = int(input("enter limit"))

for i in range(3,n+1):
    f=0
    for j in range(2,i):
        if i % j == 0 :
            f = 1;
    if f != 1:
        print(i)
        print()
