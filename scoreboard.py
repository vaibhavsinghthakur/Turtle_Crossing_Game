from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.color("white")
        self.penup()
        self.show_level()

    def increase_level(self):
        self.level+=1
        self.show_level()

    def show_level(self):
        self.clear()
        self.goto(-240, 240)
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER...", align="center", font=FONT)
