# Write a python script to accepts annual basic salary of an employee and calculates and displays the
# Income tax as per the following rules.
# Basic: < 2,50,000 Tax = 0
# Basic: 2,50,000 to 5,00,000 Tax = 10%
# Basic: > 5,00,000 Tax = 20

salary = float(input("Enter Your salary :"))

if salary < 250000:
    print("Tax = 0")
elif salary > 250000 and salary <= 500000 :
    print("Tax = ",(salary*10/100))
else:
    print("Tax = ",(salary*20/100))