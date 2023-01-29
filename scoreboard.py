from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 17, "normal")


# We don't like to have hard coding in the code bc now if we instead use AlLIGNMENT and
# Change it once then it will change throughout the entire code

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=-5, y=270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALLIGNMENT, font=FONT)
