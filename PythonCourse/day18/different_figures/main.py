import random
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("green")
turtle.speed(2)


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)


def draw_figure(sides):
    angle = 360 / sides
    for j in range(sides):
        turtle.forward(100)
        turtle.right(angle)


for fig in range(3, 11):
    change_color()
    draw_figure(fig)

screen = Screen()
screen.exitonclick()
