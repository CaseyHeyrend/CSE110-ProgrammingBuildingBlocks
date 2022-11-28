import statistics
high_vaule = -1
min_vaule = 10000000
finest_life = -1
min_life = 10000000
greatest_Country = ""
min_Country = ""
max_entity = ""
min_entity = ""
max_year = ""
min_year = ""
counter = 0
total_age = 0
year_interst = input("Enter the year of interest: ")



with open ("/Users/xxstormynightxx/Documents/GitHub/CSE110-ProgrammingBuildingBlocks/Week11/life-expectancy.csv") as data_file:
    next(data_file,None)
    for line in data_file:
        parts = line.split(",")
        entity = parts[0]
        code = parts[1]
        year = parts [2]
        expectancy = float(parts[3])

        if expectancy >high_vaule:
            high_vaule = expectancy
            max_entity = entity
            max_year = year
        if expectancy < min_vaule:
            min_vaule = expectancy
            min_entity = entity
            min_year = year
        if year == year_interst:
            total_age += expectancy
            counter += 1
            average = total_age / counter
            if expectancy > high_vaule:
                high_vaule = expectancy



