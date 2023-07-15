from turtle import Turtle
COLOUR = 'white'
HEIGHT = 600
DASH_LENGTH = 10
PEN_SIZE = 5

class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(0, -HEIGHT/2)
        self.pencolor(COLOUR)
        self.pensize(PEN_SIZE)
        self.setheading(90)
        for _ in range(round(HEIGHT/(2*DASH_LENGTH))):
            self.pd()
            self.forward(DASH_LENGTH)
            self.pu()
            self.forward(DASH_LENGTH)
        self.hideturtle()




