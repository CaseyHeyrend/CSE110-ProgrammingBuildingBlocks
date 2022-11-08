
print("Welcome to the Shopping Cart Program!")

cart = []
i_prices = []
total = []
total_price = []
item = ""
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
        price = float(input(f"What is the price of {item}? "))
        print(f"'{item}' has been added to the cart.")
    if option == 2:
        print("The contents of the shopping cart are: ")
        for item in cart:
            print(item,price) 
    if option == 3:
        remove = int(input("Which item would you like to remove? "))
    if option == 4:
        for price in total_price:
            sum += price
            print(sum(total_price))
    if option == 5:
        print("Thank you, Goodbye!")
        print("Enter esc to leave for now!")

        