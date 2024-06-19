from turtle import Turtle, Screen
STARTING = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]


class Snake():
    snake_width = 20
    segments = []
    canv_width = 600
    canv_height = 600

    def __init__(self, shape="square", colour="white"):
        self.screen = Screen()
        self.screen_setup()
        self.shape = shape
        self.colour = colour
        self.make_snake()

    def make_snake(self):
        for i in STARTING:
            self.add_segment(i)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.make_snake()
        self.move()

    def add_segment(self, position):
        sid = Turtle(self.shape)
        sid.up()
        sid.color(self.colour)
        sid.goto(position)
        self.segments.append(sid)

    def new_bit(self):
        self.add_segment(self.segments[-1].pos())

    def screen_setup(self):
        self.screen.bgcolor("black")
        self.screen.setup(width=self.canv_width, height=self.canv_height)
        self.screen.title("Snake :)")
        self.screen.tracer(0)

    def move(self):
        for seg in range(len(self.segments) - 1, -1, -1):
            if seg > 0:
                self.segments[seg].goto(self.segments[seg - 1].pos())
            else:
                self.segments[seg].forward(self.snake_width)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def steer(self):
        self.screen.listen()
        self.screen.onkey(key="Left", fun=self.left)
        self.screen.onkey(key="Right", fun=self.right)
        self.screen.onkey(key="Up", fun=self.up)
        self.screen.onkey(key="Down", fun=self.down)

    def x_boundaries(self):
        if self.segments[0].xcor() >= self.canv_width/2 - self.snake_width/2 or self.segments[0].xcor() <= -self.canv_width/2 + self.snake_width/2:
            return True

    def y_boundaries(self):
        if self.segments[0].ycor() >= self.canv_height/2 - self.snake_width/2 or self.segments[0].ycor() <= -self.canv_height/2 + self.snake_width/2:
            return True

    def self_collision(self):
        for position in self.segments[1:]:
            if self.segments[0].distance(position) < 15:
                return True
