can_ride = False

first_age = int(input("What is the age of the first rider? "))
first_height = int(input("What is the height of the first rider? "))

if first_age >= 12 and first_age < 18:
        golden1 = input("Does this rider have a golden passport (yes/no)? ")
is_second_rider = input("Is there a second rider (yes/no)")

if is_second_rider.lower() == "yes":
    second_age = int(input("What is the age of the second rider? "))
    second_height = int(input("What is the height of the second rider? "))

    if second_age >= 12 and second_age < 18:
        golden2 = input("Does this rider have a golden passport (yes/no)? ")

    # Rule 1
    if first_height < 36 or second_height < 36:#inches
        can_ride = False
    else:
        # Rule 3
        if first_age >= 18 or second_age >= 18 or golden1.lower() == "yes" or golden2.lower() == "yes":
            #At least one is an Adult
            can_ride = True
        else:
            #Nobody is an Adult
            can_ride = False
            # Rule 4?
            if first_age >= 12 and first_height >= 52 and second_age >= 12 and second_height >= 52:
                can_ride = True
            elif (first_age >= 16 and second_age >= 14) or (first_age >= 14 and second_age >= 16):
                can_ride = True
            else:
                can_ride = False
else:#There is only one rider
    #Rule 2
    if (first_age >= 18 or golden1.lower() == "yes") and first_height >= 62:
        can_ride = True
    else:
        can_ride = False

if can_ride:
    print("Welcome to the ride. Have fun!")
else:
    print("Sorry, you cannot ride.")


