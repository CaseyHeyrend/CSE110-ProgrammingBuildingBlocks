import random

keep_playing = "yes"#Stretch challenge

while keep_playing == "yes":#Stretch challenge
    magic_number = random.randint(1, 100)

guess_count = 0#Stretch challenge
guess = -1

while guess != magic_number:
    guess = int(input("What is your guess? "))
    guess_count = guess_count + 1#Stretch challenge

    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    else:
        print("You guessed it")

    print(f"It took you {guess_count} guesses")#Stretch challenge
    
    keep_playing = input("Would you like to play again (yes/no)? ")#Stretch challenge

print("Thank you for playing.")#Stretch challenge