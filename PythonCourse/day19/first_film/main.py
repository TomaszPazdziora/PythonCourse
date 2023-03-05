from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


buttons = {"a": turn_left,
           "w": move_forwards,
           "s": move_backwards,
           "d": turn_right,
           "c": clear}


def check_buttons():
    for b, func in buttons.items():
        screen.onkey(key=b, fun=func)


screen.listen()
check_buttons()
screen.exitonclick()
