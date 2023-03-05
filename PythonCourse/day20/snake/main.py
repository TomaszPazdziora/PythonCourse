from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# wyłączenie animacji
# kiedy tracer jest na zero animacja jest natychmiastowa
# i wywołuje się ją metodą render()
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

running = True
while running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # food collision detect
    if snake.head.distance(food) < 15:
        food.random_pos()
        snake.extend()
        scoreboard.increase_score()

    # wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        running = False
        scoreboard.game_over()

    # collision with tail
    # if head collides with any segment in the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            running = False
            scoreboard.game_over()

screen.exitonclick()
