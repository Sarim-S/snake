from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 17, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.current_score = 0
        with open("high_score.txt") as n_file:
            self.high_score = n_file.read()
        self.up()
        self.goto(0, 270)
        self.ht()
        self.write(arg=f"Score : {self.current_score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def more_points(self):
        self.current_score += 1
        self.clear()
        self.write(arg=f"Score : {self.current_score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > int(self.high_score):
            self.high_score = self.current_score
        self.current_score = 0
        self.clear()
        self.write(arg=f"Score : {self.current_score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def game_over(self):
        self.home()
        self.write("Game over :(", align="center", font=("Times New Roman", 15, "normal"))



