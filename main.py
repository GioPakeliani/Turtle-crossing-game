import time
from image import image
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic(image)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            scoreboard.endgame()
            game_is_on = False

    if player.is_in_top():
        player.goto(STARTING_POSITION)
        scoreboard.level_up()
        car_manager.speed_up_cars()

screen.exitonclick()
