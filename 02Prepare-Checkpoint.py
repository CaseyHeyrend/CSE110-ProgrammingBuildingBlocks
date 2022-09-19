#Taking input from the user
class Format:
    end = '\033[0m'
    underline = '\033[4m'
first = input("What is your first name? ")
last = input("What is your last name? ")
#Output
print(f"Your name is {last}, {first} {last}.")

