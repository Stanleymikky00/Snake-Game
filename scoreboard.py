from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, center=None):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        #self.write(f"score: {self.score}", align= "center", font= ("Arial", 24,"normal"))
        self.hideturtle()
        self.update_scoreboard()

    #THIS UPDATE SCOREBOARD WAS CREATED CAUSE THE NEW SCORE WAS OVERLAPPING THE PREVIOUS SCORE.
    def update_scoreboard(self):
        self.write(f"score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        #self.write(f"score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))


