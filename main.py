from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) # <- To remove animation (placing snake squares).


snake = Snake() # Creating the Snake object.
food = Food()
scoreboard = Scoreboard()

screen.listen() # <- Event listner for the screen with the following keys:
                # Calling the method and listening for the   event of each specific keypress below.
screen.onkey(snake.up,"Up") 
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True # A boolean for the game to be tracked.
while game_is_on:
    screen.update() # <- To update screen when tracer is turned off.
                    # Screen update is placed before the (for) loop,
                    # so that all the sqaures move together.
                    
    time.sleep(0.075) # <- This time module/function is used to add, 
                    # delay to the execution of a program.
        
    snake.move()    # Calling the Method for the Snake object here to move.

    # Detect collision with food:
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collsion with tail:
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.reset()
            snake.reset()
















screen.exitonclick()