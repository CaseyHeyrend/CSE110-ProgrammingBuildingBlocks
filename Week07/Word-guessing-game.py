#Word Guessing Game

import random

print("Welocme to the word guessing game!")

name = input("What is your name? ")
print("Good luck!", name)

words = ['autumn', 'halloween', 'pumpkin', 'magic', 'fall', 'witch', 
        'football', 'turkey', 'october', 'spirit', 'snow', 'winter']#12 words

#Function will choose one random
#word from this list of words
word = random.choice(words)

print("Guess the characters")
guesses = ''
# any number of turns can be used here
turns = 25

while turns > 0:
    #counts the number of times a user fails
    failed = 0

    for char in word:
            if char in guesses:
                print(char, end=" ")

            else:
                print("_")
                print(char, end=" ")
                failed += 1
            
    if failed == 0:
        print()
        print("You have won!")
        print("The word is: ",word)
        break

    print()

    guess = input("guess a letter: ")
    guesses += guess

    if guess not in word:
        turns -= 1

        print("Wrong answer")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You have lose")