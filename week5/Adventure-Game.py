print("Welcome to the Adventure Game!")
print("You are walking through a dark forest. You already had a flashlight. So no worries. But you come to a fork in the forest. Which way do you go, RIGHT or LEFT?")


direction = input()
#Right
if (direction.upper()=="RIGHT"):
    print("\nYou decide to go right. So you start to walk for a bit and come across a calm river. But something is running behind the area that was behind you. Do you CROSS the river or STAY and find out what is coming?")
    direction = input()
    if (direction.upper()=="CROSS"):
        print("\nLucky")
    elif (direction.upper()=="STAY"):
            print("\nUnlucky")
    else:
        print("Please pick one. CROSS or STAY?")
    direction = input() 


#Left
elif (direction.upper()=="LEFT"):
    print("\nYou decide to go left. So you walk for a bit and come across an abandoned cabin. You can see that the cabin is old but still usable. Do you EXPLORE the cabin or KEEP walking on the path?")
    


direction = input()
if (direction.upper()=="EXPLORE"):
    print("\n Lucky")
elif (direction.upper()=="KEEP"):
    print("\nYou decide to keep going on the path and find the abandoned fresh campsite. Then, you decide to call the rangers. But instead, rangers come and call the police.  ")
else:
    print("Please pick one. EXPLORE or KEEP?")
    direction = input()



