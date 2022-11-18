print("Enter the names and balances of bank accounts (type: quit when done) ")

names = []
balances = []
name = None

while name != "quit":
    name = input("What is the name of this account? ")
    if name != "quit":
        balance = float(input("What is the balance? "))
        names.append(name)
        balances.append(balance)

total = 0
print("\nAccount Information: ")
for i in range(len(names)):
    print(f"{names[i]} - ${balances[i]}")
    total += balances[i]
average = total / len(balances)

print()
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")