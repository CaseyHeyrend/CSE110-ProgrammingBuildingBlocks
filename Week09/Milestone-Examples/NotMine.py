prices = []
acttons = []

new_product = ''
new_price = ''
action = ''

product = new_product
products.append(product)
prices.append(new_price)

while product != 'quit' and action != '5':
    print()
    print(f"Please select one of the following: ")
    print(f"1. Add item")
    print(f"2. View cart")
    print(f"3. Remove item")
    print(f"4. Compute total")
    print(f"5. Quit")
    action = input(f'Please enter an action: ')

    if action == '1':
        new_product = input(f"What item would you like to add? ")
        print(f"'{product}' has been added to the cart.")
        print()
    elif action == '2':
        products.append(product)
        for product in products:
            print(f"The contents of the shopping cart are: ")