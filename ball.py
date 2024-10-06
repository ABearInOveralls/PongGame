from turtle import Turtle

class Ball(Turtle):
    """
    A class to represent the ball in the Pong game.

    Inherits from the Turtle class and is responsible for the ball's movement,
    bouncing behavior, and resetting its position.
    """

    def __init__(self, position):
        """
        Initializes the Ball object, sets its shape, color, speed, and position.

        Parameters:
        position (tuple): The initial position (x, y) where the ball will be placed.
        """

        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(position)
        self.ball_speed = 3


    def move(self):
        """
        Moves the ball forward in the direction it's currently facing.
        The movement is controlled by the ball's current speed.
        """
        self.forward(self.ball_speed)


    def bounce(self):
        """
        Changes the ball's direction when it hits the top or bottom walls.
        The bounce is achieved by reversing the ball's current vertical direction.
        """
        current_heading = self.heading()
        self.setheading(-current_heading)


    def rebound(self, distance_from):
        """
        Adjusts the ball's direction and speed after colliding with a paddle.

        Parameters:
        distance_from (float): The distance between the paddle and the ball at the time of collision.

        The rebound angle is adjusted based on how far from the paddle's center the ball hits.
        The closer the hit, the smaller the adjustment.
        """
        scaler = 1
        if self.heading() > 180:
            scaler = -1
        if distance_from <= 25:
            adjuster = 0
        elif distance_from <= 40:
            adjuster = 15
        else:
            adjuster = 30
        current_heading = self.heading()
        self.setheading(-current_heading + 180 + (adjuster * scaler))
        self.ball_speed += 1


    def reset_ball(self, direction):
        """
        Resets the ball to the center of the screen and sets its direction and speed.

        Parameters:
        direction (float): The new direction in degrees the ball will head after reset.
        """
        self.goto(0, 0)
        self.setheading(direction)
        self.ball_speed = 3