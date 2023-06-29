# Write a python script to accept the cost price and selling price from the keyboard. Find out if the
# seller has made a profit or loss and display how much profit or loss has been made.


cost = int(input("Enter cost price :"))
sell = int(input("Enter selling price :"))

if (cost < sell):
    print("Profit is made up of :",sell-cost)
elif(sell<cost):
    print("Loss is made up of :",cost-sell)
else:
    print("No Profit and no loss")