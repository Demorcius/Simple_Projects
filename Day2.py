
print("Welcome to the tip calculator")
bill= float(input("what was the total bill? $"))
tip= int(input("What percentage of the bill would you like to give as tip?"))
b= int(input("How many people are there"))
e= float(tip/100)
h= 1+e

total_bill = bill * h

split = total_bill/ b

splitt= round(split, 2)
print (f"Each person should pay{splitt}")
