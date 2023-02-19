# # Python Math library
import math


# 1. Write a Python program to convert degree to radian.
# ```
# Input degree: 15
# Output radian: 0.261904
# ```
def degrees_to_radians(degrees):
    # radians = math.radians(degrees)
    radians = (degrees * math.pi) / 180;
    return radians


degrees = float(input("Degree: "))
radians = degrees_to_radians(degrees)
print(radians)


# 2. Write a Python program to calculate the area of a trapezoid.
# ```
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5
# ```
def area_of_trapezoid(height, first_base, second_base):
    area = (first_base + second_base) / 2 * height
    return area


height = float(input("Height: "))
base1 = float(input("First base:: "))
base2 = float(input("Second base: "))

area = area_of_trapezoid(height, base1, base2)
print(area)


# 3. Write a Python program to calculate the area of regular polygon.
# ```
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625
# ```

def area_of_polygon(num, length):
    area = (num * length ** 2) / (4 * math.tan(math.pi / num))
    return area


num_sides = int(input("Number of sides?: "))
side_length = float(input("Length of a side?: "))

area = area_of_polygon(num_sides, side_length)
print(area)


# 4. Write a Python program to calculate the area of a parallelogram.
# ```
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0
# ```
def area_of_parallelogram(base, height):
    area = base * height
    return area


base = float(input("Length: "))
height = float(input("Height: "))

area = area_of_parallelogram(base, height)

print(area)