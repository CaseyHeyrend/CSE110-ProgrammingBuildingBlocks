#Taking input from the user

child = float(input("What is the price of a child's meal? "))
adult = float(input("What is the price of a adult's meal? "))
numChild = int(input("How many children are there? "))
numAdult = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate? "))
print()
#calculate numbers
childTotal = child * numChild
adultTotal = adult * numAdult
subTotal = adultTotal + childTotal
sales = subTotal * tax/100
Total = subTotal + sales
print()
print(f"Subtotal: ${subTotal:.2f}")
print(f"Sales Tax: ${sales}")
print(f"Total: ${Total}")

print()
pay = float(input("What is the payment amount? "))
change = float (pay - Total)
limited_float = round(change, 2)
print(f"Change: ${limited_float}")
