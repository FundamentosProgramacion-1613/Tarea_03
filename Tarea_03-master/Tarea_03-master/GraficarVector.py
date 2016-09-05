#encoding: UTF-8
#Autor: Aldo Fuentes - A01373294
#Dibujar vector

from Graphics import *
from math import *

def trazarGrafica(t, mx, my):
    for _ in range(1,5):
        t.forward(mx+50)
        t.rotate(180)
        t.forward(my+50)
        t.rotate(90)

def trazarVector(t, magnitud, angulo):
    t.rotate(angulo)
    t.forward(magnitud)
    

def main():

    
    magnitud = float(input("Magnitud"))
    angulo = float(input("Angulo"))
    mx = abs(magnitud*cos(radians(angulo)))
    my = abs(magnitud*sin(radians(angulo)))
    v = Window("Tortugas",(mx*2+100),(my*2+100))
    t = Arrow((mx+50,my+50),0)
    t.draw(v)
    t.penDown()
    t.pen.color = Color("Black")
    
    trazarGrafica(t, mx, my)
    trazarVector(t, magnitud, angulo)
    

    

main()