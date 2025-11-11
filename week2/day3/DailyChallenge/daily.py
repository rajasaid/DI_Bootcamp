import math
import turtle
import random
import time

# The goal is to create a class that represents a simple circle.
#
#A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
#The user can query the circle for either its radius or diameter.
#Your Circle class should be able to:
#
# Compute the circle’s area.
# Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# Compare two circles to see which is bigger — use a dunder method (__gt__).
# Compare two circles to check if they are equal — use a dunder method (__eq__).
# Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.

class Circle:
    def __init__(self, radius: float):
        self._radius = float(radius)

    @classmethod
    def from_diameter(cls, diameter: float):
        return cls(diameter / 2.0)

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def diameter(self) -> float:
        return self._radius * 2

    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)
    
    def __str__(self):
        return f"Circle with Radius {self._radius}"
    def __repr__(self):
        return str(self)
    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"Cannot Add Cirlce to {type(other)}")
        else:
            return Circle(self._radius + other._radius)
    def __gt__(self,other):
        if not isinstance(other, Circle):
            raise TypeError(f"Cannot Compare Cirlce to {type(other)}")
        else:
            return self._radius > other._radius
    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise TypeError(f"Cannot Compare Cirlce to {type(other)}")
        else:
            return self._radius == other._radius
    def __lt__(self,other):
        if not isinstance(other, Circle):
            raise TypeError(f"Cannot Compare Cirlce to {type(other)}")
        else:
            return self._radius < other._radius
        


## usage of the class Circle
c1 = Circle(10)
c2 = Circle.from_diameter(15)
c3 = Circle(7.5)
print (c1 > c2) # True
print (c3 == c2) # True
print(c1+c2)
circles_lst = [Circle(random.random()*100) for _ in range(10)]
print(sorted(circles_lst))

## have a screen for turtle and print circles
turtle.speed(1)
turtle.hideturtle()
turtle.bgcolor("white")
colors = ["red", "green", "blue"]
for i, c in enumerate(circles_lst):
    turtle.penup()
    turtle.goto(0, -c.radius)
    turtle.pendown()
    turtle.color(colors[i % len(colors)])
    turtle.circle(c.radius)
    time.sleep(3)
