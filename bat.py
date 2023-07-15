from turtle import Turtle
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Bat(Turtle):
    def __init__(self, position, length):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.pu()
        self.setheading(UP)
        self.goto(position)
        self.turtlesize(1, length/20)

    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DIST)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DIST)



