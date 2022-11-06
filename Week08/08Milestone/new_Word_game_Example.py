hidden = "frost"
guesses = ''

print("Welcome to the Word Game!")
print("Hint: _ _ _ _ _ ")
print()

while guesses != hidden:
    guesses = input("What is your guess? ")
    hint = " "
    for l, letter in enumerate(hidden):
        if l < len(guesses) and letter.lower() == (guesses)[1]:
            hint += letter.upper()
        elif letter.lower() in guesses:
            hint += letter.lower()
        else:
            hint += "_ "
print(f"Your word is: {hint}")
 
#
#turns = 8


#while turns > 0:#counts the number of times a user fails
   #guess = str(input("Guess the word: "))
    #if guess == hidden:
        #print("You guessed the word correctly!")
        
       #break
    #else:
        #turns = turns - 1
        #print(f"You have {turns} attempt(s),\n ")
        #for char, word in zip(hidden, guess):
            #if word in hidden and word in char:
                #print(word + " ")
            #elif word in hidden:
                #print(word + "_")
            #else:
                #print("_")
                #print(word, end= "_")
        #if turns == 0:
            #print ("Game over!")
