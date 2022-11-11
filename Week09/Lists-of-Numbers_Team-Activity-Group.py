print("Enter a list of numbers, type 0 when finished.")
numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)
#Sum Part of Core 1
sum = 0
for number in numbers:
    sum += number
print(f"The sum is: {sum}")
#average Part of Core 2
count = len(numbers)
average = sum / count
print(f"The average is: {average}")
#largest number(Max) Part of Core 3
max_num_so_far = -1
for number in numbers:
    if number > max_num_so_far:
        max_num_so_far = number
print(f"The largest number is: {max_num_so_far}")

#Stretch Challenge 1
min_num_so_far = 999999999999

for number in numbers:
    if number > 0 and number < min_num_so_far:
        min_num_so_far = number
print(f"The smallest positive number is: {min_num_so_far}")

#Stretch Challenge 2
sorted_list = sorted(numbers)
print(f"The sorted list is: ")
for number in sorted_list:
    print(number)


