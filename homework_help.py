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

    def draw(self, t: turtle.Turtle) -> None:
        # Step 1: Move to "center of shape"
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        # Step 2: Move from the center to the reference point
        t.setheading(90)
        t.forward(self.side_length/2)
        t.left(90)
        t.forward(self.side_length/2)
        t.heading(0)
        # Step 3: Draw the shape
        for _ in range(4):
            t.forward(self.side_length)
            t.right(90)


s1 = Square(50, 50, 100)
