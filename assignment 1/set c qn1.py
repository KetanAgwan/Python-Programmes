# Write a python script to generate the following pattern upto n lines
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1

n = int(input("Enter limit "))
for i in range(1,n+1):
    for space in range(1, n-i+1):
        print(end="  ")

    a = 1
    for j in range(0,i+i-1):
        if(j<i):
            print(a,end=" ")
            a=a+1
        else:
            a=a-1
            print(a-1,end=" ")
    print()
