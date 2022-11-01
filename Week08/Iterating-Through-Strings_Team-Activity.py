from operator import le


word = "commitment"

liked_letter = input("What is your liked letter? ")
#Core 1 & 2
for letter in word:
    if letter.lower() == liked_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

#Core 3
for letter in word:
    if letter.lower() == liked_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()
