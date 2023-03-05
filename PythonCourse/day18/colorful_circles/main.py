import colorgram
import random
import turtle as t

# rgb_color = []
# colors = colorgram.extract('image.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)

color_list = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203),
              (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107),
              (187, 140, 170), (85, 120, 180), (59, 39, 31)]

dot_size = 20
break_between_dots = 50
width = 600
height = 600
dots_in_row = int((width - 2 * break_between_dots) / break_between_dots)
# 10 dots in each column
# 10 dots in each row

t.colormode(255)
tim = t.Turtle()
tim.speed(15)
tim.penup()
tim.hideturtle()
x = -(width / 2 - break_between_dots)
y = -(height / 2 - break_between_dots)

for i in range(dots_in_row):
    for j in range(dots_in_row):
        tim.goto(x, y)
        tim.dot(dot_size, random.choice(color_list))
        x += break_between_dots
    x = -(width / 2 - break_between_dots)
    y += break_between_dots


screen = t.Screen()
screen.exitonclick()
