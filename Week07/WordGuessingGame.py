#Word Guessing Game
import random

print("Welocme to the word guessing game!")

secret_word = "Halloween"
user_guess = input("Please guess the secret word: ")

while user_guess != secret_word:
    user_guess = input("Please guess the secret word again: ")
else:
    print("Correct")