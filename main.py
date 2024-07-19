from poeni import Poeni
from turtle import Screen
from reket import Reket
from loptica import Loptica
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Moj tenis")
screen.bgcolor("blue")
screen.tracer(0)

desni_igrac = screen.textinput("Desni igrac", prompt="Unesi ime desnog igraca")
levi_igrac = screen.textinput("Levi igrac", prompt="Unesi ime levog igraca")

poeni = Poeni(desni_igrac, levi_igrac)
desni_reket = Reket((360, 0))
levi_reket = Reket((-360, 0))
loptica = Loptica()

screen.listen()
screen.onkey(desni_reket.reket_gore, "Up")
screen.onkey(desni_reket.reket_dole, "Down")

screen.onkey(levi_reket.reket_gore, "w")
screen.onkey(levi_reket.reket_dole, "s")

igra_traje = True

while igra_traje:
    time.sleep(loptica.brzina_lopte)
    screen.update()
    loptica.loptica_ide()

    if loptica.ycor() == 280 or loptica.ycor() == -280:
        loptica.odbij_o_zid()

    if loptica.distance(desni_reket) < 50 and loptica.xcor() > 330 or loptica.distance(levi_reket) < 50 and loptica.xcor() < -330:
        loptica.odbij_o_reket()

    if loptica.xcor() > 400:
        loptica.resetuj_poziciju()
        poeni.povecaj_levom_poene()
        poeni.osvezi_rezultat(desni_igrac, levi_igrac)

    if loptica.xcor() < -400:
        loptica.resetuj_poziciju()
        poeni.povecaj_desnom_poene()
        poeni.osvezi_rezultat(desni_igrac, levi_igrac)

screen.exitonclick()