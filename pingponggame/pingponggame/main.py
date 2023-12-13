from path import *
from ball import *
from score import *
import random

import keyboard
import time
scr = Screen()

list_random = [-3,3]
random_x = random.choice(list_random)
# random_y = random.randint(2,5)

x_velocity = random_x
y_velocity = 1

scr.setup(width =800, height=600)
scr.bgcolor("black")
scr.tracer(0)
screen_width = scr.window_width()
def quit_game():
    scr.bye()
scr.onkeypress(quit_game, 'q')

path = pathSquare()
path2 = pathSquare2()
ball = bouncing_ball()
scoreboard = score()

scr.onkey(path.move_top, "Up")
scr.onkey(path.move_bottom, "Down")
scr.listen()

ball_not_passing_path = True
game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.01)
    #path kiri
    if keyboard.is_pressed("w"):
        path.move_top()
    if keyboard.is_pressed("s"):
        path.move_bottom()

    if path.trt.xcor() > 380:
        path.trt.setx(390)
    elif path.trt.xcor() < -380:
        path.trt.setx(-390)

    if path.trt.ycor() > 280:
        path.trt.sety(250)
    elif path.trt.ycor() < -280:
        path.trt.sety(-250)
    #path kanan
    if keyboard.is_pressed("Up"):
        path2.move_top2()
    if keyboard.is_pressed("Down"):
        path2.move_bottom2()
    if path2.trt.xcor() > 380:
        path2.trt.setx(390)

    elif path2.trt.xcor() < -380:
        path2.trt.setx(-390)

    if path2.trt.ycor() > 280:
        path2.trt.sety(250)
    elif path2.trt.ycor() < -280:
        path2.trt.sety(-250)

    #menggerakkan bola
    ball.trt.sety(ball.trt.ycor() + y_velocity)
    ball.trt.setx(ball.trt.xcor() + x_velocity)
    if ball.trt.ycor() > 290:
        ball.trt.sety(290)
        y_velocity *= -1  # Memantulkan bola ke arah vertikal yang berlawanan

    if ball.trt.ycor() < -290:
        ball.trt.sety(-290)
        y_velocity *= -1

    if path.trt.distance(ball.trt) < 25:
        x_velocity *= -1 # Memantulkan bola ke arah horizontal yang berlawanan

    if path2.trt.distance(ball.trt) < 25:
        x_velocity *= -1
    # if ball.trt.xcor() > (screen_width / 2) or ball.trt.xcor() < -(screen_width / 2):
    #     x_velocity *= -1  # Memantulkan bola ke arah horizontal yang berlawanan

    #menambah score
    if ball.trt.xcor() > 390 or ball.trt.xcor() < -390:
        scoreboard.plus_score()

    #mereset posisi bola ketika dapat score / melewati batas koordinat horizontal
    if ball.trt.xcor() > 390 or ball.trt.xcor() < -390:
        ball.trt.goto(0,0)

scr.exitonclick()