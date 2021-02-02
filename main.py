from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.cars:
        if car.distance(player)<30:
            scoreboard.game_over()
            time.sleep(5)
            game_is_on = False

    if  player.is_at_finish():
        player.goto_initial_position()
        scoreboard.increase_level()
        car_manager.level_up()
