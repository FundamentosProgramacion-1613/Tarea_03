#encoding: UTF-8

# Autor: Marina Itzel Haro Hernndez, A01373471
# Dibuja un vector de acuerdo a su mágnitud y a su ángulo


from Graphics import*
import math
from math import sin, cos

def main():
    magnitud = int(input("Magnitud del vector"))
    angulo = int(input("Angulo del vector"))
    v = Window ("Vector", 600, 600)
    t = Arrow((400, 300), 0)
    t.penDown()
    t.draw(v)
    dibujarPlanoCartesiano(t)
    dibujarVector(magnitud, angulo, t)
    

    
def dibujarPlanoCartesiano(t):
    t.forward(600)
    t.rotate(180)
    t.penUp()
    t.forward(300)
    t.rotate(270)
    t.forward(300)
    t.rotate(180)
    t.penDown()
    t.forward(600)
    t.penUp()
    t.rotate(180)
    t.forward(300)
    t.rotate(270)
    t.penDown()
    
def dibujarVector(magnitud, angulo, t):
    t.rotate(angulo)
    t.forward(magnitud)
    t.rotate((90-angulo)+180)
    #usando la propiedad seno sacas cateto opuesto
    t.forward((sin(angulo))*magnitud)
    t.penUp()
    t.rotate(270)
    #usando la propiedad coseno sacas cateto adyacente
    t.forward(((cos(angulo))*magnitud))
    t.rotate(270)
    t.forward((sin(angulo))*magnitud)
    t.rotate(270)
    t.penDown()
    t.forward((cos(angulo))*magnitud)
    
    
    
main()
    

    