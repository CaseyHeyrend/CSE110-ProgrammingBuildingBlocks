#Taking input from the user
class Format:
    end = '\033[0m'
    underline = '\033[4m'
color = input("Please type your preference color: ")
hoilday = input("Please enter your favorite Hoilday: ")
Vidgames = input("Please type your favorite video game that you like to play: ")
#Output
print("Your preference color is " + Format.underline + color + Format.end)
print (type(color))
print("Your favorite Hoilday is " + Format.underline + hoilday + Format.end)
print (type(hoilday))
print("Your favorite video game that you like to play is " + Format.underline + Vidgames + Format.end)
print (type(Vidgames))