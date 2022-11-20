
print("Welcome to the Shopping Cart Program!")
item = None
cart = []
prices = []
total = []
while cart != "5":
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    option = int(input("Please enter an action: "))
    if cart != "5":
        if option == 1:
            item = input("What item would you like to add? ")
            price = float(input(f"What is the price of {item}? "))
            print(f"'{item}' has been added to the cart.")
            cart.append(item)
            prices.append(price)
            
        if option == 2:
            print("\nThe contents of the shopping cart are: ")
            for i in range(len(cart)):
                print(f"{cart[i]} - {prices[i]}")
        if option == 3:
            remove = "yes"
            remove = input("\nDo you want to update cart? ")
            if remove == "yes":
                index = int(input("Which item would you like to remove? "))
                withdraw = int(input())
                prices[index] = withdraw
                cart.remove(withdraw)
            #withdraw = int(input("Which item would you like to remove? "))

        if option == 4:
            total = 0
            for i in range(len(cart)):
                total += prices[i]
            print(f"Total: ${total:.2f}")

        if option == 5:
            print("Thank you, Goodbye!")
            break

        