print("Welcome to the Shopping Cart Program!")
cart = [] #Holds the cart items
prices = []#Holds the price of each items
total = []
total_price = []

while True:
    print()
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    select = int(input("Please enter an action: "))
    item = ""
    if select == 1:
            item = input("What item would you like to add? ")
            price = float(input(f"What is the price of {item}? "))
            print(f"'{item}' has been added to the cart.")
    if select == 2:
        print("The contents of the shopping cart are: ")
        for item in cart:
            print(item,price)
    if select == 3:
        remove = input("Which item would you like to remove? ")
        cart.remove(remove)
    if select == 4:
        for price in total_price:
            sum += price
            print(sum(total_price))
    if select == 5:
        print("Thank you, Goodbye!")





