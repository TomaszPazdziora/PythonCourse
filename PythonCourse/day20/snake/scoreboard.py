from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 180)
        self.color("white")
        self.score = 0
        self.update()

    def update(self):
        super().clear()
        super().write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        super().goto(0, 0)
        super().write(f"Game Over", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()
