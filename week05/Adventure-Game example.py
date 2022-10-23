print("Welcome to the Adventure Game!")
print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?")


c1 = input()

if (c1.upper()=="MATCH"):
    print("\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ")

elif (c1.upper()=="FLASHLIGHT"):
    print("\nYou pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
else:
    print("Please pick one. MATCH or FLASHLIGHT?")
    c1 = input()

c1_1 = input()
if (c1_1.upper()=="RUN"):
    print("\n You run and the large grizzly bear hears you are catch you. You have make your doom. You have died. This is the end")
elif (c1_1.upper()=="HIDE"):
    print("\n Lucky you hide in time and the large grizzly bear doesn't notice you and the bear leaves the another direction. Do you ")
else:
    print("Please pick one. RUN or HIDE?")
    c1_1 = input()

c1_2 = input()
if (c1_2.upper()=="FOLLOW"):
    print("\n")
elif (c1_2.upper()=="LOOK"):
    print("\n")
else:
    print("Please pick one. FOLLOW or LOOK?")
    c1_2 = input()



