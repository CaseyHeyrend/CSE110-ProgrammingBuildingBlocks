#Taking input from the user
from cmath import pi
#Area of a square

side = float(input("What is the length of a side the square (in cm)? "))
area = side ** 2
print(f"The area if the square is: {area} cm*^2")
print(f"The area of the square is: {area / 10000} m^2")
#Area of a rectangle
length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"The area of the rectangle is: {area} cm*^2")
print(f"The area of the rectangle is: {area / 10000} m^2")

#Area of a circle
radius = float(input("What is the radius of the circle (in cm)? "))
area = pi * (radius ** 2)
print(f"The area of the circle is: {area} cm*^2")
print(f"The area of the circle is: {area / 10000} m^2")
#stretch goals
lengthAll = float(input = ("Give a single length value: "))

areaSquare = lengthAll ** 2
areaCircle = pi * (lengthAll ** 2)
volumeCube = lengthAll ** 3
volumeSphere = (4 / 3) * pi * (lengthAll ** 3)

print(f"Area of a square: {areaSquare}")
print(f"Area of a circle: {areaCircle}")
print(f"Volume of a cube: {volumeCube}")
print(f"Volume of a sphere: {volumeSphere}")

