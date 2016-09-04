# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Dibujar vector en un plano 

from Graphics import *
from math import sin, cos, pi

# Función que dibuja el plano de coordenadas x y 
def dibujarPlano(t):
    t.pen.color = Color("green")
    t.forward(1000)
    t.rotate(180)
    t.forward(500)
    t.rotate(90)
    t.forward(400)
    t.rotate(180)
    t.forward(800)
    t.penUp()
    t.setX(500)
    t.setY(400)
    t.penDown()
    t.rotate(270)
    
# Función que dibuja un vector
def dibujarVector(t, magnitud, direccion):
    t.pen.color = Color("yellow")
    t.rotate(direccion)
    t.forward(magnitud)
    t.penUp()
    t.setX(500)
    t.setY(400)
    t.penDown()
    t.rotate(-direccion)

# Función que dibuja las componentes de un vector
def dibujarComponentes(t, magnitud, direccion):  
    t.pen.color = Color("red")
    componenteX = magnitud*cos(direccion*pi/180)
    componenteY = magnitud*sin(direccion*pi/180)
    t.penUp()
    t.forward(componenteX)
    t.penDown()
    t.rotate(90)
    t.forward(componenteY)
    t.rotate(90)
    t.forward(componenteX)
    
def main():
    magnitud = int(input("Introduce la magnitud del vector"))
    angulo = int(input("Introduce el ángulo del vector"))
    ventana = Window("Vector", 1000, 800)
    t = Arrow((0,400),0)
    t.draw(ventana)
    t.penDown()
    dibujarPlano(t)
    dibujarVector(t, magnitud, angulo)
    dibujarComponentes(t, magnitud, angulo)
main()