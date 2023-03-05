import random
import turtle as t

turtle = t.Turtle()
turtle.speed(20)

# when we want to get random color from our list
# col = ["dark turquoise", "coral", "dark salmon", "orchid", "burlywood"]

angle = [0, 90, 180, 270]
# needed when you want to create random color by RGB values
t.colormode(255)


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


steps = 90
angle = 360 / steps

for _ in range(steps):
    turtle.color(get_random_color())
    turtle.circle(50)
    current = turtle.heading()
    turtle.setheading(current + angle)

screen = t.Screen()
screen.exitonclick()
