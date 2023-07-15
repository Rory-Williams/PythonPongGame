from turtle import Turtle
from random import randint
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.y_dist = 10
        self.move_init()


    def move_init(self):
        self.setheading(randint(1, 4) * 90 + 45)
        self.x_move = 10 * (randint(0, 1) * 2 - 1)
        self.y_move = self.y_dist * (randint(0, 1) * 2 - 1)

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bat_bounce(self):
        self.x_move *= -1
        ychange = randint(-15, 15)
        print(ychange)
        self.y_move += ychange

    def bounce_x(self):
        self.x_move *= -1





