print("Enter the names and balances of bank accounts (type: quit when done) ")

names = []
balances = []
name = None
# Bulid the lists
while name != "quit":
    name = input("What is the name of this account? ")
    if name != "quit":
        balance = float(input("What is the balance? "))
        names.append(name)
        balances.append(balance)

#Display the accounts and the total
total = 0
print("\nAccount Information: ")
for i in range(len(names)):
    print(f"{names[i]} - ${balances[i]}")
    total += balances[i]
average = total / len(balances)

print()
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")

# Stretch Challenges:
# Highest balance
highest_name = None
highest_balance = -1

for i in range(len(names)):
    name = names[i]
    balance = balances[i]

    if balance > highest_balance:
        highest_balance = balance
        highest_name = name
print(f"Highest balance: {highest_name} - ${highest_balance:.2f}")

switch_account = "yes"
while switch_account == "yes":
    switch_account = input("\nDo you want to update an account? ")
    if switch_account == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))
        balances[index] = new_amount

        print("\nAccount Information: ")
        for i in range(len(names)):
            print(f"{i}. {names[i]} - ${balances[i]:.2f}")