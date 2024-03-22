# Write a  Python program to create a class representing a Circle. Include methods to calculate its area
# and perimeter.

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_of_circle(self):
        return math.pi * self.radius ** 2

    def perimeter_of_circle(self):
        return math.pi * self.radius * 2


radius = float(input("Input the radius of the circle: "))

circle = Circle(radius)
area = circle.area_of_circle()
perimeter = circle.perimeter_of_circle()

print(area)
print(perimeter)

