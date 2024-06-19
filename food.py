from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self, colour="sky blue"):
        super().__init__()
        self.shape("circle")
        self.color(colour)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def generate(self):
        self.penup()
        self.speed("fastest")
        self.goto(randint(-265, 265), randint(-265, 265))

