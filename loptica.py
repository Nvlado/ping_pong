from turtle import Turtle

class Loptica(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.novi_x = 10
        self.novi_y = 10
        self.brzina_lopte = 0.1

    def loptica_ide(self):
        novi_x = self.xcor() + self.novi_x
        novi_y = self.ycor() + self.novi_y
        self.goto(novi_x, novi_y)

    def odbij_o_zid(self):
        self.novi_y *= -1

    def odbij_o_reket(self):
        self.novi_x *= -1
        self.brzina_lopte *= 0.9

    def resetuj_poziciju(self):
        self.brzina_lopte = 0.1
        self.goto(0, 0)
        self.odbij_o_reket()
