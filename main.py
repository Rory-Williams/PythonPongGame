from turtle import Screen
from bat import Bat
from net import Net
from score import Score
from ball import Ball
import time

# set up dimensions
court_width = 700
court_height = 500
l_court = -court_width / 2
r_court = court_width / 2
t_court = court_height/2
b_court = -court_height/2

# set up screen
screen = Screen()
screen.setup(width=court_width+100, height=court_height+150)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

# set up score boards
left_score = Score()
left_score.position(-60, t_court+20)
right_score = Score()
right_score.position(60, t_court+20)
net = Net()
ball = Ball()
speed = 0.07

# set up bats
bat_length = 100
bat_indent = 20
left_bat = Bat((l_court+bat_indent, 0), bat_length)
right_bat = Bat((r_court-bat_indent, 0), bat_length)

# set up controls
screen.listen()
screen.onkey(right_bat.up, 'Up')
screen.onkey(right_bat.down, 'Down')
screen.onkey(left_bat.up, 'w')
screen.onkey(left_bat.down, 's')

# main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(speed)
    ball.move()

    if ball.ycor() > t_court or ball.ycor() < b_court:
        ball.bounce_y()
    # elif ball.xcor() < l_court or ball.xcor() > r_court:
    #     ball.bounce_x()

    #bouncing using position
    if ball.xcor() == left_bat.xcor()+20:
        if ball.ycor() <= left_bat.ycor() + bat_length/2 and ball.ycor() >= left_bat.ycor() - bat_length/2:
            # ball.bounce_x()
            ball.bat_bounce() # changes y dir
            print('bounced')
    elif ball.xcor() == right_bat.xcor()-20:
        if ball.ycor() <= right_bat.ycor() + bat_length/2 and ball.ycor() >= right_bat.ycor() - bat_length/2:
            # ball.bounce_x()
            ball.bat_bounce()  # changes y dir
            print('bounced')

    #bouncing using distance
    # if ball.distance(right_bat) < 50 and ball.xcor() > r_court-bat_indent:
    #     ball.bounce_x()
    #     print('bounced')
    # elif ball.distance(left_bat) < 50 and ball.xcor() < l_court+bat_indent:
    #     ball.bounce_x()
    #     print('bounced')

    if ball.xcor() > r_court or ball.xcor() < l_court:
        if ball.xcor() > r_court:
            left_score.update_score()
        else:
            right_score.update_score()
        time.sleep(0.5)
        ball.home()
        screen.update()
        time.sleep(0.5)
        ball.move_init()

screen.exitonclick()
