import random
import turtle as t

turtle = t.Turtle()
turtle.speed(20)
turtle.pensize(15)

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


for i in range(100):
    turtle.color(get_random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(angle))

screen = t.Screen()
screen.exitonclick()
