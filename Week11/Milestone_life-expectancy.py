import statistics
import os
higher_vaule = -1
min_vaule = 10000000
top_life = -1
min_life = 10000000
max_entity = "" #Country
min_entity = "" #Country
max_year = ""
min_year = ""
counter = 0
total_age = 0
year_interst = input("Enter the year of interest: ")

with open ("/Users/xxstormynightxx/Documents/GitHub/CSE110-ProgrammingBuildingBlocks/Week11/life-expectancy.csv") as data_file:
    print(os.getcwd())
    next(data_file,None)
    for line in data_file:
        parts = line.split(",")
        entity = parts[0]
        code = parts[1]
        year = parts [2]
        expectancy = float(parts[3])

        if expectancy > higher_vaule:
            higher_vaule = expectancy
            max_entity = entity #Country
            max_year = year

        if expectancy < min_vaule:
            min_vaule = expectancy
            min_entity = entity #Country
            min_year = year
        if year == year_interst:
            total_age += expectancy
            counter += 1
            average = total_age / counter
            if expectancy > higher_vaule:
                higher_vaule = expectancy

print(f"The overall max life expectancy is: {higher_vaule:.2f} from {max_entity} in {max_year}")
print(f"The overall min life expectancy is: {min_vaule:.2f} from {min_entity} in {min_year}")

print(f"\nFor the year {year_interst}:")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was in {max_entity} with {higher_vaule:.2f}")
print(f"The min life expectancy was in {min_entity} with {min_vaule:.2f}")



