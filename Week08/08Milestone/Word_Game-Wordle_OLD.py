hidden = "frost"

print("Welcome to the Word Game!")
print("Hint: _ _ _ _ _ ")
print()
guess = ''
turns = 8

while turns > 0:#counts the number of times a user fails
    guess = input("\nWhat is your guess?\n ").lower() 
    if guess == hidden:
        print("You guessed the word correctly!")
        
        break
    else:
        turns = turns - 1
        print(f"You have {turns} attempt(s),\n ")
        for char, word in zip(hidden, guess):
            if word in hidden and word in char:
                print(word + " ")
            elif word in hidden:
                print(word + "_")
            else:
                print("_")
                print(word, end= "_")
        if turns == 0:
            print ("Game over!")
