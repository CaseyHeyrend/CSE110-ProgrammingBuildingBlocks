
print("Welcome to the Shopping Cart Program!")

cart = []
prices = []
total = []
total_price = []
items = ''
while True:
    print()
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    option = int(input("Please enter an action: "))
    if option == 1:
        item = input("What item would you like to add? ")
        y = input("Press y to continue: ")# To confirm
        if item != "y":
            cart.append(item)
            print(f"'{item}' has been added to the cart.")

    if option == 2:
        print("The contents of the shopping cart are: ")
        for item in cart:
            print(item)
            y = input("Press y to continue: ")# To confirm
            if item != "y":
                break
    if option == 3:
        withdraw = int(input("Which item would you like to remove? "))
        cart.remove(withdraw)

    #if option == 4:

    if option == 5:
        print("Thank you, Goodbye!")
        break

        