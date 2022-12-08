from math import pi

def compute_area_square(side):
    return side * side
def compute_area_rectangle(length, width):
    return length * width
def compute_area_circle(radius):
    return pi * radius * radius
def compute_area(shape, vaule1, vaule2=0):
    area = -1
    if shape == "square":
        area = compute_area_square(vaule1)
    elif shape == "circle":
        area = compute_area_circle(vaule1)
    elif shape == "rectangle":
        area = compute_area_rectangle(vaule1, vaule2)

    return area
    
shape = ""

while shape != "quit":
    shape = input("What shape do you have? ")
    shape = shape.lower()

    if shape == "square":
        side = float(input("What is the length of the side? "))
        area = compute_area_square(side)
        print(f"The area is {area}.")
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area_rectangle(length, width)
        print(f"The area is {area}.")
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area_circle(radius)
        print(f"The area is {area}.")