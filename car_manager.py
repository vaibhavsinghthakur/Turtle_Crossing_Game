from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            x_coor = 300
            y_coor = random.randint(-250, 250)
            new_car.goto(x_coor, y_coor)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
           car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
