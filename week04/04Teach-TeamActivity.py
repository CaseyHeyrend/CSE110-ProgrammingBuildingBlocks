from math import exp
from math import sqrt

# input
print("Welcome to the velocity calculator. Please enter the following: ")
mass = float(input("What is Mass? "))
gravity = float(input("What us the acceleration due to gravity? "))
time = float(input("What is Time? "))
density = float(input("What is the density of the fluid? "))
area = float(input("What is the cross sectional area of the object? "))
drag_cont = float(input("What is the drag constant? (0.5 for sphere, 1.1 for cylinder) "))

#calculate 1
lowercase_c = (1 / 2) * density * area * drag_cont

#calculate  2
velocity = sqrt(mass * gravity / lowercase_c) * (1 - exp((-sqrt(mass * gravity * lowercase_c) / mass) * time))

#output
print()
print(f"The inner value of c is: {lowercase_c:.3f}")
print(f"The velovity after {time} seconds is: {velocity:.3f} m/s")


