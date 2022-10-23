#Taking input from the user

child = float(input("What is the price of a child's meal? "))
adult = float(input("What is the price of a adult's meal? "))
numChild = int(input("How many children are there? "))
numAdult = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate? "))
tip = float(input("What percentage of the tip you want to give? "))
print()
#calculate numbers
childTotal = child * numChild
adultTotal = adult * numAdult
subTotal = adultTotal + childTotal
sales = subTotal * tax/100
Total = subTotal + sales 
add_tip = (Total + (0.01 * tip) * Total)
print()
print(f"Subtotal: ${subTotal:.2f}")
print(f"Sales Tax: ${sales:.2f}")
print(f"Total: ${Total:.2f}")
print(f"Adding Tip to Total: ${add_tip:.2f}")

print()
pay = float(input("What is the payment amount? "))
change = float (pay - add_tip)
print(f"Change: ${change:.2f}")
