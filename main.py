import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
turtle.set_start_position()

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.listen()
    screen.onkeypress(turtle.go_up, "Up")
    if turtle.has_passed_finish():
        turtle.set_start_position()
        scoreboard.inrease_level()
    counter += 1
    if counter == 6:
        counter = 0
        car_manager.add_car()
    car_manager.move()

    for car in car_manager.cars:
        if car.distance(turtle) < 30:
            game_is_on = False
            scoreboard.game_over()


    screen.update()

screen.exitonclick()