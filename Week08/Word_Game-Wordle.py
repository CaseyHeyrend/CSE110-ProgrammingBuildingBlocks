hidden = "frost"

guess = " "

count = 0
turns = 8
print("Welcome to the Word Game!")
print("Hint: _ _ _ _ _ ")
while guess != hidden:
    guess = input("\nWhat is your guess?\n ").lower()   
    hint = ''
    for f, letter in enumerate(hidden):
        if f < len(guess) and letter.lower() == (guess)[f]:
            hint += letter.upper()
        elif letter.lower() in guess:
            hint += letter.lower()
        else:
            turns = turns - 1
            print(f"You have {turns} attempt(s),\n ")
            hint += "_ "
            if turns == 0:
                print("Game Over!")
    print(f"Your hint is: {hint}")
    print(f"You took {turns} attempt(s).\n")
