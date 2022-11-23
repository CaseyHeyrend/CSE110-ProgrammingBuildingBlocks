with open("/Users/xxstormynightxx/Documents/GitHub/CSE110-ProgrammingBuildingBlocks/Week11/hr_system.txt") as f:
    for line in f:
        parts = line.split(" ")
        name = parts[0]
        title = parts[2]

        print(f"Name: {name}, Title: {title}")