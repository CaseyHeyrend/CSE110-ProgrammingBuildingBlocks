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
            print("\nYou decide to go to the group of people. The group of people realizes who you are. They have been looking for you. You wander off. You are back with your group. This is one of the endings. Thanks for playing.")

        elif (direction.upper()=="PATH"):
            print("\nYou decide to continue on the path. So you walk a bit more in the direction you are heading. You see a waterfall and a waterhole. You also see a trail plaque. Finally, you see something behind the waterfall. Do you go BEHIND the waterfall or READ the trail plaque? ")
            
            direction = input()
            if (direction.upper()=="BEHIND"):
                print("\nYou decide to go behind the waterfall. You find a hidden passway behind the waterfall. You go through the hidden passway and go found two doors. One door is mossy green, and the other door is wooden brown. Do you go through the MOSSY green door or the WOODEN brown door?")
                direction = input()
                if (direction.upper()=="MOSSY"):
                    print("\nYou decide the mossy green door is met with just a bunch of overgrown nature. It is a dead end, and if you want to get through, it looks like it gets thick in the back. You cant see where the passway leads or ends. This is an ending. Thanks for playing.")
                elif (direction.upper()=="WOODEN"):
                    print("\nYou decide on the wooden brown door and see a clear passway. You walk a bit and find a chest that is glowing. You open the chest, and you find a glowing necklace. You put it on and have to be teleported back to the start of the trail. You see your vehicle and head home with the necklace still on you. This is an ending. Thanks for playing.")
                else:
                    print("\nPlease pick one. MOSSY or WOODEN?")

            elif (direction.upper()=="READ"):
                print("\nYou decide to read the trail plaque. The plaque tells you the history of the trail and the waterfall. The plaque is interesting to read, and your group manages to find where you wander off. This is an ending. Thanks for playing.")
            else:
                print("\nPlease pick one. BEHIND or READ?")
        else:
            print("\nPlease pick one. GROUP or PATH?")

    elif (direction.upper()=="STAY"):
            print("\nYou decide to stay and what was running towards you. But, unfortunately, the campsite killer was in the forest, and they found you. So, unfortunately, you have been caught, and this is the end. Thanks for playing.")
    else:
        print("\nPlease pick one. CROSS or STAY?") 
#Left
elif (direction.upper()=="LEFT"):
    print("\nYou decide to go left. So you walk for a bit and come across an abandoned cabin. You can see that the cabin is old but still usable. Do you EXPLORE the cabin or KEEP walking on the path?")
    
    direction = input()
    if (direction.upper()=="EXPLORE"):
        print("\nYou decide to explore the cabin. So you walk into the cabin, and when you step on something on the floor. Something is different from the floor. You then realize that it is a trapdoor. Do you GO in the trapdoor or RESUME to explore?")
        direction = input()
        if (direction.upper()=="GO"):
            print("\nYou decide to go into the trapdoor and discover a tunnel that leads you deep in the tunnel, where you find a door. You open the door and see a glowing sapphire portal and a box with cloth covering it. Do you go through the glowing SAPPHIRE portal or go to the BOX cover by something?")
            direction = input()
            if (direction.upper()=="SAPPHIRE"):
                print("\nYou decide you go through the glowing sapphire portal and are in a new dimension. But, unfortunately, the portal closed behind and will open back up in three hours. So, do you explore this NEW world, or do you WAIT for the portal to reopen?")
                direction = input()
                if (direction.upper()=="NEW"):
                    print("\nYou decide to explore this new world and discover a bag that doesn't have a limit. You also found a lot of treasures. Some of the treasures are real gold coins and precious gems. You grab some of the treasures and put them in your limitless bag. You see the portal reopens, and you go through. You are home, and you have a magic bag and treasures. This is the magic ending. Thanks for playing.")

                elif (direction.upper()=="WAIT"):
                    print("\nYou decide to wait for the portal to reopen, and the portal reopens, and you leave through the portal, and you are back at the start of the trail where your vehicle is. So you head home, and this is an ending. Thanks for playing.")
                else:
                    print("\nPlease pick one. NEW or WAIT?")
            elif (direction.upper()=="BOX"):
                print("\nYou decide to go to the box that is covered up, and you find a trunk. You open the trunk and see a note. The note says, ""Whoever finds this note is the owner of the contains in this trunk."" Inside the chest in real gold coins and precious gems. The end.")
            else:
                print("\nPlease pick one. SAPPHIRE or BOX?")
            
        elif (direction.upper()=="RESUME"):
            print("\nYou decide to resume exploring the cabin. You find it nice to sleep for the night, away from the killer roaming the forest and the wild animals. To be sure, you lock the door and barricade the exits. So you are safe. You bunked down for the night and waited for the morning to come. Morning comes, and you leave with the light outside—a nice ending.")  
        else:
            print("\nPlease pick one. GO or RESUME?")

    elif (direction.upper()=="KEEP"):
        print("\nYou decide to keep going on the path and find the abandoned fresh campsite. Then, you decide to call the rangers. But instead, rangers come and call the police. So this choice for the game is one of the endings.")
    else:
        print("\nPlease pick one. EXPLORE or KEEP?")
else:
    print("Please pick one. RIGHT or LEFT?")



