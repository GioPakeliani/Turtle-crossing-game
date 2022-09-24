from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-200, 240)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def endgame(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)


