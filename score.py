from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 32, 'normal')
COLOUR = 'white'

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0, 260)
        self.color(COLOUR)
        self.score = 0
        self.write(f'{self.score}', align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'{self.score}', align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGN, font=FONT)

    def position(self, x, y):
        self.clear()
        self.goto(x, y)
        self.write(f'{self.score}', align=ALIGN, font=FONT)

