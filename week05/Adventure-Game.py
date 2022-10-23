from tkinter import END


print("Welcome to the Adventure Game!")
print("You are walking through a dark forest. You already had a flashlight. So no worries. But you come to a fork in the forest. Which way do you go, RIGHT or LEFT?")

#Right
direction = input()
if (direction.upper()=="RIGHT"):
    print("\nYou decide to go right. So you start to walk for a bit and come across a calm river. But something is running behind the area that was behind you. Do you CROSS the river or STAY and find out what is coming?")
    
    direction = input()
    if (direction.upper()=="CROSS"):
        print("\nYou manger to cross the river and get away from the thing coming towards you. You start to walk more. You see a group of people that you are friends with, but the path continues. Do you go to the GROUP or continue on the PATH?")
        
        direction = input()
        if (direction.upper()=="GROUP"):
            print("\n")
            direction = input()
        elif (direction.upper()=="PATH"):
            print("\n")
        else:
            print("")

    elif (direction.upper()=="STAY"):
            print("\nYou decide to stay and what was running towards you. But, unfortunately, the campsite killer was in the forest, and they found you. So, unfortunately, you have been caught, and this is the end.")
    else:
        print("Please pick one. CROSS or STAY?") 
#Left
elif (direction.upper()=="LEFT"):
    print("\nYou decide to go left. So you walk for a bit and come across an abandoned cabin. You can see that the cabin is old but still usable. Do you EXPLORE the cabin or KEEP walking on the path?")
    
    direction = input()
    if (direction.upper()=="EXPLORE"):
        print("\nYou decide to explore the cabin. So you walk into the cabin, and when you step on something on the floor. Something is different from the floor. You then realize that it is a trapdoor. Do you GO in the trapdoor or RESUME to explore?")
        direction = input()
        if (direction.upper()=="GO"):
            print("\n")
            direction = input()
        elif (direction.upper()=="RESUME"):
            print("\n")
            
        else:
            print("Please pick one. GO or RESUME?")

    elif (direction.upper()=="KEEP"):
        print("\nYou decide to keep going on the path and find the abandoned fresh campsite. Then, you decide to call the rangers. But instead, rangers come and call the police. So this choice for the game is one of the endings.")
    else:
        print("Please pick one. EXPLORE or KEEP?")
        direction = input()

else:
    print("Please pick one. RIGHT or LEFT?")



