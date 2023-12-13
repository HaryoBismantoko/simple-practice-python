from turtle import Turtle


class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto (-100,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"score A: {self.score}", align="center", font=("Arial", 14, "normal"))
    def plus_score(self):
        self.score +=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center")


class score2(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto (100,270)
        self.hideturtle()
        self.update_score2()

    def update_score2(self):
        self.write(f"score B: {self.score}", align="center", font=("Arial", 14, "normal"))
    def plus_score2(self):
        self.score +=1
        self.clear()
        self.update_score2()
    def game_over2(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center")
