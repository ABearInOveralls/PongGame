from turtle import Turtle

class Scoreboard(Turtle):
    """
    A class to represent the scoreboard for the Pong game.

    Inherits from the Turtle class and is responsible for tracking and displaying
    the scores of the left and right players.
    """

    def __init__(self):
        """
        Initializes the Scoreboard object. Sets up the initial appearance,
        score values, and displays the scoreboard.

        Attributes:
        l_score (int): Score for the left player, initialized to 0.
        r_score (int): Score for the right player, initialized to 0.
        """
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        """
        Clears the previous score display and updates the scoreboard with
        the current scores of both players.
        """
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align='center', font=('Courier', 40, 'normal'))
        self.goto(100, 240)
        self.write(self.r_score, align='center', font=('Courier', 40, 'normal'))


    def l_point(self):
        """
        Increments the score for the left player and updates the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()


    def r_point(self):
        """
        Increments the score for the right player and updates the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()