from snake import *
from food import *
from score import *
import time

def quit_game():
    scr.bye()
scr.onkeypress(quit_game, 'q')

Snake = snake()
Food = food()
Score = score()

Snake.screen_game()
Snake.movement()
Food.food_spawn()


game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    Snake.move_forward()

    if Snake.head.distance(Food) <15:
        Food.food_respawn()
        Score.plus_score()
        Snake.add_snake()

    if Snake.head.xcor() > 280 or Snake.head.xcor() < -280 or Snake.head.ycor() > 280 or Snake.head.ycor() <-280:
        game_is_on = False
        Score.game_over()

    for segment in Snake.segments:
        if segment == Snake.head:
            pass
        elif Snake.head.distance(segment) < 10:
            game_is_on = False
            Score.game_over()

scr.exitonclick()

















