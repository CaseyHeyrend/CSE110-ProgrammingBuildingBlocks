#Taking input from the user

#Area of a square
side = float(input("What is the length of a side the square? "))
area = side ** 2
print(f"The area if the square is: {area}")

#Area of a rectangle
length = float(input("What is the length of rectangle? "))
width = float(input("What is the width of the rectangle? "))
area = length * width
print(f"The area of the rectangle is: {area}")

#Area of a circle
radius = float(input("What is the radius of the circle? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area}")
