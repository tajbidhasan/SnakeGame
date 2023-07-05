from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("Highscore_record") as file:
            saved_score = file.read()
            self.highScore = saved_score

        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highScore}", move=False, align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > int(self.highScore):
            with open("Highscore_record", mode="w") as file:
                file.write(str(self.score))

            self.highScore = self.score
        self.score = 0
        self.update_score()

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write(arg="Game Over...", move=False, align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()


