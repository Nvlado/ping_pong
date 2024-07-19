from turtle import Turtle

class Reket(Turtle):
    def __init__(self, pozicija):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.shape("square")
        self.goto(pozicija)


    def reket_gore(self):
        novi_y = self.ycor() + 50
        self.goto(self.xcor(), novi_y)

    def reket_dole(self):
        novi_y = self.ycor() - 50
        self.goto(self.xcor(), novi_y)