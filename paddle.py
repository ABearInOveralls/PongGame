from turtle import Turtle

class Paddle(Turtle):
    """
    A class to represent the paddles in the Pong game.

    Inherits from the Turtle class and is responsible for creating and managing
    the movement of paddles on the screen.
    """

    def __init__(self, position):
        """
        Initializes the Paddle object, sets its shape, size, color, and position.

        Parameters:
        position (tuple): The initial position (x, y) where the paddle will be placed.
        """
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def move_up(self):
        """
        Moves the paddle upwards by 20 pixels. Ensures the paddle does not move
        beyond the upper boundary of the game screen (y = 240).
        """
        if self.ycor() <= 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)


    def move_down(self):
        """
        Moves the paddle downwards by 20 pixels. Ensures the paddle does not move
        beyond the lower boundary of the game screen (y = -220).
        """
        if self.ycor() >= -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


    def reset_paddle(self, position):
        """
        Resets the paddle to its initial position after a point is scored.

        Parameters:
        position (tuple): The position (x, y) to which the paddle will be reset.
        """
        self.goto(position)