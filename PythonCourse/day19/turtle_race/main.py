import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

turtles = {"red": Turtle(shape="turtle"),
           "orange": Turtle(shape="turtle"),
           "yellow": Turtle(shape="turtle"),
           "green": Turtle(shape="turtle"),
           "blue": Turtle(shape="turtle"),
           "purple": Turtle(shape="turtle")}

yh = 125
# color turtles and set at starting positions
for color, tur in turtles.items():
    tur.penup()
    tur.color(color)
    tur.goto(x=-230, y=yh)
    yh -= 50

if user_bet:
    is_race_on = True

while is_race_on:
    for color in turtles:
        if turtles[color].xcor() > 230:
            winning_color = color
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtles[color].forward(rand_distance)


screen.exitonclick()
