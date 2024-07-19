from turtle import Turtle, Screen
class Poeni(Turtle):
    def __init__(self, desni_igrac, levi_igrac):
        super().__init__()
        self.poeni_desni = 0
        self.poeni_levi = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.osvezi_rezultat(desni_igrac, levi_igrac)

    def osvezi_rezultat(self, desni_igrac, levi_igrac):
        self.clear()
        self.goto(100, 250)
        self.write(f"{desni_igrac}: {self.poeni_desni}", align="center", font=("Courier", 20, "normal"))
        self.goto(-100, 250)
        self.write(f"{levi_igrac}: {self.poeni_levi}", align="center", font=("Courier", 20, "normal"))

    def povecaj_desnom_poene(self):
        self.poeni_desni += 1

    def povecaj_levom_poene(self):
        self.poeni_levi += 1