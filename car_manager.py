from turtle import Turtle
import random

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLOURS))
        self.shape("square")
        self.shapesize(1, 2, None)
        self.goingRight = bool(random.getrandbits(1))
        if self.goingRight:
            self.setpos(-280, random.randint(-200, 200))
        else:
            self.setpos(280, random.randint(-200, 200))

    def is_right(self):
        return self.goingRight


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.level = 1

    def add_car(self):
        car = Car()
        self.cars.append(car)

    def move(self):
        for c in self.cars:
            if c.is_right():
                c.forward(STARTING_MOVE_DISTANCE + (self.level-1)*MOVE_INCREMENT)
            else:
                c.forward(-(STARTING_MOVE_DISTANCE + (self.level-1)*MOVE_INCREMENT))


    """
    Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of 
    the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our 
    little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video 
    walkthrough in Step 4.
    """