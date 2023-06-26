from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over...", move=False, align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
