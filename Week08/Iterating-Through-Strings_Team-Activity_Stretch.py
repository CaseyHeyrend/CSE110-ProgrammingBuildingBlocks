quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

run_again = "yes"
while run_again == "yes":
    user_number = int(input("Please enter a number: "))

    for n, letter in enumerate(quote):
        if n % user_number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    
    print()

    run_again = input("Would you like to enter another number? ")
print()

print("Goodbye!")