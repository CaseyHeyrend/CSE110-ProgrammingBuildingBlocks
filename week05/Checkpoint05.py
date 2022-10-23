firstnum = int(input("What is the first number? "))
secondnum = int(input("What is the second number? "))

if firstnum > secondnum:
    print("The first number is greater.")
else:
    print("The first number is not greater.")

if firstnum == secondnum:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

if secondnum > firstnum:
    print("The second number is greater.")
else:
    print("The second number is not greater.")

print()
animal = input("What is youe favorite animal? ")
if animal.lower() == "tiger":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")