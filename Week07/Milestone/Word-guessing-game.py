#Word Guessing Game

import random

print("Welocme to the word guessing game!")

words = ['autumn', 'halloween', 'pumpkin', 'magic', 'fall', 'witch', 
        'football', 'turkey', 'jack', 'spirit', 'frost', 'winter']#12 words

#Function will choose one random
#word from this list of words
random_word = random.choice(words)
print("our random word", random_word)

print("Guess the characters")
guesses = ''
# any number of turns can be used here
turns = 25

while turns > 0:#counts the number of times a user fails 
    failed = 0

    for character in random_word:
        if character in guesses:
            print(character, end= " ")

        else:
            print("_")
            print(character, end= " ")
            failed += 1
            
    if failed == 0:
        print()
        print("You have won!")
        print("The word is: ",random_word)
        break

    print()

    guess = input("guess a letter: ")
    guesses += guess

    if guess not in random_word:
        turns -= 1

        print("Wrong answer")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You have lose")