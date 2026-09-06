from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", font=("Arial", 18, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", font=("Arial", 18, "normal"))