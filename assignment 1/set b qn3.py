# Write a program which accepts an integer value as command line and print “Ok” if value is between 1 to
# 50 (both inclusive) otherwise it prints ”Out of range”

num = int(input("enter number"))

if num>0 and num<51:
    print("OK")
else:
    print("out of range")