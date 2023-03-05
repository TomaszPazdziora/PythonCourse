import time
from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard

LEFT_PADDLE_LOCATION = (-350, 0)
RIGHT_PADDLE_LOCATION = (350, 0)
X_BOUND = 320

r_paddle = Paddle(RIGHT_PADDLE_LOCATION)
l_paddle = Paddle(LEFT_PADDLE_LOCATION)
ball = Ball()
screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(l_paddle.up, "W")
screen.onkey(l_paddle.down, "S")

running = True
while running:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # collision with top/bottom wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > X_BOUND or ball.distance(
            l_paddle) < 50 and ball.xcor() < -X_BOUND:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.respawn()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.respawn()
        scoreboard.r_point()

screen.exitonclick()
