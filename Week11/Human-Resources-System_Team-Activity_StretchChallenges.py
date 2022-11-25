with open("/Users/xxstormynightxx/Documents/GitHub/CSE110-ProgrammingBuildingBlocks/Week11/hr_system.txt") as f:
    for line in f:
        
        clean_line = line.strip()#Stretch Challenge
        
        parts = clean_line.split(" ")#Core minus the clean part

        name = parts[0]#Core
        id_number = parts[1]#Stretch Challenge
        title = parts[2]#Core
        salary = float(parts[3])#Stretch Challenge

        #Stretch Challenge
        pay_amount = salary / 24 
        if title.lower() == "engineer":
            pay_amount += 1000

        #print(f"Name: {name}, Title: {title}")#Core  
        print(f"{name} (ID: {id_number}), {title} - ${pay_amount:.2f}")#Stretch Challenge
