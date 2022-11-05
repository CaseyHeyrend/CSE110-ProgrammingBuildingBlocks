secret_word = "frost"

print("Welocme to the word guessing game!")
print()
secret_word = "frost"

guesses = ''
turns = 8

while turns > 0:#counts the number of times a user fails
    guess = str(input("Guess the word: "))
    if guess == secret_word:
        print("You guessed the word correctly!")
        
        break
    else:
        turns = turns - 1
        print(f"You have {turns} attempt(s),\n ")
        for char, word in zip(secret_word, guess):
            if word in secret_word and word in char:
                print(word + " ")
            elif word in secret_word:
                print(word + "_")
            else:
                print("_")
                print(word, end= "_")
        if turns == 0:
            print ("Game over!")
