from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

sid = Snake()
screen = Screen()
food = Food()
score = Scoreboard()

current_score = 0

game_on = True

food.generate()
while game_on:
    sid.steer()
    if sid.x_boundaries() or sid.y_boundaries() or sid.self_collision():
        score.reset()
        sid.reset()
    if sid.segments[0].distance(food) < 15:
        sid.new_bit()
        food.generate()
        score.more_points()
        current_score += 1

    screen.update()
    time.sleep(0.1)
    sid.move()

screen.exitonclick()
