hidden = "frost"
guess = "null"
count = 0
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
            hint += "_ "
    print(f"Your hint is: {hint}")