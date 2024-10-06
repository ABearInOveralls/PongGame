from turtle import Screen
from paddle import Paddle
from ball import Ball
import random
import time
from scoreboard import Scoreboard

# constants for screen boundaries and paddle positions
GAME_BOUNDARY = 380
RIGHT_PADDLE_POS = (350, 0)
LEFT_PADDLE_POS = (-350, 0)

# initialize screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
scoreboard = Scoreboard()

# initialize paddles
r_paddle = Paddle(RIGHT_PADDLE_POS)
l_paddle = Paddle(LEFT_PADDLE_POS)

screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

game = True

# initialize ball
ball = Ball((0, 0))
# set ball heading to random corner
starting_direction = random.choice([37.33, 142.67, 217.33, 322.67])
ball.setheading(starting_direction)

def position_reset(ball_direction):
    """
    Resets the position of the ball and paddles after a point is scored.

    Parameters:
    ball_direction (float): The new direction for the ball after resetting.

    This function resets the ball's position to the center and adjusts its direction.
    Both paddles are reset to their starting positions.
    The screen is updated and the game is paused for 1.5 seconds to give players time to adjust.
    """
    ball.reset_ball(ball_direction)
    r_paddle.reset_paddle(RIGHT_PADDLE_POS)
    l_paddle.reset_paddle(LEFT_PADDLE_POS)
    screen.update()
    time.sleep(1.5)


while game:
    ball.move()
    # detect wall collisions
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    #detect paddle collision
    if ball.distance(r_paddle) < 53 and ball.xcor() > 335:
        ball.rebound(ball.distance(r_paddle))
    if ball.distance(l_paddle) < 53 and ball.xcor() < -335:
        ball.rebound(ball.distance(l_paddle))
    # detect score
    if ball.xcor() > GAME_BOUNDARY:
        scoreboard.l_point()
        r_direction = random.choice([37.33, 322.67])
        position_reset(r_direction)
    if ball.xcor() < -GAME_BOUNDARY:
        scoreboard.r_point()
        l_direction = random.choice([142.67, 217.33])
        position_reset(l_direction)

    time.sleep(0.02)
    screen.update()

screen. exitonclick()