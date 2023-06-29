# Write python script to accept the x and y coordinate of a point and find the quadrant in which the
# point lies


x = int(input("Enter value of X :"))
y = int(input("Enter value of Y :"))

if (x>0 and y>0):
    print("(",x,",",y,")"," Belongs to FIRST quadrant")
elif (x<0 and y>0):
    print("(",x,",",y,")"," Belongs to SECOND quadrant")
elif (x<0 and y<0):
     print("(",x,",",y,")"," Belongs to THIRD quadrant")
else:
    print("(",x,",",y,")"," Belongs to FOURTH quadrant")