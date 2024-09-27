import math
import turtle
from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, t: turtle.Turtle) -> None:
        # Step 1: Move to "center of shape"
        # Step 2: Draw the shape from the "center"
        pass


class Square(Shape):

    def __init__(self, x, y, side_length: float):
        super().__init__(x, y)
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

    def draw(self, t: turtle.Turtle) -> None:
        # Step 1: Move to "center of shape"
        t.penup()
        t.goto(self.x, self.y)

        # Step 2: Move from the center to the reference point
        t.setheading(90)
        t.forward(self.side_length/2)
        t.left(90)
        t.forward(self.side_length/2)
        t.setheading(0)

        t.pendown()
        # Step 3: Draw the shape
        for _ in range(4):
            t.forward(self.side_length)
            t.right(90)

class Triangle(Shape):
    def __init__(self, x, y, side_length: float):
        super().__init__(x, y)
        self.side_length = side_length

    def draw(self, t: turtle.Turtle) -> None:
        # Step 1: Move to "center of shape"
        t.penup()
        t.goto(self.x, self.y)

        # Step 2: Move from the center to the reference point
        t.setheading(90)
        t.forward(self.side_length/2*math.sqrt(3))
        t.setheading(120)

        t.pendown()
        # Step 3: Draw the shape
        for _ in range(3):
            t.forward(self.side_length)
            t.left(120)

class Circle(Shape):
    def __init__(self, x, y, radius: float):
        super().__init__(x, y)
        self.radius = radius

    def draw(self, t: turtle.Turtle) -> None:
        # Step 1: Move to "center of shape"
        t.penup()
        t.goto(self.x, self.y)

        t.pendown()
        # Step 3: Draw the shape
        t.circle(self.radius)

class Rectangle(Shape):

    def __init__(self, x, y, length: float, height:float):
        super().__init__(x, y)
        self.length = length
        self.height = height

    def draw(self, t: turtle.Turtle) -> None:
        # Step 1: Move to "center of shape"
        t.penup()
        t.goto(self.x, self.y)

        # Step 2: Move from the center to the reference point
        t.setheading(90)
        t.forward(self.height/2)
        t.left(90)
        t.forward(self.length/2)
        t.setheading(0)

        t.pendown()
        # Step 3: Draw the shape
        sides = [self.length, self.height]
        for i in range(4):
            t.forward(sides[i%2])
            t.right(90)


def setup_turtle(color):
    t = turtle.Turtle()
    t.speed(7)  # Fastest speed
    t.color(color)
    return t

def write_label(t, text, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text, font=("Arial", 12, "normal"))

def draw_y_axis(t):
    x = 0
    y = 400
    while y != -400:
        t.goto(x, y)
        write_label(t,f"{x=},{y=}",x,y)
        y -= 50

def draw_x_axis(t):
    x = 400
    y = 0
    while x != -400:
        t.goto(x, y)
        write_label(t,f"{x=},{y=}",x,y)
        x -= 50

t = setup_turtle("blue")
# draw_y_axis(t)
t1 = setup_turtle("black")
# draw_x_axis(t1)


s1 = Square(200, 200, 100)
s1.draw(t)

# s2 = Square(-200, 200, 100)
# s2.draw(t)


tri1 = Triangle(250, 164, 100)
tri1.draw(t)


c1 = Circle(190, 215, 10)
c1.draw(t)

c1 = Circle(230, 215, 10)
c1.draw(t)

r1 = Rectangle(200, 175, 10, 50)
r1.draw(t)
turtle.done()
