
numbers = []
number = -1

print("Enter a list of numbers, type 0 when finished.")

while number != 0:
    number = int(input("Enter number: "))
    numbers.append(number)
#Sum Part of Core 1
sum = 0
for number in numbers:
    sum += number
print(f"The sum is: {sum}")
#average Part of Core 2
counting = len(numbers)
average = sum / (counting - 1)

print(f"The average is: {average}")
#largest number(Max) Part of Core 3
max_num = -1
for number in numbers:
    if number > max_num:
        max_num = number
print(f"The largest number is: {max_num}")

#Stretch Challenge 1
min_num = 999999999999

for number in numbers:
    if number > 0 and number < min_num:
        min_num_so_far = number
print(f"The smallest positive number is: {min_num}")

#Stretch Challenge 2
num_list = sorted(numbers)
print(f"The sorted list is: ")
for number in num_list:
    print(number)


